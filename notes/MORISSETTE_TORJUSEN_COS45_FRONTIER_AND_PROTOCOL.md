# Exact Resolution of the COS45 Frontier Constants and Pre-Registered 5-Gate Temporal Safety Protocol

**Author:** Marius Torjusen  
**In response to:** Louis Morissette, *"Scientific Collaboration Invitation — Marius Torjusen: COS45: Toward a Verifiable Temporal Safety Instrument for AI"* (17 October 2026) and *COS45 Hidden-Order Benchmark: Hankel–Grassmann Blind-Zone Saturation, Actionable Transfer, and Finite-Sample Audit (v1.7.0)*, Zenodo, `DOI: 10.5281/zenodo.23440691`.  
**Date:** 18 October 2026  
**Status:** Analytical Proof of Open Questions 1 & 2 (`Exact`) + Pre-Registered Collaborative Benchmark Specification (`L1` Mathematical Verification Layer)

---

## Abstract

In *COS45 v1.7.0* (`DOI: 10.5281/zenodo.23440691`), Louis Morissette formulates a deterministic Hankel–Grassmann pipeline mapping a scalar time series through a height-$a$ Hankel matrix and singular value decomposition (SVD) onto a trajectory of rank-$r$ spectral projectors $P_t \in \mathrm{Gr}(a, r)$. Using the adversarial `hidden_order` Markov process, Morissette establishes the exact second-order accessibility barrier ($\Gamma_a^{(0)} = \Gamma_a^{(1)}$ for $a \le L + 1$), the rank-2 corner perturbation at $a = L + 2$, and leaves two primary analytical questions open (`Status: Open`):

1. **Open Question 1:** An analytical proof of the actionable frontier transfer law $\chi_{a-2, 2}(a) \sim C / a$ as $a \to \infty$ and the exact closed-form value of the constant $C \approx 2.864$ (numerically extrapolated to $C \approx 2.8635$ at $a = 10^4$).
2. **Open Question 2:** The large-$a$ asymptotic closure rate of the saturated blind-zone power floor $\mathrm{Power}_{\mathrm{floor}}(a) \to \alpha$.

In Part I of this note, we resolve both open questions analytically:

$$\chi_{a-2, 2}(a) = \frac{C}{a} + \mathcal{O}(a^{-2}), \qquad \boxed{C = \frac{2\sqrt{18 + 15\pi^2}}{9} = 2.863513045853\dots}$$

and prove that the excess blind-zone power floor closes at the fourth-order rate $\mathrm{Power}_{\mathrm{floor}}(a) - \alpha = \Theta(a^{-4})$.

In Part II, we accept Morissette's invitation (*"Here is the measurement grammar. Try to break it"*) by demonstrating the three structural blind zones inherent to any standalone second-order Grassmann endpoint projector $P_t \in \mathrm{Gr}(a, r)$, and formalizing the joint **5-Gate Temporal Safety Benchmark** combining `COS45` with four orthogonal invariants:
1. **Radial Scale Complement ($\Delta_{\mathrm{scale}}$)**
2. **Geodesic-to-Chord Curvature Ratio ($\kappa_{\mathrm{path}}$)**
3. **Forward-Horizon Orbit Recurrence ($\delta_{\mathrm{orbit}}$)**
4. **Davis–Kahan Spectral-Gap Admissibility Gate (`ABSTAIN / HOLD`)**

---

## Part I: Analytical Resolution of Open Questions 1 and 2 in COS45 v1.7.0

### Theorem 1 (Exact $1/a$ Frontier Transfer Law and Closed-Form Constant $C$)

Let $\Gamma_a^{(0)} = (\rho^{|i-j|})_{1 \le i,j \le a}$ be the $a \times a$ Kac–Murdock–Szegő (KMS) Toeplitz matrix at the null parameter $\rho = 1/2$, with eigenvalues $\Lambda_1 > \Lambda_2 > \dots > \Lambda_a$ and orthonormal eigenvectors $u_1, \dots, u_a$. Let $E = e_1 e_a^\top + e_a e_1^\top$ be the rank-2 corner perturbation matrix at the actionable frontier $a = L + 2$. Then for dominant subspace rank $r = 2$, the first-order Grassmann transfer coefficient

