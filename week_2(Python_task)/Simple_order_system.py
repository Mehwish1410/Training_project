from tabulate import tabulate

# Menu for the user
Menu = ("Press 1 for Fruit Salad :Rs 100\n"
        "Press 2 for Chickpeas :Rs 100\n"
        "Press 3 for Samosa Salad :Rs 120\n"
        "Press 4 for Wrap :Rs 150\n"
        "Press 5 for Pani puri :Rs 70\n"
        "Press 6 for Yougart Balls :Rs 150\n"
        "Press 7 for Burger :Rs 120\n"
        "Press 8 for MilkShake :Rs 100\n"
        "Press 9 for Fritter :Rs 100\n"
        "Press 10 for Patties :Rs 50")

print(Menu)

# Initialize order list and control variable
order = []
back = True

# Loop to take orders
while back:
    choice = input("Please Press: ")
    order.append(choice)
    any_thing_else = input("If you want to order anything else then Press Y otherwise N. For exit press any key: ")

    if any_thing_else.lower() == "y":
        back = True
    elif any_thing_else.lower() == "n":
        back = False
    else:
        print("Exiting...")
        break

# Price and item lists
prices = []
final_items = []
total_bill = 0

# Mapping choices to items and prices
for i in order:
    match i:
        case '1':
            item = "Fruit Salad"
            price = 100
        case '2':
            item = "Chickpeas"
            price = 100
        case '3':
            item = "Samosa Salad"
            price = 120
        case '4':
            item = "Wrap"
            price = 150
        case '5':
            item = "Pani puri"
            price = 70
        case '6':
            item = "Yougart Balls"
            price = 150
        case '7':
            item = "Burger"
            price = 120
        case '8':
            item = "MilkShake"
            price = 100
        case '9':
            item = "Fritter"
            price = 100
        case '10':
            item = "Patties"
            price = 50
        case _:
            continue  # Ignore invalid choices

    final_items.append(item)
    prices.append(price)
    total_bill += price

# Generate and print the final table
headers = ['Item', 'Price']
final_list = zip(final_items, prices)
finally_table = tabulate(final_list, headers=headers, tablefmt='grid')

print(finally_table)
print("Your total bill is:", total_bill)
