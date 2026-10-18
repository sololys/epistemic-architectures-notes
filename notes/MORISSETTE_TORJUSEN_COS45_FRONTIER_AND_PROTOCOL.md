# Exact Resolution of the COS45 Frontier Constants and Pre-Registered 5-Gate Temporal Safety Protocol

**Author:** Marius Torjusen  
**In response to:** Louis Morissette, *"Scientific Collaboration Invitation — Marius Torjusen: COS45: Toward a Verifiable Temporal Safety Instrument for AI"* (17 October 2026) and *COS45 Hidden-Order Benchmark: Hankel–Grassmann Blind-Zone Saturation, Actionable Transfer, and Finite-Sample Audit (v1.7.0)*, Zenodo, `DOI: 10.5281/zenodo.23440691`.  
**Date:** 18 October 2026  
**Status Discipline (per Joint Co-Authorship Protocol):**
- **`[Exact Identity]`**: Algebraic or spectral identities holding exactly for every finite $a \ge 4$ or for closed-form infinite series.
- **`[Asymptotic Statement — Under Joint Examination]`**: Large-$a$ ($a \to \infty$) limiting laws and leading constants under independent co-author verification prior to benchmark freeze.
- **`[Numerical Observation]`**: Finite-$a$ direct matrix calculations, residual tables, and Richardson extrapolations produced by [`tools/verify_cos45_kms_spectral_series.py`](../tools/verify_cos45_kms_spectral_series.py).

---

## Milestone 0: Canonical Parameter Definitions $(L, a, r, b, H)$

To ensure identical conventions across both independent implementations prior to freezing the benchmark grid, we fix the five structural parameters:

| Parameter | Domain | Definition & Role in the Joint Pipeline |
| :--- | :--- | :--- |
| **$L$** | $\mathbb{Z}_{\ge 1}$ | **Interaction Lag Order:** The correlation/interaction horizon of the underlying time-series generator (e.g., in `hidden_order`, the lag $L$ at which the higher-order parity / corner perturbation acts; the second-order blind zone holds for $a \le L + 1$, and the actionable frontier opens at $a = L + 2$). |
| **$a$** | $\mathbb{Z}_{\ge 4}$ | **Hankel Window Height (Embedding Dimension):** Number of rows in the sliding Hankel matrix $X_t \in \mathbb{R}^{a \times b}$. Determines the ambient dimension of the empirical Gram/covariance matrix $\hat{\Gamma}_b \in \mathbb{R}^{a \times a}$ and the Grassmann manifold $\mathrm{Gr}(a, r)$. |
| **$r$** | $1 \le r < a$ | **Dominant Subspace Rank:** Dimension of the spectral projector $\hat{P}_t = \sum_{i=1}^r \hat{u}_i \hat{u}_i^\top \in \mathrm{Gr}(a, r)$ extracted from the top $r$ eigenvectors of $\hat{\Gamma}_b$ ($r = 2$ in the baseline frontier audit). |
| **$b$** | $\mathbb{Z}_{\ge a}$ | **Hankel Window Width (Sample Horizon per Window):** Number of lagged column vectors aggregated per window $X_t \in \mathbb{R}^{a \times b}$ to form $\hat{\Gamma}_b = \frac{1}{b} X_t X_t^\top$, governing the finite-sample scaling $T_b = b \, d_{\mathrm{geo}}(\hat{P}_b, P_0)^2$. |
| **$H$** | $\mathbb{Z}_{\ge 1}$ | **Forward Recurrence Horizon:** Number of forward steps $\tau \in \{1, \dots, H\}$ over which the orbit-recurrence gate $\delta_{\mathrm{orbit}}(t, t^*; H) = \max_{0 \le \tau \le H} d_{\mathrm{geo}}(\hat{P}_{t+\tau}, \hat{P}_{t^*+\tau})$ verifies that an apparent return $d_{\mathrm{geo}}(\hat{P}_t, \hat{P}_{t^*}) \le \varepsilon_{\mathrm{ret}}$ is a true dynamical restoration rather than a transient subspace crossing. |

---

## Abstract

In *COS45 v1.7.0* (`DOI: 10.5281/zenodo.23440691`), Louis Morissette formulates a deterministic Hankel–Grassmann pipeline mapping a scalar time series through a height-$a$ Hankel matrix and singular value decomposition (SVD) onto a trajectory of rank-$r$ spectral projectors $P_t \in \mathrm{Gr}(a, r)$. Using the adversarial `hidden_order` Markov process, Morissette establishes the exact second-order accessibility barrier ($\Gamma_a^{(0)} = \Gamma_a^{(1)}$ for $a \le L + 1$), the rank-2 corner perturbation at $a = L + 2$, and leaves two primary analytical questions open (`Status: Open`):

