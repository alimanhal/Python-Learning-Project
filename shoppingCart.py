foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q for exit) : ").lower()
    if food == 'q':
        break
    else:
        price = float(input(f'Enter the price of {food} : ₹'))
        foods.append(food)
        prices.append(price)
print('-----YOUR CART-----')
for food in foods:
    print(food)
for price in prices:
        total += price
print()
print(f"Your total is : ₹{total}")