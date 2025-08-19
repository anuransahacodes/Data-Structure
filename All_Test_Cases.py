# Inventory Management System

# Store products in a list, each product is represented as a dictionary
inventory = []
MAX_CAPACITY = 100  # Maximum allowed items in the inventory


def add_or_update_product():
    """Add a new product or update the quantity of an existing one."""
    if len(inventory) >= MAX_CAPACITY:
        print("Inventory is full. Cannot add more products.")
        return

    sku = input("Enter Product SKU: ").strip()
    if not sku:
        print("Error: SKU cannot be empty.")
        return

    # Check if product already exists
    for product in inventory:
        if product['sku'] == sku:
            try:
                extra_qty = int(input("Enter additional quantity: "))
                if extra_qty <= 0:
                    print("Error: Quantity must be positive.")
                    return
                product['quantity'] += extra_qty
                print("Quantity updated successfully.")
                return
            except ValueError:
                print("Invalid input. Quantity must be a number.")
                return

    # Add new product
    name = input("Enter Product Name: ").strip()
    if not name:
        print("Error: Product name cannot be empty.")
        return

    try:
        qty = int(input("Enter Quantity: "))
        if qty <= 0:
            print("Error: Quantity must be positive.")
            return
    except ValueError:
        print("Invalid input. Quantity must be a number.")
        return

    inventory.append({'sku': sku, 'name': name, 'quantity': qty})
    print("Product added successfully.")


def show_inventory():
    """Display all products in the inventory."""
    if not inventory:
        print("Inventory is empty.")
        return

    print("\nCurrent Inventory:")
    print("SKU\t\tProduct Name\t\tQuantity")
    print("-" * 50)
    for product in inventory:
        print(f"{product['sku']}\t\t{product['name']}\t\t{product['quantity']}")
    print()


def search_by_sku():
    """Search for a product by its SKU."""
    sku = input("Enter SKU to search: ").strip()
    for product in inventory:
        if product['sku'] == sku:
            print(f"Found: SKU={product['sku']}, Name={product['name']}, Quantity={product['quantity']}")
            return
    print("No product found with that SKU.")


def search_by_name():
    """Search for a product by its name."""
    name = input("Enter Product Name to search: ").strip().lower()
    for product in inventory:
        if product['name'].lower() == name:
            print(f"Found: SKU={product['sku']}, Name={product['name']}, Quantity={product['quantity']}")
            return
    print("No product found with that name.")


def delete_product():
    """Delete a product from the inventory by SKU."""
    sku = input("Enter SKU to delete: ").strip()
    for product in inventory:
        if product['sku'] == sku:
            inventory.remove(product)
            print(f"Product '{product['name']}' deleted.")
            return
    print("No product found with that SKU.")


def main():
    """Main menu loop for inventory management."""
    while True:
        print("\n=== Inventory Manager ===")
        print("1. Add / Update Product")
        print("2. Show Inventory")
        print("3. Search by SKU")
        print("4. Search by Name")
        print("5. Delete Product")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            add_or_update_product()
        elif choice == '2':
            show_inventory()
        elif choice == '3':
            search_by_sku()
        elif choice == '4':
            search_by_name()
        elif choice == '5':
            delete_product()
        elif choice == '6':
            print("Exiting Inventory Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 6.")


# Run the program
if __name__ == "__main__":
    main()
