import time

class PharmacyProduct:
    def __init__(self, product_id, name, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        return f"ID: {self.product_id} | Name: {self.name} | Price: RM{self.price:.2f} | Stock: {self.stock_quantity}"

class LinearProbeHashTable:
    def __init__(self, size=100):
        self.size = size
        self.slots = [None] * self.size

    def hash_function(self, key):
        return key % self.size

    def insert(self, product):
        index = self.hash_function(product.product_id)
        start_index = index

        while self.slots[index] is not None:
            if self.slots[index].product_id == product.product_id:
                self.slots[index] = product
                return index
            index = (index + 1) % self.size
            if index == start_index:
                raise Exception("Hash Table is Full!")

        self.slots[index] = product
        return index

    def search(self, product_id):
        index = self.hash_function(product_id)
        start_index = index

        while self.slots[index] is not None:
            if self.slots[index].product_id == product_id:
                return self.slots[index], index
            index = (index + 1) % self.size
            if index == start_index:
                break

        return None, -1

def search_array(array, product_id):
    for product in array:
        if product.product_id == product_id:
            return product
    return None

# --- NEW HELPER FUNCTION ---
def get_valid_number(prompt, num_type):
    """Keeps asking for input until a valid number is provided."""
    while True:
        try:
            return num_type(input(prompt))
        except ValueError:
            print("Invalid input! Please enter numbers only (no letters or symbols).")
# ---------------------------

def main():
    hash_table = LinearProbeHashTable(size=100)
    array_storage = []

    sample_products = [
        PharmacyProduct(1042, "Paracetamol 500mg", 5.90, 120),
        PharmacyProduct(1005, "Amoxicillin 250mg", 12.50, 45),
        PharmacyProduct(1088, "Ibuprofen 400mg", 8.20, 80),
        PharmacyProduct(1012, "Cetirizine 10mg", 6.00, 60),
    ]

    for prod in sample_products:
        hash_table.insert(prod)
        array_storage.append(prod)

    while True:
        print("\n==== Pharmacy Inventory System ====")
        print("1. Insert Product")
        print("2. Search Product")
        print("3. Exit")
        choice = input("Enter choice: ").strip()

        if choice == '1':
            # Uses the helper function to ensure valid inputs
            pid = get_valid_number("Enter Product ID: ", int)
            name = input("Enter Product Name: ")
            price = get_valid_number("Enter Price: ", float)
            stock = get_valid_number("Enter Stock Quantity: ", int)

            try:
                new_product = PharmacyProduct(pid, name, price, stock)
                slot = hash_table.insert(new_product)
                array_storage.append(new_product)
                print(f"Product inserted successfully into slot [{slot}]")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '2':
            search_id = get_valid_number("Enter Product ID to search: ", int)

            start_hash = time.perf_counter()
            found_ht, slot = hash_table.search(search_id)
            end_hash = time.perf_counter()
            time_hash = end_hash - start_hash

            start_arr = time.perf_counter()
            found_arr = search_array(array_storage, search_id)
            end_arr = time.perf_counter()
            time_arr = end_arr - start_arr

            if found_ht:
                print("\nProduct Found!")
                print(found_ht)
                print(f"Search completed in {time_hash:.6f} seconds (Hash Table)")
                print(f"Search completed in {time_arr:.6f} seconds (Array - same record)")
            else:
                print("\nProduct not found!")

        elif choice == '3':
            print("Exiting Inventory System. Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()