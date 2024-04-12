import pandas as pd
import os
import json


def read_json_files(directory_path, location):
    """
    Function to read JSON files and create DataFrame

    Args:
        directory_path (str): The path to the folder containing JSON files.
        location (str): The name of the location to add to the 'location' column.

    Returns:
        pandas.DataFrame: A DataFrame that contains all the data from the JSON files,
                          with an extra column 'location'.
    """
    dataframes = []
    for filename in os.listdir(directory_path):
        if filename.endswith(".json"):
            full_path = os.path.join(directory_path, filename)
            with open(full_path, 'r') as f:
                json_data = json.load(f)
                df = pd.DataFrame([json_data])
                df['location'] = location  # Add 'location' column
                dataframes.append(df)
    return pd.concat(dataframes, ignore_index=True)
