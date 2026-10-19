# K-POD v1.2 — Operativ Laboratorieprotokoll & Rekvisisjonsark for $^{15}\text{N}_2$ / $^1\text{H-NMR}$ ($72.5\text{ Hz}$)
## *Operational Laboratory Protocol & Falsification Sheet for the `L1` $\to$ `L3` Consequence Gate*

> **Dokument-ID // Document ID:** `KPOD-V12-L3-15N2-NMR-PROTOCOL-2026-v1.0`  
> **Forfatter & Ansvarlig // Principal Investigator:** Marius Egerhei Torjusen (ORCID: [0009-0006-0431-6637](https://orcid.org/0009-0006-0431-6637))  
> **Enhet // Entity:** Brahman  
> **Tilknyttet Hovedverk // Companion Monograph:** [`LAW_OF_CAUSAL_INERTIA.md`](./LAW_OF_CAUSAL_INERTIA.md)  
> **Kanoniske Motorer (`L1`):** `kpod_l3_fasespeil_verifier_engine.py` · `kpod_v12_digital_twin_engine.py` (`18/18 PASS`)  
> **Nåværende Portstatus // Current Gate State:** $\boxed{\text{L1 SOFTWARE OPEN}} \;\cdot\; \boxed{\text{FYSISK HOLD}} \;\cdot\; \boxed{\text{KOMMERSIELT HOLD}}$

---

## 1. Formål og Falsifikasjonskontrakt // Purpose & Falsification Contract

**Norsk:**
Dette dokumentet er det operative arbeidsarket for å avgjøre om **K-POD v1.2** ($[\text{Fe}_7\text{MoS}_9\text{C}]$ i syntetisk $[\text{P-N-P}]$-pincerligand) faktisk kløyver trippelbindingen i dinitrogen ($\text{N}\equiv\text{N}$, $945\text{ kJ/mol}$) ved romtemperatur. I henhold til `AGENTS.md` og *Treghetens lov* gir $100\,\%$ grønne enhetstester i `L1` **null fysisk autoritet** (`INSPIRED_BY != IMPLEMENTS != PROVES`). Reaktoren holdes i **$\text{FYSISK HOLD}$** inntil et akkreditert NMR-laboratorium (ISO/IEC 17025 eller universitets-NMR ved UiO / NTNU / UiB / SINTEF) returnerer rådata som passerer samtlige seks kontroller (`K1`–`K6`), `Lock 0`-massebalansen og de fire kvadrupel-vitnene under.

**English:**
This document is the operational laboratory protocol and falsification sheet required to determine whether **K-POD v1.2** ($[\text{Fe}_7\text{MoS}_9\text{C}]$ in a synthetic $[\text{P-N-P}]$ pincer ligand) cleaves the dinitrogen triple bond ($\text{N}\equiv\text{N}$, $945\text{ kJ/mol}$) under ambient conditions. Per `AGENTS.md` and *The Law of Causal Inertia*, $100\%$ passing `L1` software unit tests confer **zero physical authority** (`INSPIRED_BY != IMPLEMENTS != PROVES`). The reactor remains locked in **$\text{PHYSICAL HOLD}$** until an external spectroscopy facility returns raw FID/JCAMP-DX spectra and coulometric logs that pass all six controls (`K1`–`K6`), the `Lock 0` nitrogen mass balance, and the four physical witnesses below.

---

## 2. Den Seks-Trinns Kontrollmatrisen (`K1`–`K6`) // The Six-Stage Control Matrix

For å eliminere falske positiver fra adventitivt ammoniakk, nitrat/nitritt-forurensning i $^{15}\text{N}_2$-gassflasken, nedbrytning av ligand eller membranlekkasje av urea fra anodekammeret, kjøres følgende seks protokoller i lukket sekvens ($\text{LOD} = 1.0 \times 10^{-9}\text{ mol}$, $\text{LOQ} = 3.0 \times 10^{-9}\text{ mol}$):

