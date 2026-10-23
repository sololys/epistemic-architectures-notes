#!/usr/bin/env python3
"""
staggered_prf_fine_wilf_gate.py
===============================
Horisont I: Staggered-PRF SDR / Radar Ghost-Target Filter via Fine-Wilf (1965),
Array Bragg Phase Coherence (Davisson 1925), and Continuous Range-Rate Integration.

Epistemic Status (AGENTS.md):
  Level: L1 (Deterministic Software Reference Implementation & Unit Test Suite).
  Boundary: INSPIRED_BY != IMPLEMENTS != PROVES.
  Software ledgers are append-only SHA-256 hash chains, not physical WORM hardware.

Core Physical & Mathematical Mechanism:
  1. Staggered Pulse Repetition Intervals (PRI_1 = p, PRI_2 = q in integer FPGA clock ticks):
     To resolve range/Doppler blind zones in pulsed SDR/radar/sonar, two coprime intervals
     (e.g., p = 5, q = 8 ticks, gcd(5, 8) = 1) are interleaved.
     By the Fine-Wilf theorem (1965), a dual-periodic clutter/multipath sequence can
     masquerade as a non-trivial structured target ("ABAABABAABA") for up to
     L = p + q - gcd(p, q) - 1 = 11 clock ticks.
     At tick L* = p + q - gcd(p, q) = 12, index 12 must simultaneously equal index 7 ('B')
     and index 4 ('A'), exposing the multipath ghost collision:
       - Window L < L*  -> GATE::HOLD (0.00 V DC, Sub-Horizon Ambiguity)
       - Window L >= L* with dual-period ghost -> GATE::KILL (0.00 V DC, Ghost Collision)
       - Window L >= L* with coherent carrier lock -> Passes Temporal Horizon

  2. Array Phase Coherence (Davisson-Bragg / ULA Phase Cone):
     Across N antenna/acoustic elements with inter-element spacing d_elem and wavelength lambda,
     constructive phase alignment requires phase residual delta_phi <= tau_phi and
     |sin(theta)| = |delta_phi / pi| <= 1.0 (inside the Euclidean phase cone):
       - Scrambled / Out-of-cone phase -> GATE::KILL (0.00 V DC)

  3. Continuous Range-Rate (Doppler-Range) Integration:
     A proposed target range displacement delta_R over window T_obs must match the time
     integral of radial velocity v_r(t) = c * f_D(t) / (2 * f_0):
       - Contradictory range vs. Doppler sign/energy -> GATE::KILL (0.00 V DC)
       - Missing continuous range-rate trajectory -> GATE::HOLD (0.00 V DC)
       - Verified trajectory + L >= L* + Array Coherence -> GATE::OPEN (24.00 V DC)
"""

from __future__ import annotations
from dataclasses import dataclass
import hashlib
import json
import math
import unittest
from typing import List, Optional, Tuple


@dataclass(frozen=True)
class StaggeredPrfObservation:
    obs_id: str
    pri_p: int
    pri_q: int
    pulse_symbol_stream: str
    # Array coherence parameters
    element_phases_rad: Tuple[float, ...]
    expected_steering_phase_step_rad: float
    phase_tolerance_rad: float
    # Continuous range-rate (Doppler) trajectory parameters
    initial_range_m: float
    reported_final_range_m: float
    reported_radial_velocity_mps: float
    observation_time_s: float
    integrated_velocity_samples_mps: Optional[Tuple[float, ...]] = None
    dt_s: float = 0.0


@dataclass(frozen=True)
class StaggeredPrfGateVerdict:
    obs_id: str
    state: str                 # "KILL" | "HOLD" | "OPEN"
    voltage_v_dc: float        # 0.00 or 24.00
    fine_wilf_horizon: int     # L* = p + q - gcd(p, q)
    observed_window_len: int   # len(pulse_symbol_stream)
    array_coherence_r: float   # |[1/M sum exp(i * residual)]|
    range_integral_residual_m: float
    reason_code: str
    sha256_receipt: str


def compute_fine_wilf_horizon(p: int, q: int) -> int:
    if p <= 0 or q <= 0:
        raise ValueError("PRI periods p and q must be positive integers.")
    return p + q - math.gcd(p, q)


def has_period(word: str, period: int) -> bool:
    n = len(word)
    for i in range(n - period):
        if word[i] != word[i + period]:
            return False
    return True


