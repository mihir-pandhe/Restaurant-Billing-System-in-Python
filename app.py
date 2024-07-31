class RestaurantBillingSystem:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity):
        self.items.append((name, price, quantity))

    def calculate_total(self):
        total = sum(price * quantity for _, price, quantity in self.items)
        return total

    def display_bill(self):
        print("Itemized Bill:")
        for name, price, quantity in self.items:
            print(f"{name} (x{quantity}): ${price:.2f} each")
        print(f"Total: ${self.calculate_total():.2f}")


def main():
    billing_system = RestaurantBillingSystem()

    while True:
        print("\n1. Add item to bill")
        print("2. Display bill")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            billing_system.add_item(name, price, quantity)
        elif choice == "2":
            billing_system.display_bill()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
