# Milestone 4: Dashboard Development — Coalition Builder (Weeks 5–6)

## 🎯 Objective

The objective of this milestone is to deliver an interactive coalition comparison interface within the Global Military Power dashboard. The Coalition Builder page allows analysts to dynamically assemble multi-nation coalitions and evaluate their combined strategic strength side-by-side — moving beyond single-country comparisons to simulate real-world alliance-level military assessments.

---

## 🛠️ Module 4: Coalition Builder Page

The Coalition Builder was developed as a dedicated Power BI report page, engineered to support multi-country aggregation, dynamic filtering, and dual-coalition comparison.

### Features Implemented

1. **Multi-Country Selector:** Two independent multi-select filter panels (Coalition 1 and Coalition 2) allow users to select any combination of countries from the full dataset. Selections are reflected instantly across all visuals on the page.
2. **Aggregated Coalition Metrics:** All KPIs are aggregated at the coalition level using DAX measures, summing or averaging values across all selected member nations.
3. **Side-by-Side Comparison:** Coalition 1 and Coalition 2 metrics are displayed in parallel card layouts, enabling direct head-to-head evaluation.
4. **Reset Control:** A dedicated Reset button clears both coalition selectors and returns the page to its default state.

---

## 📊 Metrics Displayed per Coalition

| Metric | Description |
|---|---|
| **Total Countries Selected** | Count of nations included in the coalition |
| **Military Assets** | Aggregated total of all hardware units across coalition members |
| **Defense Budget** | Combined annual defense expenditure (in billions USD) |
| **Manpower** | Total personnel count (Active, Air Force, Land, Navy, Reserve) |

The Manpower visual further breaks down coalition strength into five personnel categories — Active, Air Force, Land Force, Navy, and Reserve — rendered as a stacked bar chart for proportional comparison.

---

## 📐 DAX Measures Engineered

```dax
Coalition_Total_Assets =
    CALCULATE(
        SUM(military_final[Total_Assets]),
        ALLSELECTED(military_final[Country])
    )

Coalition_Defense_Budget =
    CALCULATE(
        SUM(military_final[Defense_Budget_USD_Bn]),
        ALLSELECTED(military_final[Country])
    )

Coalition_Manpower =
    CALCULATE(
        SUM(military_final[Active_Personnel]),
        ALLSELECTED(military_final[Country])
    )
```

Separate measure groups were created for Coalition 1 and Coalition 2 using bookmark-driven filter contexts to isolate each selection independently.

---

## 📂 Deliverables

| File | Description |
|---|---|
| `Coalition Builder.pbix` | Power BI report file containing the fully developed Coalition Builder page with all visuals, DAX measures, and filter logic. |
| `Dashboard_4.pdf` | Exported PDF snapshot of the Coalition Builder page for stakeholder review. |

---

## ✅ Evaluation Benchmarks

- **Filter Isolation:** Coalition 1 and Coalition 2 selectors operate fully independently without cross-contamination of filter context.
- **Aggregation Accuracy:** All coalition-level totals match manual cross-checks against the source dataset within a 0.1% margin.
- **Performance:** Page renders with full selections (7+ countries per coalition) in under 3 seconds.
- **Reset Functionality:** The Reset control correctly clears both selectors and restores default visual states.

---

## 🎯 Outcome

Successfully delivered the Coalition Builder page, enabling multi-nation coalition assembly and real-time aggregated military comparison. The page supports up to the full dataset of countries split across two coalitions, with live-updating KPI cards, manpower breakdowns, and a clean VS comparison layout.

**Status: Milestone 3 In Progress.** The Coalition Builder page is complete. Remaining dashboard pages (Quick Stats, Nation Overview, Compare Powers) are scheduled for finalisation in the second half of Week 6.
