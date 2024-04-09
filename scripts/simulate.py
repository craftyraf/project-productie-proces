import random
import numpy as np

def simulate(share_1, share_2, lower_bound_s2, upper_bound_s2, param1_s3, param2_s3,
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
                random_value = np.random.normal(param1_s3, param2_s3)
            random_sum += random_value
        all_random_sums.append(random_sum)
    return all_random_sums
