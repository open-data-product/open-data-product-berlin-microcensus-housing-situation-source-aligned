
# Data Product Canvas - Berlin Microcensus Housing Situation (source-aligned)

## Metadata

* owner: Open Data Product
* description: Source-aligned data product providing Berlin microcensus housing situation data
* updated: 2025-06-16

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

## Transformation Steps

* [Data extractor](../lib/extract/data_extractor.py) extracts data from inout ports
* [Data copier](../lib/transform/data_copier.py) copies and renames extracted data
* [Data CSV converter](../lib/transform/convert_data_to_csv.py) converts Excel files to CSV format
* [Data aggregator](../lib/transform/aggregate_data.py) aggregates data to be used as output ports

## Output Ports

### Berlin Microcensus Housing Situation 2014 00

* owner: Open Data Product
* url: https://github.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/tree/main/data/02-silver/berlin-microcensus-housing-situation-2014-00
* updated: 2025-06-16

**Files**

* [berlin-microcensus-housing-situation-2014-00-1-apartments-by-size-year-of-construction-and-usage-type.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2014-00/berlin-microcensus-housing-situation-2014-00-1-apartments-by-size-year-of-construction-and-usage-type.csv)
* [berlin-microcensus-housing-situation-2014-00-10-households-by-usage-type.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2014-00/berlin-microcensus-housing-situation-2014-00-10-households-by-usage-type.csv)
* [berlin-microcensus-housing-situation-2014-00-11-households-by-building-size.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2014-00/berlin-microcensus-housing-situation-2014-00-11-households-by-building-size.csv)
* [berlin-microcensus-housing-situation-2014-00-12-households-by-living-area.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2014-00/berlin-microcensus-housing-situation-2014-00-12-households-by-living-area.csv)
* [berlin-microcensus-housing-situation-2014-00-13-households-by-gross-rent.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2014-00/berlin-microcensus-housing-situation-2014-00-13-households-by-gross-rent.csv)
* [berlin-microcensus-housing-situation-2014-00-14-households-by-gross-rent-per-sqm.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2014-00/berlin-microcensus-housing-situation-2014-00-14-households-by-gross-rent-per-sqm.csv)
* [berlin-microcensus-housing-situation-2014-00-15-households-by-percentage-of-household-net-income.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2014-00/berlin-microcensus-housing-situation-2014-00-15-households-by-percentage-of-household-net-income.csv)
* [berlin-microcensus-housing-situation-2014-00-16-families-by-usage-type.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2014-00/berlin-microcensus-housing-situation-2014-00-16-families-by-usage-type.csv)
* [berlin-microcensus-housing-situation-2014-00-17-families-by-building-size.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2014-00/berlin-microcensus-housing-situation-2014-00-17-families-by-building-size.csv)
* [berlin-microcensus-housing-situation-2014-00-18-families-by-living-area.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2014-00/berlin-microcensus-housing-situation-2014-00-18-families-by-living-area.csv)
* [berlin-microcensus-housing-situation-2014-00-19-apartments-by-district-occupancy-and-living-area.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2014-00/berlin-microcensus-housing-situation-2014-00-19-apartments-by-district-occupancy-and-living-area.csv)
* [berlin-microcensus-housing-situation-2014-00-2-apartments-by-year-of-construction-heating-type-living-area-and-usage-type.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2014-00/berlin-microcensus-housing-situation-2014-00-2-apartments-by-year-of-construction-heating-type-living-area-and-usage-type.csv)
* [berlin-microcensus-housing-situation-2014-00-20-apartments-by-district-year-of-construction-and-usage-type.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2014-00/berlin-microcensus-housing-situation-2014-00-20-apartments-by-district-year-of-construction-and-usage-type.csv)
* [berlin-microcensus-housing-situation-2014-00-21-apartments-by-district-usage-type-living-area-and-occupancy.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2014-00/berlin-microcensus-housing-situation-2014-00-21-apartments-by-district-usage-type-living-area-and-occupancy.csv)
* [berlin-microcensus-housing-situation-2014-00-22-apartments-by-district-and-living-area.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2014-00/berlin-microcensus-housing-situation-2014-00-22-apartments-by-district-and-living-area.csv)
* [berlin-microcensus-housing-situation-2014-00-23-apartments-by-district-and-gross-rent.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2014-00/berlin-microcensus-housing-situation-2014-00-23-apartments-by-district-and-gross-rent.csv)
* [berlin-microcensus-housing-situation-2014-00-24-apartments-by-district-and-gross-rent-per-sqm.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2014-00/berlin-microcensus-housing-situation-2014-00-24-apartments-by-district-and-gross-rent-per-sqm.csv)
* [berlin-microcensus-housing-situation-2014-00-25-households-by-percentage-of-household-net-income.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2014-00/berlin-microcensus-housing-situation-2014-00-25-households-by-percentage-of-household-net-income.csv)
* [berlin-microcensus-housing-situation-2014-00-3-apartments-by-usage-type-building-size-living-area-and-occupancy.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2014-00/berlin-microcensus-housing-situation-2014-00-3-apartments-by-usage-type-building-size-living-area-and-occupancy.csv)
* [berlin-microcensus-housing-situation-2014-00-4-apartments-by-usage-type-year-of-construction-and-living-area.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2014-00/berlin-microcensus-housing-situation-2014-00-4-apartments-by-usage-type-year-of-construction-and-living-area.csv)
* [berlin-microcensus-housing-situation-2014-00-5-apartments-by-building-size-year-of-construction-living-area-and-gross-rent-per-sqm.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2014-00/berlin-microcensus-housing-situation-2014-00-5-apartments-by-building-size-year-of-construction-living-area-and-gross-rent-per-sqm.csv)
* [berlin-microcensus-housing-situation-2014-00-6-apartments-by-building-size-year-of-construction-living-area-and-gross-rent.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2014-00/berlin-microcensus-housing-situation-2014-00-6-apartments-by-building-size-year-of-construction-living-area-and-gross-rent.csv)
* [berlin-microcensus-housing-situation-2014-00-7-apartments-by-usage-type-year-of-construction-warm-water-and-energy-type.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2014-00/berlin-microcensus-housing-situation-2014-00-7-apartments-by-usage-type-year-of-construction-warm-water-and-energy-type.csv)
* [berlin-microcensus-housing-situation-2014-00-8-apartments-by-usage-type-year-of-construction-collective-heating-and-energy-type.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2014-00/berlin-microcensus-housing-situation-2014-00-8-apartments-by-usage-type-year-of-construction-collective-heating-and-energy-type.csv)
* [berlin-microcensus-housing-situation-2014-00-9-apartments-by-usage-type-building-size-heating-and-energy-type.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2014-00/berlin-microcensus-housing-situation-2014-00-9-apartments-by-usage-type-building-size-heating-and-energy-type.csv)

