import os

import pandas as pd

from lib.tracking_decorator import TrackingDecorator


@TrackingDecorator.track_time
def convert_data_to_csv(source_path, results_path, clean=False, quiet=False):
    # Iterate over files
    for subdir, dirs, files in sorted(os.walk(source_path)):
        # Make results path
        subdir = subdir.replace(f"{source_path}/", "")
        os.makedirs(os.path.join(results_path, subdir), exist_ok=True)

        for file_name in [file_name for file_name in sorted(files)
                          if not file_name.startswith(f"~") and
                             (file_name.endswith(".xlsx") or file_name.endswith(".xls"))]:
            source_file_path = os.path.join(source_path, subdir, file_name)

            convert_file_to_csv_apartments_by_size_year_of_construction_and_usage(
                source_file_path, clean=clean, quiet=quiet)
            convert_file_to_csv_apartments_by_year_of_construction_heating_type_living_area_and_usage_type(
                source_file_path, clean=clean, quiet=quiet)
            convert_file_to_csv_apartments_by_usage_type_building_size_living_area_occupancy(
                source_file_path, clean=clean, quiet=quiet)
            convert_file_to_csv_apartments_by_usage_type_year_of_construction_and_living_area(
                source_file_path, clean=clean, quiet=quiet)
            convert_file_to_csv_apartments_by_building_size_year_of_construction_living_area_and_gross_rent_per_sqm(
                source_file_path, clean=clean, quiet=quiet)
            convert_file_to_csv_apartments_by_building_size_year_of_construction_living_area_and_gross_rent(
                source_file_path, clean=clean, quiet=quiet)
            convert_file_to_csv_apartments_by_usage_type_year_of_construction_warm_water_and_energy_type(
                source_file_path, clean=clean, quiet=quiet)


def convert_file_to_csv_apartments_by_size_year_of_construction_and_usage(
        source_file_path, clean=False, quiet=False):
    source_file_name, source_file_extension = os.path.splitext(source_file_path)
    file_path_csv = f"{source_file_name}-1-apartments-by-size-year-of-construction-and-usage.csv"

    # Check if result needs to be generated
    if not clean and os.path.exists(file_path_csv):
        if not quiet:
            print(f"✓ Already exists {os.path.basename(file_path_csv)}")
        return

    # Determine engine
    engine = build_engine(source_file_extension)

    try:
        # Iterate over sheets
        sheet = "Tab 1"
        skiprows = 6
        names = ["type", "apartments", "inhabited_by_owner", "inhabited_by_owner_percentage", "rented_out",
                 "rented_out_percentage", "uninhabited", "uninhabited_percentage"]
        drop_columns = ["year"]

        dataframe = pd.read_excel(source_file_path, engine=engine, sheet_name=sheet, skiprows=skiprows, names=names,
                                  index_col=False) \
            .drop(columns=drop_columns, errors="ignore") \
            .replace("–", 0) \
            .replace("/", 0) \
            .dropna() \
            .assign(type=lambda df: df["type"].apply(lambda row: build_type_name(row)))

        dataframe.reset_index(drop=True, inplace=True)
        dataframe = dataframe.assign(type_index=lambda df: df.index) \
            .assign(type_parent_index=lambda df: df.apply(lambda row: build_type_parent_index_1(row), axis=1)) \
            .fillna(-1) \
            .assign(type_parent_index=lambda df: df["type_parent_index"].astype(int))
        dataframe.insert(0, "type_index", dataframe.pop("type_index"))
        dataframe.insert(1, "type_parent_index", dataframe.pop("type_parent_index"))

        # Write csv file
        write_csv_file(dataframe, file_path_csv, quiet)
    except Exception as e:
        print(f"✗️ Exception: {str(e)}")


