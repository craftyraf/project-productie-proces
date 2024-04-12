import numpy as np
import scipy.stats as stats

def simulate_production(n, mean, std):
    # Generate an array of normally distributed production values
    production_values = np.random.normal(mean, std, n)
    
    # Initialize an empty list to save the simulated productions
    simulated_production = []
    
    # Simulate the production for each day
    for value in production_values:
        # Calculate the probability on 0 production with the cumulative distribution function  
        zero_production_prob = stats.norm.cdf(0, loc=value, scale=std)
        
        # Generate a random value between 0 and 1
        random_prob = np.random.rand()
        
        # Determin the simulated production value based on the probability
        if random_prob < zero_production_prob:
            simulated_production.append(0)
        else:
            simulated_production.append(value)
    
    return simulated_production
