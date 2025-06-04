places = ["Tokyo", "New York", "Islamabad", "Paris", "Barcelona"]
print("Original list:", places)
print("Alphabetical:", sorted(places))
print("Original after sorted():", places)
print("Reverse alphabetical:", sorted(places, reverse=True))
print("Original after reverse sorted():", places)

places.reverse()
print("List after reverse():", places)
places.reverse()
print("List after second reverse():", places)

places.sort()
print("List after sort():", places)
places.sort(reverse=True)
print("List after reverse sort():", places)
