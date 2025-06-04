rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'ganges': 'india'
}

# Print a sentence about each river
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# Print the names of each river
for river in rivers.keys():
    print(river.title())

# Print the names of each country
for country in rivers.values():
    print(country.title())