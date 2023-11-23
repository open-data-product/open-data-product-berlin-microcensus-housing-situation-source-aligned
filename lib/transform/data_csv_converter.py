import os
import re

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

            year = re.search(r"\b\d{4}\b", file_name).group()

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
            convert_file_to_csv_apartments_by_usage_type_year_of_construction_collective_heating_and_energy_type(
                source_file_path, clean=clean, quiet=quiet)
            convert_file_to_csv_apartments_by_usage_type_building_size_heating_and_energy_type(
                source_file_path, clean=clean, quiet=quiet)
            convert_file_to_csv_households_by_structure_and_usage_type(
                source_file_path, clean=clean, quiet=quiet)
            convert_file_to_csv_households_in_buildings_with_living_space_by_structure_and_usage_type(
                source_file_path, clean=clean, quiet=quiet)

            convert_file_to_csv_apartments_in_residential_buildings_by_district_occupancy_and_living_area(
                source_file_path, year, clean=clean, quiet=quiet)
            convert_file_to_csv_apartments_in_residential_buildings_by_district_year_of_construction_and_usage_type(
                source_file_path, year, clean=clean, quiet=quiet)
            convert_file_to_csv_apartments_in_residential_buildings_by_district_usage_type_living_area_and_occupancy(
                source_file_path, year, clean=clean, quiet=quiet)
            convert_file_to_csv_inhabited_apartments_in_residential_buildings_by_district_and_building_type(
                source_file_path, year, clean=clean, quiet=quiet)
            convert_file_to_csv_apartments_in_residential_buildings_by_district_and_living_area(
                source_file_path, year, clean=clean, quiet=quiet)
            convert_file_to_csv_apartments_in_residential_buildings_by_district_and_gross_rent(
                source_file_path, year, clean=clean, quiet=quiet)
            convert_file_to_csv_apartments_in_residential_buildings_by_district_and_gross_rent_per_sqm(
                source_file_path, year, clean=clean, quiet=quiet)
            convert_file_to_csv_main_tenant_households_in_residential_buildings_by_district_and_rental_burden(
                source_file_path, year, clean=clean, quiet=quiet)


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

        dataframe.at[dataframe[dataframe["type"] == "Insgesamt"].first_valid_index(), "type"] = "total"
        dataframe.at[dataframe[dataframe["type"] == "Zusammen"].first_valid_index(), "type"] = "condominiums"
        dataframe.at[dataframe[dataframe["type"] == "Zusammen"].first_valid_index(), "type"] = "rented_apartments"

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

        dataframe.at[dataframe[dataframe["type"] == "Insgesamt"].first_valid_index(), "type"] = "apartments"
        dataframe.at[dataframe[dataframe["type"] == "Zusammen"].first_valid_index(), "type"] = "condominiums"
        dataframe.at[dataframe[dataframe["type"] == "Zusammen"].first_valid_index(), "type"] = "rented_apartments"

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

        dataframe.at[dataframe[dataframe["type"] == "Insgesamt"].first_valid_index(), "type"] = "total"
        dataframe.at[dataframe[dataframe["type"] == "Zusammen"].first_valid_index(), "type"] = "build_before_1949"
        dataframe.at[dataframe[dataframe["type"] == "Zusammen"].first_valid_index(), "type"] = "build_after_1949"

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

        dataframe.at[dataframe[dataframe["type"] == "Insgesamt"].first_valid_index(), "type"] = "total"
        dataframe.at[dataframe[dataframe["type"] == "Zusammen"].first_valid_index(), "type"] = "build_before_1949"
        dataframe.at[dataframe[dataframe["type"] == "Zusammen"].first_valid_index(), "type"] = "build_after_1949"

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

        dataframe.at[dataframe[dataframe["type"] == "Insgesamt"].first_valid_index(), "type"] = "total"
        dataframe.at[dataframe[dataframe["type"] == "Zusammen"].first_valid_index(), "type"] = "condominiums"
        dataframe.at[dataframe[dataframe["type"] == "Zusammen"].first_valid_index(), "type"] = "rented_apartments"

        # Write csv file
        write_csv_file(dataframe, file_path_csv, quiet)
    except Exception as e:
        print(f"✗️ Exception: {str(e)}")


