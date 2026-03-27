# MILESTONE 2 README.md

**Path:** `Unified-Military-Analytics/Milestone_2/README.md`

```markdown
# Milestone 02: KPI Engineering & Feature Creation

## Objective

Transform raw military metrics into strategic intelligence by computing derived Key Performance Indicators and enriching the dataset with geographic and alliance metadata.

---

## Metadata Enrichment

### Geographic Classification
- **Continents**: 7 major continents mapped
- **Regions**: 15 sub-regions based on UN geographic classification
- **Implementation**: Rule-based mapping using country name patterns

### Alliance Flags
- **NATO**: 32 member countries identified
- **Non-Aligned**: All remaining countries classified accordingly

---

## Key Performance Indicators

| KPI | Formula | Strategic Value |
|-----|---------|-----------------|
| **Total Military Hardware** | Aircraft + Tanks + Naval Assets | Aggregate equipment volume |
| **Assets per Capita** | Total Hardware ÷ Total Manpower | Technology intensity measure |
| **Budget-to-GDP Ratio** | Defense Budget ÷ GDP | National defense priority |
| **Power Index Rank** | Rank(Power Index, ascending) | Relative military positioning |
| **Power Index Rank Gap** | Rank − 1 | Distance from top-ranked nation |

---

## Output Files

| File | Description | Dimensions |
|------|-------------|------------|
| `data/military_final.csv` | Enriched dataset with KPIs and metadata | 145 × 42 |

---

## Sample KPI Results

| Country | Power Rank | Assets per Capita | Budget-to-GDP Ratio |
|---------|------------|-------------------|---------------------|
| United States | 1 | 0.000090 | 0.032384 |
| Russia | 2 | 0.000072 | 0.034922 |
| China | 3 | 0.000006 | 0.009018 |
| India | 4 | 0.000004 | 0.007652 |

---

## Alliance Analysis

| Alliance | Countries | Defense Budget | Manpower |
|----------|-----------|----------------|----------|
| NATO | 32 | $1.50 Trillion | 447 Million |
| Non-Aligned | 113 | $1.36 Trillion | 3.30 Billion |

---

## Geographic Distribution

| Continent | Countries | Defense Budget | Manpower |
|-----------|-----------|----------------|----------|
| Asia | 41 | $853 Billion | 2.32 Billion |
| Europe | 38 | $843 Billion | 339 Million |
| Africa | 35 | $110 Billion | 562 Million |
| North America | 10 | $895 Billion | 260 Million |
| South America | 11 | $64 Billion | 217 Million |

---

## Validation Summary

| Check | Status |
|-------|--------|
| Power Index Numeric Conversion | ✅ Pass |
| NATO Flag Accuracy | ✅ Pass (32/32) |
| Geographic Mapping | ✅ Pass |
| KPI Calculation Integrity | ✅ Pass |

---

## Execution

```bash
# Ensure military_clean_data.csv is in data/ directory
jupyter notebook KPI_Engineering_and_Feature_Creation.ipynb