1. **Open Question 1:** An analytical proof of the actionable frontier transfer law $\chi_{a-2, 2}(a) \sim C / a$ as $a \to \infty$ and the exact closed-form value of the constant $C \approx 2.864$ (numerically extrapolated to $C \approx 2.8635$ at $a = 10^4$).
2. **Open Question 2:** The large-$a$ asymptotic closure rate of the saturated blind-zone power floor $\mathrm{Power}_{\mathrm{floor}}(a) \to \alpha$.

In Part I of this note, we present the analytical derivations for both open questions (`Status: Asymptotic Statement — Under Joint Examination`):

$$\chi_{a-2, 2}(a) = \frac{C}{a} + \mathcal{O}(a^{-2}), \qquad \boxed{C = \frac{2\sqrt{18 + 15\pi^2}}{9} = 2.863513045853\dots}$$

and show that the excess blind-zone power floor closes at the fourth-order rate $\mathrm{Power}_{\mathrm{floor}}(a) - \alpha = \Theta(a^{-4})$.

In Part II, we accept Morissette's invitation (*"Here is the measurement grammar. Try to break it"*) by demonstrating the three structural blind zones inherent to any standalone second-order Grassmann endpoint projector $P_t \in \mathrm{Gr}(a, r)$, and formalizing the joint **5-Gate Temporal Safety Benchmark** combining `COS45` with four orthogonal invariants:
1. **Radial Scale Complement ($\Delta_{\mathrm{scale}}$)**
2. **Geodesic-to-Chord Curvature Ratio ($\kappa_{\mathrm{path}}$)**
3. **Forward-Horizon Orbit Recurrence ($\delta_{\mathrm{orbit}}$)**
4. **Davis–Kahan Spectral-Gap Admissibility Gate (`ABSTAIN / HOLD`)**

---

## Part I: Analytical Derivation & Milestone 1 Numerical Verification of Open Questions 1 and 2

### Proposition 1 (KMS Frontier Transfer Law and Constant $C$ — `[Under Joint Examination]`)

Let $\Gamma_a^{(0)} = (\rho^{|i-j|})_{1 \le i,j \le a}$ be the $a \times a$ Kac–Murdock–Szegő (KMS) Toeplitz matrix at the null parameter $\rho = 1/2$, with eigenvalues $\Lambda_1 > \Lambda_2 > \dots > \Lambda_a$ and orthonormal eigenvectors $u_1, \dots, u_a$. Let $E = e_1 e_a^\top + e_a e_1^\top$ be the rank-2 corner perturbation matrix at the actionable frontier $a = L + 2$. Then for dominant subspace rank $r = 2$, the first-order Grassmann transfer coefficient

$$\chi_{a-2, 2}(a) := \left( \sum_{i=1}^{2} \sum_{j=3}^{a} \frac{|u_j^\top E u_i|^2}{(\Lambda_i - \Lambda_j)^2} \right)^{1/2}$$

satisfies the asymptotic law

$$\lim_{a \to \infty} a \, \chi_{a-2, 2}(a) = C = \frac{2\sqrt{18 + 15\pi^2}}{9} \approx 2.863513045852925.$$

#### Step-by-Step Derivation (Separated by Status)

1. **Centrosymmetric Parity Selection (`[Exact Identity for all finite a >= 4]`):**  
   Because both $\Gamma_a^{(0)}$ and $E = e_1 e_a^\top + e_a e_1^\top$ commute with the order-reversing involution $J (e_k) = e_{a+1-k}$ and the spectrum of $\Gamma_a^{(0)}$ is strictly simple, the eigenvectors $u_k$ (ordered by descending eigenvalue $\Lambda_k$) alternate strictly in parity:
   $$u_k(a) = (-1)^{k-1} u_k(1), \qquad k = 1, 2, \dots, a.$$
   Consequently, the corner matrix element between mode $i \in \{1, 2\}$ and mode $j \in \{3, \dots, a\}$ is
   $$u_j^\top E u_i = u_j(1) u_i(a) + u_j(a) u_i(1) = u_i(1) u_j(1) \left((-1)^{i-1} + (-1)^{j-1}\right).$$
   Thus $u_j^\top E u_i = 0$ identically whenever $j \not\equiv i \pmod 2$, and
   $$|u_j^\top E u_i|^2 = 4 \, u_i(1)^2 u_j(1)^2 \qquad \text{whenever } j \equiv i \pmod 2.$$

