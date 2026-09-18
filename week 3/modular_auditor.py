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
    return current_total + new_value


def calculate_tax(amount):
    return amount * 0.10


def generate_report(total_units, failed_attempts):
    print("Total Deliveries Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)


total_inventory = 0
failed_entries = 0

while True:
    stock_quantity = get_valid_input()

    if stock_quantity == "quit":
        break

    if stock_quantity is None:
        failed_entries = failed_entries + 1
        continue

    total_inventory = process_delivery(total_inventory, stock_quantity)
    tax = calculate_tax(stock_quantity)
    print("Accepted. Total inventory is now:", total_inventory)
    print("Tax for this delivery:", tax)

    if total_inventory > 500:
        print("Overstock Alert! Total inventory has exceeded 500 units.")
        break

generate_report(total_inventory, failed_entries)
