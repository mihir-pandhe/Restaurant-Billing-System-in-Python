class RestaurantBillingSystem:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity):
        self.items.append((name, price, quantity))

    def remove_item(self, name):
        self.items = [item for item in self.items if item[0] != name]

    def update_quantity(self, name, quantity):
        for i, item in enumerate(self.items):
            if item[0] == name:
                self.items[i] = (name, item[1], quantity)
                break

    def calculate_total(self):
        total = sum(price * quantity for _, price, quantity in self.items)
        return total

    def display_bill(self):
        print("Itemized Bill:")
        for name, price, quantity in self.items:
            print(f"{name} (x{quantity}): ${price:.2f} each")
        print(f"Total: ${self.calculate_total():.2f}")

    def display_summary(self):
        print(f"Total number of items: {len(self.items)}")
        print(f"Total bill amount: ${self.calculate_total():.2f}")


def main():
    billing_system = RestaurantBillingSystem()

    while True:
        print("\n1. Add item to bill")
        print("2. Remove item from bill")
        print("3. Update item quantity")
        print("4. Display bill")
        print("5. Display summary")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter item name: ")
            try:
                price = float(input("Enter item price: "))
                quantity = int(input("Enter item quantity: "))
                billing_system.add_item(name, price, quantity)
            except ValueError:
                print(
                    "Invalid input. Price should be a number and quantity should be an integer."
                )
        elif choice == "2":
            name = input("Enter item name to remove: ")
            billing_system.remove_item(name)
        elif choice == "3":
            name = input("Enter item name to update: ")
            try:
                quantity = int(input("Enter new item quantity: "))
                billing_system.update_quantity(name, quantity)
            except ValueError:
                print("Invalid input. Quantity should be an integer.")
        elif choice == "4":
            billing_system.display_bill()
        elif choice == "5":
            billing_system.display_summary()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