### Berlin Microcensus Housing Situation 2018 00

* owner: Open Data Product
* url: https://github.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/tree/main/data/02-silver/berlin-microcensus-housing-situation-2018-00
* updated: 2025-06-16

**Files**

* [berlin-microcensus-housing-situation-2018-00-1-apartments-by-size-year-of-construction-and-usage-type.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-1-apartments-by-size-year-of-construction-and-usage-type.csv)
* [berlin-microcensus-housing-situation-2018-00-10-apartments-by-usage-type-year-of-construction-collective-heating-and-energy-type.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-10-apartments-by-usage-type-year-of-construction-collective-heating-and-energy-type.csv)
* [berlin-microcensus-housing-situation-2018-00-11-apartments-by-usage-type-building-size-heating-and-energy-type.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-11-apartments-by-usage-type-building-size-heating-and-energy-type.csv)
* [berlin-microcensus-housing-situation-2018-00-12-apartments-by-usage-type-barrier-reduction-year-of-construction.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-12-apartments-by-usage-type-barrier-reduction-year-of-construction.csv)
* [berlin-microcensus-housing-situation-2018-00-13-households-by-usage-type.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-13-households-by-usage-type.csv)
* [berlin-microcensus-housing-situation-2018-00-14-households-by-building-type.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-14-households-by-building-type.csv)
* [berlin-microcensus-housing-situation-2018-00-15-households-by-living-area.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-15-households-by-living-area.csv)
* [berlin-microcensus-housing-situation-2018-00-16-apartments-by-room-count.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-16-apartments-by-room-count.csv)
* [berlin-microcensus-housing-situation-2018-00-17-households-by-gross-rent.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-17-households-by-gross-rent.csv)
* [berlin-microcensus-housing-situation-2018-00-18-households-by-gross-rent-per-sqm.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-18-households-by-gross-rent-per-sqm.csv)
* [berlin-microcensus-housing-situation-2018-00-19-households-by-percentage-of-household-net-income.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-19-households-by-percentage-of-household-net-income.csv)
* [berlin-microcensus-housing-situation-2018-00-2-apartments-by-year-of-construction-heating-type-living-area-and-usage-type.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-2-apartments-by-year-of-construction-heating-type-living-area-and-usage-type.csv)
* [berlin-microcensus-housing-situation-2018-00-20-families-by-usage-type.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-20-families-by-usage-type.csv)
* [berlin-microcensus-housing-situation-2018-00-21-families-by-living-area.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-21-families-by-living-area.csv)
* [berlin-microcensus-housing-situation-2018-00-22-apartments-by-room-count.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-22-apartments-by-room-count.csv)
* [berlin-microcensus-housing-situation-2018-00-23-apartments-by-district-occupancy-and-living-area.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-23-apartments-by-district-occupancy-and-living-area.csv)
* [berlin-microcensus-housing-situation-2018-00-24-apartments-by-district-year-of-construction-and-usage-type.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-24-apartments-by-district-year-of-construction-and-usage-type.csv)
* [berlin-microcensus-housing-situation-2018-00-25-apartments-by-district-usage-type-living-area-and-occupancy.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-25-apartments-by-district-usage-type-living-area-and-occupancy.csv)
* [berlin-microcensus-housing-situation-2018-00-26-apartments-by-district-and-building-type.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-26-apartments-by-district-and-building-type.csv)
* [berlin-microcensus-housing-situation-2018-00-27-apartments-by-district-and-owner.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-27-apartments-by-district-and-owner.csv)
* [berlin-microcensus-housing-situation-2018-00-28-apartments-by-district-and-living-area.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-28-apartments-by-district-and-living-area.csv)
* [berlin-microcensus-housing-situation-2018-00-29-apartments-by-district-and-gross-rent.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-29-apartments-by-district-and-gross-rent.csv)
* [berlin-microcensus-housing-situation-2018-00-3-apartments-by-usage-type-building-size-living-area-and-occupancy.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-3-apartments-by-usage-type-building-size-living-area-and-occupancy.csv)
* [berlin-microcensus-housing-situation-2018-00-30-apartments-by-district-and-gross-rent-per-sqm.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-30-apartments-by-district-and-gross-rent-per-sqm.csv)
* [berlin-microcensus-housing-situation-2018-00-31-households-by-district-and-percentage-of-household-net-income.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-31-households-by-district-and-percentage-of-household-net-income.csv)
* [berlin-microcensus-housing-situation-2018-00-4-apartments-by-usage-type-year-of-construction-and-living-area.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-4-apartments-by-usage-type-year-of-construction-and-living-area.csv)
* [berlin-microcensus-housing-situation-2018-00-5-apartments-by-usage-type-year-of-construction-and-room-count.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-5-apartments-by-usage-type-year-of-construction-and-room-count.csv)
* [berlin-microcensus-housing-situation-2018-00-6-apartments-by-building-size-year-of-construction-living-area-and-gross-rent-per-sqm.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-6-apartments-by-building-size-year-of-construction-living-area-and-gross-rent-per-sqm.csv)
* [berlin-microcensus-housing-situation-2018-00-7-apartments-by-building-size-year-of-construction-living-area-and-gross-rent.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-7-apartments-by-building-size-year-of-construction-living-area-and-gross-rent.csv)
* [berlin-microcensus-housing-situation-2018-00-8-apartments-by-building-size-year-of-construction-living-area-and-warm-rent.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-8-apartments-by-building-size-year-of-construction-living-area-and-warm-rent.csv)
* [berlin-microcensus-housing-situation-2018-00-9-apartments-by-usage-type-year-of-construction-warm-water-and-energy-type.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/02-silver/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-9-apartments-by-usage-type-year-of-construction-warm-water-and-energy-type.csv)

