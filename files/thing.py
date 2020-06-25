import json
with open("shop-items.json", "r") as f:
    with open("shop-items1.json", "w+") as f2:
        jsonFile = "".join(f.readlines())
        j = json.loads(jsonFile)
        for shop in ["blacksmith", "adventuring", "arcane", "art/games-theme", "book", "fletcher", "general", "inn", "leather", "magical-theme", "market", "meals", "potion", "shady-theme", "tailor", "temple", "transportation", "water-theme"]:
            print(shop)
            for i in range(len(j[shop])):
                n = int(input(j[shop][i]["name"] + " "))
                j[shop][i]["limited"] = n
        f2.write(json.dumps(j))