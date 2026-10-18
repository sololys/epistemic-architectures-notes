# XIII. METRISK INVARIANS, SPEKTRAL KONVERGENS OG HORISONTENS LOV ($\Vert dP \Vert_F = \sqrt{2} \Vert dP \Vert_{\text{Gr}} \land R_M(a) \to 0 \land \text{PROVISIONAL\_HOLD}_H$)

**OPERASJONELT SAMMENDRAG**

Inskripsjon av de tre matematiske og operasjonelle sluttsteinene for Grassmann-perturbasjon, spektral halekontroll og kausal tilbakevendingshorisont (Port 4). All konversasjonell innledning («You are completely right») er klampet til $0.00\text{ V DC}$. Teksten er komprimert til sin korteste deskriptive lengde ($K(x)$) og bærer sin fulle logiske dybde i både norsk og engelsk granitt.

---

*Fra samlingen som overlevde brente jords taktikk. De tekniske bladene er skåret ut; kun den litterære stammen står igjen.*

---

### XIII. Metrisk Invarians, Spektral Konvergens og Horisontens Lov (Norsk Stamme)

#### 1. Metrisk Normalisering på Grassmann-Manifolden ($\Vert dP \Vert_{\text{Gr}}$ vs. $\Vert dP \Vert_F$)

En målestokk som vakler mellom koordinatsystemer, er ingen lov.

For den perturberte operatoren $\Gamma(\varepsilon) = \Gamma_a^{(0)} + \varepsilon E$, frembringer førsteordens variasjon av rang-$r$ spektralprojektoren $P(\varepsilon) = \sum_{i=1}^r u_i(\varepsilon) u_i(\varepsilon)^T$ to symmetriske, ikke-diagonale koblingsblokker i den uperturberte egenbasisen:

$$u_j^T dP \, u_i = \varepsilon \frac{u_j^T E u_i}{\Lambda_i - \Lambda_j} \quad (1 \le i \le r < j \le a)$$

samt den transponerte tvillingblokken $u_i^T dP \, u_j$. Skillet mellom manifoldens indre geometri og det omsluttende matriserommet er eksakt:

* **Kanonisk Grassmann-Riemannsk Norm ($\Vert dP \Vert_{\text{Gr}}$):** Måler den geodetiske tangentvektoren ved å summere utelukkende over én uavhengig kryssblokk ($1 \le i \le r < j \le a$):

$$\Vert dP \Vert_{\text{Gr}} = \left( \sum_{i=1}^r \sum_{j=r+1}^a \vert{}u_j^T dP \, u_i\vert{}^2 \right)^{1/2} = \vert{}\varepsilon\vert{} \chi_{a-2, r}(a), \quad C = \frac{2\sqrt{18 + 15\pi^2}}{9} \approx 2.863513045852925$$

* **Full Frobenius-Norm ($\Vert dP \Vert_F$):** Måler totalavviket i det euklidske matriserommet $\sqrt{\text{tr}(dP^T dP)}$ over begge symmetriske blokker, og bærer dermed den ufravikelige faktoren $\sqrt{2}$:

$$\Vert dP \Vert_F = \sqrt{2} \Vert dP \Vert_{\text{Gr}} = \sqrt{2} \vert{}\varepsilon\vert{} \chi_{a-2, r}(a), \quad C_{\text{Frob}} = \sqrt{2} C = \frac{2\sqrt{36 + 30\pi^2}}{9} \approx 4.049618985477498$$

Identiteten er låst med numerisk residual under $10^{-14}$. Ingen tvetydighet tillates mellom rommets krumning og matrisens spor.

---

#### 2. Uniform Halekontroll og Tannerys Teorem

Hvorfor kan grenseverdien $\lim_{a \to \infty}$ bytte plass med den spektrale summen $\sum_{j=3}^a$ når høyfrekvente moder nær randen $\theta_j \to \pi$ bryter småvinkeltilnærmingen $\sin\theta_j \approx \theta_j$? Fordi algebraisk kansellering og spektral dempning lukker halen uniformt.

