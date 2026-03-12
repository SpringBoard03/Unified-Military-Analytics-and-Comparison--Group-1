# Milestone 1: Data Acquisition & Preparation (Weeks 1–2)

## 📌 Objective
The goal of this milestone was to gather worldwide military capability data from the Global Firepower (GFP) Index and convert the raw web information into a well-organized dataset that can be used for advanced analysis and dashboard creation.

## 🛠️ Module 1: Web Scraping Setup and Implementation
A Python-based pipeline was developed to automatically collect military statistics for more than 140 countries.

### Tasks Performed
1. **Automated URL Processing:** Generated and accessed pages corresponding to 140+ countries.
2. **Information Extraction:** Retrieved key military indicators such as manpower statistics, defense budgets, and equipment inventories.
3. **Structured Parsing:** Converted HTML page elements into structured key–value data formats.
4. **Data Export:** Stored the collected information into a raw CSV dataset for further processing.

### Technical Stack
- **Python Libraries:** `requests`, `BeautifulSoup4`, `pandas`, `re`, and `time`
- **Workflow:** Implemented controlled request intervals (approximately 1 second) to ensure stable scraping and reduce the risk of server rate-limiting.

## 📊 Data Cleaning & Standardization
After collecting the raw dataset, several preprocessing steps were carried out to prepare the data for analysis:

1. **Character Cleaning:** Removed commas, currency symbols (such as "$"), and measurement units (for example "ft") from numeric values.
2. **Data Type Conversion:** Transformed textual numeric values into appropriate integer or float formats.
3. **Handling Missing Data:** Detected and managed null or missing entries to maintain dataset consistency.
4. **Column Normalization:** Renamed fields into standardized, machine-friendly column names.

## 📂 Deliverables
| File | Description |
| :--- | :--- |
| `Data_Scraping_and_Cleaning.ipynb` | Jupyter notebook containing the full scraping and preprocessing workflow. |
| `military_raw_data.csv` | Raw dataset containing the initially scraped information. |
| `military_cleaned_ready.csv` | Processed dataset prepared for further analysis in the next milestone. |

## ✅ Evaluation Criteria
- **URL Retrieval Rate:** At least 95% successful access to the target country pages.
- **Data Coverage:** Correct extraction of metric sections for over 140 countries.
- **Data Quality:** Effective removal of special characters and successful conversion to numeric formats.

## 🎯 Outcome
At the end of this milestone, a clean and structured dataset covering military strength indicators for more than 140 countries was successfully created. This dataset forms the foundation for KPI development and the Power BI analytics dashboard that will be implemented in the following stages of the project.

---

**Status:** Milestone 1 Completed – Data successfully collected, cleaned, and prepared for further analysis.
