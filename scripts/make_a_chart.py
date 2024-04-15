import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from scipy.stats import norm


def horizontal_bar_chart(value_counts, chart_title, x_label, y_label):
    """
    Create a horizontal bar chart with customizable title and labels.

    Parameters:
    - value_counts: pandas Series containing the values and their counts for the bar chart.
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


def generate_plot_ecdf(data,
                       median_price=None,
                       avg_price=None,
                       title="Distribution and ECDF",
                       xlabel="Price",
                       ylabel="Probability",
                       bins=30):
    """
    Calculate and plot the Empirical Cumulative Distribution Function (ECDF) for a 1D array of data.

    Parameters:
    - data: array-like, the 1D array containing the data for which to calculate the ECDF.
    - median_price: float, optional, the median price to mark on the plot (vertical line).
    - avg_price: float, optional, the average price to mark on the plot (vertical line).
    - title: string, optional, the title of the plot.
    - xlabel: string, optional, the label for the x-axis.
    - ylabel: string, optional, the label for the y-axis.
    - bins: int, optional, the number of bins for the histogram.

    Displays a plot showing the histogram and ECDF of the data, with optional vertical lines
    marking the median and average prices.
    """

    n = len(data)
    x = np.sort(data)
    y = np.arange(1, n + 1) / n

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(data,
            bins=bins,
            color='skyblue',
            edgecolor='black',
            cumulative=True,
            density=True,
            alpha=0.5,
            label='Histogram')
    ax.plot(x,
            y,
            marker='.',
            linestyle='none',
            color='blue',
            label='ECDF')
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend()

    # Add vertical lines for median and average if provided
    if median_price is not None:
        ax.axvline(median_price,
                   color='red',
                   linestyle='solid',
                   linewidth=2,
                   label='Median')
    if avg_price is not None:
        ax.axvline(avg_price,
                   color='purple',
                   linestyle='solid',
                   linewidth=2,
                   label='Average')

    # Delete lines top and right
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.show()


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
    Plot the point distribution for a segment.

    Parameters:
        segment_data (DataFrame): Data for the segment.
        location (str): The name of the location.
        threshold_1 (float): The threshold value for categorizing points.
        maximum (int): The maximum value for the x-axis.
    """

    # Set histogram parameters
    width = maximum / 25

    # Plot histogram
    xmin, xmax = plt.xlim()
    plt.xlim(xmin=0, xmax=maximum)
    plt.hist(segment_data, bins=1, density=True, alpha=0.6, width=width)

    # Set plot title and labels
    plt.title(f"{location} Production < {threshold_1} (Point value)")
    plt.xlabel('Production')
    plt.ylabel('Density')


