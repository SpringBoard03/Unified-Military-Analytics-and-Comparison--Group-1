# Milestone 2: KPI Engineering & Power BI Prep (Weeks 3–4)

## 🎯 Objective
The objective of this milestone is to derive deeper analytical value from the cleaned military dataset. By calculating Key Performance Indicators (KPIs), we transition from absolute numbers to measuring proportional strategic strength—such as defense spending relative to national GDP. Additionally, we enrich the dataset with geographical metadata to enable the complex filtering and grouping required for interactive Power BI dashboards.

## 🛠️ Module 3: KPI Feature Engineering
A Python-based workflow was implemented to engineer additional analytical metrics and enrich the dataset with supporting metadata.

### **Tasks Performed:**
* **Metadata Enrichment:** Appended three new dimensions—**Continent**, **Region**, and **Alliance Flag (NATO)**—to support regional and coalition-based analysis.
* **Data Validation:** Ensured all hardware metrics (aircraft, tanks, naval assets) were numeric and handled missing values to prevent calculation errors.
* **Power Index Normalization:** Safely extracted and numericized the official Power Index scores to establish a baseline for ranking.

### **Calculated KPIs:**
* **Power Index Rank Gap:** Measures the difference between a country's rank and the top-ranked nation to highlight global positioning gaps.
* **Assets per Capita:** Calculates the density of military hardware relative to available manpower/population.
* **Budget-to-GDP Ratio:** Measures the intensity of defense spending relative to total economic output (GDP).

## 📊 Data Formatting for Visualization
The dataset was structured to support Power BI dashboard requirements:
* **Wide Format:** Each KPI and metric is stored as a column, making it suitable for statistical analysis and filtering.
* **Standardization:** Ensured the dataset loads directly into Power BI without requiring further transformation.

## 📂 Deliverables
| File | Description |
| :--- | :--- |
| `Milestone2.ipynb` | Python notebook containing the step-by-step cleaning, normalization process, and automated KPI feature engineering. |
| `military_final.csv` | The final analytics-ready dataset including all 50+ indicators and new KPIs. |

## ✅ Evaluation Benchmarks
* **KPI Accuracy:** All primary KPIs (Power Index Rank Gap, Assets per Capita, Budget-to-GDP) are correctly computed.
* **Data Health:** Final dataset contains < 2% missing data and zero structural errors.
* **Power BI Compatibility:** Data loads in Power BI without additional transformation.

---
**Status:** Milestone 2 Completed. The dataset is prepared for **Milestone 3: Full Dashboard Development**.