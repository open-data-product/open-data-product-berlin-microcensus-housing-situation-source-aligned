
# Data Product Canvas - Berlin Microcensus Housing Situation (source-aligned)

## Metadata

* owner: Open Data Product
* description: Source-aligned data product providing Berlin microcensus housing situation data
* updated: 2025-10-27

## Input Ports

### Ergebnisse des Mikrozensus 2014

* owner: Amt für Statistik Berlin-Brandenburg
* url: https://www.statistik-berlin-brandenburg.de/f-i-2-4j
* license: CC-BY-3.0-Namensnennung
* updated: 2017-04-03

**Files**

* [SB_F01-02-00_2014j04_BE.xlsx](https://download.statistik-berlin-brandenburg.de/7999ac608d606bf5/ececea9b1498/SB_F01-02-00_2014j04_BE.xlsx)

### Ergebnisse des Mikrozensus 2018

* owner: Amt für Statistik Berlin-Brandenburg
* url: https://www.statistik-berlin-brandenburg.de/f-i-2-4j
* license: CC-BY-3.0-Namensnennung
* updated: 2019-12-18

**Files**

* [SB_F01-02-00_2018j04_BE.xlsx](https://download.statistik-berlin-brandenburg.de/dbad6022b4074bc2/a5d78de25950/SB_F01-02-00_2018j04_BE.xlsx)

### Ergebnisse des Mikrozensus 2022

* owner: Amt für Statistik Berlin-Brandenburg
* url: https://www.statistik-berlin-brandenburg.de/f-i-2-4j
* license: CC-BY-3.0-Namensnennung
* updated: 2024-07-16

**Files**

* [SB_F01-02-00_2022j04_BE.xlsx](https://download.statistik-berlin-brandenburg.de/167555afd12b0012/354695ab2b73/SB_F01-02-00_2022j04_BE.xlsx)

## Transformation Steps

* [Data extractor](https://github.com/open-data-product/open-data-product-python-lib/blob/main/opendataproduct/extract/data_extractor.py) extracts data from inout ports
* [Data copier](https://github.com/open-data-product/open-data-product-python-lib/blob/main/opendataproduct/transform/data_copier.py) copies and renames extracted data
* [Data CSV converter](https://github.com/open-data-product/open-data-product-python-lib/blob/main/opendataproduct/transform/data_csv_converter.py) converts Excel files to CSV format
* [Data aggregator](https://github.com/open-data-product/open-data-product-python-lib/blob/main/opendataproduct/transform/data_aggregator.py) aggregates data to be used as output ports

## Output Ports

### Berlin Microcensus Housing Situation 2014 00 Csv

* owner: Open Data Product
* url: https://github.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/tree/main/data/03-gold/berlin-microcensus-housing-situation-2014-00-csv
* updated: 2025-10-27

**Files**

* [berlin-microcensus-housing-situation-2014-00-19-apartments-by-occupancy-and-living-area-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2014-00-csv/berlin-microcensus-housing-situation-2014-00-19-apartments-by-occupancy-and-living-area-city.csv)
* [berlin-microcensus-housing-situation-2014-00-19-apartments-by-occupancy-and-living-area-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2014-00-csv/berlin-microcensus-housing-situation-2014-00-19-apartments-by-occupancy-and-living-area-districts.csv)
* [berlin-microcensus-housing-situation-2014-00-22-apartments-by-living-area-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2014-00-csv/berlin-microcensus-housing-situation-2014-00-22-apartments-by-living-area-city.csv)
* [berlin-microcensus-housing-situation-2014-00-22-apartments-by-living-area-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2014-00-csv/berlin-microcensus-housing-situation-2014-00-22-apartments-by-living-area-districts.csv)
* [berlin-microcensus-housing-situation-2014-00-23-apartments-by-gross-rent-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2014-00-csv/berlin-microcensus-housing-situation-2014-00-23-apartments-by-gross-rent-city.csv)
* [berlin-microcensus-housing-situation-2014-00-23-apartments-by-gross-rent-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2014-00-csv/berlin-microcensus-housing-situation-2014-00-23-apartments-by-gross-rent-districts.csv)
* [berlin-microcensus-housing-situation-2014-00-24-apartments-by-gross-rent-per-sqm-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2014-00-csv/berlin-microcensus-housing-situation-2014-00-24-apartments-by-gross-rent-per-sqm-city.csv)
* [berlin-microcensus-housing-situation-2014-00-24-apartments-by-gross-rent-per-sqm-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2014-00-csv/berlin-microcensus-housing-situation-2014-00-24-apartments-by-gross-rent-per-sqm-districts.csv)
* [berlin-microcensus-housing-situation-2014-00-25-households-by-percentage-of-household-net-income-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2014-00-csv/berlin-microcensus-housing-situation-2014-00-25-households-by-percentage-of-household-net-income-city.csv)
* [berlin-microcensus-housing-situation-2014-00-25-households-by-percentage-of-household-net-income-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2014-00-csv/berlin-microcensus-housing-situation-2014-00-25-households-by-percentage-of-household-net-income-districts.csv)

### Berlin Microcensus Housing Situation 2014 00 Parquet

* owner: Open Data Product
* url: https://github.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/tree/main/data/03-gold/berlin-microcensus-housing-situation-2014-00-parquet
* updated: 2025-10-27

**Files**

* [berlin-microcensus-housing-situation-2014-00-19-apartments-by-occupancy-and-living-area-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2014-00-parquet/berlin-microcensus-housing-situation-2014-00-19-apartments-by-occupancy-and-living-area-city.parquet)
* [berlin-microcensus-housing-situation-2014-00-19-apartments-by-occupancy-and-living-area-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2014-00-parquet/berlin-microcensus-housing-situation-2014-00-19-apartments-by-occupancy-and-living-area-districts.parquet)
* [berlin-microcensus-housing-situation-2014-00-22-apartments-by-living-area-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2014-00-parquet/berlin-microcensus-housing-situation-2014-00-22-apartments-by-living-area-city.parquet)
* [berlin-microcensus-housing-situation-2014-00-22-apartments-by-living-area-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2014-00-parquet/berlin-microcensus-housing-situation-2014-00-22-apartments-by-living-area-districts.parquet)
* [berlin-microcensus-housing-situation-2014-00-23-apartments-by-gross-rent-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2014-00-parquet/berlin-microcensus-housing-situation-2014-00-23-apartments-by-gross-rent-city.parquet)
* [berlin-microcensus-housing-situation-2014-00-23-apartments-by-gross-rent-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2014-00-parquet/berlin-microcensus-housing-situation-2014-00-23-apartments-by-gross-rent-districts.parquet)
* [berlin-microcensus-housing-situation-2014-00-24-apartments-by-gross-rent-per-sqm-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2014-00-parquet/berlin-microcensus-housing-situation-2014-00-24-apartments-by-gross-rent-per-sqm-city.parquet)
* [berlin-microcensus-housing-situation-2014-00-24-apartments-by-gross-rent-per-sqm-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2014-00-parquet/berlin-microcensus-housing-situation-2014-00-24-apartments-by-gross-rent-per-sqm-districts.parquet)
* [berlin-microcensus-housing-situation-2014-00-25-households-by-percentage-of-household-net-income-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2014-00-parquet/berlin-microcensus-housing-situation-2014-00-25-households-by-percentage-of-household-net-income-city.parquet)
* [berlin-microcensus-housing-situation-2014-00-25-households-by-percentage-of-household-net-income-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2014-00-parquet/berlin-microcensus-housing-situation-2014-00-25-households-by-percentage-of-household-net-income-districts.parquet)

### Berlin Microcensus Housing Situation 2018 00 Csv

* owner: Open Data Product
* url: https://github.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/tree/main/data/03-gold/berlin-microcensus-housing-situation-2018-00-csv
* updated: 2025-10-27

**Files**

* [berlin-microcensus-housing-situation-2018-00-23-apartments-by-occupancy-and-living-area-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2018-00-csv/berlin-microcensus-housing-situation-2018-00-23-apartments-by-occupancy-and-living-area-city.csv)
* [berlin-microcensus-housing-situation-2018-00-23-apartments-by-occupancy-and-living-area-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2018-00-csv/berlin-microcensus-housing-situation-2018-00-23-apartments-by-occupancy-and-living-area-districts.csv)
* [berlin-microcensus-housing-situation-2018-00-26-apartments-by-building-type-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2018-00-csv/berlin-microcensus-housing-situation-2018-00-26-apartments-by-building-type-city.csv)
* [berlin-microcensus-housing-situation-2018-00-26-apartments-by-building-type-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2018-00-csv/berlin-microcensus-housing-situation-2018-00-26-apartments-by-building-type-districts.csv)
* [berlin-microcensus-housing-situation-2018-00-27-apartments-by-owner-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2018-00-csv/berlin-microcensus-housing-situation-2018-00-27-apartments-by-owner-city.csv)
* [berlin-microcensus-housing-situation-2018-00-27-apartments-by-owner-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2018-00-csv/berlin-microcensus-housing-situation-2018-00-27-apartments-by-owner-districts.csv)
* [berlin-microcensus-housing-situation-2018-00-28-apartments-by-living-area-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2018-00-csv/berlin-microcensus-housing-situation-2018-00-28-apartments-by-living-area-city.csv)
* [berlin-microcensus-housing-situation-2018-00-28-apartments-by-living-area-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2018-00-csv/berlin-microcensus-housing-situation-2018-00-28-apartments-by-living-area-districts.csv)
* [berlin-microcensus-housing-situation-2018-00-29-apartments-by-gross-rent-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2018-00-csv/berlin-microcensus-housing-situation-2018-00-29-apartments-by-gross-rent-city.csv)
* [berlin-microcensus-housing-situation-2018-00-29-apartments-by-gross-rent-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2018-00-csv/berlin-microcensus-housing-situation-2018-00-29-apartments-by-gross-rent-districts.csv)
* [berlin-microcensus-housing-situation-2018-00-30-apartments-by-gross-rent-per-sqm-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2018-00-csv/berlin-microcensus-housing-situation-2018-00-30-apartments-by-gross-rent-per-sqm-city.csv)
* [berlin-microcensus-housing-situation-2018-00-30-apartments-by-gross-rent-per-sqm-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2018-00-csv/berlin-microcensus-housing-situation-2018-00-30-apartments-by-gross-rent-per-sqm-districts.csv)
* [berlin-microcensus-housing-situation-2018-00-31-households-by-percentage-of-household-net-income-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2018-00-csv/berlin-microcensus-housing-situation-2018-00-31-households-by-percentage-of-household-net-income-city.csv)
* [berlin-microcensus-housing-situation-2018-00-31-households-by-percentage-of-household-net-income-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2018-00-csv/berlin-microcensus-housing-situation-2018-00-31-households-by-percentage-of-household-net-income-districts.csv)

### Berlin Microcensus Housing Situation 2018 00 Parquet

* owner: Open Data Product
* url: https://github.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/tree/main/data/03-gold/berlin-microcensus-housing-situation-2018-00-parquet
* updated: 2025-10-27

**Files**

* [berlin-microcensus-housing-situation-2018-00-23-apartments-by-occupancy-and-living-area-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2018-00-parquet/berlin-microcensus-housing-situation-2018-00-23-apartments-by-occupancy-and-living-area-city.parquet)
* [berlin-microcensus-housing-situation-2018-00-23-apartments-by-occupancy-and-living-area-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2018-00-parquet/berlin-microcensus-housing-situation-2018-00-23-apartments-by-occupancy-and-living-area-districts.parquet)
* [berlin-microcensus-housing-situation-2018-00-26-apartments-by-building-type-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2018-00-parquet/berlin-microcensus-housing-situation-2018-00-26-apartments-by-building-type-city.parquet)
* [berlin-microcensus-housing-situation-2018-00-26-apartments-by-building-type-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2018-00-parquet/berlin-microcensus-housing-situation-2018-00-26-apartments-by-building-type-districts.parquet)
* [berlin-microcensus-housing-situation-2018-00-27-apartments-by-owner-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2018-00-parquet/berlin-microcensus-housing-situation-2018-00-27-apartments-by-owner-city.parquet)
* [berlin-microcensus-housing-situation-2018-00-27-apartments-by-owner-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2018-00-parquet/berlin-microcensus-housing-situation-2018-00-27-apartments-by-owner-districts.parquet)
* [berlin-microcensus-housing-situation-2018-00-28-apartments-by-living-area-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2018-00-parquet/berlin-microcensus-housing-situation-2018-00-28-apartments-by-living-area-city.parquet)
* [berlin-microcensus-housing-situation-2018-00-28-apartments-by-living-area-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2018-00-parquet/berlin-microcensus-housing-situation-2018-00-28-apartments-by-living-area-districts.parquet)
* [berlin-microcensus-housing-situation-2018-00-29-apartments-by-gross-rent-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2018-00-parquet/berlin-microcensus-housing-situation-2018-00-29-apartments-by-gross-rent-city.parquet)
* [berlin-microcensus-housing-situation-2018-00-29-apartments-by-gross-rent-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2018-00-parquet/berlin-microcensus-housing-situation-2018-00-29-apartments-by-gross-rent-districts.parquet)
* [berlin-microcensus-housing-situation-2018-00-30-apartments-by-gross-rent-per-sqm-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2018-00-parquet/berlin-microcensus-housing-situation-2018-00-30-apartments-by-gross-rent-per-sqm-city.parquet)
* [berlin-microcensus-housing-situation-2018-00-30-apartments-by-gross-rent-per-sqm-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2018-00-parquet/berlin-microcensus-housing-situation-2018-00-30-apartments-by-gross-rent-per-sqm-districts.parquet)
* [berlin-microcensus-housing-situation-2018-00-31-households-by-percentage-of-household-net-income-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2018-00-parquet/berlin-microcensus-housing-situation-2018-00-31-households-by-percentage-of-household-net-income-city.parquet)
* [berlin-microcensus-housing-situation-2018-00-31-households-by-percentage-of-household-net-income-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2018-00-parquet/berlin-microcensus-housing-situation-2018-00-31-households-by-percentage-of-household-net-income-districts.parquet)

### Berlin Microcensus Housing Situation 2022 00 Csv

* owner: Open Data Product
* url: https://github.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/tree/main/data/03-gold/berlin-microcensus-housing-situation-2022-00-csv
* updated: 2025-10-27

**Files**

* [berlin-microcensus-housing-situation-2022-00-15-households-by-building-type-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2022-00-csv/berlin-microcensus-housing-situation-2022-00-15-households-by-building-type-city.csv)
* [berlin-microcensus-housing-situation-2022-00-15-households-by-building-type-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2022-00-csv/berlin-microcensus-housing-situation-2022-00-15-households-by-building-type-districts.csv)
* [berlin-microcensus-housing-situation-2022-00-16-apartments-by-owner-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2022-00-csv/berlin-microcensus-housing-situation-2022-00-16-apartments-by-owner-city.csv)
* [berlin-microcensus-housing-situation-2022-00-16-apartments-by-owner-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2022-00-csv/berlin-microcensus-housing-situation-2022-00-16-apartments-by-owner-districts.csv)
* [berlin-microcensus-housing-situation-2022-00-17-apartments-by-living-area-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2022-00-csv/berlin-microcensus-housing-situation-2022-00-17-apartments-by-living-area-city.csv)
* [berlin-microcensus-housing-situation-2022-00-17-apartments-by-living-area-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2022-00-csv/berlin-microcensus-housing-situation-2022-00-17-apartments-by-living-area-districts.csv)
* [berlin-microcensus-housing-situation-2022-00-18-households-by-gross-rent-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2022-00-csv/berlin-microcensus-housing-situation-2022-00-18-households-by-gross-rent-city.csv)
* [berlin-microcensus-housing-situation-2022-00-18-households-by-gross-rent-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2022-00-csv/berlin-microcensus-housing-situation-2022-00-18-households-by-gross-rent-districts.csv)

### Berlin Microcensus Housing Situation 2022 00 Parquet

* owner: Open Data Product
* url: https://github.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/tree/main/data/03-gold/berlin-microcensus-housing-situation-2022-00-parquet
* updated: 2025-10-27

**Files**

* [berlin-microcensus-housing-situation-2022-00-15-households-by-building-type-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2022-00-parquet/berlin-microcensus-housing-situation-2022-00-15-households-by-building-type-city.parquet)
* [berlin-microcensus-housing-situation-2022-00-15-households-by-building-type-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2022-00-parquet/berlin-microcensus-housing-situation-2022-00-15-households-by-building-type-districts.parquet)
* [berlin-microcensus-housing-situation-2022-00-16-apartments-by-owner-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2022-00-parquet/berlin-microcensus-housing-situation-2022-00-16-apartments-by-owner-city.parquet)
* [berlin-microcensus-housing-situation-2022-00-16-apartments-by-owner-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2022-00-parquet/berlin-microcensus-housing-situation-2022-00-16-apartments-by-owner-districts.parquet)
* [berlin-microcensus-housing-situation-2022-00-17-apartments-by-living-area-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2022-00-parquet/berlin-microcensus-housing-situation-2022-00-17-apartments-by-living-area-city.parquet)
* [berlin-microcensus-housing-situation-2022-00-17-apartments-by-living-area-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2022-00-parquet/berlin-microcensus-housing-situation-2022-00-17-apartments-by-living-area-districts.parquet)
* [berlin-microcensus-housing-situation-2022-00-18-households-by-gross-rent-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2022-00-parquet/berlin-microcensus-housing-situation-2022-00-18-households-by-gross-rent-city.parquet)
* [berlin-microcensus-housing-situation-2022-00-18-households-by-gross-rent-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation-source-aligned/main/data/03-gold/berlin-microcensus-housing-situation-2022-00-parquet/berlin-microcensus-housing-situation-2022-00-18-households-by-gross-rent-districts.parquet)

## Classification

**The nature of the exposed data (source-aligned, aggregate, consumer-aligned)**

source-aligned


---
This data product canvas uses the template of [datamesh-architecture.com](https://www.datamesh-architecture.com/data-product-canvas).