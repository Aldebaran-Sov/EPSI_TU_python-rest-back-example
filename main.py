import services.api_igbd as api
data = api.get_videogame("Baldur's Gate 3")
print (data["name"])
# print (api.get_genres_label([16, 24, 31, 15, 12]))

