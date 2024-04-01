import pandas as pd
import os
import json


def read_json_files(directory_path, location):
    """
    Functie om JSON-bestanden te lezen en DataFrame te maken

    Args:
        directory_path (str): Het pad naar de map met JSON-bestanden.
        location (str): De naam van de locatie om toe te voegen aan de 'location' kolom.

    Returns:
        pandas.DataFrame: Een DataFrame dat alle gegevens uit de JSON-bestanden bevat,
                          met een extra kolom 'location'.
    """
    dataframes = []
    for filename in os.listdir(directory_path):
        if filename.endswith(".json"):
            full_path = os.path.join(directory_path, filename)
            with open(full_path, 'r') as f:
                json_data = json.load(f)
                df = pd.DataFrame([json_data])
                df['location'] = location  # Voeg 'location' kolom toe met locatienaam
                dataframes.append(df)
    return pd.concat(dataframes, ignore_index=True)
