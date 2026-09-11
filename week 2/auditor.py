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
