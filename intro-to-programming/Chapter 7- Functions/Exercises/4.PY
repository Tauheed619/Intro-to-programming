def make_shirt(size="Large", message="I love Python"):
    print(f"The shirt is size {size} and says: {message}")

# Call the function with the default size and message
make_shirt()

# Call the function with a different size and the default message
make_shirt("Medium")

# Call the function with a custom size and message
make_shirt("Small", "Learning to code is fun!")