def convert_file_to_csv_apartments_by_usage_type_year_of_construction_collective_heating_and_energy_type(
        source_file_path, clean=False, quiet=False):
    source_file_name, source_file_extension = os.path.splitext(source_file_path)
    file_path_csv = f"{source_file_name}-8-apartments-by_usage-type-year-of-construction-collective-heating-and-energy-type.csv"

    # Check if result needs to be generated
    if not clean and os.path.exists(file_path_csv):
        if not quiet:
            print(f"✓ Already exists {os.path.basename(file_path_csv)}")
        return

    # Determine engine
    engine = build_engine(source_file_extension)

    try:
        # Iterate over sheets
        sheet = "Tab 8"
        skiprows = 8
        names = ["type", "apartments", "apartments_with_collective_heating", "district_heating", "gas", "electricity",
                 "heating_oil", "briquettes_lignite_coal_coke_hard_coal", "wood_or_other_renewable_renewable_energies"]
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
            .assign(type_parent_index=lambda df: df.apply(lambda row: build_type_parent_index_8(row), axis=1)) \
            .fillna(-1) \
            .assign(type_parent_index=lambda df: df["type_parent_index"].astype(int))
        dataframe.insert(0, "type_index", dataframe.pop("type_index"))
        dataframe.insert(1, "type_parent_index", dataframe.pop("type_parent_index"))

        dataframe.at[dataframe[dataframe["type"] == "Insgesamt"].first_valid_index(), "type"] = "total"
        dataframe.at[dataframe[dataframe["type"] == "Zusammen"].first_valid_index(), "type"] = "condominiums"
        dataframe.at[dataframe[dataframe["type"] == "Zusammen"].first_valid_index(), "type"] = "rented_apartments"

        # Write csv file
        write_csv_file(dataframe, file_path_csv, quiet)
    except Exception as e:
        print(f"✗️ Exception: {str(e)}")


def convert_file_to_csv_apartments_by_usage_type_building_size_heating_and_energy_type(
        source_file_path, clean=False, quiet=False):
    source_file_name, source_file_extension = os.path.splitext(source_file_path)
    file_path_csv = f"{source_file_name}-9-apartments-by_usage-type-building-size-heating-and-energy-type.csv"

    # Check if result needs to be generated
    if not clean and os.path.exists(file_path_csv):
        if not quiet:
            print(f"✓ Already exists {os.path.basename(file_path_csv)}")
        return

    # Determine engine
    engine = build_engine(source_file_extension)

    try:
        # Iterate over sheets
        sheet = "Tab 9"
        skiprows = 9
        names = ["type", "apartments", "apartments_with_collective_heating", "district_heating", "central_heating",
                 "floor_heating", "singles_or_more_space_ovens"]
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
            .assign(type_parent_index=lambda df: df.apply(lambda row: build_type_parent_index_9(row), axis=1)) \
            .fillna(-1) \
            .assign(type_parent_index=lambda df: df["type_parent_index"].astype(int))
        dataframe.insert(0, "type_index", dataframe.pop("type_index"))
        dataframe.insert(1, "type_parent_index", dataframe.pop("type_parent_index"))

        dataframe.at[dataframe[dataframe["type"] == "Insgesamt"].first_valid_index(), "type"] = "total"
        dataframe.at[dataframe[dataframe["type"] == "Zusammen"].first_valid_index(), "type"] = "condominiums"
        dataframe.at[dataframe[dataframe["type"] == "Zusammen"].first_valid_index(), "type"] = "rented_apartments"

        # Write csv file
        write_csv_file(dataframe, file_path_csv, quiet)
    except Exception as e:
        print(f"✗️ Exception: {str(e)}")


def convert_file_to_csv_households_by_structure_and_usage_type(source_file_path, clean=False, quiet=False):
    source_file_name, source_file_extension = os.path.splitext(source_file_path)
    file_path_csv = f"{source_file_name}-10-households-by-structure-and-usage-type.csv"

    # Check if result needs to be generated
    if not clean and os.path.exists(file_path_csv):
        if not quiet:
            print(f"✓ Already exists {os.path.basename(file_path_csv)}")
        return

    # Determine engine
    engine = build_engine(source_file_extension)

    try:
        # Iterate over sheets
        sheet = "Tab 10"
        skiprows = 5
        names = ["household_structure", "households", "owners", "owners_percentage", "main_tenants",
                 "main_tenants_percentage", "subtenants", "subtenants_percentage"]
        drop_columns = []

        dataframe = pd.read_excel(source_file_path, engine=engine, sheet_name=sheet, skiprows=skiprows, names=names,
                                  index_col=False) \
            .drop(columns=drop_columns, errors="ignore") \
            .replace("–", 0) \
            .replace("/", 0) \
            .dropna() \
            .assign(household_structure=lambda df: df["household_structure"].apply(lambda row: build_type_name(row)))

        dataframe.reset_index(drop=True, inplace=True)
        dataframe = dataframe.assign(type_index=lambda df: df.index) \
            .assign(type_parent_index=lambda df: df.apply(lambda row: build_type_parent_index_10(row), axis=1)) \
            .fillna(-1) \
            .assign(type_parent_index=lambda df: df["type_parent_index"].astype(int))
        dataframe.insert(0, "type_index", dataframe.pop("type_index"))
        dataframe.insert(1, "type_parent_index", dataframe.pop("type_parent_index"))

        # Write csv file
        write_csv_file(dataframe, file_path_csv, quiet)
    except Exception as e:
        print(f"✗️ Exception: {str(e)}")


