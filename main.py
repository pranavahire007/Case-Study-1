
# Customer Service Management System Using Queue

customers = []


def add_customer():
    name = input("Enter customer name: ").strip()

    if name:
        customers.append(name)
        print(name, "has been added to the waiting queue.")
    else:
        print("Customer name cannot be empty!")


def serve_customer():
    if not customers:
        print("No customers waiting for service.")
    else:
        name = customers.pop(0)
        print("Now serving customer:", name)


def display_queue():
    if not customers:
        print("The waiting queue is empty.")
    else:
        print("\nCustomers Waiting for Service:")
        print("-" * 35)

        for position, name in enumerate(customers, start=1):
            print(f"{position}. {name}")

        print("-" * 35)


def search_customer():
    name = input("Enter customer name to search: ").strip()

    for position, customer in enumerate(customers, start=1):
        if customer.lower() == name.lower():
            print(f"{name} is waiting at position {position}.")
            return

    print(name, "is not in the waiting queue.")


def queue_status():
    print("Total customers waiting:", len(customers))


while True:
    print("\n===== Customer Service Management System =====")
    print("1. Add Customer")
    print("2. Serve Customer")
    print("3. Display Waiting Queue")
    print("4. Search Customer")
    print("5. Queue Status")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_customer()

    elif choice == "2":
        serve_customer()

    elif choice == "3":
        display_queue()

    elif choice == "4":
        search_customer()

    elif choice == "5":
        queue_status()

    elif choice == "6":
        print("Thank you for using Customer Service Management System!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 6.")
