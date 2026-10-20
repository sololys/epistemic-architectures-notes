#!/usr/bin/env python3
"""
L2_GATE // Consequence Gate & Boundary Projection Evaluator (Omega o Pi_K)
==========================================================================
Dependencies  : Python Standard Library ONLY + L1_LAW pure functions
Epistemic Tier: L1 Deterministic Software Gate (PHYSICAL_AUTHORITY = NONE)
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
    causal_lightcone_interval_m2,
    g2_algebraic_curvature,
    g2_holonomic_spiral_state,
    involutive_residual_norm,
    monotone_fuse_valid,
    rational_conservation_residual,
    relational_gram_drift,
    riccati_are_descent_inner_product,
    sedenion_zero_divisor_distance,
)


def evaluate_gate(
    eps_iso: float = 1e-9,
    tau_gram: float = 1e-9,
    envelope_max: float = 10.0,
    min_zd_dist: float = 0.15,
) -> Dict[str, Any]:
    res_iso, sf = involutive_residual_norm((2.0, 3.0), (1.5, -1.0), (0.0, 0.0))
    within_envelope = max(abs(sf[0]), abs(sf[1])) <= envelope_max
    delta_g = relational_gram_drift(((1.0, 0.0), (0.0, 1.0)), ((0.0, 1.0), (-1.0, 0.0)))
    delta_r = rational_conservation_residual(
        (Fraction(100, 3), Fraction(200, 3)),
        (Fraction(50, 1), Fraction(50, 1)),
    )
    ds2 = causal_lightcone_interval_m2(delta_t_ns=100.0, distance_m=14.9896229)
    fuse_ok = monotone_fuse_valid(0b0001, 0b0011)

    pos_g2, vel_g2, acc_g2 = g2_holonomic_spiral_state(DT_G2_SPIRAL_S)
    kappa_g2 = g2_algebraic_curvature(vel_g2, acc_g2)
    dist_zd = sedenion_zero_divisor_distance(pos_g2)
    are_dot = riccati_are_descent_inner_product(pos_g2, vel_g2)

    if (
        res_iso > eps_iso
        or delta_g > tau_gram
        or delta_r != Fraction(0, 1)
        or not fuse_ok
        or kappa_g2 <= 0.0
        or dist_zd <= min_zd_dist
        or are_dot > 0.0
    ):
        verdict = "KILL"
        voltage_v = 0.00
    elif not within_envelope or ds2 > 0.0:
        verdict = "HOLD"
        voltage_v = 0.00
    else:
        verdict = "HOLD_READY_FOR_W2"
        voltage_v = 0.00

    payload: Dict[str, Any] = {
        "are_descent_le_zero": are_dot <= 0.0,
        "delta_g": round(delta_g, 12),
        "delta_r": str(delta_r),
        "ds2_m2": round(ds2, 6),
        "fuse_monotone": fuse_ok,
        "g2_curvature_kappa": round(kappa_g2, 6),
        "g2_zd_distance": round(dist_zd, 6),
        "residual_iso": round(res_iso, 12),
        "verdict": verdict,
        "voltage_v": voltage_v,
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
