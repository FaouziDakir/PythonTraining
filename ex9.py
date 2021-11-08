allergies = {
    "cats" : 128,
    "chocolate" : 32,
    "pollen" : 64,
    "tomatoes" : 16,
    "strawberries" : 8,
    "shellfish" : 4,
    "peanuts" : 2,
    "eggs" : 1
}

tom = 167
tomAllergies = []

for key in allergies:
    if (tom - allergies[key]) > -1:
        print("He is allergic to " + key)
        tom -= allergies[key]
    else :
        print("He is not allergic to " + key)

