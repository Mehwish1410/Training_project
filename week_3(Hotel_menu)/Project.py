import csv
import matplotlib.pyplot as plt
from datetime import datetime

restaurant_items = [
    {"name": "Burger", "order_id": 1001, "price": 500},
    {"name": "Pizza", "order_id": 1002, "price": 1200},
    {"name": "Salad", "order_id": 1003, "price": 400},
    {"name": "Pasta", "order_id": 1004, "price": 800},
    {"name": "Chips", "order_id": 1005, "price": 450},
    {"name": "Sandwich", "order_id": 1006, "price": 300},
    {"name": "Soup", "order_id": 1007, "price": 900},
    {"name": "Fish", "order_id": 1008, "price": 1200},
    {"name": "Tacos", "order_id": 1009, "price": 750},
    {"name": "Sushi", "order_id": 1010, "price": 1500},
]

# Writing to a CSV file
with open('restaurant_items.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "order_id", "price"])
    writer.writeheader()
    for item in restaurant_items:
        writer.writerow(item)

# Reading from the CSV file
def display_menu():
    with open('restaurant_items.csv', mode='r') as file:
        reader = csv.DictReader(file)
        print("Menu:")
        for row in reader:
            print(f"Order ID: {row['order_id']}, Name: {row['name']}, Price: {row['price']}")

# Function to take order from the user
def take_order():
    display_menu()
    orders = []
    total = 0

    while True:
        order_id = input("Enter the Order ID to add to your order (or type 'done' to finish): ")
        if order_id.lower() == 'done':
            break
        with open('restaurant_items.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['order_id'] == order_id:
                    orders.append(row)
                    total += int(row['price'])
                    print(f"Added {row['name']} to your order, Price: {row['price']}")
                    break
            else:
                print("Invalid Order ID. Please try again.")

    print("\nYour Order:")
    for order in orders:
        print(f"Name: {order['name']}, Price: {order['price']}")

    print(f"Total Bill: {total}")

    # Generate bill in a separate file
    bill_filename = f'bill_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
    with open(bill_filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "order_id", "price"])
        writer.writeheader()
        for order in orders:
            writer.writerow(order)
        writer.writerow({"name": "Total", "order_id": "", "price": total})

    # Append to the cumulative orders file
    with open('Total order(Day).csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "order_id", "price"])
        if file.tell() == 0:
            writer.writeheader()  # Write header if file is empty
        for order in orders:
            writer.writerow(order)
        writer.writerow({"name": "Total", "order_id": "", "price": total})

    print(f"\nBill saved to {bill_filename}")

# Generate profit graph
def generate_profit_graph():
    profits = []
    dates = []

    with open('Total order(Day).csv', mode='r') as file:
        reader = csv.DictReader(file)
        current_date = None
        daily_total = 0
        for row in reader:
            if row['name'] == 'Total':
                if current_date:
                    profits.append(daily_total)
                    dates.append(current_date)
                current_date = datetime.now().strftime("%Y-%m-%d")
                daily_total = int(row['price'])
            else:
                daily_total += int(row['price'])

    plt.plot(dates, profits, marker='o')
    plt.xlabel('Date')
    plt.ylabel('Total Profit')
    plt.title('Total Profit Over Time')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    take_order()
    generate_profit_graph()


