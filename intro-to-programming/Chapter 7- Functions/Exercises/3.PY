def make_shirt(size, message):
    print(f"The shirt is size {size} and says: {message}")

# Call the function once using positional arguments
make_shirt("Large", "Working with Python is awesome!")

# Call the function again using keyword arguments
make_shirt(size="Medium", message="Code and coffee!")