def convert_file_to_csv_households_in_buildings_with_living_space_by_structure_and_usage_type(source_file_path,
                                                                                              clean=False, quiet=False):
    source_file_name, source_file_extension = os.path.splitext(source_file_path)
    file_path_csv = f"{source_file_name}-11-households-in-buildings-with-living-space-by-structure-and-usage-type.csv"

    # Check if result needs to be generated
    if not clean and os.path.exists(file_path_csv):
        if not quiet:
            print(f"✓ Already exists {os.path.basename(file_path_csv)}")
        return

    # Determine engine
    engine = build_engine(source_file_extension)

    try:
        # Iterate over sheets
        sheet = "Tab 11"
        skiprows = 6
        names = ["household_structure", "households", "residential_buildings_with_1_apartment",
                 "residential_buildings_with_2_apartments", "residential_buildings_with_3_apartments_or_more"]
        drop_columns = []

        dataframe = pd.read_excel(source_file_path, engine=engine, sheet_name=sheet, skiprows=skiprows, names=names,
                                  index_col=False) \
            .drop(columns=drop_columns, errors="ignore") \
            .replace("–", 0) \
            .replace("/", 0) \
            .dropna() \
            .assign(household_structure=lambda df: df["household_structure"].apply(lambda row: build_type_name(row)))

        dataframe.reset_index(drop=True, inplace=True)
        dataframe = dataframe.assign(type_index=lambda df: df.index) \
            .assign(type_parent_index=lambda df: df.apply(lambda row: build_type_parent_index_11(row), axis=1)) \
            .fillna(-1) \
            .assign(type_parent_index=lambda df: df["type_parent_index"].astype(int))
        dataframe.insert(0, "type_index", dataframe.pop("type_index"))
        dataframe.insert(1, "type_parent_index", dataframe.pop("type_parent_index"))

        # Write csv file
        write_csv_file(dataframe, file_path_csv, quiet)
    except Exception as e:
        print(f"✗️ Exception: {str(e)}")


def convert_file_to_csv_apartments_in_residential_buildings_by_district_occupancy_and_living_area(source_file_path,
                                                                                                  year,
                                                                                                  clean=False,
                                                                                                  quiet=False):
    tab_index = 19 if int(year) <= 2014 else 23

    source_file_name, source_file_extension = os.path.splitext(source_file_path)
    file_path_csv = f"{source_file_name}-{tab_index}-apartments-in-residential-buildings-by-district-occupancy-and-living-area.csv"

    # Check if result needs to be generated
    if not clean and os.path.exists(file_path_csv):
        if not quiet:
            print(f"✓ Already exists {os.path.basename(file_path_csv)}")
        return

    # Determine engine
    engine = build_engine(source_file_extension)

    try:
        # Iterate over sheets
        sheet = f"Tab {tab_index}"
        skiprows = 7
        names = ["district_name", "apartments", "uninhabited_apartments", "inhabited_apartments",
                 "inhabited_apartments_living_area", "inhabited_apartments_living_area_per_apartment",
                 "inhabited_apartments_living_area_per_person", "inhabited_apartments_persons_per_apartment"]
        drop_columns = []

        dataframe = pd.read_excel(source_file_path, engine=engine, sheet_name=sheet, skiprows=skiprows, names=names,
                                  index_col=False) \
            .drop(columns=drop_columns, errors="ignore") \
            .replace("-", 0) \
            .replace("…", None) \
            .replace("–", 0) \
            .replace("—", 0) \
            .assign(district_id=lambda df: df["district_name"].apply(lambda row: build_district_id(row))) \
            .head(12) \
            .drop("district_name", axis=1) \
            .astype(str) \
            .apply(lambda x: x.str.replace('"', '')) \
            .apply(lambda x: x.str.replace(',', '.')) \
            .apply(lambda x: x.str.replace('— ', '-')) \
            .apply(lambda x: x.str.replace('– ', '-'))

        dataframe.reset_index(drop=True, inplace=True)
        dataframe.insert(0, "district_id", dataframe.pop("district_id"))

        # Write csv file
        write_csv_file(dataframe, file_path_csv, quiet)
    except Exception as e:
        print(f"✗️ Exception: {str(e)}")