For enhver endelig dimensjon $a \ge 8$ og enhver mode $1 \le k \le a$ av Kac-Murdock-Szegő-matrisen (KMS) ved $\rho = 1/2$, gir de eksakte tridiagonale sekulærligningene:

$$\Lambda(\theta_k) = \frac{3}{5 - 4\cos\theta_k}, \quad u_k(1)^2 = \frac{4 A_k^2 \sin^2\theta_k}{5 - 4\cos\theta_k}, \quad A_k^2 < \frac{2}{a - 1}, \quad \theta_k \in \left(\frac{(k-1)\pi}{a+1}, \frac{k\pi}{a}\right)$$

For de ledende modene $i \in \{1, 2\}$ og enhver eksitert mode $j \in \{3, \dots, a\}$ er den eksakte egenverdidifferansen:

$$\Lambda_i - \Lambda_j = \frac{12(\cos\theta_i - \cos\theta_j)}{(5 - 4\cos\theta_i)(5 - 4\cos\theta_j)}$$

Når det skalerte leddet $T_{i,j}(a) := a^2 \vert{}u_j^T E u_i\vert{}^2 / (\Lambda_i - \Lambda_j)^2$ dannes (som er identisk lik $0$ for motsatt paritet $j \not\equiv i \pmod 2$, og kun bærer vekt når $\mathbf{1}_{j \equiv i \pmod 2} = 1$), sluker faktoren $(5 - 4\cos\theta_j)^{-1}$ i randvekten $u_j(1)^2$ den ene potensen av $(5 - 4\cos\theta_j)^2$ fra nevneren $(\Lambda_i - \Lambda_j)^{-2}$:

$$T_{i,j}(a) = \mathbf{1}_{j \equiv i \pmod 2} \frac{4 (a A_i^2)(a A_j^2) \sin^2\theta_i \sin^2\theta_j (5 - 4\cos\theta_i)(5 - 4\cos\theta_j)}{9 (\cos\theta_i - \cos\theta_j)^2}$$

Mot den øvre spektralranden $\theta_j \to \pi$ dør telleren ut via $\sin^2\theta_j \to 0$, mens nevneren $(\cos\theta_i - \cos\theta_j)$ holdes strengt adskilt fra null (nærmer seg $1 + \cos\theta_i \approx 2$). Over hele spekteret $3 \le j \le a$ tvinger halvvinkelreduksjonen og Jordans ulikhet på $\cos\theta_i - \cos\theta_j = 2\sin\left(\frac{\theta_j - \theta_i}{2}\right)\sin\left(\frac{\theta_j + \theta_i}{2}\right)$ frem en uniform, $a$-uavhengig majorant:

$$0 \le T_{i,j}(a) \le M_{i,j} := \mathbf{1}_{j \equiv i \pmod 2} \frac{32 i^2 j^2}{(j^2 - i^2)^2} \quad \forall a \ge 8, \; \forall j \in \{3, \dots, a\}$$

Siden $\sum_{j=3}^\infty M_{i,j} < \infty$ med et uniformt haleresidual som er uavhengig av matriseordenen $a$:

$$R_M(a) := \sum_{j=M+1}^a T_{i,j}(a) \le \sum_{j=M+1}^\infty M_{i,j} \le \frac{32 i^2}{M - 1}$$

gjelder Tannerys teorem (diskret dominert konvergens) betingelsesløst. Grensen passerer gjennom summen uten lekkasje av masse:

$$\lim_{a \to \infty} a^2 \chi_{a-2, 2}(a)^2 = \sum_{i=1}^2 \sum_{j=3}^\infty \lim_{a \to \infty} T_{i,j}(a) = \frac{64}{9}(S_1 + S_2) = C^2$$

│ — [ Blad skåret ut ved bokryggen ] —