$$\chi_{a-2, 2}(a) := \left( \sum_{i=1}^{2} \sum_{j=3}^{a} \frac{|u_j^\top E u_i|^2}{(\Lambda_i - \Lambda_j)^2} \right)^{1/2}$$

satisfies the exact asymptotic law

$$\lim_{a \to \infty} a \, \chi_{a-2, 2}(a) = C = \frac{2\sqrt{18 + 15\pi^2}}{9} \approx 2.863513045853277.$$

#### Proof

1. **Centrosymmetric Parity Selection:**  
   Because both $\Gamma_a^{(0)}$ and $E = e_1 e_a^\top + e_a e_1^\top$ commute with the order-reversing involution $J (e_k) = e_{a+1-k}$, the eigenvectors $u_k$ (ordered by descending eigenvalue $\Lambda_k$) alternate strictly in parity:
   $$u_k(a) = (-1)^{k-1} u_k(1), \qquad k = 1, 2, \dots, a.$$
   Consequently, the corner matrix element between mode $i \in \{1, 2\}$ and mode $j \in \{3, \dots, a\}$ is
   $$u_j^\top E u_i = u_j(1) u_i(a) + u_j(a) u_i(1) = u_i(1) u_j(1) \left((-1)^{i-1} + (-1)^{j-1}\right).$$
   Thus $u_j^\top E u_i = 0$ whenever $j \not\equiv i \pmod 2$, and
   $$|u_j^\top E u_i|^2 = 4 \, u_i(1)^2 u_j(1)^2 \qquad \text{whenever } j \equiv i \pmod 2.$$

2. **Kac–Murdock–Szegő Boundary and Spectral Asymptotics:**  
   The inverse $(\Gamma_a^{(0)})^{-1}$ is tridiagonal, yielding the exact KMS secular parameterization $u_k(n) = A_k \sin(n\theta_k + \phi_k)$ with spectral symbol
   $$\Lambda(\theta) = \frac{1 - \rho^2}{1 - 2\rho\cos\theta + \rho^2} = \frac{3}{5 - 4\cos\theta} \qquad (\rho = 1/2).$$
   The boundary condition at $n = 0$, $\sin\phi_k = \rho \sin(\phi_k - \theta_k)$, implies
   $$\sin^2(\theta_k + \phi_k) = \frac{\sin^2\theta_k}{1 - 2\rho\cos\theta_k + \rho^2}.$$
   For any fixed mode index $k \ge 1$ as $a \to \infty$, the quantized wavenumber is $\theta_k = \frac{k\pi}{a} + \mathcal{O}(a^{-2})$, and the normalization $A_k^2 = \frac{2}{a} + \mathcal{O}(a^{-2})$ yields the exact leading boundary weight at $n = 1$:
   $$u_k(1)^2 = \frac{2}{a} \frac{\theta_k^2}{(1 - \rho)^2} + \mathcal{O}(a^{-4}) = \frac{8 k^2 \pi^2}{a^3} + \mathcal{O}(a^{-4}).$$
   Simultaneously, expanding $\Lambda(\theta)$ around $\theta = 0$ gives
   $$\Lambda(\theta) = \frac{1+\rho}{1-\rho} - \frac{\rho(1+\rho)}{(1-\rho)^3}\theta^2 + \mathcal{O}(\theta^4) = 3 - 6\theta^2 + \mathcal{O}(\theta^4),$$
   so for fixed mode indices $i < j$:
   $$\Lambda_i - \Lambda_j = \frac{6\pi^2 (j^2 - i^2)}{a^2} + \mathcal{O}(a^{-4}).$$

