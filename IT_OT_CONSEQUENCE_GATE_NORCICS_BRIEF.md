# Non-AI Consequence Gating for IT-OT Integration in Critical Infrastructure
### *Architectural Brief on Deterministic Projection ($\Phi \to \Pi_K \to \Omega \to W^2$) across Local LLM/HMI Control, Maritime GNSS Denial, and VSG Byzantine Resilience*

**Author:** Marius Egerhei Torjusen  
**Context:** Technical discussion brief following the CPS4CIP 2026 / SFI NORCICS exchange on IT-OT integration  
**Canonical Reference Architecture:** [`sololys/epistemic-architectures`](https://github.com/sololys/epistemic-architectures) ([Zenodo DOI: `10.5281/zenodo.18436983`](https://doi.org/10.5281/zenodo.18436983))  
**Public `L1` Software Demonstrators:** [`sololys/ky-rox-public-demonstrators`](https://github.com/sololys/ky-rox-public-demonstrators)  
**Epistemic Status:** `L1` Reference Architecture & Deterministic Software Specification (`INSPIRED_BY != IMPLEMENTS != PROVES`; `PHYSICAL_AUTHORITY = NONE`)

---

## 1. Epistemic Demarcation: Reference Architecture, `L1` Software Verification, and Operational Validation

A central challenge in Cyber-Physical Systems (CPS) and IT-OT integration is the structural asymmetry between **probabilistic IT inference** and **irreversible OT actuation**:

$$\boxed{\mathbf{\text{Generated Candidate } \Phi(x_t) \;\neq\; \text{Realized Physical Consequence } x_{t+1}}}$$

In virtual state space, generative models, anomaly detectors, and statistical estimators explore candidate trajectories at near-zero thermodynamic cost ($Q_{\mathrm{math}} = 0.00\,\mathrm{J}$); hypotheses can be revised or rolled back in memory without material damage. Once a command crosses into Operational Technology (OT)—switching relays, slewing maritime rudders, or modulating grid-forming inverters—the action is governed by physical conservation laws and irreversible state erasure ($Q_{\mathrm{phys}} \ge k_B T \ln 2 \cdot \Delta I_{\mathrm{phys}}$).

To keep claims falsifiable and auditable across engineering stages, we enforce a strict three-tier demarcation:

1. **Reference Architecture (`Design & Invariant Specification`):** Formal definition of state spaces, admissible sets $K \subset \mathcal{X}$, projection operators $\Pi_K$, and fail-closed verdict lattices.
2. **Software-Level Verification (`L1` Deterministic Demonstrators):** Reproducible, zero-dependency executable state machines and unit-tested invariant checkers running on deterministic synthetic traces. `L1` software proves that the *code implementation* satisfies the formal specification; it does **not** by itself certify physical hardware or field safety.
3. **Operational Validation (`HIL / Field Qualification`):** Hardware-in-the-loop (HIL), physical interlock timing, galvanic isolation, and certified OT deployment under domain-specific standards.

Between probabilistic IT inference ($\Phi$) and physical OT execution, we interpose a **non-AI, statically verifiable consequence gate**:

$$\Phi(x_t) \;\xrightarrow{\;\text{Candidate}\;}\; \Pi_K \;\xrightarrow{\;\text{Residual } \Delta_K\;}\; \Omega \in \{\mathrm{KILL}, \mathrm{HOLD}, \mathrm{OPEN}\} \;\xrightarrow{\;\text{Pre-Commit}\;}\; W^2 = \langle W_{\mathrm{machine}}, W_{\mathrm{human}} \rangle$$

governed by the strict subsumption order:

$$\boxed{\mathrm{KILL} \; (0.00\,\mathrm{V\ DC}) \;\succ\; \mathrm{HOLD} \; (0.00\,\mathrm{V\ DC}) \;\succ\; \mathrm{OPEN} \; (5.00\,\mathrm{V\ DC})}$$

where any single invariant violation vetoes actuation unconditionally, and the AI/IT layer holds zero autonomous write authority (`standalone_commit_authority = NONE`, `physical_authority = NONE`, `write_enabled = False`).

---

## 2. Three Industrial IT-OT Domains (CPS4CIP 2026 Alignment)

### Domain I — Locally Deployed LLMs & HMIs in Industrial Control (Session 3)

#### Architectural Bottleneck
When locally deployed Large Language Models (LLMs) or AI-assisted Human-Machine Interfaces (HMIs) translate natural-language operator intent or multi-sensor telemetry into PLC setpoint proposals, hallucinated parameters, unit mismatches, or out-of-envelope transitions can propagate directly into actuator registers if the HMI acts as an unmediated command source.

#### Non-AI Consequence Gate ($\Pi_K^{\mathrm{HMI}}$)
Every AI/HMI proposal $u_{\mathrm{cand}} \in \Phi(x_t)$ is treated strictly as an untrusted candidate and must pass three deterministic checks before reaching the OT bus:

1. **Forward-Invariant Control Barrier Check (Nagumo Tangency on $\partial K$):**  
   For safety barrier $K = \{x \in \mathcal{X} : h(x) \ge 0\}$, the gate evaluates whether the proposed vector field $f(x_t, u_{\mathrm{cand}})$ points into the tangent cone $T_K(x_t)$:
   $$\langle \nabla h(x_t), f(x_t, u_{\mathrm{cand}}) \rangle + \alpha(h(x_t)) \ge 0.$$
   - If $h(x_t) < 0$ or tangency fails beyond tolerance: $\Omega \to \mathrm{KILL}$ ($0.00\,\mathrm{V\ DC}$, `RC-BARRIER-BREACH-KILL`).
   - If $0 \le h(x_t) \le \varepsilon_{\mathrm{margin}}$ (boundary transition layer $\Delta_\varepsilon$): $\Omega \to \mathrm{HOLD}$ ($0.00\,\mathrm{V\ DC}$, `RC-BOUNDARY-MARGIN-HOLD`).
2. **Non-Analytic Transition Latch ($\Delta_\varepsilon$):**  
   By the Identity Theorem for holomorphic functions, no smooth analytical model can implement an exact binary cutoff ($1$ on $D_{\mathrm{adm}}$, $0$ on $D_{\mathrm{elim}}$) without becoming constant everywhere. The gate therefore enforces an explicit non-analytic transition corridor $[-\varepsilon, +\varepsilon]$ with hardware/software latch hysteresis, preventing high-frequency decision chatter near the boundary.
3. **Dual Pre-Commit Attestation ($W^2$):**  
   Irreversible mode changes require both a deterministic machine invariant receipt ($W_{\mathrm{machine}}$, RFC 8785 canonical JSON + SHA-256 ancestor hash) and an explicit human-at-the-cut-surface authorization token ($W_{\mathrm{human}}$) **prior** to energizing the $5.00\,\mathrm{V\ DC}$ output stage.

---

### Domain II — Maritime GNSS Spoofing & Jamming in Coastal and Port Operations (Session 4)

#### Architectural Bottleneck
In coastal navigation, dynamic positioning (DP), and automated port crane/vessel operations, adversarial GNSS spoofing or RF jamming corrupts external satellite timing and position fixes while cloud connectivity may be degraded or contested. Systems that equate cryptographic cloud reachability or smooth Kalman-filter innovation with physical truth can be smoothly dragged onto a false trajectory.

#### Local-First Light-Cone & Phase-Coherence Gate ($\Pi_K^{\mathrm{maritime}}$)
When external GNSS ephemeris is untrusted, physical authority is restricted strictly to the **local causal light-cone** and local physical invariants:

1. **Relativistic Ultra-Wideband (UWB) Time-of-Flight (ToF) Distance Bounding:**  
   Peer-to-peer range between vessel and port reference beacons is upper-bounded by the speed of light $c$ in the physical medium:
   $$d_{\mathrm{ToF}} = c \cdot \frac{\Delta t_{\mathrm{round}} - \Delta t_{\mathrm{proc}}}{2} \le d_{\max}, \qquad |d_{\mathrm{GNSS}} - d_{\mathrm{ToF}}| \le \tau_{\mathrm{spoof}}.$$
   Because no physical adversary can accelerate electromagnetic propagation faster than $c$, any spoofed position claim violating the causal ToF light-cone triggers $\Omega \to \mathrm{HOLD} / \mathrm{KILL}$ (`RC-CAUSAL-LIGHTCONE-VIOLATION`).
2. **Euclidean Phase-Gradient Discrimination ($\mathbb{C} \setminus [-1, 1]$):**  
   For multi-antenna Angle-of-Arrival (AoA) arrays with baseline $d_{\mathrm{ant}}$ and carrier wavelength $\lambda$, the measured phase difference $\Delta\phi$ defines the directional sine:
   $$s_{\mathrm{obs}} := \frac{\Delta\phi \cdot \lambda}{2\pi d_{\mathrm{ant}}}.$$
   Any coherent electronic-warfare or spoofing injection that drives $|s_{\mathrm{obs}}| > 1.0$ places $\theta = \arcsin(s_{\mathrm{obs}})$ into the unphysical complex domain $\mathbb{C} \setminus [-1, 1]$, immediately triggering `JAMMING_KILL` ($0.00\,\mathrm{V\ DC}$).
3. **Local-First Append-Only State Sealing:**  
   All state transitions are chained locally in an append-only SHA-256 ancestor ledger:
   $$W_{t+1} = \mathcal{H}\!\left(W_t \parallel \Phi_t \parallel \Delta_K \parallel \Omega_t \parallel \Delta t_{\mathrm{ToF}}\right),$$
   requiring zero cloud reachability to preserve causal ordering and post-incident forensic auditability.

---

### Domain III — Virtual Synchronous Generators (VSGs) & Byzantine Fault Tolerance (Sessions 2 & 4)

#### Architectural Bottleneck
Grid-forming Virtual Synchronous Generators (VSGs) emulate rotor inertia and damping in power electronics-dominated microgrids. Sub-threshold Byzantine sensor corruption or coordinated high-frequency oscillatory injection across distributed inverter nodes can excite synthetic swing-equation resonances ($\frac{d^2\delta}{dt^2}$) before traditional static threshold alarms trip.

#### Relativistic Dispersion &Multiplicative Quorum Gate ($\Pi_K^{\mathrm{VSG}}$)
1. **Dispersion Screening Threshold ($\omega^2 = \mu_{\mathrm{eff}}^2 + c_s^2 k^2$):**  
   By subjecting incoming distributed control perturbations $\psi(x, t) \sim e^{i(kx - \omega t)}$ to a screened wave operator with effective mass gap $\mu_{\mathrm{eff}} > 0$:
   $$\left(\frac{\partial^2}{\partial t^2} - c_s^2 \nabla^2 + \mu_{\mathrm{eff}}^2\right)\psi = 0 \implies \omega^2 = \mu_{\mathrm{eff}}^2 + c_s^2 k^2,$$
   sub-threshold perturbations with frequency $\omega < \mu_{\mathrm{eff}}$ acquire an imaginary wavenumber $k = i\kappa$ with $\kappa = \frac{\sqrt{\mu_{\mathrm{eff}}^2 - \omega^2}}{c_s} > 0$. Instead of propagating across the inverter network as undamped travelling waves, sub-gap Byzantine chatter becomes **exponentially evanescent** ($e^{-\kappa |x|}$) and is clamped in `HOLD` stasis ($0.00\,\mathrm{V\ DC}$).
2. **Multiplicative 6-Warrant Actuation Barrier:**  
   The physical converter modulation command $u(t)$ is gated by a multiplicative Boolean product:
   $$u(t) = u^*(t) \cdot \prod_{m=1}^{6} \mathbf{w}_m = u^*(t) \cdot \left(\mathbf{w}_{\mathrm{risk}} \cdot \mathbf{w}_{\mathrm{quorum}} \cdot \mathbf{w}_{\mathrm{precommit}} \cdot \mathbf{w}_{\mathrm{hw\_truth}} \cdot \mathbf{w}_{\mathrm{dispersion}} \cdot \mathbf{w}_{\mathrm{rocof}}\right), \quad \mathbf{w}_m \in \{0, 1\},$$
   where $\mathbf{w}_{\mathrm{quorum}} = 1$ requires Byzantine agreement across at least $2f + 1$ of $3f + 1$ independent sensing channels. If any single warrant drops to $0$, the product collapses identically to $0.00\,\mathrm{V\ DC}$.

---

## 3. Summary Matrix for Joint SFI NORCICS Technical Evaluation

| CPS4CIP Domain | Untrusted IT Candidate ($\Phi$) | Non-AI Projection Invariant ($\Pi_K$) | Fail-Closed Gate Verdict ($\Omega$) | Verification Tier |
| :--- | :--- | :--- | :--- | :--- |
| **Session 3: Local LLMs & HMIs** | Natural-language / AI setpoint proposal $u_{\mathrm{cand}}$ | Nagumo barrier tangency $\langle \nabla h, f\rangle + \alpha(h) \ge 0$, $\Delta_\varepsilon$ spline latch, $W^2$ receipt | `HOLD` in $[-\varepsilon, +\varepsilon]$; `KILL` ($0.00\,\mathrm{V\ DC}$) if $h(x) < 0$ or unlatched | `L1` deterministic gate suite $\to$ PLC/HMI HIL |
| **Session 4: Maritime GNSS Denial** | Spoofed/jammed GNSS position & ephemeris | UWB ToF causal light-cone $d_{\mathrm{ToF}} \le c\Delta t/2$, AoA $|s_{\mathrm{obs}}| \le 1$, local SHA-256 chain | `JAMMING_KILL` / `HOLD` ($0.00\,\mathrm{V\ DC}$) on light-cone or $|\sin\theta| > 1$ breach | `L1` synthetic spoofing traces $\to$ coastal/port replay |
| **Sessions 2 & 4: VSG & BFT Grid** | Byzantine inverter telemetry & oscillatory chatter | Screened dispersion gap $\omega^2 \ge \mu_{\mathrm{eff}}^2 + c_s^2 k^2$ + $(2f+1)$ multiplicative warrant | Sub-gap chatter held evanescent in `HOLD`; warrant loss $\implies \mathrm{KILL}$ ($0.00\,\mathrm{V\ DC}$) | `L1` swing-equation simulator $\to$ microgrid testbed |

---

## 4. Sammendrag på norsk (Norsk Stamme)

I integrasjonen mellom informasjonsteknologi (IT) og operasjonell teknologi (OT) i kritisk infrastruktur oppstår en fundamental termodynamisk asymmetri: en sannsynlighetsmodell eller lokal språkmodell ($\Phi$) opererer nesten kostnadsfritt i minnet ($Q_{\mathrm{math}} = 0.00\,\mathrm{J}$), mens et fysisk rorutslag, et reléinnslag eller en omformerordre i strømnettet krysser irreversibilitetsgrensen i romtid ($Q_{\mathrm{phys}} \ge k_B T \ln 2 \cdot \Delta I_{\mathrm{phys}}$).

Ved å plassere en ikke-AI, statisk verifiserbar projeksjons- og konsekvensport ($\Phi \to \Pi_K \to \Omega \to W^2$) mellom IT-inferens og OT-aktuering under subsumpsjonsloven $\mathrm{KILL} \succ \mathrm{HOLD} \succ \mathrm{OPEN}$, oppnås tre strukturelle garantier på tvers av bruksområdene i SFI NORCICS / CPS4CIP:

1. **Lokale LLM-er og HMI-er (Session 3):** Ingen AI-generert kandidat har direkte skrivemyndighet til PLS eller aktuator (`standalone_commit_authority = NONE`). Forslag som bryter Nagumo-tangentkjeglen ved sikkerhetsranden $\partial K$ eller mangler dobbelt forhåndsvitne $W^2 = \langle W_{\mathrm{machine}}, W_{\mathrm{human}} \rangle$, klemmes til $0.00\,\mathrm{V\ DC}$ før de når feltnivået.
2. **Maritim GNSS-manipulasjon (Session 4):** Når satellittsignaler eller skyforbindelse manipuleres eller faller bort i kyst- og havneoperasjoner, begrenses fysisk myndighet til den lokale kausale lyskjeglen via relativistisk UWB Time-of-Flight-avstandsmåling ($d_{\mathrm{ToF}} \le c\Delta t/2$), euklidsk fasediskriminering ($|\sin\theta| \le 1.0$) og lokal-først SHA-256-forfedrekjede.
3. **Virtuelle synkrongeneratorer og BFT (Session 2 & 4):** Ved å håndheve en relativistisk dispersjonsterskel ($\omega^2 = \mu_{\mathrm{eff}}^2 + c_s^2 k^2$) sammen med en multiplikativ $2f+1$-kvorumsbarriere ved kontrollporten, blir sub-terskel bysantinsk støy og høyfrekvent flimmer eksponentielt evanescente og holdes tilbake i $0.00\,\mathrm{V\ DC}$ stase før de kan forplante seg til frekvens- eller RoCoF-ustabilitet i kraftnettet.