def generate_plot_uniform_distribution(segment_data, location, lower_bound, upper_bound, maximum):
    """
    Plot the uniform distribution for a segment.

    Parameters:
        segment_data (DataFrame): Data for the segment.
        location (str): The location name.
        lower_bound (float): The lower bound threshold value.
        upper_bound (float): The upper bound threshold value.
        maximum (int): The maximum value for the x-axis.

    This function plots the uniform distribution for a given segment using a histogram.
    It fits a uniform distribution to the segment data and overlays it on the histogram.
    The x-axis limits are set based on the maximum value provided.
    The plot title indicates the location and the range specified by the lower and upper bound
    threshold values, and labels the axes accordingly.
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
    plt.title(f"{lower_bound} <= {location} Production < {upper_bound} (Uniform Distribution)")
    plt.xlabel('Production')
    plt.ylabel('Density')
    plt.legend()


def generate_plot_normal_distribution(segment_data, location, threshold_2, maximum, mean_norm, std_norm):
    """
    Generate the normal distribution for a segment.

    Parameters:
        segment_data (DataFrame): Data for the segment.
        location (str): The location name.
        threshold_2 (float): Threshold value 2.
        maximum (int): The maximum value for the x-axis.
        mean_norm (float): The mean of the normal distribution.
        std_norm (float): The standard deviation of the normal distribution.

    This function generates and plots the normal distribution for a given segment using a histogram.
    It overlays the normal distribution curve on the histogram based on the provided mean and standard deviation.
    The x-axis limits are set based on the maximum value provided.
    The plot title indicates the location and the threshold value, and labels the axes accordingly.
    """

    # Histogram plot for the segment
    plt.hist(segment_data, bins=50, density=True, alpha=0.6, label='Histogram')

    # Set x-axis limits
    xmin, xmax = plt.xlim()
    plt.xlim(xmin=0, xmax=maximum)

    # Generate points for the normal distribution
    x_norm = np.linspace(xmin, xmax, 100)
    p_norm = stats.norm.pdf(x_norm, mean_norm, std_norm)

    # Plot normal distribution
    plt.plot(x_norm, p_norm, 'k', linewidth=2, label='Normal distribution')

    # Set plot title and labels
    plt.title(f"{location} Production >= {threshold_2} (Normal distribution)")
    plt.xlabel('Production')
    plt.ylabel('Density')
    plt.legend()


def plot_segment_distributions(segment_1,
                               segment_2, lower_bound, upper_bound,
                               segment_3, param1_s3, param2_s3,
                               location,
                               threshold_1, threshold_2, maximum):
    """
    Plot distribution segments for a given location.

    Parameters:
        segment_1 (DataFrame): DataFrame containing data for segment 1.
        segment_2 (DataFrame): DataFrame containing data for segment 2.
        segment_3 (DataFrame): DataFrame containing data for segment 3.
        location (str): The location for which distributions are plotted.
        threshold_1 (float): Threshold value between segments 1 and 2.
        threshold_2 (float): Threshold value between segments 2 and 3.
        maximum (int): The maximum value for the x-axis.

    This function plots distribution segments for a given location across three subplots.
    Each subplot represents a segment, with its respective distribution plotted according to its type.
    Segment 1 is plotted with a point distribution, Segment 2 with a uniform distribution, and Segment 3 with a normal distribution.
    The title of each subplot indicates the location and the relevant threshold value, and the x-axis represents production.
    """

    # Create a graph for each segment
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

    # Show the whole
    plt.subplots_adjust(wspace=0.2)
    plt.show()


def plot_histogram(simulated_data, n_days, location):
    """
    Generate a histogram of production or simulation data for a given location.

    Parameters:
        simulated_data (array-like): Array containing production or simulation data.
        n_days (int): Number of days the data represents.
        location (str): Name of the location for which the data is plotted.

    This function generates a histogram of production or simulation data for a specified location.
    The number of bins is calculated based on the range of the data and the number of days.
    The x-axis represents production for the location over the specified number of days,
    and the y-axis represents the density of the data.
    """

    # Calculate the number of bins (determined by trial & error)
    num_bins = max(int((np.max(simulated_data) - np.min(simulated_data)) / (2 * (n_days + 10))),150)

    plt.hist(simulated_data, bins=num_bins, density=True, alpha=0.7)

    plt.xlabel(f"Production for {location} ({n_days} {'day' if n_days == 1 else 'days'})")
    plt.ylabel('Density')
    plt.title(
         f"Density plot for {location} ({n_days}"
         f" {'day' if n_days == 1 else 'days'})")
    plt.tight_layout()
    plt.show()


def plot_multiple_histograms(ax, simulated_data, n_days, location):
    """
    Generate multiple histograms of production or simulation data for a given location.

    Parameters:
        ax (matplotlib Axes): The Axes object to draw the histograms onto.
        simulated_data (array-like): Array containing production or simulation data.
        n_days (int): Number of days the data represents.
        location (str): Name of the location for which the data is plotted.

    This function generates multiple histograms of production or simulation data for a specified location.
    The number of histograms is determined by the number of random values (`num_values`) computed based on the number of days.
    The number of bins for each histogram is calculated based on the range of the data and the number of days.
    Each histogram's x-axis represents production for the location over the specified number of days,
    and the y-axis represents the density of the data.
    The title of each histogram indicates the number of random values used and the location and number of days.
    """

    # Calculate the number of bins (determined by trial & error)
    num_bins = max(int((np.max(simulated_data) - np.min(simulated_data)) / (2 * (n_days + 10))),150)

    ax.hist(simulated_data, bins=num_bins, density=True, alpha=0.7)
    ax.set_xlabel(f"Production for {location} ({n_days} {'day' if n_days == 1 else 'days'})")
    ax.set_ylabel('Density')
    ax.set_title(
        f"Density plot of $10^5$ random values for {location} ({n_days}"
        f" {'day' if n_days == 1 else 'days'})")


def plot_cdf(ax, simulated_data, n_days, location, include_clt=False):
    """
    Generate a Cumulative Distribution Function (CDF) line chart for production or simulation data.

    Parameters:
        ax (matplotlib Axes): The Axes object to draw the CDF chart onto.
        simulated_data (array-like): Array containing production or simulation data.
        n_days (int): Number of days the data represents.
        location (str): Name of the location for which the data is plotted.
        include_clt (bool): Whether to include the Central Limit Theorem line on the plot. Default is False.

    This function generates a Cumulative Distribution Function (CDF) line chart for a given location and number of days.
    The data is sorted, and the CDF is computed based on the sorted data.
    The x-axis represents production for the location over the specified number of days,
    and the y-axis represents the cumulative probability.
    If include_clt is True, the Central Limit Theorem (CLT) line is added to the plot.
    """

    # Sort dataset
    sorted_data = np.sort(simulated_data)

    # Calculate y values
    n = len(simulated_data)
    y_values = np.arange(1, n + 1) / n

    # Plot the CDF
    ax.plot(sorted_data, y_values, label=f"Empirical Cumulative Distribution Function ({n_days}"
                                         f" {'day' if n_days == 1 else 'days'})")

    # Set labels and title
    ax.set_xlabel(f"Production for {location} ({n_days} {'day' if n_days == 1 else 'days'})")
    ax.set_ylabel('Cumulative probability')
    ax.set_title(f"Cumulative probability for {location} ({n_days} {'day' if n_days == 1 else 'days'})")
    ax.legend()

    if include_clt:
        # Add CLT line to CDF plot
        mean_simulated = np.mean(simulated_data)
        std_simulated = np.std(simulated_data)
        x_values = np.linspace(min(simulated_data), max(simulated_data), 100)
        y_values = norm.cdf(x_values, mean_simulated, std_simulated)
        ax.plot(x_values, y_values, label='Central Limit Theorem', color='red', linestyle='--')
        ax.legend(loc='upper left')
