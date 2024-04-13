import numpy as np

"""
Map fuel_type to a categorization of a select number of values.

"""

fuel_mapping = {
    'Gasoline': 'Gasoline',
    'Hybrid': 'Hybrid',
    np.nan: 'Other',
    'Premium': 'Gasoline',
    'Electric': 'Electric',
    'Gasoline/Mild Electric Hybrid': 'Hybrid',
    'Diesel': 'Gasoline',
    'E85 Flex Fuel': 'Gasoline',
    'Flexible Fuel': 'Gasoline',
    'Gasoline Fuel': 'Gasoline',
    'Plug-In Hybrid': 'Hybrid',
    'Premium (Required)': 'Gasoline',
    'Regular Unleaded': 'Gasoline',
    'Unspecified': 'Other',
    'Unknown': 'Other',
    'Compressed Natural Gas': 'Other',
    'Other': 'Other',
    'Natural Gas': 'Other',
    'Gaseous': 'Other',
    'Bi-Fuel': 'Gasoline',
    'Flex Fuel Capability': 'Gasoline',
    'Diesel Fuel': 'Gasoline',
    'Premium Unleaded': 'Gasoline',
    'Biodiesel': 'Gasoline',
    'Bio Diesel': 'Gasoline',
    'Hydrogen Fuel Cell': 'Other',
    'Gas': 'Other',
    'PHEV': 'Hybrid',
    'Hybrid Fuel': 'Hybrid',
    'Automatic': 'Other',
    'E85 Fl': 'Gasoline',
    'Electric Fuel System': 'Electric',
    'G': 'Other',
    'B': 'Other',
    'Gas/Electric Hybrid': 'Hybrid',
    'Flex Fuel': 'Gasoline',
    'Plug-In Electric/Gas': 'Hybrid',
    'Electric': 'Electric'
}