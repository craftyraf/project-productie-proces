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
    share_1 = round((len(segment_1) * 100) / total_days_location, 2)
    share_2 = round((len(segment_2) * 100) / total_days_location, 2)
    share_3 = round((len(segment_3) * 100) / total_days_location, 2)

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
    print(f"{location}: % dagen met [productie < {threshold_1}]:", share_1, '%')
    print(f"{location}: % dagen met [{threshold_1} <= productie < {threshold_2}]:", share_2, '%')
    print(f"{location}: % dagen met [productie >= {threshold_2}]:", share_3, '%')
