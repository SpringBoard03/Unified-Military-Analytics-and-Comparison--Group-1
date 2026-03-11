Milestone 1: Data Collection and Preparation
Overview

In this milestone, the goal was to build the foundation for the military analytics project by collecting and preparing global military data. The data was scraped from multiple country pages using a list of URLs and then processed to create a structured dataset.

Since the raw scraped data contained formatting inconsistencies such as commas, symbols, and mixed data types, a cleaning process was applied to standardize the data and make it suitable for analysis and visualization in later milestones.

Objective

* Collect country-level military statistics from multiple sources.
* Convert unstructured web data into a structured dataset.
* Clean and standardize the dataset so it can be used for analytics and dashboard development.

Architecture

Country URLs
   │
   ▼
Web Scraping
(scrape_military_metrics.py)
   │
   ▼
Raw Dataset
(military_raw_data.csv)
   │
   ▼
Data Cleaning & Transformation
(clean_data.ipynb)
   │
   ▼
Final Dataset
(military_cleaned.csv)


Milestone 1 – Detailed Process Explanation
Part 1: Data Collection (Web Scraping)
Step 1: Access the Country Listing Page

The first step was to access the webpage that contains a list of all countries with their military strength profiles.

This page acts as a directory where each country has its own detailed military statistics page.
The script sends a request to this page and loads the HTML content so that the links can be extracted.

Purpose:

Identify all country profile pages
Use them as the source for scraping military metrics

Step 2: Extract Country Profile Links

From the listing page, all links that lead to individual country military strength pages were extracted.
Each of these links corresponds to a specific country and contains detailed military statistics such as:
aircraft count
tank inventory
defense budget
military personnel
naval assets
These links were then converted into complete URLs so they could be accessed individually.

Step 3: Remove Duplicate Links
After extracting the links, duplicates were removed.
This step ensures:
each country page is scraped only once
the scraping process remains efficient
the dataset does not contain duplicate rows
The links were also sorted to keep them organized.

Step 4: Scrape Data from Each Country Page
After preparing the list of country URLs, the script loops through each page.
For every country page:
The webpage is opened
The HTML content is parsed
Military metrics are located and extracted
The following types of information were collected:
country name
active personnel
reserve personnel
aircraft inventory
tank inventory
artillery systems
naval assets
defense budget
economic indicators
Each country's extracted data is temporarily stored before being added to the main dataset.

Step 5: Store the Raw Dataset
Once all country pages are processed, the collected information is organized into a structured table format.
The final raw dataset is saved as:

military_raw_data.csv

This dataset contains military statistics for 140+ countries, but it still includes formatting issues such as:
commas in numbers
currency symbols
combined values in certain columns
inconsistent formats
Because of this, a cleaning stage is required.

Part 2: Data Cleaning and Structuring

The second notebook focuses on transforming the raw dataset into a clean, analysis-ready dataset.

Step 1: Load the Raw Dataset

The raw CSV dataset generated from scraping is loaded into a data processing environment.

This allows the dataset to be inspected, cleaned, and transformed.

The goal is to convert the raw scraped values into consistent numeric fields suitable for analytics.

Step 2: Split Stock and Readiness Values

Some military equipment columns contained two values in a single field, such as:

total stock

ready-to-use units

Examples include:

tanks

self-propelled artillery

towed artillery

rocket artillery

These combined values were separated into two different columns:

stock (total available)

readiness (operational units)

This makes the dataset easier to analyze and compare between countries.

Step 3: Clean Financial Columns

Certain columns contained financial values such as:

GDP

defense budget

external debt

These values included symbols like:

dollar signs

commas

text formatting

The cleaning process removed these symbols so the values could be converted into numeric format.

This enables calculations and comparisons between countries.

Step 4: Clean Numeric Columns

Many military metrics contained formatting characters like commas.

For example:

1,200
35,000

These formatting characters were removed so that the values could be converted into proper numeric data types.

This ensures that the dataset can be used for statistical analysis.

Step 5: Handle Missing Values

Some countries had missing or incomplete data.

These cases were handled carefully to ensure:

the dataset structure remains consistent

missing values do not break analysis or visualization tools

Step 6: Save the Clean Dataset

After completing all cleaning and restructuring steps, the final dataset was exported.

Final file:
military_cleaned.csv

This dataset is now:
structured
numeric
standardized
ready for analysis and visualization

Tech Stack

* Python
* Requests & BeautifulSoup – web scraping
* Pandas – data cleaning and transformation
* Jupyter Notebook – preprocessing
* CSV – dataset storage

Output

* military_raw_data.csv – raw scraped dataset
* military_cleaned.csv – cleaned and structured dataset ready for analysis



