while True:
    topping = input("Enter a pizza topping (or 'quit' to stop): ").lower()
    if topping == 'quit':
        print("Stopping pizza topping requests.")
        break
    else:
        print(f"Adding {topping} to your pizza!")