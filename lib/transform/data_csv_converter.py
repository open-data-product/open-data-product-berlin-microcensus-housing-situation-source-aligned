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


def convert_file_to_csv_apartments_by_size_year_of_construction_and_usage(source_file_path, clean=False,
                                                                          quiet=False):
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