#### 3. Kausal Horisont og Prøvetidens Port (Port 4: $H$)

En enkeltstående tilbakevending er et sammenfall, ikke en gjenopprettelse. Man kan ikke bevise fremtiden i nåtiden uten å vente på at tiden faktisk går.

Når et underrom $\hat{P}_t$ etter et utslag vender tilbake innenfor den øyeblikkelige terskelen $d_{\text{geo}}(\hat{P}_t, P_0) \le \varepsilon_{\text{ret}}$ ved epoke $t$, har porten ingen hjemmel til å erklære $\text{OPEN}$. Et punkt er ingen bane. Porten trer i stedet inn i **$\text{PROVISIONAL\_HOLD}$** — et forseglet prøvetidsvindu av lengde $H$, der vi skiller strengt mellom to operasjonelle varianter:

* **Fremadrettet Horisont (Variant 4a — Utsatt Autorisasjon ved $t + H$):**
Full diagnostisk gjenopprettelse ($\Omega \to \text{OPEN}$) autoriseres først ved epoke $t + H$ dersom, og bare dersom, banen forblir uavbrutt innenfor det geodetiske røret gjennom hele prøvetiden:

$$\max_{0 \le \tau \le H} d_{\text{geo}}(\hat{P}_{t+\tau}, P_{t_0+\tau}) \le \tau_{\text{orbit}}$$

* **Tilbakeblikkende Horisont (Variant 4b — Øyeblikkelig Dom over Forløpt Historie ved $t$):**
En separat operasjonell test der autorisasjon ved epoke $t$ vurderer hvorvidt det tilbakelagte banesegmentet i vitneloggen over $\tau \in [-H, 0]$ allerede har vist uavbrutt persistens:

$$\max_{-H \le \tau \le 0} d_{\text{geo}}(\hat{P}_{t+\tau}, P_{t_0+\tau}) \le \tau_{\text{orbit}}$$

Før alle $H$ trinn er bevitnet innenfor røret, forblir spenningen låst i stase, og utfallet $\text{OPEN}$ betyr utelukkende at de spesifiserte diagnostiske kriteriene er oppfylt innenfor vinduet ($\text{Kandidat} \neq \text{Konsekvens}$). En svale gjør ingen sommer; ett gyldig punkt åpner ingen port.

---

---

### XIII. Metric Invariance, Spectral Convergence, and the Law of the Horizon (English Trunk)

#### 1. Metric Normalization on the Grassmann Manifold ($\Vert dP \Vert_{\text{Gr}}$ vs. $\Vert dP \Vert_F$)

A measure that shifts between coordinate frames is not a law.

For the perturbed operator $\Gamma(\varepsilon) = \Gamma_a^{(0)} + \varepsilon E$, first-order variation of the rank-$r$ spectral projector $P(\varepsilon) = \sum_{i=1}^r u_i(\varepsilon) u_i(\varepsilon)^T$ yields two symmetric off-diagonal coupling blocks in the unperturbed eigenbasis:

$$u_j^T dP \, u_i = \varepsilon \frac{u_j^T E u_i}{\Lambda_i - \Lambda_j} \quad (1 \le i \le r < j \le a)$$

alongside its transpose block $u_i^T dP \, u_j$. The distinction between the intrinsic geometry of the manifold and the ambient matrix space is exact:

* **Canonical Grassmann Riemannian Norm ($\Vert dP \Vert_{\text{Gr}}$):** Measures the geodesic tangent vector by summing strictly over a single independent cross-block ($1 \le i \le r < j \le a$):

$$\Vert dP \Vert_{\text{Gr}} = \left( \sum_{i=1}^r \sum_{j=r+1}^a \vert{}u_j^T dP \, u_i\vert{}^2 \right)^{1/2} = \vert{}\varepsilon\vert{} \chi_{a-2, r}(a), \quad C = \frac{2\sqrt{18 + 15\pi^2}}{9} \approx 2.863513045852925$$

