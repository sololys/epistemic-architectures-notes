#!/usr/bin/env python3
"""
Milestone 1 Verification Script: KMS Spectral Series & COS45 Frontier Constant C
================================================================================
Joint Technical Note & Benchmark Verification (Morissette & Torjusen, 2026)
Reference: COS45 v1.7.0 (DOI: 10.5281/zenodo.23440691)

This script reproduces and cross-checks:
  1. [EXACT IDENTITY] Centrosymmetric parity selection for the Kac-Murdock-Szego
     (KMS) matrix Gamma_a^(0) = (rho^|i-j|) and corner perturbation
     E = e_1 e_a^T + e_a e_1^T:
       u_k(a) = (-1)^(k-1) u_k(1)
       u_j^T E u_i = 0  for j != i (mod 2)
       |u_j^T E u_i|^2 = 4 * u_i(1)^2 * u_j(1)^2  for j == i (mod 2)
  2. [EXACT IDENTITY] Closed-form evaluation of the odd and even spectral series:
       S_1 = sum_{m=1}^inf (2m+1)^2 / ((2m+1)^2 - 1)^2 = 1/16 + pi^2 / 48
       S_2 = sum_{m=2}^inf 4*(2m)^2 / ((2m)^2 - 4)^2   = 1/16 + pi^2 / 12
       C   = sqrt((64/9) * (S_1 + S_2)) = 2 * sqrt(18 + 15*pi^2) / 9
  3. [ASYMPTOTIC STATEMENT UNDER EXAMINATION & NUMERICAL OBSERVATION]
     Finite-a convergence table of a * chi_{a-2, 2}(a) toward C as a increases,
     together with Richardson 1/a extrapolation and explicit tolerances.
"""

from __future__ import annotations

import math
import unittest
import numpy as np


# ============================================================================
# 1. Parameter Definitions (L, a, r, b, H)
# ============================================================================
PARAMETER_DEFINITIONS = {
    "L": "Interaction lag order of the hidden_order Markov process (a = L + 2 at the actionable frontier).",
    "a": "Hankel window height (embedding dimension, a >= 4; trajectories live on Gr(a, r)).",
    "r": "Dominant spectral subspace rank of the projector P_t in Gr(a, r) (r = 2 in the baseline frontier audit).",
    "b": "Hankel window width (number of columns / sample count per empirical covariance matrix Gamma_hat_b).",
    "H": "Forward recurrence horizon (number of steps tau in [1, H] for the orbit recurrence check delta_orbit).",
}


# ============================================================================
# 2. Exact Closed-Form Constants & Spectral Series
# ============================================================================
def exact_spectral_series_constants(rho: float = 0.5) -> dict[str, float]:
    """Return the exact analytical series values S_1, S_2, C^2, and C(rho, r=2)."""
    s1_exact = (1.0 / 16.0) + (math.pi ** 2) / 48.0
    s2_exact = (1.0 / 16.0) + (math.pi ** 2) / 12.0
    # From u_k(1)^2 = (2/a) * theta_k^2 * ((1+rho)/(1-rho)) / (1-rho)^2 -> at rho=1/2: 8*k^2*pi^2/a^3
    # and Lambda_i - Lambda_j = (2*rho*(1+rho)/(1-rho)^3) * (j^2 - i^2)*pi^2/a^2 -> at rho=1/2: 6*(j^2-i^2)*pi^2/a^2
    # Thus 4 * u_i(1)^2 * u_j(1)^2 / (Lambda_i - Lambda_j)^2 has prefactor:
    #   4 * (2 / (1-rho)^2)^2 / (2*rho*(1+rho)/(1-rho)^3)^2 = 4 * (1-rho)^2 / (rho^2 * (1+rho)^2)
    # Wait: at rho=1/2, u_k(1)^2 = (2/a) * (k*pi/a)^2 / (1 - 1/2)^2 = 8 * k^2 * pi^2 / a^3,
    # so 4 * 8 * 8 / 6^2 = 256 / 36 = 64 / 9 = ((4*(1-rho)) / (rho*(1+rho)))^2!
    prefactor = ((4.0 * (1.0 - rho)) / (rho * (1.0 + rho))) ** 2
    c_sq_exact = prefactor * (s1_exact + s2_exact)
    c_exact = math.sqrt(c_sq_exact)
    return {
        "S1_exact": s1_exact,
        "S2_exact": s2_exact,
        "C_squared_exact": c_sq_exact,
        "C_exact": c_exact,
    }


