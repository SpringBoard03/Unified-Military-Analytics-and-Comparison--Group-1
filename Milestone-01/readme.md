
# 🌍 Global Military Power Data Pipeline

## 📌 Project Overview
This project builds a **structured dataset of global military statistics** by scraping data from the Global Firepower website.  
The workflow automates **data collection, cleaning, and aggregation**, converting raw web data into a **reliable dataset ready for analytics, dashboards, and research**.

---

## 🎯 Objective
- Scrape **global military capability metrics**
- Transform raw web data into a **structured dataset**
- Clean and standardize values for **analysis & visualization**

---

---

# 📁 Project Structure

```
project/
│
├── data/
│   ├── scraped_military_data.csv
│   └── military_cleaned_data.csv
│
├── notebooks/
│   └── Milestone_01_Military_scrap_cleaned_data.ipynb
│
└── README.md
```
---

## 🧰 Tools & Technologies

| Tool | Purpose |
|-----|------|
| 🐍 Python | Core programming language |
| 📊 Pandas | Data cleaning & manipulation |
| 🌐 Requests | HTTP requests for scraping |
| 🍲 BeautifulSoup | HTML parsing |
| 🧹 Regex | Data cleaning |
| 📓 Jupyter Notebook | Development environment |

---

# 🏗 Project Architecture

Global Firepower Website  
        ↓  
🕸️ Web Scraping (Requests + BeautifulSoup)  
        ↓  
📥 Raw Data Extraction  
        ↓  
📊 Data Aggregation (Pandas DataFrames)  
        ↓  
🧹 Data Cleaning & Formatting  
        ↓  
✅ Final Structured Dataset  

---

# ⚙️ Workflow

## 1️⃣ Data Scraping Setup
Imported Python libraries:

- `requests`
- `BeautifulSoup`
- `csv`
- `time`
- `re`

Used for:
- Sending **HTTP requests**
- Parsing **HTML content**
- Storing scraped data
- Managing scraping delays

---

## 2️⃣ Data Extraction
Military indicators collected include:

- 👨‍✈️ Manpower
- 💰 Defense Budget
- ✈️ Aircraft Strength
- 🚢 Naval Assets
- 🚜 Tanks
- 🎯 Artillery Systems

Each record represents **country-level military capability metrics**.

---

## 3️⃣ Raw Dataset Generation

Scraped data is stored as:

```
data/scraped_military_data.csv
```

Structure:
- **Rows → Countries**
- **Columns → Military Indicators**

---

## 4️⃣ Data Cleaning

Using **Pandas**, the dataset is cleaned by:

- Removing commas, currency symbols, and special characters
- Converting columns to numeric types
- Standardizing column names

---

## 5️⃣ Handling Missing Values

- Missing or invalid values are detected
- Replacement strategies ensure **dataset consistency**

---

```

Ready for:

- 📊 Data analysis
- 📈 Visualization dashboards
- 🌍 Geopolitical insights

---

# 📂 Generated Output Files

| File | Description |
|-----|------|
| `data/scraped_military_data.csv` | Raw dataset collected from scraping |
| `data/military_cleaned_data.csv` | Clean dataset ready for analysis |

---


# ✅ Conclusion

This project demonstrates a **scalable Python-based data pipeline** that collects global military capability metrics and transforms them into a **clean, structured dataset suitable for analytical and visualization workflows**.

