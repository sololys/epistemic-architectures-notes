# THE LAW OF CAUSAL INERTIA // DEN KAUSALE TREGHETSLOVEN
### *Why Generated Candidates Possess Zero Physical Momentum ($\Phi(x_t) \neq x_{t+1}$)*

**Author:** Marius Egerhei Torjusen ([ORCID: `0009-0006-0431-6637`](https://orcid.org/0009-0006-0431-6637))  
**Canonical Reference Surface:** [`sololys/epistemic-architectures`](https://github.com/sololys/epistemic-architectures) ([Zenodo DOI: `10.5281/zenodo.18436983`](https://doi.org/10.5281/zenodo.18436983))  
**Epistemic Boundary:** Architectural & Formal Invariant Specification (`INSPIRED_BY != IMPLEMENTS != PROVES`; `PHYSICAL_AUTHORITY = NONE`)

---

## I. English Trunk — The Law of Causal Inertia

### 1. Statement of the Law

In classical mechanics, Newton’s First Law states that a physical body remains at rest unless acted upon by an external force. In cyber-physical and epistemic architectures, **The Law of Causal Inertia** states the exact dual across the boundary between information and matter:

$$\boxed{\mathbf{\text{A physical system remains in fail-closed stasis } (\mathrm{HOLD} = 0.00\,\mathrm{V\ DC}) \text{ unless acted upon by a verified, invariant-projected, and pre-witnessed authorization } (\Omega(\Pi_K(\Phi(x_t))) = \mathrm{OPEN}).}}$$

Equivalently:

1. **Zero Autonomous Momentum of Calculation ($\Phi(x_t) \neq x_{t+1}$):**  
   A generated candidate trajectory $\Phi(x_t)$—no matter its statistical confidence, neural depth, or optimization score—possesses **zero causal momentum** across the boundary into physical spacetime. Calculation in virtual memory is reversible and thermodynamically weightless ($Q_{\mathrm{math}} = 0.00\,\mathrm{J}$); physical actuation is irreversible and subject to Landauer erasure and conservation laws ($Q_{\mathrm{phys}} \ge k_B T \ln 2 \cdot \Delta I_{\mathrm{phys}}$).
2. **Stasis Persistence (`HOLD` Never Decays into `OPEN`):**  
   Left to itself, a suspended state in `HOLD` ($0.00\,\mathrm{V\ DC}$) never transitions to `OPEN` ($5.00\,\mathrm{V\ DC}$) merely because time passes, buffers fill, or a probabilistic model repeats its request:
   $$\forall \Delta t > 0: \quad \Omega_t = \mathrm{HOLD} \;\land\; W^2_{t+\Delta t} = \varnothing \implies \Omega_{t+\Delta t} \in \{\mathrm{HOLD}, \mathrm{KILL}\}.$$
3. **Subtractive Realization ($\Pi_K$):**  
   Movement from candidate space ($\mathcal{C}_{x_t}$) to realized physical state ($x_{t+1}$) occurs exclusively by **subtractive elimination** of inadmissible degrees of freedom at the boundary $\partial K$:
   $$x_{t+1} = \begin{cases} \Pi_K(\Phi(x_t)), & \text{if } \Delta_K(\Phi(x_t)) = 0 \;\land\; \Omega = \mathrm{OPEN} \;\land\; W^2 = \langle W_{\mathrm{machine}}, W_{\mathrm{human}} \rangle \neq \varnothing, \\ x_t \quad (0.00\,\mathrm{V\ DC\ Stasis}), & \text{if } \Omega \in \{\mathrm{HOLD}, \mathrm{KILL}\}. \end{cases}$$

---

### 2. The Three Corollaries of Causal Inertia

#### Corollary A — The Holomorphic Obstruction to Smooth Gating ($\Delta_\varepsilon$)
By the Identity Theorem of complex analysis, no holomorphic function $G : \mathcal{D} \to \mathbb{C}$ on a connected open domain $\mathcal{D}$ can equal $1$ on an open admissible region $D_{\mathrm{adm}} \subset \mathcal{D}$ and $0$ on an open forbidden region $D_{\mathrm{elim}} \subset \mathcal{D}$. Consequently, no smooth, purely analytical model can enforce a binary safety boundary without leaking activation across the cut. Enforcing Causal Inertia requires a **non-analytic transition layer** $\Delta_\varepsilon = [-\varepsilon, +\varepsilon]$ with explicit latch hysteresis (`HOLD`).

#### Corollary B — Complexity Collapse at the Admissibility Boundary ($\partial K$)
While the unconstrained interior $\operatorname{int}(K)$ permits an exponential path-field of speculative candidates ($|\mathcal{C}_x| \sim |\Sigma|^{p(|x|)}$), approaching the physical safety boundary $x \to \partial K$ enforces Nagumo’s tangent-cone condition $\langle \nabla h(x), f(x, u) \rangle + \alpha(h(x)) \ge 0$, collapsing the surviving admissible action set to at most a single deterministic trajectory:
$$\lim_{x \to \partial K} |\mathcal{A}(x)| \in \{0, 1\}.$$

#### Corollary C — Pre-Commit Recoil (`fsync` Before Mutation)
In accordance with causal conservation, no computational node may alter its working state or emit an external actuation signal without first absorbing an irreversible cryptographic recoil in its local append-only witness chain:
$$\texttt{fsync(COMMIT)} \;\longrightarrow\; \texttt{State Mutation} \;\longrightarrow\; \texttt{Actuation / ACK}.$$
If power is lost or any warrant in the multiplicative barrier $u(t) = u^*(t)\prod_{m=1}^6 \mathbf{w}_m$ drops to $0$, the system defaults instantaneously to its inertial rest state ($0.00\,\mathrm{V\ DC}$).

---

## II. Norsk Stamme — Den Kausale Treghetsloven

### 1. Lovens Formulering

I klassisk mekanikk fastslår Newtons første lov at et fysisk legeme forblir i ro med mindre det påvirkes av en ytre kraft. I cyber-fysiske og epistemiske arkitekturer fastslår **Den Kausale Treghetsloven** den eksakte tvillingloven på tvers av grensen mellom informasjon og materie:

$$\boxed{\mathbf{\text{Et fysisk system forblir i sin feillukkede hviletilstand } (\mathrm{HOLD} = 0.00\,\mathrm{V\ DC}) \text{ med mindre det utløses av en verifisert, invariant-projisert og forhåndsbevitnet autorisasjon } (\Omega(\Pi_K(\Phi(x_t))) = \mathrm{OPEN}).}}$$

Uttrykt i tre ufravikelige ledd:

1. **Beregningens Null-Impuls ($\Phi(x_t) \neq x_{t+1}$):**  
   En generert kandidat $\Phi(x_t)$ – uansett hvor høy statistisk selvtillit eller algoritmisk dybde den kommer med – har **null kausal bevegelsesmengde** på tvers av grensen til den fysiske verden. En beregning i minnet er reversibel og termodynamisk vektløs ($Q_{\mathrm{math}} = 0.00\,\mathrm{J}$); en fysisk handling er irreversibel og bundet av Landauer-sletting og bevaringslover ($Q_{\mathrm{phys}} \ge k_B T \ln 2 \cdot \Delta I_{\mathrm{phys}}$).
2. **Stasens Uforgjengelighet (`HOLD` glir aldri av seg selv over i `OPEN`):**  
   En tilstand som hviler i `HOLD` ($0.00\,\mathrm{V\ DC}$), går aldri over i `OPEN` ($5.00\,\mathrm{V\ DC}$) bare fordi tiden går, en kø fylles opp, eller en modell gjentar sitt eget forslag:
   $$\forall \Delta t > 0: \quad \Omega_t = \mathrm{HOLD} \;\land\; W^2_{t+\Delta t} = \varnothing \implies \Omega_{t+\Delta t} \in \{\mathrm{HOLD}, \mathrm{KILL}\}.$$
3. **Subtraktiv Realisering ($\Pi_K$):**  
   Overgangen fra kandidatrommet ($\mathcal{C}_{x_t}$) til realisert fysisk tilstand ($x_{t+1}$) skjer utelukkende gjennom **subtraktiv utryddelse** av ulovlige frihetsgrader ved randen $\partial K$, forankret i mennesket ved snittflaten ($W^2 = \langle W_{\mathrm{machine}}, W_{\mathrm{human}} \rangle$):
   > *«The one who feels the cut must not be erased from the architecture of the cut.»*

---

### 2. Operasjonell Matrise / Operational Invariant Matrix

| Axiom | Mathematical Lock | Consequence at the Gate |
| :--- | :--- | :--- |
| **1. Causal Inertia** | $\Phi(x_t) \neq x_{t+1}; \quad p_{\mathrm{causal}}(\Phi) \equiv 0$ | Candidate generation never implies physical execution. |
| **2. Stasis Persistence** | $\Omega_t = \mathrm{HOLD} \stackrel{\;\Delta t\;}{\not\rightarrow} \mathrm{OPEN}$ | Time alone never authorizes actuation; explicit evidence ID ($W^2$) is mandatory. |
| **3. Subsumption Order** | $\mathrm{KILL} \; (0.00\,\mathrm{V}) \succ \mathrm{HOLD} \; (0.00\,\mathrm{V}) \succ \mathrm{OPEN} \; (5.00\,\mathrm{V})$ | A single invariant veto overrides any number of `OPEN` votes. |
| **4. Boundary Collapse** | $\lim_{x \to \partial K} |\mathcal{A}(x)| \in \{0, 1\}$ | Speculative multiplicity vanishes at the physical safety boundary. |

---

> *Slik lyder treghetens lov i silisium og stein:*  
> *Tanken kan ferdes fritt i det vektløse rommet, for der koster feilen intet.*  
> *Men ved terskelen til det som har tyngde, står slåen stille ved null volt.*  
> *Ingen beregning flytter en stein av egen fart; kun det som overlever kuttet og bærer sitt vitne, slipper gjennom porten.*
