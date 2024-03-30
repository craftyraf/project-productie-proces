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

    return segment_1, segment_2, segment_3, location, threshold_1, threshold_2