### Berlin Microcensus Housing Situation 2014 00

* owner: Open Data Product
* url: https://github.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/tree/main/data/03-gold/berlin-microcensus-housing-situation-2014-00
* updated: 2025-06-16

**Files**

* [berlin-microcensus-housing-situation-2014-00-19-apartments-by-district-occupancy-and-living-area-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/03-gold/berlin-microcensus-housing-situation-2014-00/berlin-microcensus-housing-situation-2014-00-19-apartments-by-district-occupancy-and-living-area-city.csv)
* [berlin-microcensus-housing-situation-2014-00-19-apartments-by-district-occupancy-and-living-area-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/03-gold/berlin-microcensus-housing-situation-2014-00/berlin-microcensus-housing-situation-2014-00-19-apartments-by-district-occupancy-and-living-area-districts.csv)
* [berlin-microcensus-housing-situation-2014-00-22-apartments-by-district-and-living-area-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/03-gold/berlin-microcensus-housing-situation-2014-00/berlin-microcensus-housing-situation-2014-00-22-apartments-by-district-and-living-area-city.csv)
* [berlin-microcensus-housing-situation-2014-00-22-apartments-by-district-and-living-area-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/03-gold/berlin-microcensus-housing-situation-2014-00/berlin-microcensus-housing-situation-2014-00-22-apartments-by-district-and-living-area-districts.csv)
* [berlin-microcensus-housing-situation-2014-00-23-apartments-by-district-and-gross-rent-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/03-gold/berlin-microcensus-housing-situation-2014-00/berlin-microcensus-housing-situation-2014-00-23-apartments-by-district-and-gross-rent-city.csv)
* [berlin-microcensus-housing-situation-2014-00-23-apartments-by-district-and-gross-rent-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/03-gold/berlin-microcensus-housing-situation-2014-00/berlin-microcensus-housing-situation-2014-00-23-apartments-by-district-and-gross-rent-districts.csv)
* [berlin-microcensus-housing-situation-2014-00-24-apartments-by-district-and-gross-rent-per-sqm-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/03-gold/berlin-microcensus-housing-situation-2014-00/berlin-microcensus-housing-situation-2014-00-24-apartments-by-district-and-gross-rent-per-sqm-city.csv)
* [berlin-microcensus-housing-situation-2014-00-24-apartments-by-district-and-gross-rent-per-sqm-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/03-gold/berlin-microcensus-housing-situation-2014-00/berlin-microcensus-housing-situation-2014-00-24-apartments-by-district-and-gross-rent-per-sqm-districts.csv)
* [berlin-microcensus-housing-situation-2014-00-25-households-by-percentage-of-household-net-income-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/03-gold/berlin-microcensus-housing-situation-2014-00/berlin-microcensus-housing-situation-2014-00-25-households-by-percentage-of-household-net-income-city.csv)
* [berlin-microcensus-housing-situation-2014-00-25-households-by-percentage-of-household-net-income-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/03-gold/berlin-microcensus-housing-situation-2014-00/berlin-microcensus-housing-situation-2014-00-25-households-by-percentage-of-household-net-income-districts.csv)