| Kontroll-ID | Gassføde | Påtrykt Spenning | Katodesubstrat | Varighet | Krav for Godkjenning ($\Pi_K$) | Ved Avvik ($\Omega$) |
| :---: | :---: | :---: | :--- | :---: | :--- | :---: |
| **`K1`** *(Systemblank)* | $\text{Ar}$ ($99.999\,\%$) | $0.000\text{ V}$ (Åpen krets) | $[\text{Fe}_7\text{MoS}_9\text{C}]\text{-PNP}$ | $7\,200\text{ s}$ | $[\text{NH}_4^+]_{\text{kat}} \le \text{LOD}$ | `GATE::HOLD` *(Blank kontaminering)* |
| **`K2`** *(Elektroblank)* | $\text{Ar}$ ($99.999\,\%$) | $0.998\text{ V}$ ($84\text{ kHz}$ puls) | $[\text{Fe}_7\text{MoS}_9\text{C}]\text{-PNP}$ | $7\,200\text{ s}$ | $[\text{NH}_4^+]_{\text{kat}} \le \text{LOD}$ *(Utelukker ligand-nedbrytning)* | `GATE::HOLD` *(Ligand/katalysator-blødning)* |
| **`K3`** *(Gassblank)* | $^{15}\text{N}_2$ ($98+\text{ atom-}\%$, syre-/Cu-vasket) | $0.000\text{ V}$ (Åpen krets) | $[\text{Fe}_7\text{MoS}_9\text{C}]\text{-PNP}$ | $7\,200\text{ s}$ | $[{}^{15}\text{NH}_4^+]_{\text{kat}} \le \text{LOD}$ *(Utelukker $^{15}\text{NH}_3$/$^{15}\text{NO}_x$ i gassflaske)* | `GATE::HOLD` *(Uren isotopgass)* |
| **`K4`** *(Prosesskontroll)* | $^{14}\text{N}_2$ ($99.999\,\%$) | $0.998\text{ V}$ ($84\text{ kHz}$ puls) | $[\text{Fe}_7\text{MoS}_9\text{C}]\text{-PNP}$ | $14\,400\text{ s}$ | $^1\text{H-NMR}$ **1:1:1 triplett** ($J({}^{14}\text{N},{}^1\text{H}) \approx 52.3\text{ Hz}$) | `GATE::HOLD` *(Referanseavvik)* |
| **`K5`** *(Isotopbevis, $n \ge 3$)* | $^{15}\text{N}_2$ ($98+\text{ atom-}\%$, vasket) | $0.998\text{ V}$ ($84\text{ kHz}$ puls, $\tau_p = 500\text{ ns}$) | $[\text{Fe}_7\text{MoS}_9\text{C}]\text{-PNP}$ | $14\,400\text{ s}$ ($\times 3$) | $^1\text{H-NMR}$ **1:1 dublett** ($J({}^{15}\text{N},{}^1\text{H}) \in [71.0, 75.0]\text{ Hz}$, senter $72.5\text{--}73.6\text{ Hz}$), $\text{FE} \ge 80.0\,\%$ | `GATE::OPEN` *(Kun når alle 3 replikater passerer)* |
| **`K6`** *(Substratblank)* | $^{15}\text{N}_2$ ($98+\text{ atom-}\%$, vasket) | $0.998\text{ V}$ ($84\text{ kHz}$ puls) | Bart karbon-/Ti-substrat *(uten FeMoS)* | $14\,400\text{ s}$ | $[{}^{15}\text{NH}_4^+]_{\text{kat}} \le \text{LOD}$ | `GATE::HOLD` *(Bakgrunnsreduksjon)* |

---

## 3. Kvadrupel-Vitne & `Lock 0` Massebalanse // Quadruple Witness & `Lock 0` Accounting

### A. De Fire Fysiske Detektorkravene (`SPEC-334`)

