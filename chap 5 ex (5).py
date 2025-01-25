pets = []

pet = {
    'animal type': 'amphibians',
    'name': 'john',
    'owner': 'mj',
    'weight': 10,
    'eats': 'bugs',
}
pets.append(pet)

pet = {
    'animal type': 'bird',
    'name': 'clarence',
    'owner': 'rose',
    'weight': 6,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'peso',
    'owner': 'mc',
    'weight': 37,
    'eats': 'dog food',
}
pets.append(pet)

for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")