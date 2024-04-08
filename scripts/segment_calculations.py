import json
from scipy.stats import norm, cauchy


def create_segments(location, threshold_1, threshold_2, df):
    """
    Maak segmenten op basis van locatie en productie drempelwaarden.

    Parameters:
        location (str): De locatiewaarde.
        threshold_1 (float): De eerste productiedrempel.
        threshold_2 (float): De tweede productiedrempel.
        df (DataFrame): De DataFrame met de gegevens.

    Returns:
        tuple: Een tuple met drie DataFrame segmenten.
    """
    # Segment 1: Geen onderhoud en productie < threshold_1 voor de opgegeven locatie
    segment_1 = df[
        (df['location'] == location) &
        (df['production'] < threshold_1)
        ]

    # Segment 2: Geen onderhoud, threshold 1 <= productie < threshold_2 voor de opgegeven locatie
    segment_2 = df[
        (df['location'] == location) &
        (df['production'] >= threshold_1) &
        (df['production'] < threshold_2)
        ]

    # Segment 3: Geen onderhoud en productie >= threshold_2 voor de opgegeven locatie
    segment_3 = df[
        (df['location'] == location) &
        (df['production'] >= threshold_2)
        ]

    total_days_location = len(df[df['location'] == location])

    # Calculate shares
    share_1 = round(len(segment_1) / total_days_location, 4)
    share_2 = round(len(segment_2) / total_days_location, 4)
    share_3 = round(len(segment_3) / total_days_location, 4)

    return share_1, share_2, share_3, segment_1, segment_2, segment_3


def print_segment_share(location, threshold_1, threshold_2, share_1, share_2, share_3):
    """
    Print the share of days per segment.

    Parameters:
        location (str): The location name.
        threshold_1 (float): The first threshold value.
        threshold_2 (float): The second threshold value.
        share_1 (float): The share of days with production < threshold_1.
        share_2 (float): The share of days with threshold_1 <= production < threshold_2.
        share_3 (float): The share of days with production >= threshold_2.

    Returns:
        None
    """
    print(f"{location}: % dagen met [productie < {threshold_1}]:", round(100 * share_1,2), '%')
    print(f"{location}: % dagen met [{threshold_1} <= productie < {threshold_2}]:", round(100 * share_2,2), '%')
    print(f"{location}: % dagen met [productie >= {threshold_2}]:", round(100 * share_3,2), '%')


def calculate_and_save_segments_values(location, threshold_1, threshold_2, share_1, segment_2, segment_3,
                                       share_2, share_3, filename):
    """
    Calculate segment values for Segment 2 and Segment 3 and save them to a JSON file.

    Parameters:
        location (str): The location for which the parameters are calculated.
        threshold_1 (float): Threshold value 1.
        threshold_2 (float): Threshold value 2.
        segment_2 (DataFrame): Data for Segment 2.
        segment_3 (DataFrame): Data for Segment 3.
        filename (str): The filename to save the results to.

    Returns:
        results (dict): Dictionary containing calculated parameters for each segment and distribution.
    """

    # Calculate segment values
    results = {}
    lower_bound_s2 = segment_2['production'].min()
    upper_bound_s2 = segment_2['production'].max()

    param1_s3, param2_s3 = norm.fit(segment_3['production'])

    results[location] = {
        'threshold_1': threshold_1,
        'threshold_2': threshold_2,
        'share_1': share_1,
        'share_2': share_2,
        'share_3': share_3,
        'lower_bound_s2': lower_bound_s2,
        'upper_bound_s2': upper_bound_s2,
        'param1_s3': param1_s3,
        'param2_s3': param2_s3
    }

    # Save results to a JSON file
    with open(filename, 'w') as json_file:
        json.dump(results, json_file)

    return results
