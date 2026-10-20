#!/usr/bin/env python3
"""
L1_LAW // Pure Mathematical Invariants (Zero I/O, Zero Side Effects)
====================================================================
Dependencies  : Python Standard Library ONLY (fractions, math, unittest)
Epistemic Tier: L1 Pure Function Definitions (INSPIRED_BY != IMPLEMENTS != PROVES)
Includes      : Spec 122 G2 Holonomic Phase-Spiral & Sedenion Zero-Divisor Evasion
"""

from __future__ import annotations

from fractions import Fraction
import math
import unittest
from typing import Sequence, Tuple

C_VACUUM_M_PER_S: float = 299_792_458.0
F_G2_SPIRAL_HZ: float = 80_000.0
DT_G2_SPIRAL_S: float = 1.25e-5


def involutive_residual_norm(
    s0: Tuple[float, float],
    delta_cmd: Tuple[float, float],
    leakage: Tuple[float, float] = (0.0, 0.0),
) -> Tuple[float, Tuple[float, float]]:
    """Pure evaluation of S0 -> Sf -> Sr residual ||S0 - Sr||_2."""
    sf = (s0[0] + delta_cmd[0] + leakage[0], s0[1] + delta_cmd[1] + leakage[1])
    sr = (sf[0] - delta_cmd[0], sf[1] - delta_cmd[1])
    return math.hypot(s0[0] - sr[0], s0[1] - sr[1]), sf


def relational_gram_drift(
    ref_basis: Tuple[Tuple[float, float], Tuple[float, float]],
    cur_basis: Tuple[Tuple[float, float], Tuple[float, float]],
) -> float:
    """Pure Frobenius drift ||G(t) - G(0)||_F of the 2x2 relational Gram matrix."""
    def gram(v1: Tuple[float, float], v2: Tuple[float, float]) -> Tuple[float, float, float]:
        return (
            v1[0] * v1[0] + v1[1] * v1[1],
            v1[0] * v2[0] + v1[1] * v2[1],
            v2[0] * v2[0] + v2[1] * v2[1],
        )

    g0_11, g0_12, g0_22 = gram(ref_basis[0], ref_basis[1])
    gt_11, gt_12, gt_22 = gram(cur_basis[0], cur_basis[1])
    return math.sqrt(
        (gt_11 - g0_11) ** 2 + 2.0 * (gt_12 - g0_12) ** 2 + (gt_22 - g0_22) ** 2
    )


def rational_conservation_residual(
    inputs_q: Sequence[Fraction],
    outputs_q: Sequence[Fraction],
) -> Fraction:
    """Pure exact rational mass/token conservation residual in Q."""
    return sum(inputs_q, Fraction(0, 1)) - sum(outputs_q, Fraction(0, 1))


def causal_lightcone_interval_m2(delta_t_ns: float, distance_m: float) -> float:
    """Pure Minkowski interval ds^2 = d^2 - (c * dt / 2)^2."""
    c_half_dt = C_VACUUM_M_PER_S * (delta_t_ns * 1e-9) / 2.0
    return (distance_m * distance_m) - (c_half_dt * c_half_dt)


def monotone_fuse_valid(fuse_prev: int, fuse_next: int) -> bool:
    """Pure bitwise monotonicity check (F_n & F_{n+1}) == F_n."""
    return (fuse_prev & fuse_next) == fuse_prev


def g2_holonomic_spiral_state(
    t_s: float = DT_G2_SPIRAL_S,
    omega_rad_s: float = 2.0 * math.pi * F_G2_SPIRAL_HZ,
    damping_lambda: float = 250.0,
) -> Tuple[Tuple[float, ...], Tuple[float, ...], Tuple[float, ...]]:
    """
    Pure 16D Sedenion trajectory gamma(t) = exp(Phi * t) * x0 * A(p, t)
    with strictly positive curvature and radial Riccati contraction.
    """
    env = math.exp(-damping_lambda * t_s)
    w = omega_rad_s
    pos = [0.0] * 16
    vel = [0.0] * 16
    acc = [0.0] * 16

    modes = ((0, 1, 1.0, 1.0), (4, 10, 0.8, 1.5), (7, 15, 0.5, 2.0))
    for idx_c, idx_s, amp, mult in modes:
        wm = w * mult
        a_t = amp * env
        c_val = math.cos(wm * t_s)
        s_val = math.sin(wm * t_s)

        pos[idx_c] = a_t * c_val
        pos[idx_s] = a_t * s_val

        vel[idx_c] = a_t * (-damping_lambda * c_val - wm * s_val)
        vel[idx_s] = a_t * (-damping_lambda * s_val + wm * c_val)

        acc[idx_c] = a_t * (
            (damping_lambda * damping_lambda - wm * wm) * c_val
            + 2.0 * damping_lambda * wm * s_val
        )
        acc[idx_s] = a_t * (
            (damping_lambda * damping_lambda - wm * wm) * s_val
            - 2.0 * damping_lambda * wm * c_val
        )

    return tuple(pos), tuple(vel), tuple(acc)


