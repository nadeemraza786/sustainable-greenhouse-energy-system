from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
FIG = ROOT / "figures"
FIG.mkdir(exist_ok=True)

energy = pd.read_csv(DATA / "monthly_energy_demand.csv")
pv = pd.read_csv(DATA / "monthly_pv_generation.csv")
storage = pd.read_csv(DATA / "battery_storage_and_export.csv")
systems = pd.read_csv(DATA / "system_comparison.csv")
months = energy["Month"].tolist()

# Monthly energy demand
fig, ax = plt.subplots(figsize=(12, 6))
bottom = np.zeros(len(energy))
for col, label in [
    ("Heating_kWh","Heating"),
    ("Cooling_kWh","Cooling"),
    ("Irrigation_kWh","Irrigation"),
    ("Lighting_kWh","Lighting"),
]:
    ax.bar(months, energy[col], bottom=bottom, label=label)
    bottom += energy[col].to_numpy()
ax.set_title("Monthly Greenhouse Energy Demand")
ax.set_ylabel("Energy demand (kWh)")
ax.set_xlabel("Month")
ax.tick_params(axis="x", rotation=45)
ax.legend(frameon=False, ncol=4)
ax.grid(axis="y", alpha=0.25)
fig.tight_layout()
fig.savefig(FIG / "01_monthly_energy_demand.png", dpi=220, bbox_inches="tight")
plt.close(fig)

# PV generation versus demand
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(months, pv["PV_Produced_kWh"], marker="o", linewidth=2, label="PV generation")
ax.plot(months, energy["Total_kWh"], marker="o", linewidth=2, label="Greenhouse demand")
ax.fill_between(range(len(months)), energy["Total_kWh"], pv["PV_Produced_kWh"], alpha=0.12)
ax.set_title("Monthly PV Generation Compared with Greenhouse Demand")
ax.set_ylabel("Energy (kWh)")
ax.set_xlabel("Month")
ax.set_xticks(range(len(months)))
ax.set_xticklabels(months, rotation=45)
ax.legend(frameon=False)
ax.grid(alpha=0.25)
fig.tight_layout()
fig.savefig(FIG / "02_pv_generation_vs_demand.png", dpi=220, bbox_inches="tight")
plt.close(fig)

# Battery requirement
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(months, storage["Energy_Stored_per_Day_kWh"], marker="o", linewidth=2,
        label="Daily storage requirement")
ax.axhline(325, linestyle=":", linewidth=2, label="Selected battery capacity: 325 kWh")
ax.set_title("Battery Storage Requirement Across the Year")
ax.set_ylabel("Energy (kWh per day)")
ax.set_xlabel("Month")
ax.set_xticks(range(len(months)))
ax.set_xticklabels(months, rotation=45)
ax.legend(frameon=False)
ax.grid(alpha=0.25)
fig.tight_layout()
fig.savefig(FIG / "03_battery_storage_requirement.png", dpi=220, bbox_inches="tight")
plt.close(fig)

# Grid export
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(months, storage["Monthly_Grid_Export_kWh"])
ax.set_title("Estimated Monthly Electricity Export to the Grid")
ax.set_ylabel("Exported electricity (kWh)")
ax.set_xlabel("Month")
ax.tick_params(axis="x", rotation=45)
ax.grid(axis="y", alpha=0.25)
fig.tight_layout()
fig.savefig(FIG / "04_monthly_grid_export.png", dpi=220, bbox_inches="tight")
plt.close(fig)

# Operational emissions
fig, ax = plt.subplots(figsize=(9, 6))
ax.bar(systems["System"], systems["Operational_CO2_t_per_year"])
ax.set_title("Operational CO₂ Emissions Comparison")
ax.set_ylabel("CO₂ emissions (t per year)")
ax.tick_params(axis="x", rotation=15)
ax.grid(axis="y", alpha=0.25)
fig.tight_layout()
fig.savefig(FIG / "05_operational_emissions_comparison.png", dpi=220, bbox_inches="tight")
plt.close(fig)

# Investment comparison
econ = systems.dropna(subset=["Capital_Investment_EUR"])
fig, ax = plt.subplots(figsize=(9, 6))
x = np.arange(len(econ))
w = 0.36
ax.bar(x - w/2, econ["Capital_Investment_EUR"], width=w, label="Gross capital")
ax.bar(x + w/2, econ["Net_Capital_After_Grant_EUR"], width=w, label="After reported grant")
ax.set_title("Capital Investment of Proposed Energy Systems")
ax.set_ylabel("Investment (€)")
ax.set_xticks(x)
ax.set_xticklabels(econ["System"])
ax.legend(frameon=False)
ax.grid(axis="y", alpha=0.25)
fig.tight_layout()
fig.savefig(FIG / "06_capital_investment_comparison.png", dpi=220, bbox_inches="tight")
plt.close(fig)

# Annual balance
annual = pd.DataFrame({
    "Metric": ["Annual PV generation","Annual greenhouse demand","Estimated grid export"],
    "Energy_kWh": [
        pv["PV_Produced_kWh"].sum(),
        energy["Total_kWh"].sum(),
        storage["Monthly_Grid_Export_kWh"].sum()
    ]
})
fig, ax = plt.subplots(figsize=(9, 6))
ax.bar(annual["Metric"], annual["Energy_kWh"])
ax.set_title("Annual Energy Balance")
ax.set_ylabel("Energy (kWh per year)")
ax.tick_params(axis="x", rotation=12)
ax.grid(axis="y", alpha=0.25)
fig.tight_layout()
fig.savefig(FIG / "07_annual_energy_balance.png", dpi=220, bbox_inches="tight")
plt.close(fig)

print("Figures regenerated in:", FIG)
