fruits = ["apple", "banana", "cherry", "date"]
vegetables = ["carrot", "broccoli", "spinach", "pepper"]
meats = ["chicken", "beef", "turkey", "fish"]

groceries = [fruits, vegetables, meats]
print(groceries)
print(groceries[0])  # Accessing the first list (fruits)
print(groceries[1])  # Accessing the second list (vegetables)
print(groceries[2])  # Accessing the third list (meats)
print(groceries[0][1])  # Accessing "banana" from the fruits list
#to print groceries in a more readable format(grids)
for collection in groceries:
    for item in collection:
        print(item, end=" ")
    print()