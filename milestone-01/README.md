# Milestone 01 – Data Collection and Preparation

## Project Overview

This milestone focuses on collecting and preparing global military strength data for further analysis. The data is gathered from an online source and then cleaned and structured so it can be used for analysis, dashboards, and comparisons between countries.

The goal is to transform raw web data into a clean dataset that can support future insights about global military capabilities.

---

# Milestone 01 Architecture

The following architecture shows how data flows in this milestone.

```
Website (Global Firepower)
        │
        ▼
Web Scraping Script
(Python + Requests + BeautifulSoup)
        │
        ▼
Raw Dataset Generated
(raw_military_data.csv)
        │
        ▼
Data Cleaning & Standardization
(Pandas Processing)
        │
        ▼
Final Clean Dataset
(military_cleaned_data.csv)
```

This pipeline ensures that raw website data is converted into a structured dataset that can be easily analyzed.

---

# Objective

The main objectives of this milestone are:

• Collect military strength data for multiple countries

• Store the collected information in a structured dataset

• Clean and standardize the data

• Prepare the dataset for future analysis and visualization

---

# Data Source

The data is collected from the **Global Firepower Military Strength Database**, which provides information about military resources and capabilities of countries worldwide.

---

# Raw Data Collection

A Python script was created to automatically collect raw data from the website.

The script performs the following tasks:

1. Access each country’s military information page
2. Extract key indicators
3. Store the collected information in a CSV dataset

This process allows large amounts of data to be collected efficiently.

---

# Data Cleaning

After collecting the data, several cleaning steps were applied to improve data quality:

• Removed unnecessary symbols and formatting

• Converted values into numeric format

• Standardized column names

• Handled missing values

These steps ensure the dataset is ready for analysis.

---

# Dataset Files

Two datasets are generated during this milestone.

### Raw Dataset

```
data/military_raw_data.csv
```

This file contains the original scraped data.

### Clean Dataset

```
data/military_cleaned_data.csv
```

This file contains the processed and standardized data ready for analysis.

---

# Outcome

At the end of this milestone:

• Military data for many countries has been collected

• The data has been cleaned and standardized

• A structured dataset has been prepared for further analysis
