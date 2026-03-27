
# MILESTONE 1 README.md

**File path:** `milestone_01_data_collection/README.md`

```markdown
# Milestone 01: Data Collection & Preparation

## Objective

Establish a robust ETL pipeline that extracts raw military intelligence from GlobalFirepower.com and transforms it into a high-quality, analysis-ready dataset.

## Data Pipeline

### Phase 1: Acquisition
- **Source**: GlobalFirepower.com
- **Method**: Automated web scraping using BeautifulSoup and Requests
- **Coverage**: 145 countries with 34 distinct military and economic metrics
- **Rate Limiting**: 1-second delay between requests to prevent IP blocking

### Phase 2: Cleaning
- Symbol Removal: Stripped `$`, `,`, `%`, `+` characters
- Unit Stripping: Removed units (bbl, mt, km, sq km)
- Numeric Conversion: Converted all metrics to appropriate numeric types
- Null Handling: Filled missing values with 0 (appropriate for count-based metrics)

### Phase 3: Standardization
- Column naming converted to snake_case for consistency
- Data types verified and validated

## Output Specifications

| File | Description | Dimensions |
|------|-------------|------------|
| `military_raw_data.csv` | Unprocessed scraped data | 145 rows × 34 columns |
| `military_cleaned.csv` | Processed numeric dataset | 145 rows × 34 columns |

## Sample Data (Top 5 Military Powers)

| Rank | Country | Power Index | Defense Budget | Total Aircraft | Tanks |
|------|---------|-------------|----------------|----------------|-------|
| 1 | United States | 0.0741 | $831.5B | 13,032 | 4,666 |
| 2 | Russia | 0.0791 | $212.6B | 4,237 | 5,630 |
| 3 | China | 0.0919 | $303.0B | 3,529 | 5,870 |
| 4 | India | 0.1346 | $109.0B | 2,183 | 3,913 |
| 5 | South Korea | 0.1642 | $44.8B | 1,540 | 1,831 |

## Validation Results

| Validation Check | Status | Result |
|------------------|--------|--------|
| Row Count | ✅ Pass | 145 countries (≥ 140) |
| Data Types | ✅ Pass | All metrics numeric |
| Null Values | ✅ Pass | 0% missing after processing |
| Range Integrity | ✅ Pass | All values within expected ranges |

## Execution

```bash
jupyter notebook Milestone_01_Data_Preprocessing.ipynb