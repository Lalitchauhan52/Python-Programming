foods = []
prices = []
total = 0
items = 0

while True:
    food = input("Enter the food item (or q to quit): ")
    if food.lower() == 'q':
        break
    else:
        price = float(input("Enter the price of the item: $"))
        prices.append(price)
        foods.append(food)
        total += price
        items += 1
        print("-" * 40)
        print(f"{items} item(s) added. Current total: ${total:.2f}")
print("-" * 10 + "YOUR CART" + "-" * 10)
for i in range(items):
    print(f"{i + 1}. {foods[i]} - ${prices[i]:.2f}")

print("-" * 40)
print(f"Total: ${total:.2f}")