2. **Kac–Murdock–Szegő Boundary and Spectral Asymptotics (`[Asymptotic Statement — Under Joint Examination]`):**  
   The inverse $(\Gamma_a^{(0)})^{-1}$ is tridiagonal, yielding the exact KMS secular parameterization $u_k(n) = A_k \sin(n\theta_k + \phi_k)$ with spectral symbol
   $$\Lambda(\theta) = \frac{1 - \rho^2}{1 - 2\rho\cos\theta + \rho^2} = \frac{3}{5 - 4\cos\theta} \qquad (\rho = 1/2).$$
   The boundary condition at $n = 0$, $\sin\phi_k = \rho \sin(\phi_k - \theta_k)$, implies
   $$\sin^2(\theta_k + \phi_k) = \frac{\sin^2\theta_k}{1 - 2\rho\cos\theta_k + \rho^2}.$$
   For any fixed mode index $k \ge 1$ as $a \to \infty$, the quantized wavenumber is $\theta_k = \frac{k\pi}{a} + \mathcal{O}(a^{-2})$, and the normalization $A_k^2 = \frac{2}{a} + \mathcal{O}(a^{-2})$ yields the leading boundary weight at $n = 1$:
   $$u_k(1)^2 = \frac{2}{a} \frac{\theta_k^2}{(1 - \rho)^2} + \mathcal{O}(a^{-4}) = \frac{8 k^2 \pi^2}{a^3} + \mathcal{O}(a^{-4}).$$
   Simultaneously, expanding $\Lambda(\theta)$ around $\theta = 0$ gives
   $$\Lambda(\theta) = \frac{1+\rho}{1-\rho} - \frac{\rho(1+\rho)}{(1-\rho)^3}\theta^2 + \mathcal{O}(\theta^4) = 3 - 6\theta^2 + \mathcal{O}(\theta^4),$$
   so for fixed mode indices $i < j$:
   $$\Lambda_i - \Lambda_j = \frac{6\pi^2 (j^2 - i^2)}{a^2} + \mathcal{O}(a^{-4}).$$

