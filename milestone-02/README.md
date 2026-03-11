# 🚀 KPI Engineering & Power BI Preparation

## 🎯 Objective
Compute key performance indicators (KPIs) from the cleaned military dataset and prepare it for **interactive Power BI dashboards**.

## ⚙️ Approach
Using the cleaned dataset from Milestone 01, a **Python workflow** was implemented to:

- Create **derived KPI metrics** from military indicators  
- Enrich the dataset with **geographical and alliance metadata**  
- Prepare the structure for **Power BI visualization**  
- Export the dataset ready for **dashboard development**  

This ensures the dataset supports **comparative military analysis** and **interactive dashboards** without extra transformations.

## 📝 Steps Performed

### 1️⃣ Dataset Loading
- Loaded `military_updated.csv` using **Pandas**  
- Validated **columns, data types, row counts, and missing values**

### 2️⃣ KPI Feature Engineering
Computed key indicators for cross-country analysis:

- **Power Index Rank Gap** – Difference between expected rank & actual power index rank  
- **Assets per Capita** – Military assets relative to population  
- **Budget-to-GDP Ratio** – Defense spending intensity vs economic output  

### 3️⃣ Metadata Enrichment
Added supporting attributes for enhanced analysis:

- **Region & Continent**  
- **NATO alliance flag**   

### 4️⃣ Data Formatting for Power BI
Prepared two dataset formats:

- **Wide Format** – KPIs & metrics as columns for analysis & filtering  
- **Long Format** – Attribute-value pairs for flexible Power BI visualizations  

### 5️⃣ Final Dataset Export
- Exported the final structured dataset ready for **visualization and dashboards**  

## 📂 Generated Output Files

| File | Description |
|------|-------------|
| `military_updated.csv` | Final dataset with engineered KPIs and enriched metadata |
