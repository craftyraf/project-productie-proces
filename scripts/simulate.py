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
    """

    num_values = round(10 ** 6 / np.sqrt(n_days))

    all_random_sums = []
    for _ in range(num_values):
        random_sum = 0
        for _ in range(n_days):
            random_number = random.random()
            if random_number < share_1:
                random_value = 0
            elif random_number < (share_1 + share_2):
                random_value = np.random.uniform(lower_bound_s2, upper_bound_s2)
            else:
                random_value = np.random.normal(param1_s3, param2_s3)
            random_sum += random_value
        all_random_sums.append(random_sum)

    return all_random_sums
