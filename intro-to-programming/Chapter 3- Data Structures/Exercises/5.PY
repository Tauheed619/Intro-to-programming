guests = ["Albert Einstein", "Jamal Ud Din", "Muhammad Baig"]

# Guest who can't make it
print(f"Unfortunately, {guests[1]} can't make it to the dinner.")

# Replace with a new guest
guests[1] = "Abdullah Jan"

# Send updated invitations
for guest in guests:
    print(f"Dear {guest}, you are still invited to dinner.")