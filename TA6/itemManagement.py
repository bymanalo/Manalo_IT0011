class Item:
    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price
    
    def __str__(self):
        return f"ID: {self.item_id}, Name: {self.name}, Description: {self.description}, Price: {self.price:.2f} PHP"

class ItemManager:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, name, description, price):
        try:
            if item_id in self.items:
                raise ValueError("Item ID already exists.")
            if not name.strip():
                raise ValueError("Item name cannot be empty.")
            if price < 0:
                raise ValueError("Price cannot be negative.")
            
            self.items[item_id] = Item(item_id, name, description, price)
            print("Item added successfully!")
        except ValueError as e:
            print(f"Error: {e}")

    def view_items(self):
        if not self.items:
            print("No items available.")
        else:
            for item in self.items.values():
                print(item)
    
    def update_item(self, item_id, name=None, description=None, price=None):
        try:
            if not self.items:
                print("No items available to update.")
                return
            if item_id not in self.items:
                raise KeyError("Item ID not found.")
            if name:
                if not name.strip():
                    raise ValueError("Item name cannot be empty.")
                self.items[item_id].name = name
            if description:
                self.items[item_id].description = description
            if price is not None:
                if price < 0:
                    raise ValueError("Price cannot be negative.")
                self.items[item_id].price = price
            print("Item updated successfully!")
        except (KeyError, ValueError) as e:
            print(f"Error: {e}")
    
    def delete_item(self, item_id):
        try:
            if not self.items:
                print("No items available to delete.")
                return
            if item_id not in self.items:
                raise KeyError("Item ID not found.")
            del self.items[item_id]
            print("Item deleted successfully!")
        except KeyError as e:
            print(f"Error: {e}")

def get_valid_id(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def item_manager():
    manager = ItemManager()
    while True:
        print("\nItem Management Application")
        print("[1] Add Item")
        print("[2] View Items")
        print("[3] Update Item")
        print("[4] Delete Item")
        print("[5] Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            item_id = get_valid_id("Enter Item ID: ")
            name = input("Enter Item Name: ")
            description = input("Enter Description: ")
            try:
                price = float(input("Enter Price: "))
                manager.add_item(item_id, name, description, price)
            except ValueError:
                print("Invalid input. Price must be a number.")
        elif choice == "2":
            manager.view_items()
        elif choice == "3":
            if not manager.items:
                print("No items available to update.")
                continue
            item_id = get_valid_id("Enter Item ID to update: ")
            name = input("Enter new name (leave blank to keep unchanged): ") or None
            description = input("Enter new description (leave blank to keep unchanged): ") or None
            price_input = input("Enter new price (leave blank to keep unchanged): ")
            price = float(price_input) if price_input else None
            manager.update_item(item_id, name, description, price)
        elif choice == "4":
            if not manager.items:
                print("No items available to delete.")
                continue
            item_id = get_valid_id("Enter Item ID to delete: ")
            manager.delete_item(item_id)
        elif choice == "5":
            print("Thank you for using the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    item_manager()