def convert_file_to_csv_apartments_in_residential_buildings_by_district_year_of_construction_and_usage_type(
        source_file_path, year, clean=False, quiet=False):
    tab_index = 20 if int(year) <= 2014 else 24

    types = ["total", "before-1948", "1949-and-later", "_"]
    for type_index, type in enumerate(types):

        if type == "_":
            continue

        source_file_name, source_file_extension = os.path.splitext(source_file_path)
        file_path_csv = f"{source_file_name}-{tab_index}-apartments-in-residential-buildings-by-district-year-of-construction-and-usage-type-{type}.csv"

        # Check if result needs to be generated
        if not clean and os.path.exists(file_path_csv):
            if not quiet:
                print(f"✓ Already exists {os.path.basename(file_path_csv)}")
            return

        # Determine engine
        engine = build_engine(source_file_extension)

        try:
            # Iterate over sheets
            sheet = f"Tab {tab_index}"
            skiprows = 6
            names = ["district_id", "apartments", "inhabited_by_owner", "inhabited_by_owner_percentage", "rented_out",
                     "rented_out_percentage"]
            drop_columns = []

            dataframe = pd.read_excel(source_file_path, engine=engine, sheet_name=sheet, skiprows=skiprows, names=names,
                                      index_col=False) \
                            .drop(columns=drop_columns, errors="ignore") \
                            .iloc[type_index::len(types)] \
                .head(12) \
                .replace("/", 0)

            dataframe.reset_index(drop=True, inplace=True)
            dataframe = dataframe.assign(
                district_id=lambda df: df.apply(lambda row: str(row.name + 1).zfill(2), axis=1))

            # Write csv file
            write_csv_file(dataframe, file_path_csv, quiet)
        except Exception as e:
            print(f"✗️ Exception: {str(e)}")


def convert_file_to_csv_apartments_in_residential_buildings_by_district_usage_type_living_area_and_occupancy(
        source_file_path, year, clean=False, quiet=False):
    tab_index = 21 if int(year) <= 2014 else 25

    types = ["total", "owners-apartments", "rental-apartments", "_"]
    for type_index, type in enumerate(types):

        if type == "_":
            continue

        source_file_name, source_file_extension = os.path.splitext(source_file_path)
        file_path_csv = f"{source_file_name}-{tab_index}-apartments-in-residential-buildings-by-district-usage-type-living-area-and-occupancy-{type}.csv"

        # Check if result needs to be generated
        if not clean and os.path.exists(file_path_csv):
            if not quiet:
                print(f"✓ Already exists {os.path.basename(file_path_csv)}")
            return

        # Determine engine
        engine = build_engine(source_file_extension)

        try:
            # Iterate over sheets
            sheet = f"Tab {tab_index}"
            skiprows = 6
            names = ["district_id", "apartments", "living_area", "living_area_per_apartment", "persons_per_apartment",
                     "living_area_per_person"]
            drop_columns = []

            dataframe = pd.read_excel(source_file_path, engine=engine, sheet_name=sheet, skiprows=skiprows, names=names,
                                      index_col=False) \
                            .drop(columns=drop_columns, errors="ignore") \
                            .iloc[type_index::len(types)] \
                .head(12) \
                .replace("/", 0)

            dataframe.reset_index(drop=True, inplace=True)
            dataframe = dataframe.assign(
                district_id=lambda df: df.apply(lambda row: str(row.name + 1).zfill(2), axis=1))

            # Write csv file
            write_csv_file(dataframe, file_path_csv, quiet)
        except Exception as e:
            print(f"✗️ Exception: {str(e)}")


