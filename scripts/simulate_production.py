import numpy as np
import scipy.stats as stats

def simulate_production(n, mean, std):
    # Genereer een array van normaal verdeelde productiewaarden
    production_values = np.random.normal(mean, std, n)
    
    # Initialiseer een lege lijst om de gesimuleerde producties op te slaan
    simulated_production = []
    
    # Simuleer de productie voor elke dag
    for value in production_values:
        # Bereken de kans op 0 productie met de cumulatieve distributiefunctie (CDF) van de normaalverdeling
        zero_production_prob = stats.norm.cdf(0, loc=value, scale=std)
        
        # Genereer een willekeurige waarde tussen 0 en 1
        random_prob = np.random.rand()
        
        # Bepaal de gesimuleerde productiewaarde op basis van de kans
        if random_prob < zero_production_prob:
            simulated_production.append(0)
        else:
            simulated_production.append(value)
    
    return simulated_production