3. **Termwise Cancellation of $\pi^4$ and $1/a$ Scaling:**  
   Substituting $u_i(1)^2$, $u_j(1)^2$, and $\Lambda_i - \Lambda_j$ into each same-parity term $(i, j)$ gives:
   $$\frac{|u_j^\top E u_i|^2}{(\Lambda_i - \Lambda_j)^2} = \frac{4 \left(\frac{8 i^2 \pi^2}{a^3}\right) \left(\frac{8 j^2 \pi^2}{a^3}\right)}{\left(\frac{6\pi^2 (j^2 - i^2)}{a^2}\right)^2} \left(1 + \mathcal{O}(a^{-1})\right) = \frac{1}{a^2} \cdot \frac{64}{9} \frac{i^2 j^2}{(j^2 - i^2)^2} \left(1 + \mathcal{O}(a^{-1})\right).$$
   Because the summand decays as $j^{-2}$ for large $j$, the tail $j > M$ is bounded uniformly in $a$ by $\mathcal{O}(M^{-1} a^{-2})$, justifying passage to the limit term-by-term by dominated convergence.

4. **Exact Evaluation of the Odd and Even Spectral Series:**  
   - For $i = 1$ (summing over odd $j = 2m+1 \ge 3$, i.e., $m \ge 1$):
     $$S_1 := \sum_{m=1}^{\infty} \frac{(2m+1)^2}{\left((2m+1)^2 - 1\right)^2} = \frac{1}{16} \sum_{m=1}^{\infty} \left(\frac{1}{m} + \frac{1}{m+1}\right)^2 = \frac{1}{16} + \frac{\pi^2}{48}.$$
   - For $i = 2$ (summing over even $j = 2m \ge 4$, i.e., $m \ge 2$):
     $$S_2 := \sum_{m=2}^{\infty} \frac{4(2m)^2}{\left((2m)^2 - 4\right)^2} = \sum_{m=2}^{\infty} \frac{m^2}{(m^2 - 1)^2} = \frac{1}{4}\sum_{m=2}^{\infty}\left(\frac{1}{m-1} + \frac{1}{m+1}\right)^2 = \frac{1}{16} + \frac{\pi^2}{12}.$$
   Combining both channels:
   $$C^2 = \frac{64}{9} (S_1 + S_2) = \frac{64}{9} \left(\frac{1}{8} + \frac{5\pi^2}{48}\right) = \frac{8}{9} + \frac{20\pi^2}{27} = \frac{24 + 20\pi^2}{27}.$$
   Taking the square root yields
   $$C = \frac{2\sqrt{18 + 15\pi^2}}{9} \approx 2.863513045853,$$
   matching Morissette's numerical extrapolation $C \approx 2.8635$ at $a = 10^4$ to all reported figures. $\blacksquare$

> **Remark (General KMS Parameter $\rho \in (0, 1)$):** Because $u_k(1)^2 \propto \frac{1}{(1-\rho)^2}$ and $\Lambda_i - \Lambda_j \propto \frac{\rho(1+\rho)}{(1-\rho)^3}$, the ratio $\frac{u_i(1)^2 u_j(1)^2}{(\Lambda_i - \Lambda_j)^2}$ scales as $\left(\frac{1-\rho}{\rho(1+\rho)}\right)^2$. Thus for arbitrary $\rho \in (0, 1)$:
> $$C(\rho, r=2) = \frac{8(1-\rho)}{3\rho(1+\rho)} \sqrt{\frac{1}{8} + \frac{5\pi^2}{48}} = \frac{1-\rho}{\rho(1+\rho)} \frac{\sqrt{6 + 5\pi^2}}{3\sqrt{3}}.$$

---

### Proposition 2 (Resolution of Open Question 2: $\Theta(a^{-4})$ Blind-Zone Floor Closure)

In the saturated blind zone ($L \ge 2a - 3$), the population projectors coincide ($\Gamma_a^{(0)} = \Gamma_a^{(1)}$), and the asymptotic test statistic is governed by the eigenvalues $w^{(k)} = \mathrm{eig}\left((\Sigma_k)^{1/2} M (\Sigma_k)^{1/2}\right)$ for $k \in \{0, 1\}$.