def partial_spectral_series(n_terms: int = 200_000) -> dict[str, float]:
    """Compute high-precision partial sums of S_1 and S_2 for direct numerical check."""
    m1 = np.arange(1, n_terms + 1, dtype=np.float64)
    odd = 2.0 * m1 + 1.0
    s1_num = float(np.sum((odd ** 2) / ((odd ** 2 - 1.0) ** 2)))
    # Since (2m+1)^2 / ((2m+1)^2 - 1)^2 = (1/16) * (1/m + 1/(m+1))^2 = (1/16)*(1/m^2 + 1/(m+1)^2 + 2/(m(m+1))),
    # the exact telescoping + Euler-Maclaurin tail for m > N is 1/(4*(N + 0.5))
    s1_tail_corr = 1.0 / (4.0 * (n_terms + 0.5))

    m2 = np.arange(2, n_terms + 2, dtype=np.float64)
    even = 2.0 * m2
    s2_num = float(np.sum(4.0 * (even ** 2) / ((even ** 2 - 4.0) ** 2)))
    # Summand is m^2 / (m^2 - 1)^2 ~ 1/m^2 for m >= N+2; midpoint integral tail is 1/(N + 1.5)
    s2_tail_corr = 1.0 / (n_terms + 1.5)

    return {
        "S1_partial": s1_num,
        "S1_richardson": s1_num + s1_tail_corr,
        "S2_partial": s2_num,
        "S2_richardson": s2_num + s2_tail_corr,
    }


# ============================================================================
# 3. Direct Numerical KMS Matrix & Grassmann Frontier Coefficient chi_{a-2, r}(a)
# ============================================================================
def build_kms_matrix(a: int, rho: float = 0.5) -> np.ndarray:
    """Construct the exact a x a Kac-Murdock-Szego matrix Gamma_a^(0)_{i,j} = rho^|i-j|."""
    idx = np.arange(a)
    return np.power(rho, np.abs(idx[:, None] - idx[None, :])).astype(np.float64)


def compute_chi_and_check_identities(a: int, r: int = 2, rho: float = 0.5) -> dict[str, float]:
    """
    Compute chi_{a-2, r}(a) directly from the eigendecomposition of Gamma_a^(0)
    and verify the exact centrosymmetric parity identities at finite a.
    """
    gamma = build_kms_matrix(a, rho=rho)
    evals, evecs = np.linalg.eigh(gamma)
    # Sort in descending order: Lambda_1 > Lambda_2 > ... > Lambda_a
    order = np.argsort(evals)[::-1]
    lambdas = evals[order]
    u = evecs[:, order]

    # 1. Check centrosymmetric parity identity: u_k(a-1) == (-1)^(k-1) u_k(0)
    # Note: 0-indexed k_idx = k - 1, so sign is (-1)^k_idx
    signs = np.array([1.0 if (k_idx % 2 == 0) else -1.0 for k_idx in range(a)])
    # Eigenvectors from eigh have arbitrary global sign, but the relative sign between
    # endpoints u[0, k_idx] and u[a-1, k_idx] is strictly (-1)^k_idx because Lambda_k are distinct!
    parity_residual = float(np.max(np.abs(u[-1, :] - signs * u[0, :])))

    # 2. Construct corner perturbation E = e_1 e_a^T + e_a e_1^T
    # For any vectors x, y: (y^T E x) = y[0]*x[-1] + y[-1]*x[0]
    u_top = u[0, :]
    u_bot = u[-1, :]

    chi_sq_direct = 0.0
    chi_sq_parity_formula = 0.0
    max_opposite_parity_leakage = 0.0

    for i_idx in range(r):
        for j_idx in range(r, a):
            mel_direct = u_top[j_idx] * u_bot[i_idx] + u_bot[j_idx] * u_top[i_idx]
            denom_sq = (lambdas[i_idx] - lambdas[j_idx]) ** 2
            chi_sq_direct += (mel_direct ** 2) / denom_sq

            if (i_idx % 2) != (j_idx % 2):
                max_opposite_parity_leakage = max(max_opposite_parity_leakage, abs(mel_direct))
            else:
                mel_sq_formula = 4.0 * (u_top[i_idx] ** 2) * (u_top[j_idx] ** 2)
                chi_sq_parity_formula += mel_sq_formula / denom_sq

    chi_direct = math.sqrt(chi_sq_direct)
    chi_formula = math.sqrt(chi_sq_parity_formula)

    return {
        "a": float(a),
        "L": float(a - 2),
        "chi_a": chi_direct,
        "a_times_chi": a * chi_direct,
        "parity_endpoint_residual": parity_residual,
        "opposite_parity_leakage": max_opposite_parity_leakage,
        "direct_vs_parity_formula_diff": abs(chi_direct - chi_formula),
    }