def convert_file_to_csv_inhabited_apartments_in_residential_buildings_by_district_and_building_type(
        source_file_path, year, clean=False, quiet=False):
    if int(year) <= 2014:
        print(f"⚠ Does exist in year {year}")
        return
    tab_index = 26

    source_file_name, source_file_extension = os.path.splitext(source_file_path)
    file_path_csv = f"{source_file_name}-{tab_index}-apartments-in-residential-buildings-by-district-and-building-type.csv"

    # Check if result needs to be generated
    if not clean and os.path.exists(file_path_csv):
        if not quiet:
            print(f"✓ Already exists {os.path.basename(file_path_csv)}")
        return

    # Determine engine
    engine = build_engine(source_file_extension)

    try:
        # Iterate over sheets
        sheet = f"Tab {tab_index}"
        skiprows = 7
        names = ["district_name", "apartments", "single_family_houses", "single_family_houses_detached",
                 "single_family_houses_semi_detached", "single_family_houses_terraced", "multi_family_houses",
                 "multi_family_houses_detached", "multi_family_houses_terraced"]
        drop_columns = []

        dataframe = pd.read_excel(source_file_path, engine=engine, sheet_name=sheet, skiprows=skiprows, names=names,
                                  index_col=False) \
            .drop(columns=drop_columns, errors="ignore") \
            .replace("/", 0) \
            .assign(district_id=lambda df: df["district_name"].apply(lambda row: build_district_id(row))) \
            .head(12) \
            .drop("district_name", axis=1)

        dataframe.reset_index(drop=True, inplace=True)
        dataframe = dataframe.assign(
            district_id=lambda df: df.apply(lambda row: str(row.name + 1).zfill(2), axis=1))

        dataframe.reset_index(drop=True, inplace=True)
        dataframe.insert(0, "district_id", dataframe.pop("district_id"))

        # Write csv file
        write_csv_file(dataframe, file_path_csv, quiet)
    except Exception as e:
        print(f"✗️ Exception: {str(e)}")


def convert_file_to_csv_apartments_in_residential_buildings_by_district_and_living_area(
        source_file_path, year, clean=False, quiet=False):
    tab_index = 22 if int(year) <= 2014 else 28
    sheet = "Tab 22-23" if int(year) <= 2014 else "Tab 28-29"

    source_file_name, source_file_extension = os.path.splitext(source_file_path)
    file_path_csv = f"{source_file_name}-{tab_index}-apartments-in-residential-buildings-by-district-and-living-area.csv"

    # Check if result needs to be generated
    if not clean and os.path.exists(file_path_csv):
        if not quiet:
            print(f"✓ Already exists {os.path.basename(file_path_csv)}")
        return

    # Determine engine
    engine = build_engine(source_file_extension)

    try:
        # Iterate over sheets
        sheet = sheet
        skiprows = 7
        names = ["district_name", "apartments", "living_area_below_40sqm", "living_area_between_40_and_60sqm",
                 "living_area_between_60_and_80sqm", "living_area_between_80_and_100sqm",
                 "living_area_between_100_and_120sqm", "living_area_between_above_120sqm"]
        drop_columns = []

        dataframe = pd.read_excel(source_file_path, engine=engine, sheet_name=sheet, skiprows=skiprows, names=names,
                                  index_col=False) \
            .drop(columns=drop_columns, errors="ignore") \
            .replace("/", 0) \
            .assign(district_id=lambda df: df["district_name"].apply(lambda row: build_district_id(row))) \
            .head(12) \
            .drop("district_name", axis=1)

        dataframe.reset_index(drop=True, inplace=True)
        dataframe = dataframe.assign(
            district_id=lambda df: df.apply(lambda row: str(row.name + 1).zfill(2), axis=1))

        dataframe.reset_index(drop=True, inplace=True)
        dataframe.insert(0, "district_id", dataframe.pop("district_id"))

        # Write csv file
        write_csv_file(dataframe, file_path_csv, quiet)
    except Exception as e:
        print(f"✗️ Exception: {str(e)}")


