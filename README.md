# Sustainable Greenhouse Energy System Design

### Techno-economic assessment and Python visualization of renewable energy supply concepts for greenhouse cultivation in Sicily

<p align="center">
  <strong>Python • Renewable Energy • Photovoltaics • Battery Storage • Biogas • Energy Systems • Data Visualization</strong>
</p>

---

## Project Overview

This project evaluates the energy supply of a **1,000 m² cut rose greenhouse in Sicily, Italy** and compares renewable alternatives with a conventional energy supply concept.

The engineering analysis combines greenhouse energy demand, photovoltaic generation, battery storage, biogas integration, economic performance and carbon emissions. The original academic calculations were reorganized into a reproducible Python based GitHub project with structured datasets and visual analysis.

The two renewable concepts investigated are:

**System 1**  
Photovoltaic generation with LiFePO4 battery storage

**System 2**  
Photovoltaic generation with biogas based backup generation

---

## Engineering Objective

The objective is to evaluate whether a greenhouse can meet its annual energy requirement using locally suitable renewable resources while improving environmental performance and maintaining economic feasibility.

The analysis follows five main questions:

1. How much energy does the greenhouse require throughout the year?
2. How much electricity can the photovoltaic system generate?
3. What battery capacity is required to shift solar energy outside sunshine hours?
4. How does a photovoltaic and biogas concept compare with battery storage?
5. How do the proposed systems compare in capital cost, operational emissions and energy autonomy?

---

## System Boundary

| Parameter | Reported Value |
| --- | ---: |
| Location | Sicily, Italy |
| Greenhouse area | 1,000 m² |
| Cultivation area | 700 m² |
| Greenhouse volume | 3,100 m³ |
| Maximum plant count | 7,000 plants |
| Annual rose production | 210,000 stems |
| Annual energy demand used in the monthly balance | 114,271.55 kWh |
| Installed PV capacity | 187 kW |
| Annual PV generation | 385,411.49 kWh |
| Selected battery capacity | 325 kWh |

---

## Energy System Architecture

```text
                     Solar Resource
                          |
                          v
                    PV Generation
                          |
              +-----------+-----------+
              |                       |
              v                       v
        Direct Consumption       Energy Storage
                                      |
                                      v
                              LiFePO4 Battery
                                      |
                                      v
                                  Inverter
                                      |
                                      v
                                  Greenhouse

Alternative concept

                    PV Generation
                          |
              +-----------+-----------+
              |                       |
              v                       v
        Direct Consumption      Biogas Generator
                                      |
                                      v
                                  Greenhouse
```

The greenhouse load includes heating, cooling, irrigation and supplemental lighting.

---

## Python Project Structure

```text
sustainable greenhouse energy system

data
    annual_energy_balance.csv
    battery_storage_and_export.csv
    monthly_energy_demand.csv
    monthly_pv_generation.csv
    system_comparison.csv

figures
    01_monthly_energy_demand.png
    02_pv_generation_vs_demand.png
    03_battery_storage_requirement.png
    04_monthly_grid_export.png
    05_operational_emissions_comparison.png
    06_capital_investment_comparison.png
    07_annual_energy_balance.png

src
    visualize.py

README.md
requirements.txt
```

---

# Results

## 1. Monthly Greenhouse Energy Demand

Heating dominates the winter period, while cooling becomes the major energy requirement during the warmer months. July and August show the highest monthly demand.

![Monthly Greenhouse Energy Demand](figures/01_monthly_energy_demand.png)

**Engineering interpretation**

The seasonal profile shows that greenhouse operation is strongly temperature dependent. Heating drives winter demand, while cooling creates the summer peak. Irrigation and lighting represent much smaller shares of the total annual energy balance.

---

## 2. Photovoltaic Generation Compared with Demand

The photovoltaic system was sized at approximately **187 kW installed capacity** and the reported annual generation is approximately **385 MWh**.

![PV Generation Compared with Demand](figures/02_pv_generation_vs_demand.png)

**Key result**

Annual photovoltaic generation is substantially higher than the greenhouse annual demand. This creates the possibility of energy storage and electricity export during periods of surplus production.

---

## 3. Battery Storage Requirement

The storage calculation evaluates how much energy must be shifted from sunshine hours to the remaining hours of the day.

![Battery Storage Requirement](figures/03_battery_storage_requirement.png)

The maximum calculated daily storage requirement occurs in February at approximately **321.58 kWh**. Based on this result, the project selected a **325 kWh LiFePO4 battery system**.

---

## 4. Grid Export Potential

Electricity remaining after greenhouse demand and storage requirements can be exported to the electricity grid.

![Monthly Grid Export](figures/04_monthly_grid_export.png)

The monthly profile shows substantial export potential, particularly during months with strong photovoltaic production.

---

## 5. Operational Carbon Emissions

![Operational Emissions Comparison](figures/05_operational_emissions_comparison.png)

| Energy Supply Concept | Operational CO₂ Emissions |
| --- | ---: |
| Conventional supply | 93.7 t per year |
| PV plus battery | 0 t per year |
| PV plus biogas | 18.54 t per year |

The photovoltaic and battery concept provides the lowest reported **operational** emissions.

**Important note**