def convert_file_to_csv_apartments_by_year_of_construction_heating_type_living_area_and_usage_type(
        source_file_path, clean=False, quiet=False):
    source_file_name, source_file_extension = os.path.splitext(source_file_path)
    file_path_csv = f"{source_file_name}-2-apartments-by-year-of-construction-heating-type-living-area-and-usage-type.csv"

    # Check if result needs to be generated
    if not clean and os.path.exists(file_path_csv):
        if not quiet:
            print(f"✓ Already exists {os.path.basename(file_path_csv)}")
        return

    # Determine engine
    engine = build_engine(source_file_extension)

    try:
        # Iterate over sheets
        sheet = "Tab 2"
        skiprows = 6
        names = ["type", "apartments", "condominium", "condominium_percentage", "rented_apartments",
                 "rented_apartments_percentage"]
        drop_columns = []

        dataframe = pd.read_excel(source_file_path, engine=engine, sheet_name=sheet, skiprows=skiprows, names=names,
                                  index_col=False) \
            .drop(columns=drop_columns, errors="ignore") \
            .replace("–", 0) \
            .replace("/", 0) \
            .dropna() \
            .assign(type=lambda df: df["type"].apply(lambda row: build_type_name(row)))

        dataframe.reset_index(drop=True, inplace=True)
        dataframe = dataframe.assign(type_index=lambda df: df.index) \
            .assign(type_parent_index=lambda df: df.apply(lambda row: build_type_parent_index_2(row), axis=1)) \
            .fillna(-1) \
            .assign(type_parent_index=lambda df: df["type_parent_index"].astype(int))
        dataframe.insert(0, "type_index", dataframe.pop("type_index"))
        dataframe.insert(1, "type_parent_index", dataframe.pop("type_parent_index"))

        # Write csv file
        write_csv_file(dataframe, file_path_csv, quiet)
    except Exception as e:
        print(f"✗️ Exception: {str(e)}")


def convert_file_to_csv_apartments_by_usage_type_building_size_living_area_occupancy(
        source_file_path, clean=False, quiet=False):
    source_file_name, source_file_extension = os.path.splitext(source_file_path)
    file_path_csv = f"{source_file_name}-3-apartments-by-usage-type-building-size-living-area-occupancy.csv"

    # Check if result needs to be generated
    if not clean and os.path.exists(file_path_csv):
        if not quiet:
            print(f"✓ Already exists {os.path.basename(file_path_csv)}")
        return

    # Determine engine
    engine = build_engine(source_file_extension)

    try:
        # Iterate over sheets
        sheet = "Tab 3"
        skiprows = 6
        names = ["type", "apartments", "living_area", "living_area_per_apartment", "persons_per_apartment",
                 "living_area_per_person"]
        drop_columns = []

        dataframe = pd.read_excel(source_file_path, engine=engine, sheet_name=sheet, skiprows=skiprows, names=names,
                                  index_col=False) \
            .drop(columns=drop_columns, errors="ignore") \
            .dropna() \
            .assign(type=lambda df: df["type"].apply(lambda row: build_type_name(row)))

        dataframe.reset_index(drop=True, inplace=True)
        dataframe = dataframe.assign(type_index=lambda df: df.index) \
            .assign(type_parent_index=lambda df: df.apply(lambda row: build_type_parent_index_3(row), axis=1)) \
            .fillna(-1) \
            .assign(type_parent_index=lambda df: df["type_parent_index"].astype(int))
        dataframe.insert(0, "type_index", dataframe.pop("type_index"))
        dataframe.insert(1, "type_parent_index", dataframe.pop("type_parent_index"))

        dataframe.at[0, "type"] = "apartments"
        dataframe.at[7, "type"] = "condominiums"
        dataframe.at[14, "type"] = "rented_apartments"

        # Write csv file
        write_csv_file(dataframe, file_path_csv, quiet)
    except Exception as e:
        print(f"✗️ Exception: {str(e)}")


