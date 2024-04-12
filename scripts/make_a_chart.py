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


# ECDF calculation
def ecdf(data):
    """Calculate ECDF for a 1D array."""
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
    Plot the point distribution for a segment.

    Parameters:
        segment_data (DataFrame): Data for the segment.
        location (str): The location name.
        threshold_1 (float): Threshold value 1.

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
    plt.title(f"{location} Production < {threshold_1} (Point value)")
    plt.xlabel('Production')
    plt.ylabel('Density')


def generate_plot_uniform_distribution(segment_data, location, lower_bound, upper_bound, maximum):
    """
    Plot the uniform distribution for a segment.

    Parameters:
        segment_data (DataFrame): Data for the segment.
        location (str): The location name.
        threshold_1 (float): Threshold value 1.
        threshold_2 (float): Threshold value 2.
        maximum (int): Maximum value for the x-axis.
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

    Returns:
        None
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


def plot_segment_distributions(segment_1, segment_2, lower_bound, upper_bound, segment_3, param1_s3,
                               param2_s3, location, threshold_1, threshold_2, maximum):
    """
    Plot distribution segments for a given location.

    Parameters:
        segment_1 (DataFrame): DataFrame containing data for segment 1.
        segment_2 (DataFrame): DataFrame containing data for segment 2.
        segment_3 (DataFrame): DataFrame containing data for segment 3.
        location (str): The location for which distributions are plotted.
        threshold_1 (float): Threshold value between segments 1 and 2.
        threshold_2 (float): Threshold value between segments 2 and 3.
        combined_df_cleaned (DataFrame): DataFrame containing all clean data.
        distribution_1 (callable): Function to generate distribution in segment 1.
        distribution_2 (callable): Function to generate distribution in segment 2.
        distribution_3 (callable): Function to generate distribution in segment 3.

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
    # Compute num_values
    num_values = round(10 ** 6 / np.sqrt(n_days))

    # Calculate the number of bins (determined by trial & error)
    num_bins = max(int((np.max(simulated_data) - np.min(simulated_data)) / (2 * (n_days + 10))),150)

    plt.hist(simulated_data, bins=num_bins, density=True, alpha=0.7)


def plot_multiple_histograms(ax, simulated_data, n_days, location):
    # Compute num_values
    num_values = round(10 ** 6 / np.sqrt(n_days))

    # Calculate the number of bins (determined by trial & error)
    num_bins = max(int((np.max(simulated_data) - np.min(simulated_data)) / (2 * (n_days + 10))),150)

    ax.hist(simulated_data, bins=num_bins, density=True, alpha=0.7)
    ax.set_xlabel(f"Production for {location} ({n_days} {'day' if n_days == 1 else 'days'})")
    ax.set_ylabel('Density')
    ax.set_title(
        f"Density plot of $10^{int(np.floor(np.log10(num_values)))}$ random\n values for {location} ({n_days}"
        f" {'day' if n_days == 1 else 'days'})")


def plot_cdf(ax, simulated_data, n_days, location):
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


def line_chart_daily_production(data, location, chart_title):
    plt.plot(data, marker='o')
    plt.title(f"{location} {chart_title}")
    plt.xlabel('Day')
    plt.ylabel('Production')
    plt.grid(True)
    plt.show()
