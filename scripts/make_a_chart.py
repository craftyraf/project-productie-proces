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


def generate_point_distribution(segment_data, location, threshold_1, maximum, chart_color):
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
    plt.xlim(xmin=0, xmax=maximum)
    plt.hist(segment_data, bins=1, density=True, alpha=0.6, color=chart_color, width=width)

    # Set plot title and labels
    plt.title(f"{location} Productie < {threshold_1} (Puntwaarde)")
    plt.xlabel('Productie')
    plt.ylabel('Dichtheid')


def generate_uniform_distribution(segment_data, location, threshold_1, threshold_2, maximum, chart_color):
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
    plt.hist(segment_data, bins=50, density=True, alpha=0.6, color=chart_color, label='Histogram')

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


def generate_normal_distribution(segment_data, location, threshold_2, maximum, chart_color):
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
    plt.hist(segment_data, bins=50, density=True, alpha=0.6, color=chart_color, label='Histogram')

    # Stel x-as limieten in
    xmin = 0
    xmax = maximum

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


def generate_cauchy_distribution(segment_data, location, threshold_2, maximum, chart_color):
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
    plt.hist(segment_data, bins=50, density=True, alpha=0.6, color=chart_color, label='Histogram')

    # Bepaal de x-limieten van de plot
    xmin = 0
    xmax = maximum

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
