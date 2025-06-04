person = {
    'first_name': 'Tauheed',
    'last_name': 'Aqdas',
    'age': 20,
    'city': 'Abu Dhabi'
}

# Print each piece of information
for key, value in person.items():
    print(f"{key.replace('_', ' ').title()}: {value}")