1. **Kjernefysisk Spinn-Kobling ($^1\text{H-NMR}$ ved $400\text{--}600\text{ MHz}$ i $\text{DMSO-}d_6$ / syret $\text{H}_2\text{O}$ med $\text{Maleinsyre}$ internstandard):**
   * $^{15}\text{N}$ har kjernefysisk spinn $I = 1/2$, som splitter ammoniumprotonene ($^{15}\text{NH}_4^+$, $\delta \approx 6.98\text{ ppm}$) i en skarp **dublett** ($2$ topper, intensitetsforhold $1:1$) med koblingskonstant:
     $$J({}^{15}\text{N}, {}^1\text{H}) = 72.5\text{--}73.6\text{ Hz} \quad (\text{akseptansebånd i motor: } [71.0, 75.0]\text{ Hz})$$
   * $^{14}\text{N}$ ($I = 1$) gir en **triplett** ($3$ topper, $1:1:1$) med $J({}^{14}\text{N}, {}^1\text{H}) \approx 52.3\text{ Hz}$. Enhver synlig $^{14}\text{N}$-triplett i `K5` eller relaksasjonsforsinkelse $d_1 < 5 T_1$ utløser umiddelbart `GATE::HOLD`.
2. **Membra-Isolasjon & Urea-Krysskontaminering:**
   * Konsentrasjonen av urea og nitrat/nitritt i katolytten etter kjøring må verifiseres til:
     $$[\text{CO(NH}_2)_2]_{\text{katolytt}} \le 1.0 \times 10^{-9}\text{ mol} \quad (\text{LOD}), \qquad [\text{NO}_2^- + \text{NO}_3^-]_{\text{katolytt}} \le \text{LOD}$$
3. **Katalysator-Integritet ($^{57}\text{Fe}$ Mössbauer & GC-TCD Oksygenlås):**
   * Online GC-TCD overvåker $[\text{O}_2] \le 0.1\text{ ppm}$. Ved $[\text{O}_2] > 0.1\text{ ppm}$ utløser 5-Lock CDC FPGA-vakten ($\tau = 12.5\ \mu\text{s}$) umiddelbart `GATE::KILL` ($0.00\text{ V DC}$) for å beskytte $[\text{Fe}_7\text{MoS}_9\text{C}]$-klyngen mot oksidasjon.
   * Post-run $^{57}\text{Fe}$ Mössbauer-isomerskift skal ligge i $\delta \in [0.38, 0.42]\text{ mm/s}$ (bekrefter intakt klynge, ingen $\text{Fe}_2\text{O}_3$-dannelse).
4. **Coulometrisk Faradaisk Regnskap ($z = 3$):**
   * Integrert ladning $Q_{\text{tot}} = \int_0^T I(t)\,dt$ må korrespondere med kvantifisert $^{15}\text{NH}_4^+$ via NMR-integrasjon:
     $$\text{FE}({}^{15}\text{NH}_3) = \frac{3 \cdot F \cdot n({}^{15}\text{NH}_4^+)}{Q_{\text{tot}}} \ge 80.0\,\% \quad (\text{nominelt designpunkt: } 89.2\,\%)$$

### B. `Lock 0` — Støkiometrisk Skille mellom Isotopisk Kløyving og Netto Nitrogenfiksering

Som kodet i `kpod_v12_digital_twin_engine.py` (`Kardinaltest 7 & 8`), skiller protokollen strengt mellom to regimer:

* **Regime A — Anodisk Urea-Depolarisering (`UOR`, $E^0 = 0.37\text{ V}$, $V_{\text{cell}} \approx 0.998\text{ V}$):**
  $$\text{Anode: } \text{CO(NH}_2)_2 + 6\text{OH}^- \to \text{N}_2 + 5\text{H}_2\text{O} + \text{CO}_2 + 6e^-, \qquad \text{Katode: } {}^{15}\text{N}_2 + 6\text{H}^+ + 6e^- \to 2\,{}^{15}\text{NH}_3$$
  Her beviser $^{15}\text{N}_2$-dubletten ($72.5\text{ Hz}$) på katoden — kombinert med $[\text{Urea}]_{\text{katolytt}} \le \text{LOD}$ — at katoden utfører ekte elektrokjemisk $\text{N}\equiv\text{N}$-kløyving ved romtemperatur, mens det totale systemets netto fikserte nitrogenbalanse er $\Delta N_{\text{fixed}} = N_{\text{out, NH}_3} - N_{\text{in, urea}} = 0$ (energigjerrig elektrokjemisk nitrogen-oppgradering av husdyrgjødsel).