def convert_file_to_csv_apartments_in_residential_buildings_by_district_and_gross_rent(
        source_file_path, year, clean=False, quiet=False):
    tab_index = 23 if int(year) <= 2014 else 29
    sheet = "Tab 22-23" if int(year) <= 2014 else "Tab 28-29"

    source_file_name, source_file_extension = os.path.splitext(source_file_path)
    file_path_csv = f"{source_file_name}-{tab_index}-apartments-in-residential-buildings-by-district-and-gross-rent.csv"

    # Check if result needs to be generated
    if not clean and os.path.exists(file_path_csv):
        if not quiet:
            print(f"✓ Already exists {os.path.basename(file_path_csv)}")
        return

    # Determine engine
    engine = build_engine(source_file_extension)

    try:
        # Iterate over sheets
        sheet = sheet
        skiprows = 34
        names = ["district_name", "apartments", "gross_rent_below_300_euros", "gross_rent_between_300_and_400_euros",
                 "gross_rent_between_400_and_500_euros", "gross_rent_between_500_and_600_euros",
                 "gross_rent_above_600_euros", "average_gross_rent"]
        drop_columns = []

        dataframe = pd.read_excel(source_file_path, engine=engine, sheet_name=sheet, skiprows=skiprows, names=names,
                                  index_col=False) \
            .drop(columns=drop_columns, errors="ignore") \
            .replace("/", 0) \
            .assign(district_id=lambda df: df["district_name"].apply(lambda row: build_district_id(row))) \
            .head(12) \
            .drop("district_name", axis=1)

        dataframe.reset_index(drop=True, inplace=True)
        dataframe = dataframe.assign(
            district_id=lambda df: df.apply(lambda row: str(row.name + 1).zfill(2), axis=1))

        dataframe.reset_index(drop=True, inplace=True)
        dataframe.insert(0, "district_id", dataframe.pop("district_id"))

        # Write csv file
        write_csv_file(dataframe, file_path_csv, quiet)
    except Exception as e:
        print(f"✗️ Exception: {str(e)}")


def convert_file_to_csv_apartments_in_residential_buildings_by_district_and_gross_rent_per_sqm(
        source_file_path, year, clean=False, quiet=False):
    tab_index = 24 if int(year) <= 2014 else 30

    source_file_name, source_file_extension = os.path.splitext(source_file_path)
    file_path_csv = f"{source_file_name}-{tab_index}-apartments-in-residential-buildings-by-district-and-gross-rent-per-sqm.csv"

    # Check if result needs to be generated
    if not clean and os.path.exists(file_path_csv):
        if not quiet:
            print(f"✓ Already exists {os.path.basename(file_path_csv)}")
        return

    # Determine engine
    engine = build_engine(source_file_extension)

    try:
        # Iterate over sheets
        sheet = f"Tab {tab_index}"
        skiprows = 8
        names = ["district_name", "apartments", "gross_rent_per_sqm_below_6_euros",
                 "gross_rent_per_sqm_between_6_and_7_euros",
                 "gross_rent_per_sqm_between_7_and_8_euros", "gross_rent_between_per_sqm_8_and_9_euros",
                 "gross_rent_per_sqm_above_9_euros", "average_gross_rent_per_sqm"]
        drop_columns = []

        dataframe = pd.read_excel(source_file_path, engine=engine, sheet_name=sheet, skiprows=skiprows, names=names,
                                  index_col=False) \
            .drop(columns=drop_columns, errors="ignore") \
            .replace("/", 0) \
            .assign(district_id=lambda df: df["district_name"].apply(lambda row: build_district_id(row))) \
            .head(12) \
            .drop("district_name", axis=1)

        dataframe.reset_index(drop=True, inplace=True)
        dataframe = dataframe.assign(
            district_id=lambda df: df.apply(lambda row: str(row.name + 1).zfill(2), axis=1))

        dataframe.reset_index(drop=True, inplace=True)
        dataframe.insert(0, "district_id", dataframe.pop("district_id"))

        # Write csv file
        write_csv_file(dataframe, file_path_csv, quiet)
    except Exception as e:
        print(f"✗️ Exception: {str(e)}")


