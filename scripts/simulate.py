import random
import numpy as np

def simulate(share_1, share_2, lower_bound_s2, upper_bound_s2, param1_s3, param2_s3,
             n_days):

    """
    Simulate production processes for three production segments over a specified number of days.

    Parameters:
        share_1 (float): Share of production for segment 1.
        share_2 (float): Share of production for segment 2.
        lower_bound_s2 (float): Lower bound threshold for segment 2.
        upper_bound_s2 (float): Upper bound threshold for segment 2.
        param1_s3 (float): Parameter 1 for segment 3 (mean for normal distribution).
        param2_s3 (float): Parameter 2 for segment 3 (standard deviation for normal distribution).
        n_days (int): Number of days for which to simulate the production process.

    Returns:
        list: A list of simulated production values for each simulated day.

    This function simulates the production process for three production segments over a specified number of days.
    Each segment is defined by its share of production and threshold values.
    For each simulated day, random values are generated according to the defined segments,
    and the total production for that day is calculated and appended to a list.
    The function returns a list containing the simulated production values for each simulated day.

    Note:
        This function utilizes vectorized operations for efficient random number generation.
    """

    num_values = 10**5
    random_numbers = np.random.random((num_values, n_days))
    all_random_sums = []

    for i in range(num_values):
        random_values = random_numbers[i]
        random_sum = np.sum(np.where(random_values < share_1, 0,
                                     np.where(random_values < (share_1 + share_2),
                                              np.random.uniform(lower_bound_s2, upper_bound_s2, n_days),
                                              np.random.normal(param1_s3, param2_s3, n_days))))
        all_random_sums.append(random_sum)

    return all_random_sums
