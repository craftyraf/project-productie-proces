import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from scipy.stats import cauchy

def horizontal_bar_chart(value_counts, chart_title, x_label, y_label):
    """
    Create a horizontal bar chart for the specified column in the DataFrame, with customizable title and labels.

    Parameters:
    - df: pandas DataFrame containing the data.
    - column_name: string, the name of the column for which to create the bar chart.
    - chart_title: string, the title of the chart.
    - x_label: string, the label for the x-axis.
    - y_label: string, the label for the y-axis.
    """

    # Set up the figure size
    plt.figure(figsize=(10, 6))

    # Plot a horizontal bar chart
    value_counts.plot(kind='barh')

    # Set the title and labels with the provided arguments
    plt.title(chart_title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    # Customize the axis and spines
    ax = plt.gca()  # Get current axis
    ax.xaxis.tick_top()  # Move the x-axis to the top
    ax.xaxis.set_label_position('top')  # Move the x-axis label to the top
    ax.spines['right'].set_visible(False)  # Remove the right spine
    ax.spines['bottom'].set_visible(False)  # Remove the bottom spine

    # Display the plot
    plt.show()


# Berekening van ECDF
def ecdf(data):
    """Bereken ECDF voor een 1D array van data."""
    n = len(data)
    x = np.sort(data)
    y = np.arange(1, n + 1) / n
    return x, y


def generate_point_distribution(segment_data, location, threshold_1, maximum):
    """
    Plot de puntverdeling voor een segment.

    Parameters:
        segment_data (DataFrame): Gegevens voor het segment.
        location (str): De locatienaam.
        threshold_1 (float): Drempelwaarde 1.

    Returns:
        None
    """

    # Set histogram parameters
    width = maximum / 25

    # Plot histogram
    xmin, xmax = plt.xlim()
    plt.xlim(xmin=0, xmax=maximum)
    plt.hist(segment_data, bins=1, density=True, alpha=0.6, color='g', width=width)

    # Set plot title and labels
    plt.title(f"{location} Productie < {threshold_1} (Puntwaarde)")
    plt.xlabel('Productie')
    plt.ylabel('Dichtheid')


def generate_uniform_distribution(segment_data, location, threshold_1, threshold_2, maximum):
    """
    Plot de uniforme verdeling voor een segment.

    Parameters:
        segment_data (DataFrame): Data voor het segment.
        location (str): De locatienaam.
        threshold_1 (float): Drempelwaarde 1.
        threshold_2 (float): Drempelwaarde 2.
        maximum (int): Maximale waarde voor de x-as.

    Returns:
        None
    """
    # Fit uniform distribution to the segment data
    mean_norm, std_norm = stats.uniform.fit(segment_data)

    # Plot histogram
    plt.hist(segment_data, bins=50, density=True, alpha=0.6, color='g', label='Histogram')

    # Set x-axis limits
    xmin, xmax = plt.xlim()
    plt.xlim(xmin=0, xmax=maximum)

    # Generate points for the uniform distribution
    x_norm = np.linspace(xmin, xmax, 100)
    p_norm = stats.uniform.pdf(x_norm, mean_norm, std_norm)

    # Plot uniform distribution
    plt.plot(x_norm, p_norm, 'k', linewidth=2, label='Uniforme verdeling')

    # Set plot title and labels
    plt.title(f"{threshold_1} <= {location} Productie < {threshold_2} (Uniforme verdeling)")
    plt.xlabel('Productie')
    plt.ylabel('Dichtheid')
    plt.legend()

    return xmin, xmax


def generate_normal_distribution(segment_data, location, threshold_2, maximum):
    """
    Genereer de normale verdeling voor een segment.

    Parameters:
        segment_data (DataFrame): Gegevens voor het segment.
        location (str): De locatienaam.
        threshold_2 (float): Drempelwaarde 2.

    Returns:
        None
    """
    # Fit normale verdeling aan de segmentgegevens
    mean_norm, std_norm = stats.norm.fit(segment_data)

    # Histogram plot voor het segment
    plt.hist(segment_data, bins=50, density=True, alpha=0.6, color='g', label='Histogram')

    # Stel x-as limieten in
    xmin, xmax = plt.xlim()
    plt.xlim(xmin=0, xmax=maximum)

    # Genereer punten voor de normale verdeling
    x_norm = np.linspace(xmin, xmax, 100)
    p_norm = stats.norm.pdf(x_norm, mean_norm, std_norm)

    # Plot normale verdeling
    plt.plot(x_norm, p_norm, 'k', linewidth=2, label='Normaalverdeling')

    # Stel plot titel en labels in
    plt.title(f"{location} Productie >= {threshold_2} (Normaalverdeling)")
    plt.xlabel('Productie')
    plt.ylabel('Dichtheid')
    plt.legend()

    return mean_norm, std_norm


def generate_cauchy_distribution(segment_data, location, threshold_2, maximum):
    """
    Genereer de Cauchy-verdeling voor een segment.

    Parameters:
        segment_data (DataFrame): Gegevens voor het segment.

    Returns:
        None
    """
    # Fit de Cauchy-verdeling aan de segmentgegevens
    loc, scale = cauchy.fit(segment_data)

    # Histogram plot voor de segmentgegevens
    plt.hist(segment_data, bins=50, density=True, alpha=0.6, color='g', label='Histogram')

    # Bepaal de x-limieten van de plot
    xmin, xmax = plt.xlim()
    plt.xlim(xmin=0, xmax=maximum)

    # Genereer punten voor de Cauchy-verdeling
    x = np.linspace(xmin, xmax, 100)
    p = cauchy.pdf(x, loc=loc, scale=scale)

    # Plot de Cauchy-verdeling
    plt.plot(x, p, 'k', linewidth=2, label='Cauchy verdeling')

    # Stel titel en labels in voor de plot
    plt.title(f"{location} Productie >= {threshold_2} (Cauchy verdeling)")
    plt.xlabel('Productie')
    plt.ylabel('Dichtheid')
    plt.legend()

    return loc, scale


def plot_segment_distributions(segment_1, distribution_1, segment_2, distribution_2, segment_3, distribution_3,
                               location, threshold_1, threshold_2, combined_df_cleaned):
    """
    Plot distributiesegmenten voor een bepaalde locatie.

    Parameters:
        segment_1 (DataFrame): DataFrame met gegevens voor segment 1.
        segment_2 (DataFrame): DataFrame met gegevens voor segment 2.
        segment_3 (DataFrame): DataFrame met gegevens voor segment 3.
        locatie (str): De locatie waarvoor distributies worden geplot.
        drempel_1 (float): Drempelwaarde tussen segmenten 1 en 2.
        drempel_2 (float): Drempelwaarde tussen segmenten 2 en 3.
        gecombineerd_df_schoongemaakt (DataFrame): DataFrame met alle schone gegevens.
        verdeling_1 (callable): Functie voor het genereren van distributie in segment 1.
        verdeling_2 (callable): Functie voor het genereren van distributie in segment 2.
        verdeling_3 (callable): Functie voor het genereren van distributie in segment 3.
    """

    # Bepaal xmax als het maximum van de productie van de desbetreffende locatie
    # afgerond naar boven naar het dichtstbijzijnde veelvoud van 50, met een marge van 5%.
    maximum = int(np.ceil(combined_df_cleaned[combined_df_cleaned['location'] == location]['production'].max() / 50 *
                          1.05)* 50)

    # Maak een grafiek voor elk segment
    plt.subplots(1, 3, figsize=(25, 4), gridspec_kw={'width_ratios': [4, 4, 4]})

    # Segment 1
    plt.subplot(1, 3, 1)
    distribution_1(segment_1['production'], location, threshold_1, maximum)

    # Segment 2
    plt.subplot(1, 3, 2)
    distribution_2(segment_2['production'], location, threshold_1, threshold_2, maximum)

    # Segment 3
    plt.subplot(1, 3, 3)
    distribution_3(segment_3['production'], location, threshold_2, maximum)

    # Toon het geheel
    plt.subplots_adjust(wspace=0.2)
    plt.show()


def line_chart_daily_production(data, location, chart_title):
    plt.plot(data, marker='o')
    plt.title(f"{location} {chart_title}")
    plt.xlabel('Dag')
    plt.ylabel('Productie')
    plt.grid(True)
    plt.show()