### Berlin Microcensus Housing Situation 2018 00

* owner: Open Data Product
* url: https://github.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/tree/main/data/03-gold/berlin-microcensus-housing-situation-2018-00
* updated: 2025-06-16

**Files**

* [berlin-microcensus-housing-situation-2018-00-23-apartments-by-district-occupancy-and-living-area-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/03-gold/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-23-apartments-by-district-occupancy-and-living-area-city.csv)
* [berlin-microcensus-housing-situation-2018-00-23-apartments-by-district-occupancy-and-living-area-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/03-gold/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-23-apartments-by-district-occupancy-and-living-area-districts.csv)
* [berlin-microcensus-housing-situation-2018-00-26-apartments-by-district-and-building-type-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/03-gold/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-26-apartments-by-district-and-building-type-city.csv)
* [berlin-microcensus-housing-situation-2018-00-26-apartments-by-district-and-building-type-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/03-gold/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-26-apartments-by-district-and-building-type-districts.csv)
* [berlin-microcensus-housing-situation-2018-00-27-apartments-by-district-and-owner-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/03-gold/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-27-apartments-by-district-and-owner-city.csv)
* [berlin-microcensus-housing-situation-2018-00-27-apartments-by-district-and-owner-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/03-gold/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-27-apartments-by-district-and-owner-districts.csv)
* [berlin-microcensus-housing-situation-2018-00-28-apartments-by-district-and-living-area-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/03-gold/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-28-apartments-by-district-and-living-area-city.csv)
* [berlin-microcensus-housing-situation-2018-00-28-apartments-by-district-and-living-area-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/03-gold/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-28-apartments-by-district-and-living-area-districts.csv)
* [berlin-microcensus-housing-situation-2018-00-29-apartments-by-district-and-gross-rent-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/03-gold/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-29-apartments-by-district-and-gross-rent-city.csv)
* [berlin-microcensus-housing-situation-2018-00-29-apartments-by-district-and-gross-rent-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/03-gold/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-29-apartments-by-district-and-gross-rent-districts.csv)
* [berlin-microcensus-housing-situation-2018-00-30-apartments-by-district-and-gross-rent-per-sqm-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/03-gold/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-30-apartments-by-district-and-gross-rent-per-sqm-city.csv)
* [berlin-microcensus-housing-situation-2018-00-30-apartments-by-district-and-gross-rent-per-sqm-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/03-gold/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-30-apartments-by-district-and-gross-rent-per-sqm-districts.csv)
* [berlin-microcensus-housing-situation-2018-00-31-households-by-district-and-percentage-of-household-net-income-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/03-gold/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-31-households-by-district-and-percentage-of-household-net-income-city.csv)
* [berlin-microcensus-housing-situation-2018-00-31-households-by-district-and-percentage-of-household-net-income-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-microcensus-housing-situation/main/data/03-gold/berlin-microcensus-housing-situation-2018-00/berlin-microcensus-housing-situation-2018-00-31-households-by-district-and-percentage-of-household-net-income-districts.csv)

## Classification

**The nature of the exposed data (source-aligned, aggregate, consumer-aligned)**

source-aligned


---
This data product canvas uses the template of [datamesh-architecture.com](https://www.datamesh-architecture.com/data-product-canvas).