def generate_convergence_table(
    a_grid: tuple[int, ...] = (8, 16, 32, 64, 128, 256, 512, 1024),
    rho: float = 0.5,
) -> list[dict[str, float]]:
    """Compute the convergence table across a_grid with 1st and 2nd order Richardson extrapolation."""
    exact_c = exact_spectral_series_constants(rho=rho)["C_exact"]
    rows: list[dict[str, float]] = []
    prev_row: dict[str, float] | None = None

    for a in a_grid:
        res = compute_chi_and_check_identities(a=a, r=2, rho=rho)
        a_chi = res["a_times_chi"]
        abs_err = abs(a_chi - exact_c)
        if prev_row is not None and abs(a - 2.0 * prev_row["a"]) < 1e-9:
            # First-order Richardson extrapolation eliminating the O(a^-1) term:
            # C_rich1(a) = 2 * (a * chi(a)) - ((a/2) * chi(a/2))
            c_rich1 = 2.0 * a_chi - prev_row["a_times_chi"]
            rich1_err = abs(c_rich1 - exact_c)
            if not math.isnan(prev_row.get("richardson_C", float("nan"))):
                # Second-order Richardson extrapolation eliminating the O(a^-2) term:
                # C_rich2(a) = (4 * C_rich1(a) - C_rich1(a/2)) / 3
                c_rich2 = (4.0 * c_rich1 - prev_row["richardson_C"]) / 3.0
                rich2_err = abs(c_rich2 - exact_c)
            else:
                c_rich2 = float("nan")
                rich2_err = float("nan")
        else:
            c_rich1 = float("nan")
            rich1_err = float("nan")
            c_rich2 = float("nan")
            rich2_err = float("nan")

        res["abs_error_to_C"] = abs_err
        res["scaled_error_a_times_diff"] = a * (a_chi - exact_c)
        res["richardson_C"] = c_rich1
        res["richardson_abs_err"] = rich1_err
        res["richardson2_C"] = c_rich2
        res["richardson2_abs_err"] = rich2_err
        rows.append(res)
        prev_row = res

    return rows


