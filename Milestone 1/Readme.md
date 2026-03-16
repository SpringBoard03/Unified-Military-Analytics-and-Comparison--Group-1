Milestone 1 — Data Collection and Preparation
🎯 Objective

The aim of this milestone is to gather global military data and convert it into a structured dataset that can be used for further analysis and dashboard creation.
Data is collected from publicly available military statistics sources and processed using Python.

🔎 Data Collection

A Python-based scraping workflow was used to collect military metrics for multiple countries.

Tasks Performed

Retrieved military statistics from source web pages

Extracted key indicators such as manpower, aircraft, tanks, and defense budget

Parsed webpage content into structured data format

Stored the extracted data into a CSV dataset

Tools Used

Python

requests

BeautifulSoup

pandas

🧹 Data Cleaning and Preparation

After collecting the raw data, preprocessing steps were applied to make the dataset suitable for analysis.

Cleaning Steps

Removed commas, percentage symbols, and currency characters

Converted text values into numeric format

Standardized column names

Checked and handled missing values

This ensured the dataset is consistent and ready for further processing.

📊 Outputs
File	Description
data/military_raw_data.csv	Raw dataset collected from web sources
data/military_cleaned.csv	Cleaned dataset ready for analysis
Data_Collection_and_Preparation.ipynb	Notebook containing scraping and cleaning process

✔ Validation Metrics

URL Retrieval Rate: At least 95% of country pages successfully processed

Data Coverage: Military metrics captured for 140+ countries

Data Consistency: All numeric indicators standardized and free from formatting characters.

✅ Outcome

Military data successfully collected for multiple countries

Raw data cleaned and standardized

Final dataset prepared for KPI engineering and dashboard development in the next milestone
