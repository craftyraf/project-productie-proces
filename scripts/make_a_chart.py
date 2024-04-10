import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

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


def calculate_maximum(combined_df_cleaned, location):
    """
    Calculate the maximum value for the x-axis based on production data for a specified location.

    Parameters:
        combined_df_cleaned (DataFrame): Combined DataFrame containing production data.
        location (str): The location for which the maximum value is to be calculated.

    Returns:
        int: The maximum value for the x-axis.
    """
    # Extract the relevant data for the specified location
    location_data = combined_df_cleaned[combined_df_cleaned['location'] == location]

    # Find the maximum production value for the specified location
    max_production = location_data['production'].max()

    # Calculate the maximum value for the x-axis, ensuring it's a multiple of 50 and adding a 5% buffer
    maximum_unrounded = max_production / 50 * 1.05
    maximum_rounded = np.ceil(maximum_unrounded)
    maximum = int(maximum_rounded * 50)

    return maximum


def generate_plot_point_distribution(segment_data, location, threshold_1, maximum):
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
    plt.hist(segment_data, bins=1, density=True, alpha=0.6, width=width)

    # Set plot title and labels
    plt.title(f"{location} Productie < {threshold_1} (Puntwaarde)")
    plt.xlabel('Productie')
    plt.ylabel('Dichtheid')


def generate_plot_uniform_distribution(segment_data, location, lower_bound, upper_bound, maximum):
    """
    Plot de uniforme verdeling voor een segment.

    Parameters:
        segment_data (DataFrame): Data voor het segment.
        location (str): De locatienaam.
        threshold_1 (float): Drempelwaarde 1.
        threshold_2 (float): Drempelwaarde 2.
        maximum (int): Maximale waarde voor de x-as.
    """

    # Fit uniform distribution to the segment data
    mean_norm, std_norm = stats.uniform.fit(segment_data)

    # Plot histogram
    plt.hist(segment_data, bins=50, density=True, alpha=0.6, label='Histogram')

    # Set x-axis limits
    xmin, xmax = plt.xlim()
    plt.xlim(xmin=0, xmax=maximum)

    # Generate points for the uniform distribution
    x_norm = np.linspace(xmin, xmax, 100)
    p_norm = stats.uniform.pdf(x_norm, mean_norm, std_norm)

    # Plot uniform distribution
    plt.plot(x_norm, p_norm, 'k', linewidth=2, label='Uniforme verdeling')

    # Set plot title and labels
    plt.title(f"{lower_bound} <= {location} Productie < {upper_bound} (Uniforme verdeling)")
    plt.xlabel('Productie')
    plt.ylabel('Dichtheid')
    plt.legend()


def generate_plot_normal_distribution(segment_data, location, threshold_2, maximum, mean_norm, std_norm):
    """
    Genereer de normale verdeling voor een segment.

    Parameters:
        segment_data (DataFrame): Gegevens voor het segment.
        location (str): De locatienaam.
        threshold_2 (float): Drempelwaarde 2.

    Returns:
        None
    """

    # Histogram plot voor het segment
    plt.hist(segment_data, bins=50, density=True, alpha=0.6, label='Histogram')

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



def plot_segment_distributions(segment_1, segment_2, lower_bound, upper_bound, segment_3, param1_s3,
                               param2_s3, location, threshold_1, threshold_2, maximum):
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

    # Maak een grafiek voor elk segment
    plt.subplots(1, 3, figsize=(25, 4), gridspec_kw={'width_ratios': [4, 4, 4]})

    # Segment 1
    plt.subplot(1, 3, 1)
    generate_plot_point_distribution(segment_1['production'], location, threshold_1, maximum)

    # Segment 2
    plt.subplot(1, 3, 2)
    generate_plot_uniform_distribution(segment_2['production'], location, lower_bound, upper_bound, maximum)

    # Segment 3
    plt.subplot(1, 3, 3)
    generate_plot_normal_distribution(segment_3['production'], location, threshold_2, maximum, param1_s3, param2_s3)

    # Toon het geheel
    plt.subplots_adjust(wspace=0.2)
    plt.show()


def plot_multiple_histograms(ax, simulated_data, n_days, location):
    # Compute num_values
    num_values = round(10 ** 6 / np.sqrt(n_days))

    # Calculate the number of bins (bepaald via trial & error)
    num_bins = max(int((np.max(simulated_data) - np.min(simulated_data)) / (2 * (n_days + 10))),150)

    ax.hist(simulated_data, bins=num_bins, density=True, alpha=0.7)
    ax.set_xlabel(f"Productie voor {location} ({n_days} {'dag' if n_days == 1 else 'dagen'})")
    ax.set_ylabel('Density')
    ax.set_title(
        f"Density plot van ca. $10^{int(np.floor(np.log10(num_values)))}$ random\n waarden voor {location} ({n_days}"
        f" {'dag' if n_days == 1 else 'dagen'})")

def plot_histogram(simulated_data, n_days, location):
    # Compute num_values
    num_values = round(10 ** 6 / np.sqrt(n_days))

    # Calculate the number of bins (bepaald via trial & error)
    num_bins = max(int((np.max(simulated_data) - np.min(simulated_data)) / (2 * (n_days + 10))),150)

    plt.hist(simulated_data, bins=num_bins, density=True, alpha=0.7)


def plot_cdf(ax, simulated_data, n_days, location):
    # Sorteer dataset
    sorted_data = np.sort(simulated_data)

    # Bereken y-waarden
    n = len(simulated_data)
    y_values = np.arange(1, n + 1) / n

    # Plot the CDF
    ax.plot(sorted_data, y_values, label=f"Empirische Cumulatieve Distributiefunctie ({n_days}"
                                         f" {'dag' if n_days == 1 else 'dagen'})")

    # Set labels and title
    ax.set_xlabel(f"Productie voor {location} ({n_days} {'dag' if n_days == 1 else 'dagen'})")
    ax.set_ylabel('Cumulatieve kans')
    ax.set_title(f"Cumulatieve kans voor {location} ({n_days} {'dag' if n_days == 1 else 'dagen'})")
    ax.legend()


def line_chart_daily_production(data, location, chart_title):
    plt.plot(data, marker='o')
    plt.title(f"{location} {chart_title}")
    plt.xlabel('Dag')
    plt.ylabel('Productie')
    plt.grid(True)
    plt.show()
