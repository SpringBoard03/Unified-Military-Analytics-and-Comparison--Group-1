# Milestone 2: KPI Engineering & Power BI Preparation (Weeks 3–4)

## 🎯 Objective
The purpose of this milestone is to extract deeper analytical insights from the cleaned military dataset. By generating Key Performance Indicators (KPIs), the analysis moves beyond simple absolute values to more meaningful comparative metrics—such as defense expenditure relative to national GDP. In addition, the dataset is enriched with geographical metadata, allowing advanced filtering, grouping, and segmentation when building interactive Power BI dashboards.

## 🛠️ Module 3: KPI Feature Engineering
A Python-based workflow was developed to create additional analytical indicators and enhance the dataset with relevant metadata.

### Tasks Performed
- **Metadata Enrichment:** Added geographical and alliance-related attributes including Continent, Region, and NATO Alliance Flag.
- **Data Validation:** Reviewed hardware-related metrics and resolved inconsistencies or missing values.
- **Power Index Formatting:** Standardized the official Power Index values for consistent analysis.

### Calculated KPIs
- **Power Index Rank Gap:** Calculates the difference between a country's rank and the leading country, highlighting the global competitive gap.
- **Assets per Capita:** Determines the availability of military equipment relative to the manpower or population of a country.
- **Budget-to-GDP Ratio:** Measures the proportion of defense spending compared to the total economic output (GDP).

## 📊 Data Formatting for Visualization
The dataset was organized to meet Power BI dashboard requirements:

- **Wide Data Format:** Each metric and KPI is stored as a separate column, enabling efficient filtering, aggregation, and analysis.
- **Standardized Structure:** Ensured the dataset can be directly imported into Power BI without requiring additional preprocessing.

## 📂 Deliverables

| File | Description |
| :--- | :--- |
| `Exploratory_Data_Analysis.ipynb` | Python notebook documenting the step-by-step workflow for validation, normalization, and KPI feature engineering. |
| `military_final.csv` | Final dataset containing 50+ indicators along with the newly created KPIs, ready for analytical use. |

## ✅ Evaluation Benchmarks
- **KPI Accuracy:** All major KPIs (Power Index Rank Gap, Assets per Capita, Budget-to-GDP Ratio) are calculated correctly.
- **Data Quality:** Final dataset contains less than 2% missing values and no structural inconsistencies.
- **Power BI Compatibility:** Dataset loads seamlessly into Power BI without requiring additional transformations.

## 🎯 Outcome
This milestone successfully introduced new analytical KPIs—Rank Gap, Assets per Capita, and Budget-to-GDP Ratio—while also enriching the dataset with geographical metadata. The result is a fully validated, analytics-ready dataset optimized for building interactive Power BI dashboards.

---

**Status:** Milestone 2 Completed. Dataset is ready for **Milestone 3: Full Dashboard Development.**
