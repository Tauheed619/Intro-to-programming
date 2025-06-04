def describe_city(city, country="Pakistan"):
    print(f"{city} is in {country}.")

# Call the function with the default country (Iceland)
describe_city("Lahore")

# Call the function with a different country
describe_city("Paris", "France")

# Call the function with another city and country
describe_city("Tokyo", "Japan")