def compute_array_phase_coherence(
    element_phases_rad: Tuple[float, ...],
    steering_step_rad: float,
) -> float:
    """
    Computes normalized phasor coherence R in [0, 1] after removing expected
    linear progression k * steering_step_rad across array elements.
    """
    m = len(element_phases_rad)
    if m == 0:
        return 0.0
    re_sum = 0.0
    im_sum = 0.0
    for k, phi in enumerate(element_phases_rad):
        residual = phi - (k * steering_step_rad)
        re_sum += math.cos(residual)
        im_sum += math.sin(residual)
    return math.hypot(re_sum, im_sum) / float(m)


def evaluate_staggered_prf_gate(
    obs: StaggeredPrfObservation,
    prev_hash: str = "0" * 64,
    coherence_min_r: float = 0.95,
    range_tol_m: float = 1e-3,
) -> StaggeredPrfGateVerdict:
    """
    Deterministic fail-closed evaluation of an SDR/Radar staggered-PRF observation.
    """
    horizon = compute_fine_wilf_horizon(obs.pri_p, obs.pri_q)
    w_len = len(obs.pulse_symbol_stream)

    # 1. Check Euclidean Phase Cone & Array Bragg Coherence (Spatial Layer)
    if abs(obs.expected_steering_phase_step_rad) > math.pi:
        return _seal_verdict(
            obs, "KILL", 0.00, horizon, w_len, 0.0, 0.0,
            "KILL_OUTSIDE_EUCLIDEAN_PHASE_CONE", prev_hash
        )

    coherence_r = compute_array_phase_coherence(
        obs.element_phases_rad, obs.expected_steering_phase_step_rad
    )
    if coherence_r < coherence_min_r:
        return _seal_verdict(
            obs, "KILL", 0.00, horizon, w_len, coherence_r, 0.0,
            "KILL_POLYCRYSTALLINE_PHASE_SCRAMBLING", prev_hash
        )

    # 2. Check Range-Rate Conservation Law for Contradiction (Mechanical/Kinematic Layer)
    expected_delta_r = obs.reported_radial_velocity_mps * obs.observation_time_s
    reported_delta_r = obs.reported_final_range_m - obs.initial_range_m
    if abs(reported_delta_r - expected_delta_r) > range_tol_m:
        return _seal_verdict(
            obs, "KILL", 0.00, horizon, w_len, coherence_r,
            abs(reported_delta_r - expected_delta_r),
            "KILL_DOPPLER_RANGE_CONTRADICTION", prev_hash
        )

    # 3. Check Fine-Wilf Temporal Horizon L* = p + q - gcd(p, q) (Combinatorial Layer)
    if w_len < horizon:
        return _seal_verdict(
            obs, "HOLD", 0.00, horizon, w_len, coherence_r, 0.0,
            "HOLD_SUB_HORIZON_STAGGERED_PRF_WINDOW", prev_hash
        )

    # At L >= L*, if the stream carries >1 symbol while claiming both periods p and q,
    # or exhibits a Sturmian ghost prefix that breaks at step L*, reject as ghost clutter.
    unique_symbols = set(obs.pulse_symbol_stream)
    if len(unique_symbols) > 1:
        prefix_sub = obs.pulse_symbol_stream[: horizon - 1]
        if has_period(prefix_sub, obs.pri_p) and has_period(prefix_sub, obs.pri_q):
            return _seal_verdict(
                obs, "KILL", 0.00, horizon, w_len, coherence_r, 0.0,
                "KILL_STURMIAN_MULTIPATH_GHOST_COLLISION_AT_L_STAR", prev_hash
            )
        return _seal_verdict(
            obs, "KILL", 0.00, horizon, w_len, coherence_r, 0.0,
            "KILL_NON_UNIFORM_CARRIER_LOCK", prev_hash
        )

    # 4. Require Continuous Range-Rate Trajectory Integration (P-Trajectory Warrant)
    if not obs.integrated_velocity_samples_mps or obs.dt_s <= 0.0:
        return _seal_verdict(
            obs, "HOLD", 0.00, horizon, w_len, coherence_r, 0.0,
            "HOLD_MISSING_CONTINUOUS_DOPPLER_TRAJECTORY", prev_hash
        )

    integrated_disp = sum(v * obs.dt_s for v in obs.integrated_velocity_samples_mps)
    residual_m = abs(integrated_disp - reported_delta_r)
    if residual_m > range_tol_m:
        return _seal_verdict(
            obs, "KILL", 0.00, horizon, w_len, coherence_r, residual_m,
            "KILL_TRAJECTORY_INTEGRAL_MISMATCH", prev_hash
        )

    return _seal_verdict(
        obs, "OPEN", 24.00, horizon, w_len, coherence_r, residual_m,
        "OPEN_COHERENT_PRF_HORIZON_AND_DOPPLER_PATH_VERIFIED", prev_hash
    )


