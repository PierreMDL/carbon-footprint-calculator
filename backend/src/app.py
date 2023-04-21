from flask import Flask, request
import json

from utils.formulas import *

app = Flask(__name__)


"""
This app was designed swiftly to be private:
There is no user-friendly API, no validation, we just throw the result as a response
 or null with HTTP 400 BAD REQUEST if the query parameters are wrong,
 like if the emission type is not known for that calculation.
Basic logging wouldn't hurt.
In hindsight, I could have made it better, with a convienient api,
 possibly meant for public use (because why not)
Also Formula as classes would have been better I suppose.
Now each formula is mapped to an endpoint, and does one calculation at a time,
 meaning that there must be as many calls as there are emission factors.
 Reducing the calculation in the server would make more sense.
"""

@app.get("/transportation")
def get_carbon_footprint_for_transportation():
    data = request.args
    try:
        distance = int(data["amount"])
        emission_factor_id = str(data["emission_factor_id"])
        emission_factor_type = TransportationEmissionFactors[emission_factor_id]
        number_of_people = float(data["number_of_people"])
    except (KeyError, ValueError):
        return (json.dumps(None), 400)
    return json.dumps(transportation_formula(
        distance=distance,
        emission_factor=emission_factor_type.value,
        number_of_people=number_of_people,
    ))


@app.get("/diet")
def get_carbon_footprint_for_diet():
    data = request.args
    try:
        food_consumption = int(data["amount"])
        emission_factor_id = str(data["emission_factor_id"])
        emission_factor_type = DietEmissionFactors[emission_factor_id]
        number_of_people = float(data["number_of_people"])
    except (KeyError, ValueError):
        return (json.dumps(None), 400)
    return json.dumps(diet_formula(
        food_consumption=food_consumption,
        emission_factor=emission_factor_type.value,
        number_of_people=number_of_people,
    ))


@app.get("/energy")
def get_carbon_footprint_for_energy():
    data = request.args
    try:
        energy_consumption = int(data["amount"])
        emission_factor_id = str(data["emission_factor_id"])
        emission_factor_type = EnergyEmissionFactors[emission_factor_id]
        number_of_people = float(data["number_of_people"])
    except (KeyError, ValueError):
        return (json.dumps(None), 400)
    return json.dumps(energy_formula(
        energy_consumption=energy_consumption,
        emission_factor=emission_factor_type.value,
        number_of_people=number_of_people,
    ))


@app.get("/waste")
def get_carbon_footprint_for_waste():
    data = request.args
    try:
        waste_amount = int(data["amount"])
        emission_factor_id = str(data["emission_factor_id"])
        emission_factor_type = WasteEmissionFactors[emission_factor_id]
    except (KeyError, ValueError):
        return (json.dumps(None), 400)
    return json.dumps(waste_formula(
        waste_amount=waste_amount,
        emission_factor=emission_factor_type.value,
    ))
