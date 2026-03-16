# Milestone 2: KPI Engineering & Power BI Preparation (Weeks 3–4)

## 🎯 Objective
The purpose of this milestone is to enhance the cleaned military dataset by deriving meaningful analytical insights through Key Performance Indicators (KPIs). Instead of analyzing only raw military statistics, this stage focuses on evaluating proportional strategic strength, such as defense spending relative to economic output.

In addition, the dataset is enriched with geographical and alliance-related metadata to support advanced filtering and grouping required for interactive Power BI dashboards.

## ⚙️ Module 3: KPI Feature Engineering
A Python-based workflow was implemented to generate additional analytical metrics and enrich the dataset with supporting metadata.

### **Tasks Performed:**
1. **Metadata Enrichment:** Added geographical attributes such as Continent, Region, and alliance indicators (e.g., NATO membership).
2. **Data Validation:** Reviewed equipment and manpower metrics to correct inconsistencies and handle missing values.
3. **Power Index Standardization:** Organized official Global Firepower Power Index scores into a consistent format for analysis.

### **Calculated KPIs:**
* **Power Index Rank Gap:** Indicates the difference between a country's ranking and the top-ranked nation to highlight global strategic gaps.
* **Assets per Capita:** Represents the availability of military equipment relative to population or manpower.
* **Budget-to-GDP Ratio:** Shows the proportion of national economic output allocated to defense spending.

## 📊 Data Formatting for Visualization
The dataset was structured to ensure smooth integration with Power BI dashboards:

* **Wide Format:** Each KPI and metric is stored as an individual column, allowing easier filtering, grouping, and analysis.
* **Standardized Dataset:** The dataset structure ensures it can be imported directly into Power BI without requiring additional transformations.

## 📂 Deliverables
| File | Description |
| :--- | :--- |
| `KPI_Feature_Extraction.ipynb` | Python notebook containing KPI calculations, data validation, and preprocessing steps. |
| `military_final.csv` | Final dataset including original indicators along with the newly generated KPIs. |

## ✅ Evaluation Benchmarks
* **KPI Accuracy:** All primary KPIs (Power Index Rank Gap, Assets per Capita, Budget-to-GDP Ratio) are correctly calculated.
* **Data Quality:** Final dataset contains less than 2% missing values and no structural inconsistencies.
* **Power BI Compatibility:** Dataset loads successfully in Power BI without additional preprocessing.

## 🎯 Outcome
Successfully generated an analytics-ready dataset enriched with strategic KPIs and geographical metadata. The processed dataset is fully prepared for building interactive visual dashboards in the next phase of the project.

---

**Status:** Milestone 2 Completed. The dataset is prepared for **Milestone 3: Dashboard Development**.