def convert_file_to_csv_main_tenant_households_in_residential_buildings_by_district_and_rental_burden(
        source_file_path, year, clean=False, quiet=False):
    tab_index = 25 if int(year) <= 2014 else 31

    source_file_name, source_file_extension = os.path.splitext(source_file_path)
    file_path_csv = f"{source_file_name}-{tab_index}-main-tenant-households-in-residential-buildings-by-district-and-rental-burden.csv"

    # Check if result needs to be generated
    if not clean and os.path.exists(file_path_csv):
        if not quiet:
            print(f"✓ Already exists {os.path.basename(file_path_csv)}")
        return

    # Determine engine
    engine = build_engine(source_file_extension)

    try:
        # Iterate over sheets
        sheet = f"Tab {tab_index}"
        skiprows = 8
        names = ["district_name", "total", "percentage_of_household_net_income_below_15%",
                 "percentage_of_household_net_income_between_15_and_25%",
                 "percentage_of_household_net_income_between_25_and_35%",
                 "percentage_of_household_net_income_between_35_and_45%",
                 "percentage_of_household_net_income_above_45%", "average_percentage_of_household_net_income"]
        drop_columns = []

        dataframe = pd.read_excel(source_file_path, engine=engine, sheet_name=sheet, skiprows=skiprows, names=names,
                                  index_col=False) \
            .drop(columns=drop_columns, errors="ignore") \
            .replace("/", 0) \
            .assign(district_id=lambda df: df["district_name"].apply(lambda row: build_district_id(row))) \
            .head(12) \
            .drop("district_name", axis=1)

        dataframe.reset_index(drop=True, inplace=True)
        dataframe = dataframe.assign(
            district_id=lambda df: df.apply(lambda row: str(row.name + 1).zfill(2), axis=1))

        dataframe.reset_index(drop=True, inplace=True)
        dataframe.insert(0, "district_id", dataframe.pop("district_id"))

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

    elif value == "Privatperson(en)":
        return "private_individuals"
    elif value == "privatwirtschaftliches Unternehmen":
        return "private_company"
    elif value == "öffentliche Einrichtung":
        return "public_institution"
    elif value == "Wohnungs-/Baugenossenschaft":
        return "housing_building_cooperative"

    elif value == "Haushalte":
        return "households"
    elif value == "mit 1 Person":
        return "with_1_person"
    elif value == "darunter weiblich":
        return "female"
    elif value == "mit 2 Personen":
        return "with_2_persons"
    elif value == "mit 3 Personen":
        return "with_3_persons"
    elif value == "mit 4 Personen":
        return "with_4_persons"
    elif value == "mit 5 und mehr Personen":
        return "with_5_persons_or_more"
    elif value == "mit Kindern unter 18 Jahren":
        return "with_children_below_18"
    elif value == "mit 1 Kind":
        return "with_1_child"
    elif value == "mit 2 Kindern":
        return "with_2_children"
    elif value == "mit 3 Kindern":
        return "with_3_children"
    elif value == "mit 4 und mehr Kindern":
        return "with_4_children_or_more"
    elif value == "ohne Kinder unter 18 Jahren":
        return "without_children_below_18"
    elif value == "unter 700":
        return "net_household_income_below_700_euros"
    elif value == "700  –     900":
        return "net_household_income_between_700_and_900_euros"
    elif value == "900  –  1 100":
        return "net_household_income_between_900_and_1100_euros"
    elif value == "1 100  –  1 300":
        return "net_household_income_between_1100_and_1300_euros"
    elif value == "1 300  –  1 500":
        return "net_household_income_between_1300_and_1500_euros"
    elif value == "1 500  –  2 000":
        return "net_household_income_between_1500_and_2000_euros"
    elif value == "2 000  –  3 200":
        return "net_household_income_between_2000_and_3200_euros"
    elif value == "3 200  –  4 500":
        return "net_household_income_between_3200_and_4500_euros"
    elif value == "4 500  –  6 000":
        return "net_household_income_between_4500_and_6000_euros"
    elif value == "6 000  –  7 500":
        return "net_household_income_between_6000_and_7500_euros"
    elif value == "7 500 und mehr":
        return "net_household_income_above_7500_euros"
    elif value == "1 Einkommensbezieher":
        return "with_1_income_earner"
    elif value == "2 und mehr Einkommensbezieher":
        return "with_2_income_earner_or_more"
    elif value == "Erwerbspersonen":
        return "employable_persons"
    elif value == "Erwerbstätige":
        return "employed_persons"
    elif value == "Selbstständige":
        return "self_employed"
    elif value == "Beamte":
        return "civil_servants"
    elif value == "Angestellte":
        return "employed"
    elif value == "Arbeiter":
        return "workers"
    elif value == "Erwerbslose":
        return "unemployed_persons"
    elif value == "Nichterwerbspersonen":
        return "non_employable_persons"
    elif value == "darunter Rentner":
        return "pensioners"
    elif value == "unter 25":
        return "age_of_main_income_earner_below_25"
    elif value == "25 – 30":
        return "age_of_main_income_earner_between_25_and_30"
    elif value == "30 – 40":
        return "age_of_main_income_earner_between_30_and_40"
    elif value == "40 – 50":
        return "age_of_main_income_earner_between_40_and_50"
    elif value == "50 – 60":
        return "age_of_main_income_earner_between_50_and_60"
    elif value == "60 – 65":
        return "age_of_main_income_earner_between_60_and_65"
    elif value == "65 und mehr":
        return "age_of_main_income_earner_between_65_and_more"

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
        return None