def convert_file_to_csv_apartments_by_usage_type_year_of_construction_and_living_area(
        source_file_path, clean=False, quiet=False):
    source_file_name, source_file_extension = os.path.splitext(source_file_path)
    file_path_csv = f"{source_file_name}-4-apartments-by-usage-type-year-of-construction-and-living-area.csv"

    # Check if result needs to be generated
    if not clean and os.path.exists(file_path_csv):
        if not quiet:
            print(f"✓ Already exists {os.path.basename(file_path_csv)}")
        return

    # Determine engine
    engine = build_engine(source_file_extension)

    try:
        # Iterate over sheets
        sheet = "Tab 4"
        skiprows = 6
        names = ["type", "apartments", "below_40sqm", "between_40_and_60sqm", "between_60_and_80sqm",
                 "between_80_and_100sqm", "between_100_and_120sqm", "more_than_120sqm"]
        drop_columns = []

        dataframe = pd.read_excel(source_file_path, engine=engine, sheet_name=sheet, skiprows=skiprows, names=names,
                                  index_col=False) \
            .drop(columns=drop_columns, errors="ignore") \
            .replace("–", 0) \
            .replace("/", 0) \
            .dropna() \
            .assign(type=lambda df: df["type"].apply(lambda row: build_type_name(row)))

        dataframe.reset_index(drop=True, inplace=True)
        dataframe = dataframe.assign(type_index=lambda df: df.index) \
            .assign(type_parent_index=lambda df: df.apply(lambda row: build_type_parent_index_4(row), axis=1)) \
            .fillna(-1) \
            .assign(type_parent_index=lambda df: df["type_parent_index"].astype(int))
        dataframe.insert(0, "type_index", dataframe.pop("type_index"))
        dataframe.insert(1, "type_parent_index", dataframe.pop("type_parent_index"))

        dataframe.at[0, "type"] = "apartments"
        dataframe.at[7, "type"] = "condominiums"
        dataframe.at[14, "type"] = "rented_apartments"

        # Write csv file
        write_csv_file(dataframe, file_path_csv, quiet)
    except Exception as e:
        print(f"✗️ Exception: {str(e)}")


def convert_file_to_csv_apartments_by_building_size_year_of_construction_living_area_and_gross_rent_per_sqm(
        source_file_path, clean=False, quiet=False):
    source_file_name, source_file_extension = os.path.splitext(source_file_path)
    file_path_csv = f"{source_file_name}-5-apartments-by-building-size-year-of-construction-living-area-and-gross-rent-per-sqm.csv"

    # Check if result needs to be generated
    if not clean and os.path.exists(file_path_csv):
        if not quiet:
            print(f"✓ Already exists {os.path.basename(file_path_csv)}")
        return

    # Determine engine
    engine = build_engine(source_file_extension)

    try:
        # Iterate over sheets
        sheet = "Tab 5"
        skiprows = 6
        names = ["type", "apartments", "below_6_euros", "between_6_and_7_euros", "between_7_and_8_euros",
                 "between_8_and_9_euros", "between_9_and_10_euros", "more_than_10_euros", "average"]
        drop_columns = []

        dataframe = pd.read_excel(source_file_path, engine=engine, sheet_name=sheet, skiprows=skiprows, names=names,
                                  index_col=False) \
            .drop(columns=drop_columns, errors="ignore") \
            .replace("–", 0) \
            .replace("/", 0) \
            .dropna() \
            .assign(type=lambda df: df["type"].apply(lambda row: build_type_name(row)))

        dataframe.reset_index(drop=True, inplace=True)
        dataframe = dataframe.assign(type_index=lambda df: df.index) \
            .assign(type_parent_index=lambda df: df.apply(lambda row: build_type_parent_index_5_6(row), axis=1)) \
            .fillna(-1) \
            .assign(type_parent_index=lambda df: df["type_parent_index"].astype(int))
        dataframe.insert(0, "type_index", dataframe.pop("type_index"))
        dataframe.insert(1, "type_parent_index", dataframe.pop("type_parent_index"))

        dataframe.at[13, "type"] = "build_before_1949"
        dataframe.at[20, "type"] = "build_after_1949"

        # Write csv file
        write_csv_file(dataframe, file_path_csv, quiet)
    except Exception as e:
        print(f"✗️ Exception: {str(e)}")