# ============================================================================
# 4. Unit Test Suite (Explicit Tolerances)
# ============================================================================
class TestMilestone1KMSSpectralSeries(unittest.TestCase):
    def test_01_exact_spectral_series_identities(self) -> None:
        exact = exact_spectral_series_constants(rho=0.5)
        num = partial_spectral_series(n_terms=200_000)
        self.assertLess(abs(exact["S1_exact"] - num["S1_richardson"]), 1e-11)
        self.assertLess(abs(exact["S2_exact"] - num["S2_richardson"]), 1e-11)
        self.assertAlmostEqual(exact["C_exact"], 2.863513045852925, places=12)

    def test_02_exact_finite_a_centrosymmetric_parity_identities(self) -> None:
        for a in (8, 16, 32, 64, 128):
            res = compute_chi_and_check_identities(a=a, r=2, rho=0.5)
            self.assertLess(res["parity_endpoint_residual"], 1e-13)
            self.assertLess(res["opposite_parity_leakage"], 1e-14)
            self.assertLess(res["direct_vs_parity_formula_diff"], 1e-14)

    def test_03_asymptotic_convergence_and_richardson_extrapolation(self) -> None:
        rows = generate_convergence_table((16, 32, 64, 128, 256, 512, 1024), rho=0.5)
        # Monotone convergence of a * chi_{a-2, 2}(a) toward C
        errors = [r["abs_error_to_C"] for r in rows]
        for k in range(len(errors) - 1):
            self.assertLess(errors[k + 1], errors[k])
        # At a = 1024:
        #   - Direct error |a*chi(a) - C| < 1.5e-2
        #   - 1st-order Richardson error |C_rich1(1024) - C| < 2.5e-4
        #   - 2nd-order Richardson error |C_rich2(1024) - C| < 1.0e-5
        self.assertLess(rows[-1]["abs_error_to_C"], 1.5e-2)
        self.assertLess(rows[-1]["richardson_abs_err"], 2.5e-4)
        self.assertLess(rows[-1]["richardson2_abs_err"], 1.0e-5)


def print_milestone1_report() -> None:
    exact = exact_spectral_series_constants(rho=0.5)
    num = partial_spectral_series(n_terms=200_000)
    print("=" * 108)
    print("MILESTONE 1 VERIFICATION: KMS SPECTRAL SERIES & COS45 FRONTIER CONSTANT C")
    print("=" * 108)
    print(f"Exact S1 = 1/16 + pi^2/48          = {exact['S1_exact']:.15f} (Num: {num['S1_richardson']:.15f})")
    print(f"Exact S2 = 1/16 + pi^2/12          = {exact['S2_exact']:.15f} (Num: {num['S2_richardson']:.15f})")
    print(f"Exact C  = 2*sqrt(18 + 15*pi^2)/9  = {exact['C_exact']:.15f}")
    print("-" * 108)
    print(
        f"{'a':>5} | {'L=a-2':>5} | {'chi_{a-2,2}(a)':>14} | {'a*chi(a)':>12} | "
        f"{'|a*chi - C|':>11} | {'Rich1 C_ext':>12} | {'|Rich1 - C|':>11} | {'Rich2 C_ext':>12} | {'|Rich2 - C|':>11}"
    )
    print("-" * 108)
    rows = generate_convergence_table((8, 16, 32, 64, 128, 256, 512, 1024), rho=0.5)
    for r in rows:
        r1_str = f"{r['richardson_C']:12.8f}" if not math.isnan(r["richardson_C"]) else f"{'N/A':>12}"
        e1_str = f"{r['richardson_abs_err']:11.3e}" if not math.isnan(r["richardson_abs_err"]) else f"{'N/A':>11}"
        r2_str = f"{r['richardson2_C']:12.8f}" if not math.isnan(r["richardson2_C"]) else f"{'N/A':>12}"
        e2_str = f"{r['richardson2_abs_err']:11.3e}" if not math.isnan(r["richardson2_abs_err"]) else f"{'N/A':>11}"
        print(
            f"{int(r['a']):5d} | {int(r['L']):5d} | {r['chi_a']:14.8f} | {r['a_times_chi']:12.8f} | "
            f"{r['abs_error_to_C']:11.3e} | {r1_str} | {e1_str} | {r2_str} | {e2_str}"
        )
    print("=" * 108)


if __name__ == "__main__":
    print_milestone1_report()
    unittest.main(verbosity=2)
