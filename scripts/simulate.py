import random
import numpy as np
from scipy.stats import cauchy


def simulate(share_1, share_2, lower_bound_s2, upper_bound_s2, distribution_s3, param1_s3, param2_s3,
             n_days):

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
                if distribution_s3 == "normal":
                    random_value = np.random.normal(param1_s3, param2_s3)
                elif distribution_s3 == "cauchy":
                    random_value = cauchy.rvs(loc=param1_s3, scale=param2_s3, size=1)
                    #random_value = param1_s3 + param2_s3 * np.tan(np.pi * (np.random.rand() - 0.5))
                    # #np.random.standard_cauchy()
            random_sum += random_value
        all_random_sums.append(random_sum)
    return all_random_sums
