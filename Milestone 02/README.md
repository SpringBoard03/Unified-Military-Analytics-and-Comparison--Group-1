## 🚀 Milestone 2 — KPI Engineering & Power BI Preparation

### 🎯 Objective
Enhance the cleaned military dataset by creating meaningful **Key Performance Indicators (KPIs)** to enable strategic analysis beyond raw statistics.  
The dataset was also enriched with **geographical and alliance metadata** to support advanced filtering and grouping in Power BI dashboards.

### ⚙️ KPI Feature Engineering
A Python workflow was developed to generate analytical metrics and improve dataset quality.

#### 🔧 Tasks Performed
- 🌍 Added metadata such as **Continent, Region, and alliance indicators (e.g., NATO membership)**  
- ✅ Validated manpower and equipment metrics to fix inconsistencies and handle missing values  
- 📊 Standardized **Global Firepower Power Index scores** for consistent analysis  

#### 📈 Calculated KPIs
- 🥇 **Power Index Rank Gap** → Difference between a country's rank and the top global rank  
- 👥 **Assets per Capita** → Military equipment availability relative to population/manpower  
- 💰 **Budget-to-GDP Ratio** → Share of national economic output spent on defense  

### 📊 Dataset Preparation for Power BI
- 📐 Structured in **wide format** where each KPI is stored as a separate column  
- ⚡ Optimized dataset to ensure **direct import into Power BI without additional transformation**

### 📦 Deliverables

| 📁 File | 📝 Description |
|--------|---------------|
| `KPI_Feature_Extraction.ipynb` | Notebook containing KPI engineering, validation, and preprocessing workflow |
| `military_final.csv` | Final analytics-ready dataset with original metrics and engineered KPIs |

### ✅ Evaluation Benchmarks
- 🎯 Correct computation of all major KPIs  
- 🧹 Less than **2% missing values** with no structural inconsistencies  
- 📊 Seamless loading and usability in Power BI  

### 🎯 Outcome
Produced an **analytics-ready military dataset enriched with strategic KPIs and geographical metadata**, fully prepared for building interactive dashboards in the next milestone.

**Status:** ✅ Milestone 2 Completed