def convert_file_to_csv_apartments_by_building_size_year_of_construction_living_area_and_gross_rent(
        source_file_path, clean=False, quiet=False):
    source_file_name, source_file_extension = os.path.splitext(source_file_path)
    file_path_csv = f"{source_file_name}-6-apartments-by-building-size-year-of-construction-living-area-and-gross-rent.csv"

    # Check if result needs to be generated
    if not clean and os.path.exists(file_path_csv):
        if not quiet:
            print(f"✓ Already exists {os.path.basename(file_path_csv)}")
        return

    # Determine engine
    engine = build_engine(source_file_extension)

    try:
        # Iterate over sheets
        sheet = "Tab 6"
        skiprows = 8
        names = ["type", "apartments", "below_300_euros", "between_300_and_400_euros", "between_400_and_500_euros",
                 "between_500_and_600_euros", "between_600_and_700_euros", "between_700_and_800_euros",
                 "more_than_800_euros"]
        drop_columns = []

        dataframe = pd.read_excel(source_file_path, engine=engine, sheet_name=sheet, skiprows=skiprows, names=names,
                                  index_col=False) \
            .drop(columns=drop_columns, errors="ignore") \
            .replace("–", 0) \
            .replace("/", 0) \
            .dropna() \
            .assign(type=lambda df: df["type"].apply(lambda row: build_type_name(row)))

        dataframe.reset_index(drop=True, inplace=True)
        dataframe = dataframe.assign(type_index=lambda df: df.index) \
            .assign(type_parent_index=lambda df: df.apply(lambda row: build_type_parent_index_5_6(row), axis=1)) \
            .fillna(-1) \
            .assign(type_parent_index=lambda df: df["type_parent_index"].astype(int))
        dataframe.insert(0, "type_index", dataframe.pop("type_index"))
        dataframe.insert(1, "type_parent_index", dataframe.pop("type_parent_index"))

        dataframe.at[15, "type"] = "build_before_1949"
        dataframe.at[22, "type"] = "build_after_1949"

        # Write csv file
        write_csv_file(dataframe, file_path_csv, quiet)
    except Exception as e:
        print(f"✗️ Exception: {str(e)}")


def convert_file_to_csv_apartments_by_usage_type_year_of_construction_warm_water_and_energy_type(
        source_file_path, clean=False, quiet=False):
    source_file_name, source_file_extension = os.path.splitext(source_file_path)
    file_path_csv = f"{source_file_name}-7-apartments-by_usage-type-year-of-construction-warm-water-and-energy-type.csv"

    # Check if result needs to be generated
    if not clean and os.path.exists(file_path_csv):
        if not quiet:
            print(f"✓ Already exists {os.path.basename(file_path_csv)}")
        return

    # Determine engine
    engine = build_engine(source_file_extension)

    try:
        # Iterate over sheets
        sheet = "Tab 7"
        skiprows = 8
        names = ["type", "apartments", "district_heating", "gas", "electricity", "heating_oil",
                 "briquettes_lignite_coal_coke_hard_coal", "wood_or_other_renewable_renewable_energies"]
        drop_columns = []

        dataframe = pd.read_excel(source_file_path, engine=engine, sheet_name=sheet, skiprows=skiprows, names=names,
                                  index_col=False) \
            .drop(columns=drop_columns, errors="ignore") \
            .replace("–", 0) \
            .replace("/", 0) \
            .dropna() \
            .assign(type=lambda df: df["type"].apply(lambda row: build_type_name(row)))

        dataframe.reset_index(drop=True, inplace=True)
        dataframe = dataframe.assign(type_index=lambda df: df.index) \
            .assign(type_parent_index=lambda df: df.apply(lambda row: build_type_parent_index_7(row), axis=1)) \
            .fillna(-1) \
            .assign(type_parent_index=lambda df: df["type_parent_index"].astype(int))
        dataframe.insert(0, "type_index", dataframe.pop("type_index"))
        dataframe.insert(1, "type_parent_index", dataframe.pop("type_parent_index"))
        #
        dataframe.at[7, "type"] = "condominiums"
        dataframe.at[14, "type"] = "rented_apartments"

        # Write csv file
        write_csv_file(dataframe, file_path_csv, quiet)
    except Exception as e:
        print(f"✗️ Exception: {str(e)}")


#
# Transformers
#

