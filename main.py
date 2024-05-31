customer_name = input("What is your name?")
fruit_options = ["Apple", "Grape", "Orange"]
apple_cost = 2
grape_cost = 1
orange_cost = 3
fruit_selection = int(input(f"Welcome{customer_name}. Which fruit would you like to buy?" f"\n1. {fruit_options[0]} $2" f"\n2. {fruit_options[1]} $1" f"\n3. {fruit_options[2]} $3"))
print(f"You bought {fruit_selection}")
number_apple = fruit_selection
number_grape = fruit_selection
number_orange = fruit_selection
subtotal = int(apple_cost * number_apple + grape_cost * number_grape + orange_cost * number_orange)
tax = 0.05 * subtotal
total = subtotal + tax

while True:
    response = input("Would you like to buy another piece of fruit? yes or no")
    if response == "yes":
        print(fruit_selection)
    else:
        print(f"Receipt for{customer_name}")
        print(f"{number_apple} apple(s) at $2 apiece")
        print(f"{number_grape} grape(s) at $1 apiece")
        print(f"{number_orange} orange(s) at $3 apiece")
        print(f"Subtotal: ${subtotal}")
        print(f"5% Tax: ${tax}")
        print(f"Total: ${total}")