* **Full Matrix Frobenius Norm ($\Vert dP \Vert_F$):** Measures total deviation in ambient Euclidean matrix space $\sqrt{\text{tr}(dP^T dP)}$ across both symmetric blocks, carrying the invariant factor $\sqrt{2}$:

$$\Vert dP \Vert_F = \sqrt{2} \Vert dP \Vert_{\text{Gr}} = \sqrt{2} \vert{}\varepsilon\vert{} \chi_{a-2, r}(a), \quad C_{\text{Frob}} = \sqrt{2} C = \frac{2\sqrt{36 + 30\pi^2}}{9} \approx 4.049618985477498$$

This identity holds to a numerical residual below $10^{-14}$. No ambiguity is permitted between the curvature of the subspace and the trace of the matrix.

---

#### 2. Uniform Tail Control and Tannery’s Theorem

Why may the limit $\lim_{a \to \infty}$ be interchanged with the spectral sum $\sum_{j=3}^a$ when high-frequency modes near the upper edge $\theta_j \to \pi$ violate the small-angle approximation $\sin\theta_j \approx \theta_j$? Because algebraic cancellation and boundary damping seal the spectral tail uniformly.

For every finite dimension $a \ge 8$ and every mode $1 \le k \le a$ of the Kac-Murdock-Szegő (KMS) matrix at $\rho = 1/2$, the exact tridiagonal secular equations dictate:

$$\Lambda(\theta_k) = \frac{3}{5 - 4\cos\theta_k}, \quad u_k(1)^2 = \frac{4 A_k^2 \sin^2\theta_k}{5 - 4\cos\theta_k}, \quad A_k^2 < \frac{2}{a - 1}, \quad \theta_k \in \left(\frac{(k-1)\pi}{a+1}, \frac{k\pi}{a}\right)$$

For the principal modes $i \in \{1, 2\}$ and any excited mode $j \in \{3, \dots, a\}$, the exact spectral gap is:

$$\Lambda_i - \Lambda_j = \frac{12(\cos\theta_i - \cos\theta_j)}{(5 - 4\cos\theta_i)(5 - 4\cos\theta_j)}$$

When forming the scaled summand $T_{i,j}(a) := a^2 \vert{}u_j^T E u_i\vert{}^2 / (\Lambda_i - \Lambda_j)^2$ (which vanishes identically for opposite parities $j \not\equiv i \pmod 2$ and is non-zero solely when $\mathbf{1}_{j \equiv i \pmod 2} = 1$), the factor $(5 - 4\cos\theta_j)^{-1}$ in the boundary weight $u_j(1)^2$ annihilates one power of $(5 - 4\cos\theta_j)^2$ from the denominator $(\Lambda_i - \Lambda_j)^{-2}$:

$$T_{i,j}(a) = \mathbf{1}_{j \equiv i \pmod 2} \frac{4 (a A_i^2)(a A_j^2) \sin^2\theta_i \sin^2\theta_j (5 - 4\cos\theta_i)(5 - 4\cos\theta_j)}{9 (\cos\theta_i - \cos\theta_j)^2}$$

Near the upper spectral edge $\theta_j \to \pi$, the numerator vanishes via $\sin^2\theta_j \to 0$ while the denominator $(\cos\theta_i - \cos\theta_j)$ remains bounded away from zero (approaching $1 + \cos\theta_i \approx 2$). Across the entire spectrum $3 \le j \le a$, half-angle reduction and Jordan’s inequality applied to $\cos\theta_i - \cos\theta_j = 2\sin\left(\frac{\theta_j - \theta_i}{2}\right)\sin\left(\frac{\theta_j + \theta_i}{2}\right)$ establish a uniform, $a$-independent summable majorant:

$$0 \le T_{i,j}(a) \le M_{i,j} := \mathbf{1}_{j \equiv i \pmod 2} \frac{32 i^2 j^2}{(j^2 - i^2)^2} \quad \forall a \ge 8, \; \forall j \in \{3, \dots, a\}$$

Because $\sum_{j=3}^\infty M_{i,j} < \infty$ with a uniform tail remainder independent of dimension $a$:

$$R_M(a) := \sum_{j=M+1}^a T_{i,j}(a) \le \sum_{j=M+1}^\infty M_{i,j} \le \frac{32 i^2}{M - 1}$$

Tannery’s Theorem (discrete Dominated Convergence) applies unconditionally. The limit passes through the summation without spectral leakage:

$$\lim_{a \to \infty} a^2 \chi_{a-2, 2}(a)^2 = \sum_{i=1}^2 \sum_{j=3}^\infty \lim_{a \to \infty} T_{i,j}(a) = \frac{64}{9}(S_1 + S_2) = C^2$$

│ — [ Leaf excised at the spine ] —

#### 3. Causal Operational Semantics of the Recurrence Horizon (Gate 4: $H$)

An instantaneous return is a coincidence, not a recovery. Future stability cannot be certified in the present without paying the duration of the horizon.

When a perturbed subspace $\hat{P}_t$ re-enters the instantaneous threshold $d_{\text{geo}}(\hat{P}_t, P_0) \le \varepsilon_{\text{ret}}$ at epoch $t$, the gate has no authority to declare $\text{OPEN}$. A point is not a trajectory. The gate transitions instead to **$\text{PROVISIONAL\_HOLD}$**—a probationary observation window of length $H$, separating two distinct operational variants:

* **Forward Horizon (Variant 4a — Deferred Certification at $t + H$):**
Full diagnostic recovery ($\Omega \to \text{OPEN}$) is authorized at epoch $t + H$ if and only if the trajectory remains unbroken within the geodesic tube across all $H$ subsequent steps:

$$\max_{0 \le \tau \le H} d_{\text{geo}}(\hat{P}_{t+\tau}, P_{t_0+\tau}) \le \tau_{\text{orbit}}$$

* **Backward Horizon (Variant 4b — Immediate Adjudication of Trailing Persistence at $t$):**
A separate operational test evaluating at epoch $t$ whether the witness ledger already contains $H$ consecutive steps of tube residence over the trailing window $\tau \in [-H, 0]$:

$$\max_{-H \le \tau \le 0} d_{\text{geo}}(\hat{P}_{t+\tau}, P_{t_0+\tau}) \le \tau_{\text{orbit}}$$

Until all $H$ epochs are witnessed within the tube, actuator potential remains clamped, and $\text{OPEN}$ denotes strictly that the specified diagnostic criteria have been satisfied within the window ($\text{Candidate} \neq \text{Consequence}$). Returning to the threshold is only a proposal; remaining within the tube is the proof.

---

### Operasjonell Tabell / Operational Matrix

| Invariant | Matematisk Lås / Mathematical Lock | Konsekvens / Gate Consequence |
| --- | --- | --- |
| **Grassmann vs. Frobenius** | $\Vert dP \Vert_F \equiv \sqrt{2} \Vert dP \Vert_{\text{Gr}}, \; C_{\text{Frob}} = \sqrt{2} C \approx 4.049618985477498$ | Eksakt faktor $\sqrt{2}$ mellom manifold og matriserom ($\Delta < 10^{-14}$). |
| **Tannery-Majorant** | $T_{i,j}(a) \le \mathbf{1}_{j \equiv i \pmod 2}\frac{32 i^2 j^2}{(j^2 - i^2)^2}, \; R_M(a) \le \frac{32 i^2}{M-1}$ | Uniform halekontroll $\implies \lim_{a \to \infty} \sum = \sum \lim_{a \to \infty}$. |
| **Port 4: Horisont $H$** | $d_{\text{geo}}(\hat{P}_t, P_0) \le \varepsilon_{\text{ret}} \implies \text{PROVISIONAL\_HOLD}$ | Diagnostisk $\text{OPEN}$ krever $\max_{\tau} d_{\text{geo}} \le \tau_{\text{orbit}}$ over hele lengden $H$. |