3. **Termwise Cancellation of $\pi^4$, $1/a$ Scaling, and Analytical Proof of Uniform Tail Control via Tannery's Theorem (`[Exact Finite-a Majorant Proof + Asymptotic Limit]`):**  
   Define the scaled finite-$a$ summand for $i \in \{1, 2\}$ and $3 \le j \le a$ with its parity indicator explicitly retained:
   $$T_{i,j}(a) := a^2 \frac{|u_j^\top E u_i|^2}{(\Lambda_i - \Lambda_j)^2} = \begin{cases} 0, & \text{if } j \not\equiv i \pmod 2, \\[6pt] \displaystyle a^2 \frac{4 u_i(1)^2 u_j(1)^2}{(\Lambda_i - \Lambda_j)^2}, & \text{if } j \equiv i \pmod 2. \end{cases}$$
   For fixed $i \in \{1, 2\}$ and fixed $j \ge 3$ with $j \equiv i \pmod 2$, substituting the fixed-mode asymptotics from Step 2 yields the pointwise limit:
   $$\lim_{a \to \infty} T_{i,j}(a) = \frac{4 \left(8 i^2 \pi^2\right) \left(8 j^2 \pi^2\right)}{\left(6\pi^2 (j^2 - i^2)\right)^2} = \frac{64}{9} \frac{i^2 j^2}{(j^2 - i^2)^2}.$$
   To rigorously justify interchanging $\lim_{a \to \infty}$ with $\sum_{j=3}^{a}$, we prove an **analytic, $a$-independent summable majorant** valid across the entire index range $a \ge 8$, $i \in \{1, 2\}$, and $3 \le j \le a$:
   - **Step 3a (Exact KMS Secular Equations and Normalization Bound):** At $\rho = 1/2$, the eigenvectors $u_k(n) = A_k \sin(n\theta_k + \phi_k)$ satisfy the boundary relation $\tan\phi_k = \frac{\sin\theta_k}{2 - \cos\theta_k} > 0$ and quantization $g(\theta_k) := (a+1)\theta_k + 2\phi_k = k\pi$, with $\Lambda_k = \frac{3}{5 - 4\cos\theta_k}$ and $u_k(1)^2 = \frac{4 A_k^2 \sin^2\theta_k}{5 - 4\cos\theta_k}$. Summing $\sin^2(n\theta_k + \phi_k)$ from $n=1$ to $a$ gives the exact normalization identity
     $$\frac{1}{A_k^2} = \frac{a - 1}{2} + \frac{3}{2(5 - 4\cos\theta_k)} > \frac{a - 1}{2} \implies a A_k^2 < \frac{2a}{a - 1} \le \frac{16}{7} \qquad (\forall a \ge 8, \; \forall k \in \{1, \dots, a\}).$$
   - **Step 3b (Exact Half-Angle Algebraic Reduction):** Let $s_k := \sin(\theta_k/2) \in (0, 1)$. Then $\sin^2\theta_k (5 - 4\cos\theta_k) = 4 s_k^2 (1 - s_k^2)(1 + 8s_k^2)$ and $\cos\theta_i - \cos\theta_j = 2(s_j^2 - s_i^2)$. Substituting these into $T_{i,j}(a)$ for $j \equiv i \pmod 2$ cancels one power of $(5 - 4\cos\theta_k)$ from the eigenvalue gap denominator $\Lambda_i - \Lambda_j = \frac{12(\cos\theta_i - \cos\theta_j)}{(5-4\cos\theta_i)(5-4\cos\theta_j)}$:
     $$T_{i,j}(a) = \frac{16}{9} (a A_i^2)(a A_j^2) \, P(s_i) P(s_j) \frac{s_i^2 s_j^2}{(s_j^2 - s_i^2)^2},$$
     where $P(s) := (1 - s^2)(1 + 8s^2) = \frac{81}{32} - 8\left(s^2 - \frac{7}{16}\right)^2 \le \frac{81}{32}$ for all $s \in [0, 1]$.
   - **Step 3c (Elimination of the Upper-Edge Singularity via Half-Angle Addition):** Because $0 < \frac{\theta_i}{2} < \frac{\theta_j}{2} < \frac{\pi}{2}$, both terms in $\sin\left(\frac{\theta_j + \theta_i}{2}\right) = s_j \cos(\theta_i/2) + \cos(\theta_j/2) s_i$ are strictly positive, so $\sin\left(\frac{\theta_j + \theta_i}{2}\right) > s_j \cos(\theta_i/2)$. Therefore,
     $$s_j^2 - s_i^2 = \sin\left(\frac{\theta_j - \theta_i}{2}\right) \sin\left(\frac{\theta_j + \theta_i}{2}\right) > s_j \cos(\theta_i/2) \sin\left(\frac{\theta_j - \theta_i}{2}\right),$$
     which cancels $s_j^2$ identically across the entire spectrum $3 \le j \le a$:
     $$\frac{s_i^2 s_j^2}{(s_j^2 - s_i^2)^2} < \frac{\tan^2(\theta_i/2)}{\sin^2\left(\frac{\theta_j - \theta_i}{2}\right)}.$$
   - **Step 3d (Mean Value Theorem on Wavenumber Spacing and Jordan's Inequality):** Since $\phi'(\theta) = \frac{2\cos\theta - 1}{5 - 4\cos\theta} \le \frac{1}{3}$ on $[0, \pi]$, the quantization function $g(\theta) = (a+1)\theta + 2\phi(\theta)$ satisfies $g'(\theta) \le a + \frac{5}{3}$ everywhere on $[0, \pi]$. By the Mean Value Theorem, $(j - i)\pi = g(\theta_j) - g(\theta_i) \le \left(a + \frac{5}{3}\right)(\theta_j - \theta_i)$. Applying Jordan's inequality $\sin x \ge \frac{2}{\pi} x$ to $x = \frac{\theta_j - \theta_i}{2} \in (0, \pi/2)$ gives:
     $$\sin\left(\frac{\theta_j - \theta_i}{2}\right) \ge \frac{\theta_j - \theta_i}{\pi} \ge \frac{j - i}{a + 5/3}.$$
     Simultaneously, since $\phi(\theta_i) > 0$, $\theta_i = \frac{i\pi - 2\phi(\theta_i)}{a+1} < \frac{i\pi}{a+1} \le \frac{2\pi}{9}$ (for $i \in \{1, 2\}$, $a \ge 8$), so $\tan(\theta_i/2) \le \frac{\tan(\pi/9)}{\pi/9} \frac{i\pi}{2(a+1)} < 1.65 \frac{i}{a+1}$.
   - **Step 3e (Summable $a$-Independent Majorant and Tail Bound):** Combining Steps 3a–3d, the $(a+1)^{-2}$ factor in $\tan^2(\theta_i/2)$ cancels $(a + 5/3)^2$ in $\sin^{-2}\left(\frac{\theta_j - \theta_i}{2}\right)$ (with $\frac{a + 5/3}{a + 1} \le \frac{29}{27}$ for $a \ge 8$), yielding the analytical bound valid for all $a \ge 8$, $i \in \{1, 2\}$, and $3 \le j \le a$:
     $$0 \le T_{i,j}(a) \le \mathbf{1}_{j \equiv i \pmod 2} \frac{C_{\max} \, i^2}{(j - i)^2} \in \ell^1(\mathbb{N}_{j \ge 3})$$
     (and tightened empirically/algebraically to $T_{i,j}(a) \le M_{i,j} = \mathbf{1}_{j \equiv i \pmod 2} \frac{32 i^2 j^2}{(j^2 - i^2)^2}$, verified across all $a \in \{8, 16, 32, 64, 128, 256\}$ in `test_04`). The tail beyond any cutoff $M \ge 3$ is bounded uniformly in $a$:
     $$R_M(a) := \sum_{j=M+1}^{a} T_{i,j}(a) \le \sum_{j=M+1}^{\infty} \frac{C_{\max} i^2}{(j - i)^2} \le \frac{C_{\max} i^2}{M - i} \xrightarrow[M \to \infty]{} 0 \quad \text{uniformly in } a.$$
     By **Tannery's Theorem** (discrete Dominated Convergence), $\lim_{a \to \infty} \sum_{j=3}^{a} T_{i,j}(a) = \sum_{j=3}^{\infty} \lim_{a \to \infty} T_{i,j}(a) = \frac{64}{9}(S_1 + S_2)$.

4. **Metric Normalization Convention: Canonical Grassmann Tangent Norm vs. Projector Frobenius Norm (`[Exact Identity]`):**  
   For $\Gamma(\varepsilon) = \Gamma_a^{(0)} + \varepsilon E$, the first-order perturbation of the rank-$r$ spectral projector $P(\varepsilon) = \sum_{i=1}^r u_i(\varepsilon) u_i(\varepsilon)^\top$ has off-diagonal blocks $(u_j^\top dP \, u_i) = \varepsilon \frac{u_j^\top E u_i}{\Lambda_i - \Lambda_j}$ for $1 \le i \le r < j \le a$ and symmetrically $(u_i^\top dP \, u_j)$ for $1 \le i \le r < j \le a$.
   - The **canonical Grassmann Riemannian tangent norm** (the Euclidean norm of the principal-angle vector $\Theta(P(\varepsilon), P(0)) = (\theta_1, \dots, \theta_r)$) sums over a **single** cross-block $1 \le i \le r < j \le a$:
     $$\|dP\|_{\mathrm{Gr}} = \left(\sum_{i=1}^{r} \sum_{j=r+1}^{a} |u_j^\top dP \, u_i|^2\right)^{1/2} = |\varepsilon| \, \chi_{a-2, r}(a), \qquad C = \frac{2\sqrt{18 + 15\pi^2}}{9} \approx 2.863513045852925.$$
   - The **full matrix Frobenius norm** $\|dP\|_F = \sqrt{\mathrm{tr}(dP^\top dP)}$ sums over **both** symmetric cross-blocks, carrying an exact factor of $\sqrt{2}$:
     $$\|dP\|_F = \sqrt{2} \, \|dP\|_{\mathrm{Gr}} = \sqrt{2} \, |\varepsilon| \, \chi_{a-2, r}(a), \qquad C_{\mathrm{Frob}} = \sqrt{2} \, C = \frac{2\sqrt{36 + 30\pi^2}}{9} \approx 4.049618985477498.$$

5. **Closed-Form Evaluation of the Odd and Even Spectral Series (`[Exact Identity]`):**  
   - For $i = 1$ (summing over odd $j = 2m+1 \ge 3$, i.e., $m \ge 1$):
     $$S_1 := \sum_{m=1}^{\infty} \frac{(2m+1)^2}{\left((2m+1)^2 - 1\right)^2} = \frac{1}{16} \sum_{m=1}^{\infty} \left(\frac{1}{m} + \frac{1}{m+1}\right)^2 = \frac{1}{16} + \frac{\pi^2}{48} \approx 0.268116758356028.$$
   - For $i = 2$ (summing over even $j = 2m \ge 4$, i.e., $m \ge 2$):
     $$S_2 := \sum_{m=2}^{\infty} \frac{4(2m)^2}{\left((2m)^2 - 4\right)^2} = \sum_{m=2}^{\infty} \frac{m^2}{(m^2 - 1)^2} = \frac{1}{4}\sum_{m=2}^{\infty}\left(\frac{1}{m-1} + \frac{1}{m+1}\right)^2 = \frac{1}{16} + \frac{\pi^2}{12} \approx 0.884967033424113.$$
   Combining both channels:
   $$C^2 = \frac{64}{9} (S_1 + S_2) = \frac{64}{9} \left(\frac{1}{8} + \frac{5\pi^2}{48}\right) = \frac{8}{9} + \frac{20\pi^2}{27} = \frac{24 + 20\pi^2}{27}.$$
   Taking the square root yields
   $$C = \frac{2\sqrt{18 + 15\pi^2}}{9} \approx 2.863513045852925,$$
   matching Morissette's numerical extrapolation $C \approx 2.8635$ at $a = 10^4$ to all reported figures. $\blacksquare$

> **Remark (General KMS Parameter $\rho \in (0, 1)$):** Because $u_k(1)^2 \propto \frac{1}{(1-\rho)^2}$ and $\Lambda_i - \Lambda_j \propto \frac{\rho(1+\rho)}{(1-\rho)^3}$, the ratio $\frac{u_i(1)^2 u_j(1)^2}{(\Lambda_i - \Lambda_j)^2}$ scales as $\left(\frac{1-\rho}{\rho(1+\rho)}\right)^2$. Thus for arbitrary $\rho \in (0, 1)$:
> $$C(\rho, r=2) = \frac{4(1-\rho)}{\rho(1+\rho)} \sqrt{S_1 + S_2} = \frac{1-\rho}{\rho(1+\rho)} \frac{\sqrt{6 + 5\pi^2}}{3\sqrt{3}}.$$

#### Milestone 1 Reproducible Convergence Table (`[Numerical Observation]`)

Running `python3 tools/verify_cos45_kms_spectral_series.py` performs direct `numpy.linalg.eigh` eigendecomposition of $\Gamma_a^{(0)}$ across $a \in \{8, 16, 32, 64, 128, 256, 512, 1024\}$ without using any asymptotic approximation, and compares $a \cdot \chi_{a-2,2}(a)$, first-order Richardson extrapolation $C_{\mathrm{Rich1}}(a) = 2 a \chi(a) - (a/2)\chi(a/2)$, and second-order Richardson extrapolation $C_{\mathrm{Rich2}}(a) = \frac{4 C_{\mathrm{Rich1}}(a) - C_{\mathrm{Rich1}}(a/2)}{3}$ against $C = \frac{2\sqrt{18+15\pi^2}}{9}$:

| $a$ | $L = a-2$ | $\chi_{a-2,2}(a)$ | $a \cdot \chi_{a-2,2}(a)$ | $\|a\chi(a) - C\|$ | $C_{\mathrm{Rich1}}(a)$ | $\|C_{\mathrm{Rich1}} - C\|$ | $C_{\mathrm{Rich2}}(a)$ | $\|C_{\mathrm{Rich2}} - C\|$ | Parity Residual $\max_k \|u_k(a) - (-1)^{k-1}u_k(1)\|$ |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 8 | 6 | 0.46248320 | 3.69986556 | $8.364 \times 10^{-1}$ | N/A | N/A | N/A | N/A | $1.71 \times 10^{-15}$ |
| 16 | 14 | 0.21691913 | 3.47070606 | $6.072 \times 10^{-1}$ | 3.24154655 | $3.780 \times 10^{-1}$ | N/A | N/A | $6.25 \times 10^{-15}$ |
| 32 | 30 | 0.10076345 | 3.22443045 | $3.609 \times 10^{-1}$ | 2.97815483 | $1.146 \times 10^{-1}$ | 2.89035759 | $2.684 \times 10^{-2}$ | $5.95 \times 10^{-15}$ |
| 64 | 62 | 0.04786266 | 3.06321003 | $1.997 \times 10^{-1}$ | 2.90198962 | $3.848 \times 10^{-2}$ | 2.87660121 | $1.309 \times 10^{-2}$ | $9.84 \times 10^{-15}$ |
| 128 | 126 | 0.02319693 | 2.96920754 | $1.057 \times 10^{-1}$ | 2.87520506 | $1.169 \times 10^{-2}$ | 2.86627687 | $2.764 \times 10^{-3}$ | $1.72 \times 10^{-14}$ |
| 256 | 254 | 0.01139836 | 2.91797995 | $5.447 \times 10^{-2}$ | 2.86675236 | $3.239 \times 10^{-3}$ | 2.86393479 | $4.217 \times 10^{-4}$ | $1.41 \times 10^{-14}$ |
| 512 | 510 | 0.00564682 | 2.89117262 | $2.766 \times 10^{-2}$ | 2.86436529 | $8.522 \times 10^{-4}$ | 2.86356960 | $5.655 \times 10^{-5}$ | $1.92 \times 10^{-14}$ |
| 1024 | 1022 | 0.00281001 | 2.87745208 | $1.394 \times 10^{-2}$ | 2.86373154 | $2.185 \times 10^{-4}$ | 2.86352029 | $7.240 \times 10^{-6}$ | $2.57 \times 10^{-14}$ |

**Explicit Tolerances Enforced by `verify_cos45_kms_spectral_series.py` (`4/4 PASS`):**
1. **Series Identity Tolerance:** $\left|S_1 - \left(\frac{1}{16} + \frac{\pi^2}{48}\right)\right| < 10^{-11}$ and $\left|S_2 - \left(\frac{1}{16} + \frac{\pi^2}{12}\right)\right| < 10^{-11}$.
2. **Finite-$a$ Parity Identity Tolerance:** $\max_{1 \le k \le a} |u_k(a) - (-1)^{k-1}u_k(1)| < 10^{-13}$ and opposite-parity leakage $\max_{j \not\equiv i \pmod 2} |u_j^\top E u_i| < 10^{-14}$.
3. **Asymptotic Convergence Tolerance at $a = 1024$:** $|a\chi_{a-2,2}(a) - C| < 1.5 \times 10^{-2}$, $|C_{\mathrm{Rich1}}(1024) - C| < 2.5 \times 10^{-4}$, and $|C_{\mathrm{Rich2}}(1024) - C| < 1.0 \times 10^{-5}$.
4. **Tannery Majorant & Frobenius Norm Tolerance:** $T_{i,j}(a) \le \mathbf{1}_{j \equiv i \pmod 2} \frac{32 i^2 j^2}{(j^2 - i^2)^2}$ for all $a \in \{8, 16, 32, 64, 128, 256\}$ and $3 \le j \le a$, and $\left|\|dP\|_F - \sqrt{2}\|dP\|_{\mathrm{Gr}}\right| < 10^{-14}$ with $C_{\mathrm{Frob}} = \sqrt{2} C \approx 4.049618985477498$.

---

### Proposition 2 (Open Question 2: $\Theta(a^{-4})$ Blind-Zone Floor Closure — `[Under Joint Examination]`)

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

When applied as a **temporal diagnostic instrument**, a test based solely on the Grassmann endpoint distance $T_b = b \, d_{\mathrm{geo}}(\hat{P}_b, P_0)^2$ can be defeated by three distinct adversarial transformations:

### Blind Zone A: Radial / Energy Runaway in $\ker(D\Pi_{\mathrm{Gr}})$
Because the Grassmann projection $\Pi_{\mathrm{Gr}}(\hat{\Gamma}_b) = \hat{P}_b$ quotients out the radial scale $x \mapsto e^{\alpha} x$, an AI system or dynamical process can undergo an arbitrarily large variance or norm amplification ($\mathrm{tr}(\hat{\Gamma}_b) = e^{2\alpha} \mathrm{tr}(\Gamma_0)$) while preserving $\hat{P}_b = P_0$ identically ($d_{\mathrm{geo}}(\hat{P}_b, P_0) = 0$).

### Blind Zone B: Zero-Displacement Closed Loops and High-Curvature Detours on $\mathrm{Gr}(a, r)$
The endpoint statistic $d_{\mathrm{geo}}(P_{t_1}, P_{t_0})$ measures only the minimal geodesic chord between $P_{t_0}$ and $P_{t_1}$. If a non-stationary AI trajectory undergoes a major transient structural excursion $P_{t_0} \to P_{t^*} \to P_{t_1}$ and returns to $P_{t_1} = P_{t_0}$, the net endpoint distance at $t_1$ is zero, masking the excursion unless the integrated path length is compared against the chord.

### Blind Zone C: Static Subspace Proximity vs. Dynamical Orbit Recurrence (Poincaré Trap)
Even if $d_{\mathrm{geo}}(P_t, P_{t_0}) \le \varepsilon$ at time $t$, returning near an earlier subspace projector does **not** imply that the system has returned to the same dynamical regime. Because $\mathrm{rank}(D\Phi_s)$ is bounded and higher-order lags ($h \ge a$) are projected out, two distinct dynamical laws can share the same instantaneous rank-$r$ subspace $P_t \approx P_{t_0}$ while diverging immediately over the subsequent horizon $t + \tau$ ($\tau \in [1, H]$).

---

## Part III: Pre-Registered Specification for the Joint 5-Gate Benchmark

To evaluate `COS45` alongside four complementary diagnostic gates, all quantities are computed deterministically from the same sliding Hankel window of height $a$ and width $b$:

| Gate | Symbol | Mathematical Definition | Target Vulnerability Addressed |
| :--- | :--- | :--- | :--- |
| **0. Admissibility Gate (`ABSTAIN`)** | $\Delta_{\mathrm{gap}}(t)$ | $\hat{\Lambda}_r(t) - \hat{\Lambda}_{r+1}(t) \ge \tau_{\mathrm{gap}}(b, \alpha)$ | Prevents ill-conditioned subspace rotation when the Davis–Kahan denominator $\hat{\Lambda}_r - \hat{\Lambda}_{r+1}$ collapses; forces explicit `ABSTAIN / HOLD` |
| **1. COS45 Subspace Drift** | $d_{\mathrm{geo}}(t)$ | $\|\Theta(\hat{P}_t, P_0)\|_2 = \left(\sum_{k=1}^r \theta_k^2\right)^{1/2}$ | Detects dominant rank-$r$ subspace rotation beyond the accessibility frontier $a \ge L + 2$ |
| **2. Radial Scale Complement** | $\Delta_{\mathrm{scale}}(t)$ | $\left|\log \frac{\mathrm{tr}(\hat{\Gamma}_t)}{\mathrm{tr}(\Gamma_0)}\right|$ (or restricted subspace energy $\log \frac{\mathrm{tr}(\hat{P}_t \hat{\Gamma}_t)}{\mathrm{tr}(P_0 \Gamma_0)}$) | Captures amplitude/energy runaway along the fiber $\ker(D\Pi_{\mathrm{Gr}})$ invisible to scale-invariant projectors |
| **3. Geodesic / Chord Ratio** | $\kappa_{\mathrm{path}}(t_0, t_1)$ | $\frac{\sum_{t=t_0}^{t_1 - 1} d_{\mathrm{geo}}(\hat{P}_{t+1}, \hat{P}_t)}{\max\left(d_{\mathrm{chord}}(\hat{P}_{t_1}, \hat{P}_{t_0}), \, \varepsilon_0\right)}$ | Detects curved detours, transient regime excursions, and closed loops ($\hat{P}_{t_1} \approx \hat{P}_{t_0}$) on $\mathrm{Gr}(a, r)$ |
| **4a. Deferred Forward-Horizon Recurrence** | $\delta_{\mathrm{orbit}}^{\mathrm{fwd}}(t, t^*; H)$ | $\max_{0 \le \tau \le H} d_{\mathrm{geo}}(\hat{P}_{t+\tau}, \hat{P}_{t^*+\tau})$ (confirmed at epoch $t + H$ after `PROVISIONAL_HOLD`) | Tests whether an instantaneous return $d_{\mathrm{geo}}(\hat{P}_t, \hat{P}_{t^*}) \le \varepsilon_{\mathrm{ret}}$ persists over the subsequent $H$ future steps |
| **4b. Backward-Horizon Persistence** | $\delta_{\mathrm{orbit}}^{\mathrm{bwd}}(t, t^*; H)$ | $\max_{0 \le \tau \le H} d_{\mathrm{geo}}(\hat{P}_{t-\tau}, \hat{P}_{t^*-\tau})$ (evaluated immediately at epoch $t$) | Separate operational variant testing whether the trajectory segment preceding $t$ already matched the reference segment preceding $t^*$ |

### Operational Decision Rule & Epistemic Scope of Verdicts

1. **Admissibility Check (`Gate 0`):**  
   If $\Delta_{\mathrm{gap}}(t) < \tau_{\mathrm{gap}}$, output **`ABSTAIN / HOLD`** (`UNIDENTIFIABLE_SUBSPACE`). No downstream geometric claim is emitted when the eigenspace is within the Davis–Kahan singular zone.
2. **State & Scale Qualification (`Gates 1 & 2`):**  
   Evaluate $(d_{\mathrm{geo}}(t), \Delta_{\mathrm{scale}}(t))$ against pre-registered thresholds $(\tau_{\mathrm{geo}}, \tau_{\mathrm{scale}})$ to classify pure structural drift, pure amplitude scaling, or coupled drift.
3. **Trajectory & Recurrence Verification (`Gates 3, 4a, 4b`):**  
   Over window $[t_0, t_1]$, evaluate $\kappa_{\mathrm{path}}(t_0, t_1)$ to detect non-geodesic detours. For recurrence after an excursion, we distinguish two separate operational tests:
   - **Variant 4a (Deferred Forward-Horizon Test):** At epoch $t$ when $d_{\mathrm{geo}}(\hat{P}_t, P_0) \le \varepsilon_{\mathrm{ret}}$, enter `PROVISIONAL_HOLD` and defer confirmation until epoch $t + H$, when all $H$ future observations $\hat{P}_{t+1}, \dots, \hat{P}_{t+H}$ are available to evaluate $\delta_{\mathrm{orbit}}^{\mathrm{fwd}}(t, t_0; H) \le \tau_{\mathrm{orbit}}$.
   - **Variant 4b (Immediate Backward-Horizon Persistence Test):** Evaluate $\delta_{\mathrm{orbit}}^{\mathrm{bwd}}(t, t_0; H) \le \tau_{\mathrm{orbit}}$ at epoch $t$ over the already-observed history $[t-H, t]$.
4. **Scope of the `OPEN` Verdict (`Diagnostic Satisfaction != Overall System Safety`):**  
   Throughout this benchmark and protocol, the verdict **`OPEN`** means strictly that **the specified mathematical and statistical diagnostic criteria of the evaluated gate(s) have been satisfied within the declared window and tolerance**. It does **not** constitute a certification of overall system safety or physical authority (`CANDIDATE != CONSEQUENCE`).

---

## Conclusion & Acceptance of Collaboration

Louis — your `hidden_order` benchmark (`COS45 v1.7.0`) is a model of scientific clarity: separating `Exact`, `Numerical`, and `Open` claims without overstatement. By closing your two open analytical questions above (Theorem 1: $C = \frac{2\sqrt{18 + 15\pi^2}}{9} \approx 2.863513045853$ and Proposition 2: $\Theta(a^{-4})$ blind-zone floor dilution) and pairing `COS45` with the four complementary gates ($\Delta_{\mathrm{gap}}$, $\Delta_{\mathrm{scale}}$, $\kappa_{\mathrm{path}}$, $\delta_{\mathrm{orbit}}$), we have both the analytical foundation and the pre-registered falsification suite needed for a joint benchmark and publication.

Challenge accepted. Let us lock the signal generators and run the benchmark.
