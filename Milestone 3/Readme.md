# Milestone 3: Dashboard Development — Compare Powers

## 🎯 Objective

The objective of this milestone is to deliver an interactive head-to-head comparison interface within the Global Military Power dashboard. The Compare Powers page empowers analysts to dynamically select and evaluate the military strengths of different nations side-by-side, offering deep insights into individual national capabilities, rankings, and strategic imbalances.

---

## 🛠️ Module 3: Compare Powers Page Features

Building on the KPIs engineered in Milestone 2, this visualization acts as a focused comparative analytical tool.

### Features Implemented

1. **Dual Country Selectors:** Interactive slicers allowing users to select two distinct nations (e.g., USA vs. China) for direct head-to-head evaluation.
2. **Side-by-Side Visualizations:** Metric cards are split into two complementary columns, directly comparing individual statistics like Manpower, Defense Budget, and Total Assets.
3. **Asset Distribution Charts:** Visual distribution of land, air, and naval assets allowing for quick identification of each country's specialization (e.g., a superior navy vs. superior artillery).
4. **Global Rank Context:** Quick callouts to highlight the absolute power index ranking and show proportional gaps in global standing.

---

## 📊 Core Metrics Analyzed

| Metric Category | Indicators Displayed |
|---|---|
| **Economics** | Defense Budget (in billions USD), Budget-to-GDP Ratio |
| **Manpower** | Active Military Personnel, Reserve Personnel, Paramilitary Forces |
| **Air Power** | Total Aircraft, Fighter/Interceptor Jets, Attack Helicopters |
| **Land Forces** | Combat Tanks, Armored Vehicles, Artillery |
| **Naval Power** | Fleet Strength, Aircraft Carriers, Submarines, Patrol Vessels |

---

## 📂 Deliverables

| File | Description |
| :--- | :--- |
| `Compare Powers.pbix` | Power BI report file containing the interactive Compare Powers dashboard, full visual relationships, and filter logic. |
| `Compare Powers.pdf` | Exported PDF snapshot of the Compare Powers dashboard state for stakeholder review and presentations. |

---

## ✅ Evaluation Benchmarks

- **Cross-Filtering Accuracy:** Making selections on one filter immediately updates all associated KPI cards and charts accurately without bleeding context.
- **Metric Formatting:** Financial numbers are correctly formatted representing Billions, and large manpower figures are abbreviated for visual clarity.
- **Data Integrity:** Visualized values perfectly match the source `military_final.csv` generated at the end of Milestone 2.

---

## 🎯 Outcome

Successfully delivered the Compare Powers dashboard page. Analysts can now intuitively extract side-by-side military statistics, vastly simplifying the manual process of comparing different countries' strategic strength across an array of categories.

**Status: Milestone 3 Completed.** The Compare Powers page is fully functional. The groundwork is laid for aggregate alliance assessments in **Milestone 4 (Coalition Builder)**.