def build_type_parent_index_8(row):
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
        return 13
    elif row_index == 21:
        return 13
    elif row_index == 22:
        return 13
    elif row_index == 23:
        return 13
    elif row_index == 24:
        return 13
    elif row_index == 25:
        return 13
    elif row_index == 26:
        return -1
    elif row_index == 27:
        return 26
    elif row_index == 28:
        return 26
    elif row_index == 29:
        return 26
    elif row_index == 30:
        return 26
    elif row_index == 31:
        return 26
    elif row_index == 32:
        return 26
    elif row_index == 33:
        return 26
    elif row_index == 34:
        return 26
    elif row_index == 35:
        return 26
    elif row_index == 36:
        return 26
    elif row_index == 37:
        return 26
    elif row_index == 38:
        return 26
    else:
        return None


def build_type_parent_index_9(row):
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
        return -1
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
    else:
        return None


def build_type_parent_index_10(row):
    row_index = row.name

    if row_index == 0:
        return -1
    elif row_index == 1:
        return 0
    elif row_index == 2:
        return 1
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
        return 0
    elif row_index == 13:
        return -1
    elif row_index == 14:
        return -1
    elif row_index == 15:
        return -1
    elif row_index == 16:
        return -1
    elif row_index == 17:
        return -1
    elif row_index == 18:
        return -1
    elif row_index == 19:
        return -1
    elif row_index == 20:
        return -1
    elif row_index == 21:
        return -1
    elif row_index == 22:
        return -1
    elif row_index == 23:
        return -1
    elif row_index == 24:
        return -1
    elif row_index == 25:
        return -1
    elif row_index == 26:
        return -1
    elif row_index == 27:
        return 26
    elif row_index == 28:
        return 27
    elif row_index == 29:
        return 27
    elif row_index == 30:
        return 27
    elif row_index == 31:
        return 27
    elif row_index == 32:
        return 26
    elif row_index == 33:
        return -1
    elif row_index == 34:
        return 33
    elif row_index == 35:
        return -1
    elif row_index == 36:
        return -1
    elif row_index == 37:
        return -1
    elif row_index == 38:
        return -1
    elif row_index == 39:
        return -1
    elif row_index == 40:
        return -1
    elif row_index == 41:
        return -1
    else:
        return None


def build_type_parent_index_11(row):
    row_index = row.name

    if row_index == 0:
        return -1
    elif row_index == 1:
        return 0
    elif row_index == 2:
        return 1
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
        return -1
    elif row_index == 10:
        return -1
    elif row_index == 11:
        return -1
    elif row_index == 12:
        return -1
    elif row_index == 13:
        return -1
    elif row_index == 14:
        return -1
    elif row_index == 15:
        return -1
    elif row_index == 16:
        return -1
    elif row_index == 17:
        return -1
    elif row_index == 18:
        return -1
    elif row_index == 19:
        return -1
    elif row_index == 20:
        return -1
    elif row_index == 21:
        return -1

    elif row_index == 22:
        return -1
    elif row_index == 23:
        return 22
    elif row_index == 24:
        return 23
    elif row_index == 25:
        return 23
    elif row_index == 26:
        return 23
    elif row_index == 27:
        return 23
    elif row_index == 28:
        return 23
    elif row_index == 29:
        return -1
    elif row_index == 30:
        return 29
    elif row_index == 31:
        return -1
    elif row_index == 32:
        return -1
    elif row_index == 33:
        return -1
    elif row_index == 34:
        return -1
    elif row_index == 35:
        return -1
    elif row_index == 36:
        return -1
    elif row_index == 37:
        return -1
    else:
        return None


def build_district_id(value):
    value = str(value).lstrip().rstrip() \
        .replace(" ", "") \
        .replace("—", "-") \
        .replace("–", "-")

    if value == "Mitte":
        return "01"
    elif value == "Friedrichshain-Kreuzberg":
        return "02"
    elif value == "Pankow":
        return "03"
    elif value == "Charlottenburg-Wilmersdorf":
        return "04"
    elif value == "Spandau":
        return "05"
    elif value == "Steglitz-Zehlendorf":
        return "06"
    elif value == "Tempelhof-Schöneberg":
        return "07"
    elif value == "Neukölln":
        return "08"
    elif value == "Treptow-Köpenick":
        return "09"
    elif value == "Marzahn-Hellersdorf":
        return "10"
    elif value == "Lichtenberg":
        return "11"
    elif value == "Reinickendorf":
        return "12"
    else:
        return None


def build_district_name_year_of_construction(value):
    return str(value).lstrip().rstrip() \
        .replace("bis 1948", "until 1948") \
        .replace("1949 und später", "1949 and later")


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