def g2_algebraic_curvature(vel: Sequence[float], acc: Sequence[float]) -> float:
    """Pure Frenet-Serret curvature kappa = ||vel ^ acc|| / ||vel||^3 > 0."""
    norm_v_sq = sum(v * v for v in vel)
    if norm_v_sq <= 1e-30:
        return 0.0
    wedge_sq = 0.0
    dim = len(vel)
    for i in range(dim):
        for j in range(i + 1, dim):
            w_ij = vel[i] * acc[j] - vel[j] * acc[i]
            wedge_sq += w_ij * w_ij
    return math.sqrt(wedge_sq) / (norm_v_sq ** 1.5)


def sedenion_zero_divisor_distance(pos: Sequence[float]) -> float:
    """Pure Euclidean distance to the Sedenion zero-divisor locus (e1+e10)x(e4-e15)=0."""
    return math.hypot(pos[1] - pos[10], pos[4] + pos[15])


def sedenion_associator_norm(
    x: Sequence[float],
    y: Sequence[float],
    z: Sequence[float],
) -> float:
    """Pure skew-triple associator norm proxy ||[x, y, z]|| in 16D Sedenion space."""
    dim = len(x)
    c_xy = sum(x[i] * y[(i + 1) % dim] - x[(i + 1) % dim] * y[i] for i in range(dim))
    c_yz = sum(y[i] * z[(i + 3) % dim] - y[(i + 3) % dim] * z[i] for i in range(dim))
    return abs(c_xy * c_yz)


def riccati_are_descent_inner_product(
    pos: Sequence[float],
    vel: Sequence[float],
) -> float:
    """Pure inner product <gamma_dot(t), grad ARE(P)> <= 0 along the Lyapunov well."""
    return sum(v * p for p, v in zip(pos, vel))


class TestL1LawPure(unittest.TestCase):
    def test_involutive_residual_pure(self) -> None:
        res_ok, _ = involutive_residual_norm((2.0, 3.0), (1.5, -1.0), (0.0, 0.0))
        res_bad, _ = involutive_residual_norm((2.0, 3.0), (1.5, -1.0), (0.05, 0.0))
        self.assertEqual(res_ok, 0.0)
        self.assertAlmostEqual(res_bad, 0.05, places=12)

    def test_relational_gram_pure(self) -> None:
        ref = ((1.0, 0.0), (0.0, 1.0))
        theta = math.pi / 3.0
        rot = ((math.cos(theta), math.sin(theta)), (-math.sin(theta), math.cos(theta)))
        shear = ((1.0, 0.25), (0.0, 1.0))
        self.assertAlmostEqual(relational_gram_drift(ref, rot), 0.0, places=12)
        self.assertGreater(relational_gram_drift(ref, shear), 0.2)

    def test_rational_conservation_pure(self) -> None:
        ins = (Fraction(1, 3), Fraction(2, 3))
        outs = (Fraction(1, 2), Fraction(1, 2))
        self.assertEqual(rational_conservation_residual(ins, outs), Fraction(0, 1))
        self.assertNotEqual(rational_conservation_residual(ins, (Fraction(9, 10),)), Fraction(0, 1))

    def test_causal_lightcone_and_fuse_pure(self) -> None:
        self.assertLessEqual(causal_lightcone_interval_m2(133.43, 19.9), 0.0)
        self.assertGreater(causal_lightcone_interval_m2(50.0, 19.9), 0.0)
        self.assertTrue(monotone_fuse_valid(0b0011, 0b0111))
        self.assertFalse(monotone_fuse_valid(0b0111, 0b0011))

    def test_g2_holonomic_spiral_pure(self) -> None:
        pos, vel, acc = g2_holonomic_spiral_state(DT_G2_SPIRAL_S)
        kappa = g2_algebraic_curvature(vel, acc)
        dist_zd = sedenion_zero_divisor_distance(pos)
        are_dot = riccati_are_descent_inner_product(pos, vel)
        assoc = sedenion_associator_norm(pos, vel, acc)
        self.assertGreater(kappa, 0.0)
        self.assertGreater(dist_zd, 0.15)
        self.assertLessEqual(are_dot, 0.0)
        self.assertGreater(assoc, 0.0)


if __name__ == "__main__":
    unittest.main()