1. **Macroscopic Null Dispersion Scaling ($\Theta(a^4)$):**  
   In the Grassmann metric $M_{h,h'} = \sum_{i \le r < j} \frac{(u_j^\top E_h u_i)(u_j^\top E_{h'} u_i)}{(\Lambda_i - \Lambda_j)^2}$, macroscopic lag bands $E_h$ ($h \propto a$) couple low-lying modes with matrix elements of order $\mathcal{O}(1)$ across the $\Theta(a^{-2})$ spectral gap. Integrating over the $a - 1$ lag coordinates under $\Sigma_0$ yields dominant null weights scaling as
   $$w_1^{(0)}(a), \, w_2^{(0)}(a) = \Theta(a^4)$$
   (verified in `cos45_blind_saturation_results.json`: $w_1^{(0)}(16) = 19.306 \to w_1^{(0)}(32) = 319.185 = 16.53 \times w_1^{(0)}(16) \approx 2^4 w_1^{(0)}(16)$).

2. **Microscopic Lag Localization of $\Delta\Sigma = \Sigma_1 - \Sigma_0$ ($\mathcal{O}(1)$ Shift):**  
   By contrast, Morissette's exact closed form for $\Delta\Sigma = \Sigma_1 - \Sigma_0$ at $L \ge 2a - 3$,
   $$(\Sigma_1 - \Sigma_0)_{h,h'} = 2 \cdot 2^{-(h+h')} \sum_j \sum_{m=1}^{c_j} \binom{c_j}{m} \frac{3^m \lambda^m}{1 - \lambda^m},$$
   decays exponentially as $2^{-(h+h')}$ and is supported exclusively on microscopic lags $h, h' = \mathcal{O}(1)$. For fixed $h = \mathcal{O}(1)$, $E_h$ differs from a polynomial in the tridiagonal inverse $(\Gamma_a^{(0)})^{-1}$ only at a bounded number of corner entries. Because polynomials in $(\Gamma_a^{(0)})^{-1}$ commute with $\Gamma_a^{(0)}$, their off-diagonal elements $u_j^\top E_h u_i$ vanish identically in the bulk, leaving only boundary terms of order $u_i(1) u_j(1) = \mathcal{O}(a^{-3})$. Dividing by $\Lambda_i - \Lambda_j = \Theta(a^{-2})$ gives Jacobian entries $J_{(i,j), h} = \mathcal{O}(a^{-1})$ at fixed $h$, so the perturbation $\Delta w_i(a) = w_i^{(1)}(a) - w_i^{(0)}(a)$ remains bounded ($\mathcal{O}(1)$) as $a \to \infty$.

3. **Fourth-Order Power Dilution:**  
   Because the relative dispersion shift scales as
   $$\frac{w_i^{(1)}(a) - w_i^{(0)}(a)}{w_i^{(0)}(a)} = \Theta(a^{-4}),$$
   the survival-function expansion at the nominal $(1-\alpha)$ quantile $q(a) = \Theta(a^4)$ yields the asymptotic closure rate:
   $$\boxed{\mathrm{Power}_{\mathrm{floor}}(a) - \alpha = \Theta(a^{-4}) \qquad (a \to \infty)}$$
   (matching the numerical decay from $a=16 \to 32$ in Table 3 of *COS45 v1.7.0*: $\frac{1.1798\% - 1\%}{1.0109\% - 1\%} = \frac{0.1798}{0.01093} = 16.45 \approx 2^4$).

---

## Part II: "Try to Break It" — Three Structural Blind Zones of a Standalone Grassmann Endpoint Statistic

In his collaboration invitation, Morissette summarizes the `COS45` pipeline:
$$\text{Time Series } (s_t) \longrightarrow \text{Hankel Matrix } (X_t) \longrightarrow \text{SVD / Gram } (\hat{\Gamma}_b) \longrightarrow \text{Spectral Projector } (\hat{P}_b) \longrightarrow \text{Trajectory on } \mathrm{Gr}(a, r),$$
and highlights its core mathematical properties:
- **Scaling invariance:** $x \mapsto t x \implies P(tx) = P(x)$ for all $t \ne 0$.
- **Rank bound of the differential:** $\mathrm{rank}(D\Phi_s) \le \min\{n-1, \, r(a-r), \, 3a-5\}$.

When applied as a **temporal safety instrument for AI**, a test based solely on the Grassmann endpoint distance $T_b = b \, d_{\mathrm{geo}}(\hat{P}_b, P_0)^2$ can be defeated by three distinct adversarial transformations:

### Blind Zone A: Radial / Energy Runaway in $\ker(D\Pi_{\mathrm{Gr}})$
Because the Grassmann projection $\Pi_{\mathrm{Gr}}(\hat{\Gamma}_b) = \hat{P}_b$ quotients out the radial scale $x \mapsto e^{\alpha} x$, an AI system or dynamical process can undergo an arbitrarily large variance or norm amplification ($\mathrm{tr}(\hat{\Gamma}_b) = e^{2\alpha} \mathrm{tr}(\Gamma_0)$) while preserving $\hat{P}_b = P_0$ identically ($d_{\mathrm{geo}}(\hat{P}_b, P_0) = 0$).

### Blind Zone B: Zero-Displacement Closed Loops and High-Curvature Detours on $\mathrm{Gr}(a, r)$
The endpoint statistic $d_{\mathrm{geo}}(P_{t_1}, P_{t_0})$ measures only the minimal geodesic chord between $P_{t_0}$ and $P_{t_1}$. If a non-stationary AI trajectory undergoes a major transient structural excursion $P_{t_0} \to P_{t^*} \to P_{t_1}$ and returns to $P_{t_1} = P_{t_0}$, the net endpoint distance at $t_1$ is zero, masking the excursion unless the integrated path length is compared against the chord.

### Blind Zone C: Static Subspace Proximity vs. Dynamical Orbit Recurrence (Poincaré Trap)
Even if $d_{\mathrm{geo}}(P_t, P_{t_0}) \le \varepsilon$ at time $t$, returning near an earlier subspace projector does **not** imply that the system has returned to the same dynamical regime. Because $\mathrm{rank}(D\Phi_s)$ is bounded and higher-order lags ($h \ge a$) are projected out, two distinct dynamical laws can share the same instantaneous rank-$r$ subspace $P_t \approx P_{t_0}$ while diverging immediately over the subsequent horizon $t + \tau$ ($\tau \in [1, H]$).

---

## Part III: Pre-Registered Specification for the Joint 5-Gate Benchmark

To turn `COS45` into a complete, fail-closed temporal verification instrument, we augment the Grassmann trajectory $\{P_t\}_{t=1}^T \subset \mathrm{Gr}(a, r)$ with four complementary gates. All five quantities are computed deterministically from the same sliding Hankel window of height $a$ and width $b$:

| Gate | Symbol | Mathematical Definition | Target Vulnerability Closed |
| :--- | :--- | :--- | :--- |
| **0. Admissibility Gate (`ABSTAIN`)** | $\Delta_{\mathrm{gap}}(t)$ | $\hat{\Lambda}_r(t) - \hat{\Lambda}_{r+1}(t) \ge \tau_{\mathrm{gap}}(b, \alpha)$ | Prevents ill-conditioned subspace rotation when the Davis–Kahan denominator $\hat{\Lambda}_r - \hat{\Lambda}_{r+1}$ collapses; forces explicit `ABSTAIN / HOLD` |
| **1. COS45 Subspace Drift** | $d_{\mathrm{geo}}(t)$ | $\|\Theta(\hat{P}_t, P_0)\|_2 = \left(\sum_{k=1}^r \theta_k^2\right)^{1/2}$ | Detects dominant rank-$r$ subspace rotation beyond the accessibility frontier $a \ge L + 2$ |
| **2. Radial Scale Complement** | $\Delta_{\mathrm{scale}}(t)$ | $\left|\log \frac{\mathrm{tr}(\hat{\Gamma}_t)}{\mathrm{tr}(\Gamma_0)}\right|$ (or restricted subspace energy $\log \frac{\mathrm{tr}(\hat{P}_t \hat{\Gamma}_t)}{\mathrm{tr}(P_0 \Gamma_0)}$) | Captures amplitude/energy runaway along the fiber $\ker(D\Pi_{\mathrm{Gr}})$ invisible to scale-invariant projectors |
| **3. Geodesic / Chord Ratio** | $\kappa_{\mathrm{path}}(t_0, t_1)$ | $\frac{\sum_{t=t_0}^{t_1 - 1} d_{\mathrm{geo}}(\hat{P}_{t+1}, \hat{P}_t)}{\max\left(d_{\mathrm{chord}}(\hat{P}_{t_1}, \hat{P}_{t_0}), \, \varepsilon_0\right)}$ | Detects curved detours, transient regime excursions, and closed loops ($\hat{P}_{t_1} \approx \hat{P}_{t_0}$) on $\mathrm{Gr}(a, r)$ |
| **4. Orbit Recurrence ($\delta_{\mathrm{orbit}}$)** | $\delta_{\mathrm{orbit}}(t, t^*; H)$ | $\max_{0 \le \tau \le H} d_{\mathrm{geo}}(\hat{P}_{t+\tau}, \hat{P}_{t^*+\tau})$ given $d_{\mathrm{geo}}(\hat{P}_t, \hat{P}_{t^*}) \le \varepsilon_{\mathrm{ret}}$ | Distinguishes a genuine dynamical restoration from a false instantaneous crossing of the baseline subspace |

### Operational Decision Rule (Chronology of Evidence)

At every evaluation epoch $t$, the joint instrument executes in strict non-commutative order:

1. **Admissibility Check (`Gate 0`):**  
   If $\Delta_{\mathrm{gap}}(t) < \tau_{\mathrm{gap}}$, output **`ABSTAIN / HOLD`** (`UNIDENTIFIABLE_SUBSPACE`). No downstream geometric claim is emitted when the eigenspace is within the Davis–Kahan singular zone.
2. **State & Scale Qualification (`Gates 1 & 2`):**  
   Evaluate $(d_{\mathrm{geo}}(t), \Delta_{\mathrm{scale}}(t))$ against pre-registered thresholds $(\tau_{\mathrm{geo}}, \tau_{\mathrm{scale}})$ to classify pure structural drift, pure amplitude scaling, or coupled drift.
3. **Trajectory & Recurrence Verification (`Gates 3 & 4`):**  
   Over window $[t_0, t_1]$, evaluate $\kappa_{\mathrm{path}}(t_0, t_1)$ to detect non-geodesic detours, and whenever a return $d_{\mathrm{geo}}(\hat{P}_t, P_0) \le \varepsilon_{\mathrm{ret}}$ is observed after an excursion, require $\delta_{\mathrm{orbit}}(t, t_0; H) \le \tau_{\mathrm{orbit}}$ before certifying recovery.

---

## Conclusion & Acceptance of Collaboration

Louis — your `hidden_order` benchmark (`COS45 v1.7.0`) is a model of scientific clarity: separating `Exact`, `Numerical`, and `Open` claims without overstatement. By closing your two open analytical questions above (Theorem 1: $C = \frac{2\sqrt{18 + 15\pi^2}}{9} \approx 2.863513045853$ and Proposition 2: $\Theta(a^{-4})$ blind-zone floor dilution) and pairing `COS45` with the four complementary gates ($\Delta_{\mathrm{gap}}$, $\Delta_{\mathrm{scale}}$, $\kappa_{\mathrm{path}}$, $\delta_{\mathrm{orbit}}$), we have both the analytical foundation and the pre-registered falsification suite needed for a joint benchmark and publication.

Challenge accepted. Let us lock the signal generators and run the benchmark.
