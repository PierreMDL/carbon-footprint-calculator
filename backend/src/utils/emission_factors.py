from enum import Enum

"""
I prefer Enums over dicts in that situation:
This indicates that the element name should not ideally never be changed,
since the emission factor type is a query parameter of the request object.
All units in grams for consistency
All units in float for consistency
"""


# In grams of CO2 / passenger-km
class TransportationEmissionFactors(Enum):
    CAR = 0.118
    BUS = 0.023
    TRAIN_ELEC = 0.007
    TRAIN_DIESEL = 0.059
    AIRPLANE = 0.233


# In grams of CO2 / kg
class DietEmissionFactors(Enum):
    BEEF = 60. * 1000
    LAMB = 24. * 1000
    PORK = 7. * 1000
    CHICKEN = 6. * 1000
    FISH = 5. * 1000  # NOTE - Farmed
    EGGS = 4.8 * 1000
    MILK = 1.9 * 1000
    CHEESE = 13.5 * 1000
    VEGETABLES = 0.2 * 1000 # NOTE - Seasonal and locally grown


# In grams of CO2 / kWh
class EnergyEmissionFactors(Enum):
    COAL = 1000.
    NATURAL_GAS = 500.
    OIL = 800.
    NUCLEAR = 16.
    WIND = 10.
    SOLAR = 40.
    HYDRO = 24.
    BIOMASS = 230.
    GEOTHERMAL = 2.


# In grams of CO2e / kg  # TODO check what CO2e is
class WasteEmissionFactors(Enum):
    FOOD = 0.62 * 1000
    PAPER = 1.37 * 1000
    PLASTIC = 6. * 1000
    GLASS = 0.48 * 1000