def build_type_name(value):
    value = str(value).lstrip().rstrip()

    if value == "Wohnungen":
        return "apartments"
    elif value == "bis 1918":
        return "until_2018"
    elif value == "1919 – 1948":
        return "between_1919_and_1948"
    elif value == "1949 – 1978":
        return "between_1949_and_1978"
    elif value == "1979 – 1990":
        return "between_1979_and_1990"
    elif value == "1991 – 2000":
        return "between_1991_and_2000"
    elif value == "2001 und später":
        return "2001_and_later"
    elif value == "mit 1 Wohnung":
        return "with_1_apartment"
    elif value == "mit 2 Wohnungen":
        return "with_2_apartments"
    elif value == "mit 3 – 6 Wohnungen":
        return "with_3_to_6_apartments"
    elif value == "mit 7 – 12 Wohnungen":
        return "with_7_to_12_apartments"
    elif value == "mit 13 und mehr Wohnungen":
        return "with_13_or_more_apartments"

    elif value == "Bewohnte Wohnungen":
        return "inhabited_apartments"
    elif value == "bis 1990 errichtet":
        return "build_before_1990"
    elif value == "1991 und später errichtet":
        return "build_after_1991"
    elif value == "mit Sammelheizung²":
        return "collective_heating"
    elif value == "Fernheizung":
        return "district_heating"
    elif value == "Block-/Zentralheizung":
        return "central_heating"
    elif value == "Etagenheizung":
        return "floor_heating"
    elif value == "mit Einzel- oder Mehrraumöfen":
        return "single_or_multi_room_ovens"
    elif value == "unter  40":
        return "area_below_40sqm"
    elif value == "40 –   60":
        return "area_between_40_and_60sqm"
    elif value == "60 –   80":
        return "area_between_60_and_80sqm"
    elif value == "80 – 100":
        return "area_between_80_and_100sqm"
    elif value == "100 – 120":
        return "area_between_100_and_120sqm"
    elif value == "120 und mehr":
        return "area_above_120sqm"

    elif value == "1 Wohnung":
        return "1_apartment"
    elif value == "2 Wohnungen":
        return "2_apartments"
    elif value == "3 –    6 Wohnungen":
        return "between_3_and_6_apartments"
    elif value == "7 –  12 Wohnungen":
        return "between_7_and_12_apartments"
    elif value == "7 –  9 Wohnungen":
        return "between_7_and_9_apartments"
    elif value == "10 –  20 Wohnungen":
        return "between_10_and_20_apartments"
    elif value == "13 –  20 Wohnungen":
        return "between_13_and_20_apartments"
    elif value == "21 und mehr Wohnungen":
        return "more_than_21_apartments"

    elif value == "Insgesamt":
        return "total"

    else:
        return value


def build_type_parent_index_1(row):
    row_index = row.name

    if row_index == 0:
        return -1
    elif row_index == 1:
        return 0
    elif row_index == 2:
        return 0
    elif row_index == 3:
        return 0
    elif row_index == 4:
        return 0
    elif row_index == 5:
        return 0
    elif row_index == 6:
        return 0
    elif row_index == 7:
        return 0
    elif row_index == 8:
        return 7
    elif row_index == 9:
        return 7
    elif row_index == 10:
        return 7
    elif row_index == 11:
        return 7
    elif row_index == 12:
        return 7
    elif row_index == 13:
        return 7
    elif row_index == 14:
        return 0
    elif row_index == 15:
        return 14
    elif row_index == 16:
        return 14
    elif row_index == 17:
        return 14
    elif row_index == 18:
        return 14
    elif row_index == 19:
        return 14
    elif row_index == 20:
        return 14
    elif row_index == 21:
        return 0
    elif row_index == 22:
        return 21
    elif row_index == 23:
        return 21
    elif row_index == 24:
        return 21
    elif row_index == 25:
        return 21
    elif row_index == 26:
        return 21
    elif row_index == 27:
        return 21
    elif row_index == 28:
        return 0
    elif row_index == 29:
        return 28
    elif row_index == 30:
        return 28
    elif row_index == 31:
        return 28
    elif row_index == 32:
        return 28
    elif row_index == 33:
        return 28
    elif row_index == 34:
        return 28
    elif row_index == 35:
        return 0
    elif row_index == 36:
        return 35
    elif row_index == 37:
        return 35
    elif row_index == 38:
        return 35
    elif row_index == 39:
        return 35
    elif row_index == 40:
        return 35
    elif row_index == 41:
        return 35
    else:
        return None


