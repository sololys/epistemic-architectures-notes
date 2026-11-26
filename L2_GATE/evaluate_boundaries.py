#!/usr/bin/env python3
"""
L2_GATE // Consequence Gate & Boundary Projection Evaluator (Omega o Pi_K, 0 Float)
===================================================================================
Dependencies  : Python Standard Library ONLY + L1_LAW pure functions
Epistemic Tier: L1 Deterministic Software Gate (PHYSICAL_AUTHORITY = NONE)
Legal Boundary: MATHEMATICS != LEGAL_MANDATE (0% algorithmic legal capacity)
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys
from typing import Any, Dict

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from L1_LAW.invariants_pure import (
    DT_G2_SPIRAL_S,
    F_G2_SPIRAL_HZ,
    aps_anomaly_inflow_index,
    asymmetric_bft_quorum_verdict,
    causal_lightcone_interval_m2,
    d0_to_d3_taxonomy_admissible,
    g2_algebraic_curvature,
    g2_holonomic_spiral_state,
    involutive_residual_norm,
    monotone_fuse_valid,
    rational_conservation_residual,
    relational_gram_drift,
    riccati_are_descent_inner_product,
    rosetta3_isometry_verified,
    sedenion_zero_divisor_distance,
)


def evaluate_gate(
    eps_iso: Fraction = Fraction(1, 1_000_000_000),
    tau_gram: Fraction = Fraction(1, 1_000_000_000),
    envelope_max: Fraction = Fraction(10, 1),
    min_zd_dist: Fraction = Fraction(3, 20),
) -> Dict[str, Any]:
    res_iso, sf = involutive_residual_norm(
        (Fraction(2, 1), Fraction(3, 1)),
        (Fraction(3, 2), Fraction(-1, 1)),
        (Fraction(0, 1), Fraction(0, 1)),
    )
    within_envelope = max(abs(sf[0]), abs(sf[1])) <= envelope_max
    delta_g = relational_gram_drift(
        ((Fraction(1, 1), Fraction(0, 1)), (Fraction(0, 1), Fraction(1, 1))),
        ((Fraction(0, 1), Fraction(1, 1)), (Fraction(-1, 1), Fraction(0, 1))),
    )
    delta_r = rational_conservation_residual(
        (Fraction(100, 3), Fraction(200, 3)),
        (Fraction(50, 1), Fraction(50, 1)),
    )
    ds2 = causal_lightcone_interval_m2(
        delta_t_ns=Fraction(100, 1),
        distance_m=Fraction(149_896_229, 10_000_000),
    )
    fuse_ok = monotone_fuse_valid(0b0001, 0b0011)

    pos_g2, vel_g2, acc_g2 = g2_holonomic_spiral_state(DT_G2_SPIRAL_S)
    kappa_g2 = g2_algebraic_curvature(vel_g2, acc_g2)
    dist_zd = sedenion_zero_divisor_distance(pos_g2)
    are_dot = riccati_are_descent_inner_product(pos_g2, vel_g2)

    d3_ok = d0_to_d3_taxonomy_admissible(("D0", "D1", "D2", "D3"), F_G2_SPIRAL_HZ)
    rosetta_ok = rosetta3_isometry_verified("W2_STATE_01", "W2_STATE_01", "W2_STATE_01")
    bft_verdict = asymmetric_bft_quorum_verdict(fault_tolerance_f=1, allow_votes=3, veto_votes=0)
    aps_idx, aps_res_q = aps_anomaly_inflow_index(Fraction(5, 2), Fraction(1, 1), 0)

    if (
        res_iso > eps_iso
        or delta_g > tau_gram
        or delta_r != Fraction(0, 1)
        or not fuse_ok
        or kappa_g2 <= Fraction(0, 1)
        or dist_zd <= min_zd_dist
        or are_dot > Fraction(0, 1)
        or not d3_ok
        or not rosetta_ok
        or bft_verdict == "KILL"
        or aps_res_q != Fraction(0, 1)
    ):
        verdict = "KILL"
        voltage_mv = 0
    elif not within_envelope or ds2 > Fraction(0, 1) or bft_verdict != "OPEN":
        verdict = "HOLD"
        voltage_mv = 0
    else:
        verdict = "HOLD_READY_FOR_W2"
        voltage_mv = 0

    payload: Dict[str, Any] = {
        "aps_index": aps_idx,
        "aps_residual_q": str(aps_res_q),
        "are_descent_le_zero": are_dot <= Fraction(0, 1),
        "bft_quorum": bft_verdict,
        "d0_to_d3_sealed": d3_ok,
        "delta_g": str(delta_g),
        "delta_r": str(delta_r),
        "ds2_m2": str(ds2),
        "fuse_monotone": fuse_ok,
        "g2_curvature_kappa": str(kappa_g2),
        "g2_zd_distance": str(dist_zd),
        "legal_authority": "NONE_HUMAN_L01_REQUIRED",
        "residual_iso": str(res_iso),
        "rosetta3_isometry": rosetta_ok,
        "verdict": verdict,
        "voltage_mv": voltage_mv,
        "voltage_v": "0.00",
        "within_envelope": within_envelope,
    }
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    payload["gate_sha256"] = hashlib.sha256(encoded).hexdigest()
    return payload


def main() -> int:
    result = evaluate_gate()
    if result["verdict"] == "KILL":
        print(json.dumps(result, sort_keys=True))
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
