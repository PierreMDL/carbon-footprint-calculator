from .emission_factors import *
"""
Using float: precision is not much important
"""


def transportation_formula(
    distance: int,           # In kilometers
    emission_factor: float,  # In grams of CO2 per passenger-kilometer
    number_of_people: float  # Average
) -> float:
    carbon_footprint = (distance * emission_factor) / number_of_people
    return carbon_footprint


def diet_formula(
    food_consumption: int,  # In grams
    emission_factor: float, # In grams of CO2 per kilogram
    number_of_people: float # Average
) -> float:
    carbon_footprint = (food_consumption * emission_factor) / number_of_people
    return carbon_footprint


def energy_formula(
    energy_consumption: int, # In kWh
    emission_factor: float,  # In grams of CO2 per kWh 
    number_of_people: float  # Average
) -> float:
    carbon_footprint = (energy_consumption * emission_factor) / number_of_people
    return carbon_footprint


def waste_formula(
    waste_amount: int,      # In grams
    emission_factor: float  # In grams of CO2e per kilogram
) -> float:
    carbon_footprint = waste_amount * emission_factor
    return carbon_footprint