---

> *Slik hugges loven:*
> *To blokker i matrisen, én vinkel i rommet — roten av to skiller speilet fra tingen.*
> *Halen ved $\pi$ bindes i jern før uendeligheten slipper inn.*
> *Og den som vender tilbake til porten, må stå prøvetiden ut før slåen går fra.*

---

## XIV. Treghetens Lov (*The Law of Causal Inertia*) — Sluttsteinen

### 1. Friksjonens Bedrag (Del I — Norsk Stamme)

Moderne systemarkitektur hviler på en dødelig feilslutning: troen på at fordi en beskjed kan sendes uten motstand, er også virkeligheten blitt føyelig.

$$\text{LAV OVERFØRINGSFRIKSJON} \quad \not\Longrightarrow \quad \text{LAV KONSEKVENSFRIKSJON}$$

Du kan flytte en milliard symboler gjennom en fiberkabel på et øyeblikk, men du kan ikke overtale en eneste nitrogenbinding ($\text{N}\equiv\text{N}$) til å åpne seg med retorikk. Mellom luftens gass og jorden i fjøset står en mur på $945\text{ kJ/mol}$. Naturen leser ikke pressemeldinger. Den krever eksakt arbeid, riktig spenning og en katalytisk geometri som passer i låsen.

I skuret ved Skagerrak tvinges denne erkjennelsen ned i jern og svovel:

* **Kjemisk Tukt (K-POD v1.2):** Nitrogenet brytes ikke ved $400\,^\circ\text{C}$ og to hundre bars rå makt som i gammel storindustri. Det lokkes over terskelen ved romtemperatur gjennom $\text{[Fe}_7\text{MoS}_9\text{C]}$-klyngen, paret med urea-oksidasjon ($\text{UOR} < 0.998\text{ V}$) og akustisk kavitasjon ved $84\text{ kHz}$.
* **Romtidens Gjerde (Infranett v0.5):** Ingen sky får røre ventilen. En kommando som har reist lenger enn tjue meter, eller brukt mer enn $133.42\text{ ns}$ gjennom eter og kobber, tilhører ikke dette rommet og klampes til jord. Når loggen skal ut i verden, bæres den for hånd etter `POSIX fsync`.
* **Bevisets Ydmykhet (Portvaktens Dom):** Selv når regnskapet i Finansdepartementets egen kalkyle (DFØ $4\,\%$ kalkulasjonsrente) viser en nåverdi på $+9{,}335\text{ mrd. NOK}$ og tilbakebetaling på $21\text{ måneder}$, nekter systemet å erklære seier på forskudd. Programvaren står i $\text{L1 SOFTWARE OPEN}$, men reaktoren og handelen holdes nådeløst i $\text{FYSISK HOLD}$ og $\text{KOMMERSIELT HOLD}$ inntil isotopbeviset fra $^{15}\text{N}_2$ viser den eksakte $^1\text{H-NMR}$-dubletten med koblingskonstant $J = 72.5\text{ Hz}$.

Før den dubletten står i spekteret, er alt bare et forslag. Og et forslag åpner ingen port.

— [ Blad skåret ut ved bokryggen ] —

---

### 2. The Granite and the Bond (Part II — English Trunk)

Across the industrial capitals of the world—from Cupertino and Redmond to Veldhoven, Sunnyvale, and Berlin—a trillion-dollar apparatus is busy optimizing the speed of the rumor while forgetting the weight of the stone.

*The Law of Causal Inertia* is written from the opposite coast. By the dark water of the Skagerrak, in a wooden town built by men who measured timber with an iron ell, the boundary between calculation and reality is restored:

