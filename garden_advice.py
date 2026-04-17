def plant_advice(season, plant_type):
    """
    Returns gardening advice based on season and plant type.
    """

    advice = ""

    # Advice based on season
    if season == "summer":
        advice += "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        advice += "Protect your plants from frost with covers.\n"
    else:
        advice += "No advice for this season.\n"

    # Advice based on plant type
    if plant_type == "flower":
        advice += "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        advice += "Keep an eye out for pests!"
    else:
        advice += "No advice for this type of plant."

    return advice


# Get user input
season = input("Enter the current season: ").lower()
plant_type = input("Enter the plant type: ").lower()

# Call function and print result
result = plant_advice(season, plant_type)
print(result)

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
