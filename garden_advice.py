# Dictionaries to store advice
season_advice = {
    "summer": "Water your plants regularly and provide some shade.\n",
    "winter": "Protect your plants from frost with covers.\n"
}

plant_advice_dict = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!"
}


def plant_advice(season, plant_type):
    """
    Returns gardening advice based on season and plant type.
    """
    advice = ""
    advice += season_advice.get(season, "No advice for this season.\n")
    advice += plant_advice_dict.get(plant_type, "No advice for this type of plant.")
    return advice


# --- Program execution ---
season = input("Enter the current season: ").lower()
plant_type = input("Enter the plant type: ").lower()

result = plant_advice(season, plant_type)
print(result)

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
