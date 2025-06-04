guests = ["Albert Einstein", "Abdullah Jan", "Muhammad Baig"]

print("Sorry, I can only invite two people to dinner.")

# Remove guests one by one and apologize
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest}, I can't invite you to dinner.")

# Confirm invitations to remaining guests
for guest in guests:
    print(f"{guest}, you're still invited to dinner.")

# Clear the list
del guests[0]
del guests[0]

# Confirm the list is empty
if not guests:
    print("The guest list is now empty.")
else:
    print("Guest list is not empty:", guests)