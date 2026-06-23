# Climate Physical Risk Intelligence — Learning Path & Project Portfolio

> *From Class 12 + NumPy to a corporate climate risk specialist role.*
> *Every project here is production-quality analysis, not coursework.*

<br>

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Xarray](https://img.shields.io/badge/Xarray-2dd6a0?style=flat-square)
![GeoPandas](https://img.shields.io/badge/GeoPandas-139C5A?style=flat-square)
![CMIP6](https://img.shields.io/badge/CMIP6-b48cff?style=flat-square)
![GEE](https://img.shields.io/badge/Google_Earth_Engine-4285F4?style=flat-square&logo=google&logoColor=white)
![TCFD](https://img.shields.io/badge/TCFD_Framework-f5a623?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active_Learning-2dd6a0?style=flat-square)

</div>

---

## What this repository is

This is not a collection of tutorials or copy-pasted exercises.

Every project in this repository is designed to answer a real analytical question using real public data — the kind of question that climate risk consultancies at MSCI, S&P Global Sustainalytics, Verisk, and CRISIL answer for paying clients. I am building these in public, documenting my methodology, and publishing my findings so that by the time I graduate, this repository is a portfolio of professional-grade work, not just evidence of learning.

**The target role:** Climate Physical Risk Intelligence Specialist at a rating agency, risk consultancy, or ESG analytics firm.

**The method:** 8 phases over 12 months, parallel to a Bachelor's degree, with one publishable project per phase.

---

## Repository structure

```
climate-datasci-learning-path/
│
├── math-foundations/
│   ├── M01_carbon_budget_log_clock/
│   ├── M02_monsoon_volatility_fingerprint/
│   ├── M03_distribution_comparison_river_data/
│   ├── M04_return_period_atlas_10_rivers/
│   ├── M05_temperature_attribution_15_cities/
│   └── M06_cmip6_disagreement_map/
│
├── phase1_python_data_stack/
│   └── P1_01_district_vulnerability_index/
│
├── phase1b_machine_learning/
│   └── ML01_drought_early_warning_engine/
│
├── phase2_geospatial/
│   └── P2_01_coastal_displacement_scenarios/
│
├── phase3_climate_data_cloud/
│   └── P3_01_urban_heat_island_forensics/
│
├── phase4_climate_science/
│   └── P4_01_ssp_divergence_moment/
│
├── phase5_corporate_risk/
│   └── P5_01_thermal_powerplant_cvar/     ← CAPSTONE
│
└── resources/
    ├── datasets.md
    ├── papers.md
    └── tcfd_reports_read.md
```

---

## Projects — full index

Each project card shows: what was built, the key finding, and the exact technical pipeline used.

---

### MATH FOUNDATIONS

#### `M·01` India's Remaining Carbon Budget — A Logarithmic Clock
![Level](https://img.shields.io/badge/Level-1_Algebra_&_Logs-2dd6a0?style=flat-square)
![Status](https://img.shields.io/badge/-Complete-2dd6a0?style=flat-square)

India's cumulative CO₂ emissions plotted on a log scale, crossed with IPCC AR6 remaining carbon budgets for 1.5°C and 2°C pathways. Computes the year at which India exhausts its population-weighted fair-share budget at current emission growth rates.

**Key tools:** `Pandas · Matplotlib · plt.yscale('log') · df.cumsum()`
**Key math:** Logarithms · exponential growth · linear extrapolation
**Finding:** `[To be filled when complete]`

→ [`view project`](./math-foundations/M01_carbon_budget_log_clock/)

---

#### `M·02` The Indian Monsoon Volatility Fingerprint (1951–2023)
![Level](https://img.shields.io/badge/Level-2_Descriptive_Statistics-4da6ff?style=flat-square)
![Status](https://img.shields.io/badge/-Complete-2dd6a0?style=flat-square)

Z-score normalised heatmap of annual JJAS monsoon rainfall for 36 Indian states across 7 decades. Reveals which states show statistically significant increases in rainfall volatility — the physical signature of a destabilising monsoon system.

**Key tools:** `Pandas · Seaborn · df.groupby() · pivot_table()`
**Key math:** Standard deviation · z-scores (x − μ)/σ · decadal averaging
**Finding:** `[To be filled when complete]`

→ [`view project`](./math-foundations/M02_monsoon_volatility_fingerprint/)

---

#### `M·03` Why the Normal Distribution Kills People — A Visual Proof
![Level](https://img.shields.io/badge/Level-3_Probability_Distributions-f5a623?style=flat-square)
![Status](https://img.shields.io/badge/-In_Progress-f5a623?style=flat-square)

Comparison of Normal, Log-Normal, and GEV distribution fits to annual maximum discharge data for the Ganga, Krishna, and Brahmaputra rivers. Shows how the 1-in-100-year flood estimate changes by 40–100% depending on distribution choice — and which distribution the data actually supports.

**Key tools:** `scipy.stats.norm · scipy.stats.lognorm · scipy.stats.genextreme · QQ-plots`
**Key math:** PDF · CDF · MLE fitting · percentile function (.ppf) · fat tails

→ [`view project`](./math-foundations/M03_distribution_comparison_river_data/)

---

#### `M·04` Return Period Atlas — 10 Indian Rivers, Raw Data to 200-Year Estimates
![Level](https://img.shields.io/badge/Level-4_Extreme_Value_Theory-ff6b6b?style=flat-square)
![Status](https://img.shields.io/badge/-In_Progress-f5a623?style=flat-square)

Formal flood frequency analysis using GEV distribution fitted to annual maximum discharge series for 10 Indian rivers. Produces 10/25/50/100/200-year return level estimates with 95% bootstrap confidence intervals. The exact methodology used in professional hydrological risk assessments.

**Key tools:** `scipy.stats.genextreme · NumPy bootstrap · Matplotlib log-scale`
**Key math:** `Return level = GEV.ppf(1 − 1/T, c, loc, scale)` · bootstrap CI · GEV shape parameter interpretation

→ [`view project`](./math-foundations/M04_return_period_atlas_10_rivers/)

---

#### `M·05` Separating Urbanisation from Climate: India's Temperature Attribution Problem
![Level](https://img.shields.io/badge/Level-5_Linear_Regression-b48cff?style=flat-square)
![Status](https://img.shields.io/badge/-Planned-6b7585?style=flat-square)

Multiple linear regression decomposing observed temperature trends in 15 Indian cities into global warming signal (CO₂ concentration) and urban heat island signal (population growth). Uses partial R² decomposition to quantify what fraction of each city's warming is climate vs urbanisation.

**Key tools:** `statsmodels.OLS · sklearn · Matplotlib stacked bar`
**Key math:** `Temp = β₀ + β₁×CO₂ + β₂×Population` · partial R² · coefficient interpretation

→ [`view project`](./math-foundations/M05_temperature_attribution_15_cities/)

---

#### `M·06` The CMIP6 Disagreement Map — Where Models Are Most Uncertain About India
![Level](https://img.shields.io/badge/Level-6_Ensemble_Statistics-40c9c9?style=flat-square)
![Status](https://img.shields.io/badge/-Planned-6b7585?style=flat-square)

Inter-model standard deviation of precipitation projections across 15 CMIP6 models for India under SSP5-8.5. Maps regions of high model agreement vs fundamental disagreement. Includes IPCC-style confidence hatching — the same technique used in AR6 Chapter 12 figures.

**Key tools:** `Xarray · xr.concat() · Cartopy · scipy.interpolate (regridding)`
**Key math:** Ensemble percentiles · inter-model spread · 80% agreement threshold · grid-cell area weighting

→ [`view project`](./math-foundations/M06_cmip6_disagreement_map/)

---

### PHASE 1 — PYTHON DATA STACK

#### `P1·01` Climate Vulnerability Index — All 739 Indian Districts
![Phase](https://img.shields.io/badge/Phase-1_Python_Data_Stack-a8e063?style=flat-square)
![Status](https://img.shields.io/badge/-Building-f5a623?style=flat-square)

Composite vulnerability index scoring all 739 Indian districts across 5 indicators: rainfall anomaly trend, temperature increase, drought frequency, flood event frequency, and adaptive capacity (district GDP proxy). Produces a ranked table and state-level aggregation chart.

**Key tools:** `Pandas pd.merge() · fillna() · Seaborn correlation heatmap · df.style`
**Key math:** Min-max normalisation · weighted composite · correlation matrix · sensitivity analysis
**Data:** IMD · NDMA · NITI Aayog · data.gov.in

→ [`view project`](./phase1_python_data_stack/P1_01_district_vulnerability_index/)

---

### PHASE 1b — MACHINE LEARNING

#### `ML·01` 90-Day Agricultural Drought Early Warning Engine
![Phase](https://img.shields.io/badge/Phase-1b_Machine_Learning-f5a623?style=flat-square)
![Status](https://img.shields.io/badge/-Planned-6b7585?style=flat-square)

Random forest classifier predicting drought severity category 90 days in advance using lagged climate signals (SPI, ENSO index, temperature anomaly, soil moisture). Trained on 30 years of NDMA district drought declaration data using time-series cross-validation.

**Key tools:** `sklearn.RandomForestClassifier · class_weight='balanced' · joblib`
**Key math:** Precision/recall/F1 · feature importance (Gini) · lag feature engineering · time-series CV
**Live:** Model updated monthly with current SPI/ENSO inputs

→ [`view project`](./phase1b_machine_learning/ML01_drought_early_warning_engine/)

---

### PHASE 2 — GEOSPATIAL

#### `P2·01` India's Shrinking Coastline — Displacement Under 3 SLR Scenarios
![Phase](https://img.shields.io/badge/Phase-2_Geospatial-4da6ff?style=flat-square)
![Status](https://img.shields.io/badge/-Planned-6b7585?style=flat-square)

SRTM DEM thresholded at 0.5m, 1.0m, and 2.0m SLR to compute inundation polygons. Joined with GPW v4 population density raster to compute displaced population per Indian state per scenario. Three-panel Cartopy map + state-level displacement table.

**Key tools:** `Rasterio · GeoPandas sjoin() · rasterio.features.shapes() · Cartopy`
**Key math:** Raster thresholding · population count = density × area · spatial aggregation
**Data:** SRTM 90m DEM · CoastalDEM v2 · GPW v4 · GADM shapefiles · IPCC AR6 Table 9.9

→ [`view project`](./phase2_geospatial/P2_01_coastal_displacement_scenarios/)

---

### PHASE 3 — CLIMATE DATA & CLOUD

#### `P3·01` Urban Heat Island Forensics — 20 Cities, 20 Years
![Phase](https://img.shields.io/badge/Phase-3_Climate_Data-ff6b6b?style=flat-square)
![Status](https://img.shields.io/badge/-Planned-6b7585?style=flat-square)

Google Earth Engine extraction of MODIS MOD11A2 Land Surface Temperature for 20 Indian cities (2003–2023). Urban core (5km radius) vs rural ring (15–20km annulus) comparison. Computes UHI intensity time series and correlates growth rate with population expansion.

**Key tools:** `Google Earth Engine Python API · geemap · ee.Reducer.mean() · ee.ImageCollection`
**Key math:** UHI = urban LST − rural LST · linear trend slope · Pearson correlation
**Data:** MODIS MOD11A2 (via GEE) · Census India populations

→ [`view project`](./phase3_climate_data_cloud/P3_01_urban_heat_island_forensics/)

---

### PHASE 4 — CLIMATE SCIENCE

#### `P4·01` The SSP Divergence Moment — When Does India's Emissions Choice Lock In?
![Phase](https://img.shields.io/badge/Phase-4_Climate_Science-b48cff?style=flat-square)
![Status](https://img.shields.io/badge/-Planned-6b7585?style=flat-square)

Finds the year at which the 95th percentile of the SSP1-2.6 ensemble no longer overlaps the 5th percentile of the SSP5-8.5 ensemble — the statistical point of no return where emissions pathways become irreversible. Computed at both national and grid-cell level across India. Includes a 1-page corporate policy brief.

**Key tools:** `Xarray · xr.quantile() · Cartopy · NASA Nex-GDDP-CMIP6`
**Key math:** Ensemble percentile spread · statistical non-overlap test · area-weighted national mean

→ [`view project`](./phase4_climate_science/P4_01_ssp_divergence_moment/)

---

### PHASE 5 — CORPORATE RISK · CAPSTONE

#### `P5·01` ⚡ Climate Value at Risk — India's 20 Largest Thermal Power Plants (2030–2050)
![Phase](https://img.shields.io/badge/Phase-5_Corporate_Risk-f5a623?style=flat-square)
![Status](https://img.shields.io/badge/-Planned-6b7585?style=flat-square)
![Type](https://img.shields.io/badge/Type-CAPSTONE-ff6b6b?style=flat-square)

**This is the capstone project.**

Asset-level physical climate risk assessment for India's 20 largest coal thermal power plants. Three physical hazard channels: temperature increase (cooling water stress → thermal efficiency loss), flood inundation risk (FATHOM flood depth maps), and water withdrawal stress (WRI Aqueduct). Risk quantified as revenue loss under low/central/high scenarios using CMIP6 ensemble 5th/50th/95th percentile temperature projections. Output structured in TCFD disclosure format.

```
Risk = Hazard × Exposure × Vulnerability
     where Hazard    = CMIP6 temperature increase / flood return period / water stress score
           Exposure  = installed MW × capacity factor × electricity price
           Vulnerability = plant age × cooling technology × proximity to water body
```

**Key tools:** `Xarray · GeoPandas · Rasterio · Cartopy · Pandas`
**Key math:** Weighted risk scoring · financial loss function · ensemble uncertainty bands · TCFD structure
**Output:** Risk-ranked table · asset map by risk tier · 3-page executive report (PDF)
**Data:** WRI Global Power Plant DB · NASA Nex-GDDP-CMIP6 · WRI Aqueduct · FATHOM · CEA reports

→ [`view project`](./phase5_corporate_risk/P5_01_thermal_powerplant_cvar/)

---

## Methodology notes

### On uncertainty
Every quantitative output in this repository reports uncertainty ranges, not point estimates. A single number without a confidence interval is not analysis — it is an assertion. All climate projections use ensemble 5th/50th/95th percentile spread across CMIP6 models.

### On distribution choice
Climate extremes are not normally distributed. All extreme event analysis in this repository uses Generalized Extreme Value (GEV) or Log-Normal distributions fitted to empirical data, validated with QQ-plots. Using a Normal distribution on flood frequency data is a methodological error documented and demonstrated in `M·03`.

### On time-series validation
All machine learning models in this repository use time-ordered train/test splits, never random shuffles. Shuffling a climate time series and calling it cross-validation is data leakage. See `ML·01` methodology notes.

### On attribution
Observed trends are always decomposed into their drivers where possible. Conflating global warming signal with urban heat island effect or land use change produces misleading risk estimates. See `M·05` for the regression-based attribution approach.

---

## Learning path and progress

```
MATH FOUNDATIONS              STATUS          CODING PHASES              STATUS
──────────────────────        ──────          ──────────────────────     ──────
Level 1: Algebra & logs       ██████░░░░ 60%  Phase 1: Python stack      ████░░░░░░ 40%
Level 2: Descriptive stats    ███░░░░░░░ 30%  Phase 1b: ML basics        ░░░░░░░░░░  0%
Level 3: Distributions        ░░░░░░░░░░  0%  Phase 2: Geospatial        ░░░░░░░░░░  0%
Level 4: Extreme values       ░░░░░░░░░░  0%  Phase 3: Climate data      ░░░░░░░░░░  0%
Level 5: Regression           ░░░░░░░░░░  0%  Phase 4: Climate science   ░░░░░░░░░░  0%
Level 6: Ensemble stats       ░░░░░░░░░░  0%  Phase 5: Corporate risk    ░░░░░░░░░░  0%

[update this manually each week]
```

---

## Data sources used across this repository

| Dataset | Source | Format | Used in |
|---------|--------|--------|---------|
| CO₂ emissions by country | Our World in Data | CSV | M·01 |
| IMD subdivision rainfall (1951–present) | India Meteorological Dept | CSV | M·02, P1·01 |
| River discharge — annual maximum | India-WRIS / CWC | CSV | M·03, M·04 |
| India district shapefiles | GADM | SHP | P1·01, P2·01 |
| SRTM 90m Digital Elevation Model | NASA Earthdata | GeoTIFF | P2·01 |
| GPW v4 Population Density | CIESIN | GeoTIFF | P2·01 |
| MODIS MOD11A2 Land Surface Temperature | NASA via GEE | Image Collection | P3·01 |
| ERA5 Historical Reanalysis | Copernicus CDS | NetCDF | Phase 3 |
| CMIP6 / Nex-GDDP projections | NASA (SSP1-2.6, SSP5-8.5) | NetCDF | M·06, P4·01, P5·01 |
| Global Power Plant Database | WRI | CSV | P5·01 |
| WRI Aqueduct Water Risk | WRI | API / SHP | P5·01 |
| FATHOM India flood depth maps | FATHOM (academic) | GeoTIFF | P5·01 |
| NDMA drought declarations | NDMA India | CSV / PDF | ML·01 |

---

## Reading list

Papers, reports, and books being read alongside this work:

- [ ] IPCC AR6 — Chapter 12: Central and Southern Asia (India-specific projections)
- [ ] IPCC AR6 — Technical Summary Annex on Uncertainty Guidance
- [ ] RBI Report on Climate Risk and Sustainable Finance (2022)
- [ ] TCFD Recommendations Report (2017) — core framework document
- [ ] GARP SCR Study Guide — Sustainability and Climate Risk
- [x] *Naked Statistics* — Charles Wheelan (probability intuition, highly readable)
- [ ] *Introduction to Hydrology* — Ven Te Chow (Chapter on frequency analysis)
- [ ] Infosys TCFD Disclosure Report 2023
- [ ] Tata Steel TCFD Disclosure Report 2023

---

## Certifications in progress

| Certification | Provider | Status | Target |
|--------------|---------|--------|--------|
| Statistics & Probability | Khan Academy | 🟡 In Progress | Month 2 |
| Pandas + Data Viz | Kaggle Learn | ✅ Complete | — |
| GIS Specialization | Coursera · UC Davis | ⬜ Planned | Month 4 |
| Climate Anomalies Specialization | Coursera · CU Boulder | ⬜ Planned | Month 7 |
| Sustainability & Climate Risk (SCR®) | GARP | ⬜ Planned | Month 12 |

---

<div align="center">

*Building publicly. Every project is designed to be the kind of work that gets cited, not just graded.*

**Anuj Sharma** · Climate Risk Intelligence Specialist in training · India

</div>
