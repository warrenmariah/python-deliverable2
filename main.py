customer_name = input("What is your name?")
fruit_options = ["Apple", "Grape", "Orange"]
apple_cost = 2
grape_cost = 1
orange_cost = 3
print(f"1. {fruit_options[0]} $2")
print(f"2. {fruit_options[1]} $1")
print(f"3. {fruit_options[2]} $3")
apple_selection = int(input(f"Welcome{customer_name}. How many apples would you like to buy?"))
print(f"You bought {apple_selection} apple(s).")
grape_selection = int(input(f"Welcome{customer_name}. How many grapes would you like to buy?"))
print(f"You bought {grape_selection} grape(s).")
orange_selection = int(input(f"Welcome{customer_name}. How many oranges would you like to buy?"))
print(f"You bought {orange_selection} orange(s).")
number_apple = apple_selection
number_grape = grape_selection
number_orange = orange_selection
subtotal = int(apple_cost * number_apple + grape_cost * number_grape + orange_cost * number_orange)
tax = 0.05 * subtotal
total = subtotal + tax
print(f"Receipt for{customer_name}")
print(f"{number_apple} apple(s) at $2 apiece")
print(f"{number_grape} grape(s) at $1 apiece")
print(f"{number_orange} orange(s) at $3 apiece")
print(f"Subtotal: ${subtotal}")
print(f"5% Tax: ${tax}")
print(f"Total: ${total}")
