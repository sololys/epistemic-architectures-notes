#!/usr/bin/env python3
"""
Milestone 1 & Audit Verification Script: KMS Spectral Series, Secular Bounds,
Tr(R^-2) Horizon Asymptotics, and COS45 Temporal Complementarity (7/7 Tests)
=============================================================================
Joint Technical Note & Benchmark Verification (Morissette & Torjusen, 2026)
Reference: Louis Morissette, COS45 v1.7.0 (DOI: 10.5281/zenodo.23440691)

This script reproduces and cross-checks all 7 verification points from the
public Morissette–Torjusen audit:

  1. [EXACT IDENTITY — test_01]
     Closed-form evaluation of the odd and even spectral series and both norm
     conventions (canonical Grassmann tangent norm vs. projector Frobenius norm):
       S_1    = sum_{m=1}^inf (2m+1)^2 / ((2m+1)^2 - 1)^2 = 1/16 + pi^2 / 48
       S_2    = sum_{m=2}^inf 4*(2m)^2 / ((2m)^2 - 4)^2   = 1/16 + pi^2 / 12
       C      = sqrt((64/9) * (S_1 + S_2)) = 2 * sqrt(18 + 15*pi^2) / 9
              = 2.863513045852925...
       C_Frob = sqrt(2) * C = 2 * sqrt(36 + 30*pi^2) / 9
              = 4.049618985477498...

  2. [EXACT IDENTITY — test_02]
     Centrosymmetric parity selection for the Kac–Murdock–Szego (KMS) matrix
     Gamma_a^(0) = (rho^|i-j|) and corner perturbation E = e_1 e_a^T + e_a e_1^T:
       u_k(a) = (-1)^(k-1) u_k(1)
       u_j^T E u_i = 0  for j != i (mod 2)
       |u_j^T E u_i|^2 = 4 * u_i(1)^2 * u_j(1)^2  for j == i (mod 2)

  3. [DEMONSTRATED LIMIT vs. NUMERICAL REMAINDER OBSERVATION — test_03]
     Distinguishes the proven first-order limit:
       lim_{a -> inf} a * chi_{a-2, 2}(a) = C   [Demonstrated via Tannery]
     from the second-order asymptotic remainder expansion:
       chi_{a-2, 2}(a) = C / a + O(a^-2)        [Numerical Observation / Remainder Control]
     evaluated across a in {8, 16, 32, 64, 128, 256, 512, 1024} via Richardson extrapolation.

  4. [EXACT FINITE-a MAJORANT & NORM RATIO — test_04]
     Verifies the uniform a-independent Tannery majorant:
       T_{i,j}(a) <= 1_{j == i (mod 2)} * 32 * i^2 * j^2 / (j^2 - i^2)^2
     and the exact finite-a identity ||dP||_F = sqrt(2) * ||dP||_Gr.

  5. [EXACT KMS SECULAR EQUATIONS, BOUNDARY SIGN & NORMALIZATION — test_05]
     Verifies for u_k(n) = A_k sin(n*theta_k + phi_k) at rho = 1/2:
       - Boundary condition at n = 0: sin(phi_k) = rho * sin(theta_k + phi_k)
         <=> tan(phi_k) = sin(theta_k) / (2 - cos(theta_k)) > 0 on (0, pi).
       - Phase derivative bound: -1/3 <= phi'(theta) = (2*cos(theta) - 1)/(5 - 4*cos(theta)) <= 1/3.
       - Exact normalization identity:
         1 / A_k^2 = (a + 1)/2 + phi'(theta_k) = a/2 + 3 / (2*(5 - 4*cos(theta_k))) > a/2 > (a - 1)/2.

  6. [EXACT KMS Tr(R^-2) IDENTITY & SINGULAR HORIZON LIMITS — test_06]
     For the n x n KMS matrix R_{ij} = rho^|i-j| (n >= 2), verifies the exact formula:
       Tr(R^-2) = (2 + (n - 2)*(1 + rho^2)^2 + 2*(n - 1)*rho^2) / (1 - rho^2)^2
     and its two distinct asymptotic regimes:
       - lim_{rho -> 0}   (1 - rho^2)   * Tr(R^-2) = n
       - lim_{rho -> 1^-} (1 - rho^2)^2 * Tr(R^-2) = 6n - 8
         (while (1 - rho^2) * Tr(R^-2) diverges as (6n - 8)/(1 - rho^2) -> +inf).

  7. [EQUAL-MEAN / EQUAL-VARIANCE TEMPORAL DEPENDENCY BENCHMARK — test_07]
     Implements Louis Morissette's proposed complementary signal test: two signals
     of identical mean and identical variance with distinct temporal dependencies
     (including a lag-(a-1) corner dependency invisible to lower-order lags and a
     pure radial scale shock), verifying how COS45 (Gate 1) and the CVTK/NLK
     admissibility/scale/orbit gates (Gates 0, 2, 4) complement each other.
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
    """Return the exact analytical series values S_1, S_2, C^2, C(rho, r=2), and C_Frob."""
    s1_exact = (1.0 / 16.0) + (math.pi ** 2) / 48.0
    s2_exact = (1.0 / 16.0) + (math.pi ** 2) / 12.0
    prefactor = ((4.0 * (1.0 - rho)) / (rho * (1.0 + rho))) ** 2
    c_sq_exact = prefactor * (s1_exact + s2_exact)
    c_exact = math.sqrt(c_sq_exact)
    c_frob_exact = math.sqrt(2.0) * c_exact
    return {
        "S1_exact": s1_exact,
        "S2_exact": s2_exact,
        "C_squared_exact": c_sq_exact,
        "C_exact": c_exact,
        "C_Frob_exact": c_frob_exact,
    }


def partial_spectral_series(n_terms: int = 200_000) -> dict[str, float]:
    """Compute high-precision partial sums of S_1 and S_2 for direct numerical check."""
    m1 = np.arange(1, n_terms + 1, dtype=np.float64)
    odd = 2.0 * m1 + 1.0
    s1_num = float(np.sum((odd ** 2) / ((odd ** 2 - 1.0) ** 2)))
    s1_tail_corr = 1.0 / (4.0 * (n_terms + 0.5))

    m2 = np.arange(2, n_terms + 2, dtype=np.float64)
    even = 2.0 * m2
    s2_num = float(np.sum(4.0 * (even ** 2) / ((even ** 2 - 4.0) ** 2)))
    s2_tail_corr = 1.0 / (n_terms + 1.5)

    return {
        "S1_partial": s1_num,
        "S1_richardson": s1_num + s1_tail_corr,
        "S2_partial": s2_num,
        "S2_richardson": s2_num + s2_tail_corr,
    }


# ============================================================================
# 3. Direct Numerical KMS Matrix, Secular Equations & Tr(R^-2)
# ============================================================================
def build_kms_matrix(a: int, rho: float = 0.5) -> np.ndarray:
    """Construct the exact a x a Kac-Murdock-Szego matrix R_{i,j} = rho^|i-j|."""
    idx = np.arange(a)
    return np.power(rho, np.abs(idx[:, None] - idx[None, :])).astype(np.float64)


def kms_trace_inv_squared_exact(n: int, rho: float) -> float:
    """
    Exact closed-form formula for Tr(R^-2) of the n x n KMS matrix R_{i,j} = rho^|i-j| (n >= 2):
      Tr(R^-2) = (2 + (n - 2)*(1 + rho^2)^2 + 2*(n - 1)*rho^2) / (1 - rho^2)^2
    """
    if n < 2:
        raise ValueError("KMS Tr(R^-2) formula requires n >= 2.")
    num = 2.0 + (n - 2.0) * ((1.0 + rho * rho) ** 2) + 2.0 * (n - 1.0) * (rho * rho)
    den = (1.0 - rho * rho) ** 2
    return num / den


def compute_chi_and_check_identities(a: int, r: int = 2, rho: float = 0.5) -> dict[str, float]:
    """
    Compute chi_{a-2, r}(a) directly from the eigendecomposition of Gamma_a^(0)
    and verify the exact centrosymmetric parity identities at finite a.
    """
    gamma = build_kms_matrix(a, rho=rho)
    evals, evecs = np.linalg.eigh(gamma)
    order = np.argsort(evals)[::-1]
    lambdas = evals[order]
    u = evecs[:, order]

    signs = np.array([1.0 if (k_idx % 2 == 0) else -1.0 for k_idx in range(a)])
    parity_residual = float(np.max(np.abs(u[-1, :] - signs * u[0, :])))

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
            c_rich1 = 2.0 * a_chi - prev_row["a_times_chi"]
            rich1_err = abs(c_rich1 - exact_c)
            if not math.isnan(prev_row.get("richardson_C", float("nan"))):
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


def grassmann_geodesic_distance(p1: np.ndarray, p2: np.ndarray, r: int = 2) -> float:
    """Compute the canonical Grassmann geodesic distance ||Theta(P1, P2)||_2 from rank-r projectors."""
    evals1, evecs1 = np.linalg.eigh(p1)
    u1 = evecs1[:, np.argsort(evals1)[::-1][:r]]
    evals2, evecs2 = np.linalg.eigh(p2)
    u2 = evecs2[:, np.argsort(evals2)[::-1][:r]]
    svals = np.linalg.svd(u1.T @ u2, compute_uv=False)
    svals_clipped = np.clip(svals, -1.0, 1.0)
    thetas = np.arccos(svals_clipped)
    return float(np.linalg.norm(thetas))


# ============================================================================
# 4. Unit Test Suite (7/7 Explicit Audit Tests)
# ============================================================================
class TestMilestone1KMSSpectralSeries(unittest.TestCase):
    def test_01_exact_spectral_series_and_norm_constants(self) -> None:
        """Test 1: Exact series S_1, S_2 and constants C (Grassmann) vs C_Frob = sqrt(2)*C."""
        exact = exact_spectral_series_constants(rho=0.5)
        num = partial_spectral_series(n_terms=200_000)
        self.assertLess(abs(exact["S1_exact"] - num["S1_richardson"]), 1e-11)
        self.assertLess(abs(exact["S2_exact"] - num["S2_richardson"]), 1e-11)
        self.assertAlmostEqual(exact["C_exact"], 2.863513045852925, places=12)
        self.assertAlmostEqual(exact["C_Frob_exact"], 4.049618985477498, places=12)
        self.assertLess(abs(exact["C_Frob_exact"] - math.sqrt(2.0) * exact["C_exact"]), 1e-15)

    def test_02_exact_finite_a_centrosymmetric_parity_identities(self) -> None:
        """Test 2: Exact centrosymmetric parity u_k(a) = (-1)^(k-1) u_k(1) and selection rule."""
        for a in (8, 16, 32, 64, 128):
            res = compute_chi_and_check_identities(a=a, r=2, rho=0.5)
            self.assertLess(res["parity_endpoint_residual"], 1e-13)
            self.assertLess(res["opposite_parity_leakage"], 1e-14)
            self.assertLess(res["direct_vs_parity_formula_diff"], 1e-14)

    def test_03_asymptotic_convergence_and_richardson_extrapolation(self) -> None:
        """Test 3: Convergence of a*chi(a) -> C and numerical 1/a remainder observation."""
        rows = generate_convergence_table((16, 32, 64, 128, 256, 512, 1024), rho=0.5)
        errors = [r["abs_error_to_C"] for r in rows]
        for k in range(len(errors) - 1):
            self.assertLess(errors[k + 1], errors[k])
        self.assertLess(rows[-1]["abs_error_to_C"], 1.5e-2)
        self.assertLess(rows[-1]["richardson_abs_err"], 2.5e-4)
        self.assertLess(rows[-1]["richardson2_abs_err"], 1.0e-5)

    def test_04_tannery_uniform_tail_majorant_and_frobenius_norm(self) -> None:
        """Test 4: Uniform Tannery majorant M_{i,j} and exact ||dP||_F = sqrt(2)*||dP||_Gr."""
        for a in (16, 32, 64, 128, 256):
            gamma = build_kms_matrix(a, rho=0.5)
            evals, evecs = np.linalg.eigh(gamma)
            order = np.argsort(evals)[::-1]
            lambdas = evals[order]
            u = evecs[:, order]

            dp_eigen = np.zeros((a, a), dtype=np.float64)
            u_top = u[0, :]
            u_bot = u[-1, :]
            r = 2
            for i_idx in range(r):
                i_mode = i_idx + 1
                for j_idx in range(r, a):
                    j_mode = j_idx + 1
                    mel = u_top[j_idx] * u_bot[i_idx] + u_bot[j_idx] * u_top[i_idx]
                    val = mel / (lambdas[i_idx] - lambdas[j_idx])
                    dp_eigen[j_idx, i_idx] = val
                    dp_eigen[i_idx, j_idx] = val

                    term_a_sq = (a ** 2) * (val ** 2)
                    majorant = 32.0 * (i_mode ** 2) * (j_mode ** 2) / ((j_mode ** 2 - i_mode ** 2) ** 2)
                    self.assertLessEqual(term_a_sq, majorant)

            chi_gr = math.sqrt(float(np.sum(dp_eigen[r:, :r] ** 2)))
            frob_dp = float(np.linalg.norm(dp_eigen, ord="fro"))
            self.assertLess(abs(frob_dp - math.sqrt(2.0) * chi_gr), 1e-14)

    def test_05_secular_normalization_phase_derivative_and_boundary_sign(self) -> None:
        """
        Test 5: Verifies the KMS secular equations at rho = 1/2 (audit corrections):
          - Boundary sign at n = 0: sin(phi_k) = rho * sin(theta_k + phi_k)
            <=> tan(phi_k) = sin(theta_k) / (2 - cos(theta_k)) > 0 on (0, pi).
          - Phase derivative bound on [0, pi]:
            -1/3 <= phi'(theta) = (2*cos(theta) - 1)/(5 - 4*cos(theta)) <= 1,
            giving a + 1/3 <= g'(theta) = a + 1 + 2*phi'(theta) <= a + 3.
          - Exact normalization: 1/A_k^2 = (1/2)*g'(theta_k) = (a+1)/2 + phi'(theta_k)
            = a/2 + 3/(2*(5 - 4*cos(theta_k))) >= a/2 + 1/6 > (a - 1)/2.
        """
        rho = 0.5
        thetas = np.linspace(0.0, math.pi, 10_001)
        phi_prime = (2.0 * np.cos(thetas) - 1.0) / (5.0 - 4.0 * np.cos(thetas))
        # At theta = 0, phi'(0) = +1; at theta = pi, phi'(pi) = -1/3
        self.assertAlmostEqual(float(np.max(phi_prime)), 1.0, places=14)
        self.assertAlmostEqual(float(np.min(phi_prime)), -1.0 / 3.0, places=14)

        for a in (8, 16, 32, 64):
            gamma = build_kms_matrix(a, rho=rho)
            evals, evecs = np.linalg.eigh(gamma)
            lambdas = evals[::-1]
            u_mat = evecs[:, ::-1]
            ns = np.arange(1, a + 1, dtype=np.float64)

            for k_idx in range(a):
                k = k_idx + 1
                lam = float(lambdas[k_idx])
                cos_th = (5.0 - 3.0 / lam) / 4.0
                th = math.acos(max(-1.0, min(1.0, cos_th)))
                phi = math.atan2(math.sin(th), 2.0 - math.cos(th))

                # 1. Positivity of phi on (0, pi) and boundary condition sin(phi) = rho*sin(th + phi)
                self.assertGreater(phi, 0.0)
                self.assertLess(abs(math.sin(phi) - rho * math.sin(th + phi)), 1e-14)

                # 2. Quantization (a + 1)*theta_k + 2*phi_k = k*pi
                quant_res = abs(((a + 1) * th + 2.0 * phi) - k * math.pi)
                self.assertLess(quant_res, 1e-10)

                # 3. Exact normalization 1/A_k^2 = a/2 + 3/(2*(5 - 4*cos(th))) = (a+1)/2 + phi'(th)
                sum_sin_sq = float(np.sum(np.sin(ns * th + phi) ** 2))
                exact_inv_a_sq = (a / 2.0) + 1.5 / (5.0 - 4.0 * math.cos(th))
                self.assertLess(abs(sum_sin_sq - exact_inv_a_sq), 1e-9)
                self.assertGreaterEqual(exact_inv_a_sq, (a / 2.0) + (1.0 / 6.0) - 1e-12)
                self.assertGreater(exact_inv_a_sq, (a - 1.0) / 2.0)

                # 4. Match normalized eigenvector endpoint weight u_k(1)^2
                a_k_sq = 1.0 / exact_inv_a_sq
                u1_sq_secular = 4.0 * a_k_sq * (math.sin(th) ** 2) / (5.0 - 4.0 * math.cos(th))
                u1_sq_num = float(u_mat[0, k_idx] ** 2)
                self.assertLess(abs(u1_sq_secular - u1_sq_num), 1e-10)

    def test_06_kms_inverse_squared_trace_identities_and_limits(self) -> None:
        """
        Test 6: Verifies Louis Morissette's exact KMS Tr(R^-2) formula for n >= 2:
          Tr(R^-2) = (2 + (n - 2)*(1 + rho^2)^2 + 2*(n - 1)*rho^2) / (1 - rho^2)^2
        and its two limits:
          - lim_{rho -> 0}   (1 - rho^2)   * Tr(R^-2) = n
          - lim_{rho -> 1^-} (1 - rho^2)^2 * Tr(R^-2) = 6n - 8
        """
        for n in (2, 4, 8, 16, 32):
            for rho in (0.1, 0.25, 0.5, 0.75, 0.9):
                r_mat = build_kms_matrix(n, rho=rho)
                r_inv = np.linalg.inv(r_mat)
                tr_inv_sq_num = float(np.trace(r_inv @ r_inv))
                tr_inv_sq_exact = kms_trace_inv_squared_exact(n, rho)
                self.assertLess(abs(tr_inv_sq_num - tr_inv_sq_exact) / tr_inv_sq_exact, 1e-12)

            # Limit rho -> 0: (1 - rho^2) * Tr(R^-2) -> n
            rho_small = 1e-7
            lim_rho0 = (1.0 - rho_small ** 2) * kms_trace_inv_squared_exact(n, rho_small)
            self.assertLess(abs(lim_rho0 - float(n)), 1e-10)

            # Limit rho -> 1^-: (1 - rho^2)^2 * Tr(R^-2) -> 6n - 8
            rho_near1 = 1.0 - 1e-8
            lim_rho1 = ((1.0 - rho_near1 ** 2) ** 2) * kms_trace_inv_squared_exact(n, rho_near1)
            self.assertLess(abs(lim_rho1 - float(6 * n - 8)), 5e-6)

    def test_07_temporal_stability_gate_and_cos45_complementarity(self) -> None:
        """
        Test 7: Equal-mean, equal-variance temporal dependency benchmark (Morissette & Torjusen).
        Constructs covariance matrices corresponding to signals with identical mean (0)
        and identical variance (1):
          - Case A (Temporal dependency change at unit variance): KMS(rho=0.5) vs perturbed
            corner/spectral structure normalized to identical diagonal variance 1.0.
            Scalar variance gate Delta_scale == 0, while COS45 geodesic drift d_geo > 0.
          - Case B (Pure radial variance shock e^(2*alpha) * Gamma_0):
            COS45 projector is invariant (d_geo == 0), while Gate 2 radial scale
            Delta_scale = |log(tr(Gamma_1)/tr(Gamma_0))| > 0 detects the shock.
        """
        a = 16
        r = 2
        rho = 0.5
        gamma_0 = build_kms_matrix(a, rho=rho)
        evals0, evecs0 = np.linalg.eigh(gamma_0)
        u0 = evecs0[:, np.argsort(evals0)[::-1][:r]]
        p0 = u0 @ u0.T

        # Case A: Equal mean (0) and equal variance (diag = 1, trace = a), but distinct
        # temporal dependency (corner lag perturbation E = e_1 e_a^T + e_a e_1^T).
        eps = 0.01
        e_corner = np.zeros((a, a), dtype=np.float64)
        e_corner[0, a - 1] = 1.0
        e_corner[a - 1, 0] = 1.0
        gamma_temporal = gamma_0 + eps * e_corner

        # Verify identical variance (diagonal entries == 1.0) and identical trace == a:
        self.assertLess(float(np.max(np.abs(np.diag(gamma_temporal) - 1.0))), 1e-15)
        delta_scale_case_a = abs(math.log(float(np.trace(gamma_temporal)) / float(np.trace(gamma_0))))
        self.assertLess(delta_scale_case_a, 1e-15)

        # COS45 projector detects the temporal dependency change cleanly:
        evals_t, evecs_t = np.linalg.eigh(gamma_temporal)
        ut = evecs_t[:, np.argsort(evals_t)[::-1][:r]]
        pt = ut @ ut.T
        d_geo_case_a = grassmann_geodesic_distance(p0, pt, r=r)
        chi_expected = compute_chi_and_check_identities(a=a, r=r, rho=rho)["chi_a"]
        self.assertGreater(d_geo_case_a, 1e-3)
        self.assertLess(abs(d_geo_case_a - eps * chi_expected) / (eps * chi_expected), 5e-3)

        # Case B: Pure radial scale amplification (variance shock) with identical temporal correlation
        scale_factor = 2.25
        gamma_scaled = scale_factor * gamma_0
        evals_s, evecs_s = np.linalg.eigh(gamma_scaled)
        us = evecs_s[:, np.argsort(evals_s)[::-1][:r]]
        ps = us @ us.T
        d_geo_case_b = grassmann_geodesic_distance(p0, ps, r=r)
        delta_scale_case_b = abs(math.log(float(np.trace(gamma_scaled)) / float(np.trace(gamma_0))))
        self.assertLess(d_geo_case_b, 1e-14)
        self.assertAlmostEqual(delta_scale_case_b, math.log(scale_factor), places=12)


def print_milestone1_report() -> None:
    exact = exact_spectral_series_constants(rho=0.5)
    num = partial_spectral_series(n_terms=200_000)
    print("=" * 108)
    print("MILESTONE 1 & AUDIT VERIFICATION: KMS SPECTRAL SERIES & COS45 FRONTIER CONSTANT C (7/7 TESTS)")
    print("=" * 108)
    print(f"Exact S1     = 1/16 + pi^2/48          = {exact['S1_exact']:.15f} (Num: {num['S1_richardson']:.15f})")
    print(f"Exact S2     = 1/16 + pi^2/12          = {exact['S2_exact']:.15f} (Num: {num['S2_richardson']:.15f})")
    print(f"Exact C      = 2*sqrt(18 + 15*pi^2)/9  = {exact['C_exact']:.15f} [Canonical Grassmann norm]")
    print(f"Exact C_Frob = sqrt(2) * C             = {exact['C_Frob_exact']:.15f} [Projector Frobenius norm]")
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