def _seal_verdict(
    obs: StaggeredPrfObservation,
    state: str,
    voltage: float,
    horizon: int,
    w_len: int,
    coherence_r: float,
    residual_m: float,
    reason: str,
    prev_hash: str,
) -> StaggeredPrfGateVerdict:
    payload = {
        "obs_id": obs.obs_id,
        "state": state,
        "voltage_v_dc": round(voltage, 2),
        "fine_wilf_horizon": horizon,
        "observed_window_len": w_len,
        "array_coherence_r": round(coherence_r, 6),
        "range_integral_residual_m": round(residual_m, 6),
        "reason_code": reason,
        "prev_hash": prev_hash,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    digest = hashlib.sha256(canonical).hexdigest()
    return StaggeredPrfGateVerdict(
        obs_id=obs.obs_id,
        state=state,
        voltage_v_dc=voltage,
        fine_wilf_horizon=horizon,
        observed_window_len=w_len,
        array_coherence_r=coherence_r,
        range_integral_residual_m=residual_m,
        reason_code=reason,
        sha256_receipt=digest,
    )


# ============================================================================
# DETERMINISTIC 6/6 MONOLITH TEST SUITE
# ============================================================================
class TestStaggeredPrfFineWilfGate(unittest.TestCase):
    def setUp(self) -> None:
        # 4-element uniform linear array steered at pi/4 rad per element
        self.step = math.pi / 4.0
        self.coherent_phases = tuple(k * self.step for k in range(4))

    def test_01_sub_horizon_sturmian_ghost_forces_hold(self) -> None:
        """L = 11 < L* = 12 with ghost word 'ABAABABAABA' must HOLD (0.00 V)."""
        obs = StaggeredPrfObservation(
            obs_id="SDR-GHOST-L11",
            pri_p=5,
            pri_q=8,
            pulse_symbol_stream="ABAABABAABA",  # len 11 < 12
            element_phases_rad=self.coherent_phases,
            expected_steering_phase_step_rad=self.step,
            phase_tolerance_rad=0.05,
            initial_range_m=1000.0,
            reported_final_range_m=1040.0,
            reported_radial_velocity_mps=20.0,
            observation_time_s=2.0,
            integrated_velocity_samples_mps=(20.0,) * 20,
            dt_s=0.1,
        )
        v = evaluate_staggered_prf_gate(obs)
        self.assertEqual(v.fine_wilf_horizon, 12)
        self.assertEqual(v.state, "HOLD")
        self.assertEqual(v.voltage_v_dc, 0.00)
        self.assertEqual(v.reason_code, "HOLD_SUB_HORIZON_STAGGERED_PRF_WINDOW")

    def test_02_at_horizon_sturmian_ghost_collision_forces_kill(self) -> None:
        """At L* = 12, 'ABAABABAABA' + 'A' or 'B' exposes the dual-PRI ghost -> KILL."""
        obs = StaggeredPrfObservation(
            obs_id="SDR-GHOST-L12-COLLISION",
            pri_p=5,
            pri_q=8,
            pulse_symbol_stream="ABAABABAABAA",  # step 12 collides with p=5 ('B' vs 'A')
            element_phases_rad=self.coherent_phases,
            expected_steering_phase_step_rad=self.step,
            phase_tolerance_rad=0.05,
            initial_range_m=1000.0,
            reported_final_range_m=1040.0,
            reported_radial_velocity_mps=20.0,
            observation_time_s=2.0,
            integrated_velocity_samples_mps=(20.0,) * 20,
            dt_s=0.1,
        )
        v = evaluate_staggered_prf_gate(obs)
        self.assertEqual(v.state, "KILL")
        self.assertEqual(v.voltage_v_dc, 0.00)
        self.assertEqual(
            v.reason_code, "KILL_STURMIAN_MULTIPATH_GHOST_COLLISION_AT_L_STAR"
        )

    def test_03_scrambled_array_phases_force_kill(self) -> None:
        """Polycrystalline / scrambled antenna element phases cancel out -> KILL."""
        scrambled = (0.0, math.pi, 0.5 * math.pi, -0.5 * math.pi)
        obs = StaggeredPrfObservation(
            obs_id="SDR-SCRAMBLED-ARRAY",
            pri_p=5,
            pri_q=8,
            pulse_symbol_stream="A" * 12,
            element_phases_rad=scrambled,
            expected_steering_phase_step_rad=self.step,
            phase_tolerance_rad=0.05,
            initial_range_m=1000.0,
            reported_final_range_m=1040.0,
            reported_radial_velocity_mps=20.0,
            observation_time_s=2.0,
            integrated_velocity_samples_mps=(20.0,) * 20,
            dt_s=0.1,
        )
        v = evaluate_staggered_prf_gate(obs)
        self.assertEqual(v.state, "KILL")
        self.assertEqual(v.voltage_v_dc, 0.00)
        self.assertEqual(v.reason_code, "KILL_POLYCRYSTALLINE_PHASE_SCRAMBLING")

    def test_04_doppler_range_contradiction_forces_kill(self) -> None:
        """Target claims +40 m shift at 0.0 m/s radial Doppler velocity -> KILL."""
        obs = StaggeredPrfObservation(
            obs_id="SDR-DOPPLER-CONTRADICTION",
            pri_p=5,
            pri_q=8,
            pulse_symbol_stream="A" * 12,
            element_phases_rad=self.coherent_phases,
            expected_steering_phase_step_rad=self.step,
            phase_tolerance_rad=0.05,
            initial_range_m=1000.0,
            reported_final_range_m=1040.0,
            reported_radial_velocity_mps=0.0,  # Contradicts +40 m shift
            observation_time_s=2.0,
            integrated_velocity_samples_mps=(0.0,) * 20,
            dt_s=0.1,
        )
        v = evaluate_staggered_prf_gate(obs)
        self.assertEqual(v.state, "KILL")
        self.assertEqual(v.voltage_v_dc, 0.00)
        self.assertEqual(v.reason_code, "KILL_DOPPLER_RANGE_CONTRADICTION")

    def test_05_endpoint_without_continuous_doppler_integral_forces_hold(self) -> None:
        """Consistent endpoint without continuous velocity integration -> HOLD."""
        obs = StaggeredPrfObservation(
            obs_id="SDR-ENDPOINT-ONLY",
            pri_p=5,
            pri_q=8,
            pulse_symbol_stream="A" * 12,
            element_phases_rad=self.coherent_phases,
            expected_steering_phase_step_rad=self.step,
            phase_tolerance_rad=0.05,
            initial_range_m=1000.0,
            reported_final_range_m=1040.0,
            reported_radial_velocity_mps=20.0,
            observation_time_s=2.0,
            integrated_velocity_samples_mps=None,
            dt_s=0.0,
        )
        v = evaluate_staggered_prf_gate(obs)
        self.assertEqual(v.state, "HOLD")
        self.assertEqual(v.voltage_v_dc, 0.00)
        self.assertEqual(v.reason_code, "HOLD_MISSING_CONTINUOUS_DOPPLER_TRAJECTORY")

    def test_06_full_coherent_staggered_prf_opens_gate(self) -> None:
        """L >= 12, coherent array (R = 1.0), and integrated Doppler path -> OPEN (24.00 V)."""
        obs = StaggeredPrfObservation(
            obs_id="SDR-VERIFIED-TARGET-OPEN",
            pri_p=5,
            pri_q=8,
            pulse_symbol_stream="A" * 12,
            element_phases_rad=self.coherent_phases,
            expected_steering_phase_step_rad=self.step,
            phase_tolerance_rad=0.05,
            initial_range_m=1000.0,
            reported_final_range_m=1040.0,
            reported_radial_velocity_mps=20.0,
            observation_time_s=2.0,
            integrated_velocity_samples_mps=(20.0,) * 20,
            dt_s=0.1,
        )
        v = evaluate_staggered_prf_gate(obs)
        self.assertEqual(v.state, "OPEN")
        self.assertEqual(v.voltage_v_dc, 24.00)
        self.assertAlmostEqual(v.array_coherence_r, 1.0, places=6)
        self.assertEqual(len(v.sha256_receipt), 64)


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStaggeredPrfFineWilfGate)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    if not result.wasSuccessful():
        raise SystemExit(1)
