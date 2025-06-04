while True:
    age = input("Enter your age (or type 'quit' to stop): ")
    if age.lower() == 'quit':
        print("Thank you for using the ticket system.")
        break
    age = int(age)
    if age < 3:
        print("Your ticket is free!")
    elif 3 <= age <= 12:
        print("Your ticket costs AED 10.")
    else:
        print("Your ticket costs AED 15.")