def build_type_parent_index_2(row):
    row_index = row.name

    if row_index == 0:
        return 1
    elif row_index == 1:
        return 0
    elif row_index == 2:
        return 0
    elif row_index == 3:
        return 0
    elif row_index == 4:
        return 0
    elif row_index == 5:
        return 0
    elif row_index == 6:
        return 0
    elif row_index == 7:
        return 0
    elif row_index == 8:
        return 0
    elif row_index == 9:
        return 0
    elif row_index == 10:
        return 0
    elif row_index == 11:
        return 0
    elif row_index == 12:
        return 0
    elif row_index == 13:
        return 0
    elif row_index == 14:
        return 0
    elif row_index == 15:
        return 14
    elif row_index == 16:
        return 14
    elif row_index == 17:
        return 14
    elif row_index == 18:
        return 14
    elif row_index == 19:
        return 14
    elif row_index == 20:
        return 14
    elif row_index == 21:
        return 14
    elif row_index == 22:
        return 14
    elif row_index == 23:
        return 14
    elif row_index == 24:
        return 14
    elif row_index == 25:
        return 14
    elif row_index == 26:
        return 14
    elif row_index == 27:
        return 14
    elif row_index == 28:
        return 0
    elif row_index == 29:
        return 28
    elif row_index == 30:
        return 28
    elif row_index == 31:
        return 28
    elif row_index == 32:
        return 28
    elif row_index == 33:
        return 28
    elif row_index == 34:
        return 28
    elif row_index == 35:
        return 28
    elif row_index == 36:
        return 28
    elif row_index == 37:
        return 28
    elif row_index == 38:
        return 28
    elif row_index == 39:
        return 28
    elif row_index == 40:
        return 28
    elif row_index == 41:
        return 28
    elif row_index == 42:
        return 0
    elif row_index == 43:
        return 42
    elif row_index == 44:
        return 42
    elif row_index == 45:
        return 42
    elif row_index == 46:
        return 42
    elif row_index == 47:
        return 42
    elif row_index == 48:
        return 42
    elif row_index == 49:
        return 42
    elif row_index == 50:
        return 42
    elif row_index == 51:
        return 42
    elif row_index == 52:
        return 42
    elif row_index == 53:
        return 42
    elif row_index == 54:
        return 42
    elif row_index == 55:
        return 42
    elif row_index == 56:
        return 0
    elif row_index == 57:
        return 56
    elif row_index == 58:
        return 56
    elif row_index == 59:
        return 56
    elif row_index == 60:
        return 56
    elif row_index == 61:
        return 56
    elif row_index == 62:
        return 56
    elif row_index == 63:
        return 56
    elif row_index == 64:
        return 56
    elif row_index == 65:
        return 56
    elif row_index == 66:
        return 56
    elif row_index == 67:
        return 56
    elif row_index == 68:
        return 56
    elif row_index == 69:
        return 56
    elif row_index == 70:
        return 0
    elif row_index == 71:
        return 70
    elif row_index == 72:
        return 70
    elif row_index == 73:
        return 70
    elif row_index == 74:
        return 70
    elif row_index == 75:
        return 70
    elif row_index == 76:
        return 70
    elif row_index == 77:
        return 70
    elif row_index == 78:
        return 70
    elif row_index == 79:
        return 70
    elif row_index == 80:
        return 70
    elif row_index == 81:
        return 70
    elif row_index == 82:
        return 70
    elif row_index == 83:
        return 70
    else:
        return None


