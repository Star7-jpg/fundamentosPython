#Diccionarios
#{"key": "value":, "key": "value"}

team = {
    "name": "City",
    "country": "England",
    "champion": 1,
    "players": ['halland', 'grealish']
}

print(type(team))
print(team)

print(team["name"])
print(team["players"])
team["players"].append("Kevin")
team["name"] = "Manchester City"
team["leage"] = "Premiere league"

print(team)