* **Regime B — Netto De Novo Nitrogenfiksering (`OER` / Nitrogenfri Anode, $\Delta N_{\text{fixed}} > 0$):**
  For å åpne `Lock 0` for netto tilførsel av nytt fiksert nitrogen til biosfæren ($\Delta N_{\text{fixed}} > 0$), kjøres et dedikert replikatsett med **nitrogenfri anolytt** ($\text{fixed\_n\_in\_mol\_day} = 0$).

---

## 4. Budsjett og Rekvisisjonsliste (Oppstart 1 — $150\,000\text{ NOK}$) // Requisition & Budget

| Post | Beskrivelse / Spesifikasjon | Estimert Kostnad (NOK) |
| :--- | :--- | ---: |
| **1. Isotopgass ($^{15}\text{N}_2$)** | $2 \times 1\text{ L}$ sylinder $^{15}\text{N}_2$ ($98+\text{ atom-}\%$, Sigma-Aldrich / Cambridge Isotope Labs) inkl. lavtrykksregulator | $48\,000\text{ kr}$ |
| **2. Gassrensing (Pre-Trap)** | Syrefelle ($0.05\text{ M H}_2\text{SO}_4$) + alkalisk felle ($0.1\text{ M KOH}$) + redusert $\text{Cu}$-kolonne for fjerning av spor-$^{15}\text{NH}_3$ og $^{15}\text{NO}_x$ | $14\,000\text{ kr}$ |
| **3. NMR-Spektroskopi** | Ekstern instrumenttid ved $500/600\text{ MHz}$ kryoprobe $^1\text{H-NMR}$ ($24$ prøver: `K1`–`K6` inkl. $3\times\text{K5}$ i Regime A og Regime B, $\text{DMSO-}d_6$) | $42\,000\text{ kr}$ |
| **4. Elektrokjemisk Celledrift** | Nafion/bipolar membran-sett, deutererte reagenser, kalibrert coulometer-logg og GC-TCD $\text{O}_2$-kontroll | $28\,000\text{ kr}$ |
| **5. Uavhengig Attestasjon** | Analytisk rapport og signert SHA-256 rådata-pakke (FID + integrasjonstabell) fra utførende laboratorium | $18\,000\text{ kr}$ |
| **SUM (`L3` Verifikasjonspakke)** | **Komplett fysisk portåpningstesting (`K1`–`K6`)** | **$150\,000\text{ kr}$** |

---

## 5. Deterministisk Inntak i `L1`-Motoren // Deterministic Ingestion Command

Når laboratoriet leverer de målte verdiene fra `K1`–`K6`, kjøres sjekken lokalt uten nettverkstilkobling:

```bash
PYTHONPATH=03_ENGINES/ENGINES/micro_engines python3 -m unittest \
  03_ENGINES/tests/test_kpod_l3_fasespeil_verifier_engine.py \
  03_ENGINES/tests/test_kpod_v12_digital_twin_engine.py -v
```

### Signaturblokk ved Porten // Gate Signature Block

* **Programvarestatus (`L1`):** `18/18 PASS` (`OPEN`)
* **Fysisk reaktorstatus (`L3`):** `HOLD` *(avventer signert $^1\text{H-NMR}$ FID med $J({}^{15}\text{N}, {}^1\text{H}) = 72.5\text{ Hz}$)*
* **Kommersiell status:** `HOLD` *(ingen lisensiering eller emisjon før `L3 = OPEN`)*