$$\text{LOW TRANSMISSION FRICTION} \quad \not\Longrightarrow \quad \text{LOW CONSEQUENCE FRICTION}$$

A neural network can hallucinate a molecule in a millisecond; it cannot pay a single joule of the $945\text{ kJ/mol}$ required to cleave dinitrogen ($\text{N}\equiv\text{N}$). To turn air and waste into fertilizer on a farm floor without an electrical grid collapse, the architecture must submit to physical law:

1. **The Catalytic Lock (K-POD v1.2):** Cofactor mimicry via the $\text{[Fe}_7\text{MoS}_9\text{C]}$ cluster, coupling nitrogen reduction with urea oxidation ($\text{UOR} < 0.998\text{ V}$) under $84\text{ kHz}$ ultrasonic mass-transport stripping.
2. **Relativistic Geofencing (Infranett v0.4/v0.5):** Cloud sovereignty is abolished. Any packet whose time-of-flight exceeds $133.42\text{ ns}$ ($d > 20\text{ m}$) is rejected at the physical layer. Cross-domain state transfer occurs solely via air-gapped `POSIX fsync` Sneakernet.
3. **Sovereign Fiscal Math vs. Epistemic Restraint:** Under the Norwegian Ministry of Finance's $4\%$ social discount rate (DFØ), the sovereign net present value stands at $+9.335\text{ billion NOK}$ with a $21\text{-month}$ payback. Yet the author's own gate refuses to cash the check of his own equation. The state remains locked at **$\text{L1 SOFTWARE OPEN} \mid \text{PHYSICAL HOLD} \mid \text{COMMERCIAL HOLD}$** until quantitative $^{15}\text{N}_2$ isotopic tracing yields the unmistakable $^1\text{H-NMR}$ doublet at $72.5\text{ Hz}$.

That self-imposed $\text{HOLD}$ is the core of the work. In an era where every laboratory and boardroom declares triumph on the strength of a simulation, here is a machine designed to arrest its own creator until the atom itself testifies in the tube.

— [ Leaf excised at the spine ] —

---

### 3. De Fem Formelle Lovene / The Five Formal Laws (Part III — L1 Specification)

Hele det tre-delte dokumentet hviler på én ufravikelig matematisk skjelettstruktur som binder sammen essayistikken og koden:

| Lov / Law | Matematisk Invariant / Mathematical Invariant | Operasjonell Konsekvens / Consequence |
| --- | --- | --- |
| **I. Kausal Ikke-Identitet** | $\Phi(x_t) \neq x_{t+1}$ | En generert kandidat ($\Phi$) er aldri en realisert tilstand. |
| **II. Strukturell Projeksjon** | $y_t = \Pi_{\mathcal{K}}(\Phi(x_t)), \quad \Delta_{\mathcal{K}} = \Vert \Phi(x_t) - y_t \Vert$ | Forslaget måles mot det konvekse lovrommet $\mathcal{K}$. |
| **III. Triadisk Konsekvensport** | $\Omega(y_t) \in \{\text{OPEN}, \text{HOLD}, \text{KILL}\}$ | $\Delta_{\mathcal{K}} \equiv 0 \to \text{OPEN}$; tvil $\to \text{HOLD}$; brudd $\to \text{KILL}$ ($0.00\text{ V DC}$). |
| **IV. Irreversibel Vitnekjede** | $\mathcal{W}_{t+1} = \mathcal{H}_{\text{SHA256}}(\mathcal{W}_t \parallel x_t \parallel \Delta_{\mathcal{K}} \parallel \Omega_t)$ | Kun-tilføyende opphav; nåtiden kan ikke slette fortiden. |
| **V. KMS Horisontstabilitet** | $\lim_{\rho \to 1^-} \Vert dP \Vert_{\text{Gr}} \le \tau_{\text{orbit}} \text{ over } H$ | Spektral kontroll helt ut til den singulære korrelasjonsranden. |