Zero operational emissions do not mean zero lifecycle emissions. The original project also discusses emissions associated with manufacturing photovoltaic modules and LiFePO4 batteries. The chart above compares the reported operational stage only.

---

## 6. Capital Investment

![Capital Investment Comparison](figures/06_capital_investment_comparison.png)

| System | Gross Capital Investment | Reported Capital After Grant |
| --- | ---: | ---: |
| PV plus battery | €175,309 | €105,185.40 |
| PV plus biogas | €169,034 | €108,020.40 |

The project considered government support for renewable energy investment when evaluating the effective capital requirement.

---

## 7. Annual Energy Balance

![Annual Energy Balance](figures/07_annual_energy_balance.png)

The annual comparison highlights the relationship between photovoltaic generation, greenhouse demand and estimated electricity export.

---

# Technical Methodology

## Greenhouse Energy Demand

The thermal load was estimated using the basic heat transfer relationship

```text
Q = U × A × ΔT
```

where:

```text
Q   thermal load
U   overall heat transfer coefficient
A   greenhouse surface area
ΔT  indoor and outdoor temperature difference
```

Seasonal heating and cooling demand were combined with irrigation and supplemental lighting demand to obtain the annual energy requirement.

---

## Photovoltaic System

The photovoltaic system was evaluated using monthly solar irradiation and sunshine duration for Sicily.

Key design values from the project include:

| Parameter | Value |
| --- | ---: |
| Number of modules | 340 |
| Module arrangement | 34 modules per string |
| Parallel strings | 5 |
| Number of subarrays | 2 |
| Installed capacity | 187 kW |
| Module area used | 880.6 m² |

Monthly production was then compared with greenhouse demand.

---

## Battery Storage

The daily storage requirement was calculated from the difference between total daily demand and the energy consumed directly during sunshine hours.

```text
Daily demand = Monthly demand ÷ Number of days

Hourly demand = Daily demand ÷ 24

Direct PV use = Hourly demand × Sunshine hours

Storage requirement = Daily demand minus Direct PV use
```

The maximum result was used to select the battery capacity.

---

## Biogas Concept

The second renewable concept uses photovoltaic generation together with biogas based electricity production.

The reported maximum daily biogas energy requirement was approximately **325 kWh**.

The original calculation considered:

```text
Biogas energy content
CHP electrical efficiency
CHP thermal efficiency
Daily operating hours
Required biogas volume
Cow dung feedstock requirement
Digester volume
Gas holder volume
```

---

# Economic Assessment

The project compares capital expenditure, annual maintenance, operating cost, government support and income from exported photovoltaic electricity.

Reported annual electricity export income:

| System | Annual Export Income |
| --- | ---: |
| PV plus battery | €29,825.40 |
| PV plus biogas | €38,691.56 |

The original project reports a payback period of approximately **7 years for the PV plus battery concept**. A modified biogas concept using externally supplied biogas was reported with a payback period of approximately **8 years**.

---

# Key Engineering Findings

**Renewable generation potential**

The photovoltaic system produces significantly more annual electricity than the greenhouse annual demand in the reported model.

**Seasonal demand**

Heating dominates winter operation and cooling dominates the summer period.

**Storage sizing**

The maximum calculated storage requirement supports a battery capacity of approximately 325 kWh.

**Carbon performance**

The photovoltaic and battery system provides the lowest reported operational carbon emissions among the evaluated concepts.

**Economic performance**

Government support and electricity export improve the economic feasibility of both renewable concepts.

**System selection**

Based on the reported technical, environmental and economic assessment, the original project identified the photovoltaic and battery concept as the preferred solution.

---

# Reproduce the Visualizations

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Run the visualization script:

```bash
python src/visualize.py
```

The figures will be generated inside the `figures` directory.

---

# Tools and Skills Demonstrated

| Area | Application |
| --- | --- |
| Python | Data analysis and visualization |
| Pandas | Structured energy dataset processing |
| Matplotlib | Engineering plots |
| Energy modelling | Monthly supply and demand balance |
| Solar energy | PV generation assessment |
| Battery systems | Storage requirement calculation |
| Biogas | Renewable backup generation concept |
| Heat transfer | Greenhouse heating and cooling demand |
| Techno economic analysis | Capital cost, income and payback assessment |
| Sustainability analysis | Operational CO₂ comparison |

---

# Data Quality Note

The original academic report contains several energy demand totals that are not fully consistent across later sections.

To avoid combining incompatible values, this repository uses the **114,271.55 kWh annual demand derived from the detailed monthly energy balance** as the main reference for the Python visualizations.

This choice is documented intentionally so that the analysis remains transparent and reproducible.

---

# Academic Context

This work originated as a group project for the **Renewable Thermal Power Plants** course at **Friedrich Alexander University Erlangen Nürnberg**.

The GitHub version restructures the original engineering calculations into a clearer portfolio format with reproducible Python based visualizations.

---

# Author

## Nadeem Raza

Chemical Engineer  
M.Sc. Clean Energy Processes  
Friedrich Alexander University Erlangen-Nürnberg

Research interests include materials, hydrogen technologies, electrochemical systems, renewable energy and energy system modelling.

[LinkedIn](https://www.linkedin.com/in/nadeem-raza-255902208/)

