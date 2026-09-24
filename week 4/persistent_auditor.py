import os


def load_inventory():
    total = 0
    history = []

    if not os.path.exists("inventory.txt"):
        print("No inventory file found. Starting with empty inventory.")
        return total, history

    file = open("inventory.txt", "r")
    lines = file.readlines()
    file.close()

    if len(lines) > 0:
        total = int(lines[0])

    for line in lines[1:]:
        history.append(int(line))

    print("Loaded inventory. Current total:", total)
    return total, history


def save_inventory(total, history):
    file = open("inventory.txt", "w")
    file.write(str(total) + "\n")
    for amount in history:
        file.write(str(amount) + "\n")
    file.close()
    print("Inventory saved to inventory.txt")


def get_valid_input():
    user_input = input("Enter stock quantity (or 'quit' to stop): ")

    if user_input == "quit":
        return "quit"

    if not user_input.isdigit():
        print("Error: please enter a whole number.")
        return None

    stock_quantity = int(user_input)

    if stock_quantity < 0:
        print("Error: negative stock quantity is not allowed.")
        return None

    return stock_quantity


def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total


def calculate_tax(amount):
    tax = amount * 0.10
    return tax


def generate_report(total_units, failed_attempts):
    print("Total Deliveries Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)


total_inventory, history = load_inventory()
failed_entries = 0

while True:
    result = get_valid_input()

    if result == "quit":
        break

    if result is None:
        failed_entries = failed_entries + 1
        continue

    total_inventory = process_delivery(total_inventory, result)
    history.append(result)
    tax = calculate_tax(result)
    print("Accepted. Total inventory is now:", total_inventory)
    print("Tax for this delivery:", tax)

    if total_inventory > 500:
        print("Overstock Alert! Total inventory has exceeded 500 units.")
        break

generate_report(total_inventory, failed_entries)
print("Transaction History:", history)
save_inventory(total_inventory, history)