def build_type_parent_index_3(row):
    row_index = row.name

    if row_index == 0:
        return -1
    elif row_index == 1:
        return 0
    elif row_index == 2:
        return 0
    elif row_index == 3:
        return 0
    elif row_index == 4:
        return 0
    elif row_index == 5:
        return 0
    elif row_index == 6:
        return 0
    elif row_index == 7:
        return -1
    elif row_index == 8:
        return 7
    elif row_index == 9:
        return 7
    elif row_index == 10:
        return 7
    elif row_index == 11:
        return 7
    elif row_index == 12:
        return 7
    elif row_index == 13:
        return 7
    elif row_index == 14:
        return -1
    elif row_index == 15:
        return 14
    elif row_index == 16:
        return 14
    elif row_index == 17:
        return 14
    elif row_index == 18:
        return 14
    elif row_index == 19:
        return 14
    elif row_index == 20:
        return 14
    else:
        return None


def build_type_parent_index_4(row):
    row_index = row.name

    if row_index == 0:
        return -1
    elif row_index == 1:
        return 0
    elif row_index == 2:
        return 0
    elif row_index == 3:
        return 0
    elif row_index == 4:
        return 0
    elif row_index == 5:
        return 0
    elif row_index == 6:
        return 0
    elif row_index == 7:
        return -1
    elif row_index == 8:
        return 7
    elif row_index == 9:
        return 7
    elif row_index == 10:
        return 7
    elif row_index == 11:
        return 7
    elif row_index == 12:
        return 7
    elif row_index == 13:
        return 7
    elif row_index == 14:
        return -1
    elif row_index == 15:
        return 14
    elif row_index == 16:
        return 14
    elif row_index == 17:
        return 14
    elif row_index == 18:
        return 14
    elif row_index == 19:
        return 14
    elif row_index == 20:
        return 14
    else:
        return None


def build_type_parent_index_5_6(row):
    row_index = row.name

    if row_index == 0:
        return -1
    elif row_index == 1:
        return 0
    elif row_index == 2:
        return 0
    elif row_index == 3:
        return 0
    elif row_index == 4:
        return 0
    elif row_index == 5:
        return 0
    elif row_index == 6:
        return 0
    elif row_index == 7:
        return 0
    elif row_index == 8:
        return 0
    elif row_index == 9:
        return 0
    elif row_index == 10:
        return 0
    elif row_index == 11:
        return 0
    elif row_index == 12:
        return 0
    elif row_index == 13:
        return -1
    elif row_index == 14:
        return 13
    elif row_index == 15:
        return 13
    elif row_index == 16:
        return 13
    elif row_index == 17:
        return 13
    elif row_index == 18:
        return 13
    elif row_index == 19:
        return 13
    elif row_index == 20:
        return -1
    elif row_index == 21:
        return 20
    elif row_index == 22:
        return 20
    elif row_index == 23:
        return 20
    elif row_index == 24:
        return 20
    elif row_index == 25:
        return 20
    elif row_index == 26:
        return 20
    else:
        return None


def build_type_parent_index_7(row):
    row_index = row.name

    if row_index == 0:
        return -1
    elif row_index == 1:
        return 0
    elif row_index == 2:
        return 0
    elif row_index == 3:
        return 0
    elif row_index == 4:
        return 0
    elif row_index == 5:
        return 0
    elif row_index == 6:
        return 0
    elif row_index == 7:
        return -1
    elif row_index == 8:
        return 7
    elif row_index == 9:
        return 7
    elif row_index == 10:
        return 7
    elif row_index == 11:
        return 7
    elif row_index == 12:
        return 7
    elif row_index == 13:
        return 7
    elif row_index == 14:
        return -1
    elif row_index == 15:
        return 14
    elif row_index == 16:
        return 14
    elif row_index == 17:
        return 14
    elif row_index == 18:
        return 14
    elif row_index == 19:
        return 14
    elif row_index == 20:
        return 14
    else:
        return 999


#
# Helpers
#

def build_engine(source_file_extension):
    return "openpyxl" if source_file_extension == ".xlsx" else None


def write_csv_file(dataframe, file_path, quiet):
    if dataframe.shape[0] > 0:
        dataframe.to_csv(file_path, index=False)
        if not quiet:
            print(f"✓ Convert {os.path.basename(file_path)}")
    else:
        if not quiet:
            print(dataframe.head())
            print(f"✗️ Empty {os.path.basename(file_path)}")
