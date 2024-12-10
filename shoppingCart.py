# Initialize empty lists to store food items and their prices
foods = []  # List to hold names of food items
prices = []  # List to hold prices of food items
total = 0  # Variable to hold the total cost

# Start a loop to continuously take user inputs
while True:
    # Ask the user to input a food item or 'q' to exit
    food = input("Enter a food to buy (q for exit) : ").lower()
    if food == 'q':  # If the user enters 'q', exit the loop
        break
    else:
        # Ask the user to input the price of the food item
        price = float(input(f'Enter the price of {food} : ₹'))
        foods.append(food)  # Add the food item to the foods list
        prices.append(price)  # Add the price to the prices list

# Print the shopping cart summary
print('-----YOUR CART-----')
for food in foods:  # Iterate over the foods list to display each item
    print(food)

# Calculate the total price of all items
for price in prices:  # Iterate over the prices list to calculate the sum
    total += price

# Print the total cost of the shopping cart
print()
print(f"Your total is : ₹{total}")
