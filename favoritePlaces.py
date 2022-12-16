# Compiling pole results
favoritePlaces = {
    "kaitlynn": ["grandparents' house", "cat cafe", "home"],
    "alphys": ["lab", "garbage dump", "anywhere with Undyne"],
    "sans": ["grilby's", "snowdin", "the door to the ruins"] 
    }


# printing results
for person, place in favoritePlaces.items():
    print(f"{person.title()}'s favorite places are:")
    for place in favoritePlaces[person]:
        print(place)
    print("\n \n")