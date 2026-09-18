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


total_inventory = 0
failed_entries = 0

while True:
    user_input = input("Enter stock quantity (or 'quit' to stop): ")

    if user_input == "quit":
        break

    if not user_input.isdigit():
        print("Error: please enter a whole number.")
        failed_entries = failed_entries + 1
        continue

    stock_quantity = int(user_input)

    if stock_quantity < 0:
        print("Error: negative stock quantity is not allowed.")
        failed_entries = failed_entries + 1
        continue

    total_inventory = total_inventory + stock_quantity
    print("Accepted. Total inventory is now:", total_inventory)

    if total_inventory > 500:
        print("Overstock Alert! Total inventory has exceeded 500 units.")
        break

print("Total Units Processed:", total_inventory)
print("Number of Failed/Rejected Entries:", failed_entries)
