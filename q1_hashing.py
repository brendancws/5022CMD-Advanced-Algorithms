
import time  # Imports the time module to measure how long searching takes


# ============================================================
# CLASS 1: PHARMACY PRODUCT
# ============================================================
# This class represents a single product in the pharmacy.
# Each product contains four important attributes:
# 1. Product ID - A unique number used to identify the product
# 2. Name - The name of the medicine or pharmacy product
# 3. Price - The selling price of the product in Malaysian Ringgit
# 4. Stock Quantity - The number of units available in inventory
#
# Using a class allows the system to store all information
# belonging to one product together as a single object.
# ============================================================

class PharmacyProduct:

    # Constructor method that runs whenever a new product is created.
    # It receives the product details and stores them in the object.
    def __init__(self, product_id, name, price, stock_quantity):
        self.product_id = product_id  # Stores the unique product ID
        self.name = name  # Stores the product name
        self.price = price  # Stores the selling price
        self.stock_quantity = stock_quantity  # Stores available stock

    # Defines how the product information appears when printed.
    # The price is formatted to display exactly two decimal places.
    def __str__(self):
        return f"ID: {self.product_id} | Name: {self.name} | Price: RM{self.price:.2f} | Stock: {self.stock_quantity}"


# ============================================================
# CLASS 2: LINEAR PROBING HASH TABLE
# ============================================================
# This class implements a hash table using linear probing.
#
# A hash table stores products at positions calculated using
# a hash function instead of searching through every product.
#
# Linear probing is a collision-handling technique.
# A collision happens when two product IDs produce the same
# hash index.
#
# When a collision occurs, the program checks the next
# available slot until it finds an empty position.
#
# This allows products with different IDs to be stored
# even when they produce the same initial hash index.
# ============================================================

class LinearProbeHashTable:

    # Initializes the hash table with a default size of 100 slots.
    # Every slot is initially set to None, meaning it is empty.
    def __init__(self, size=100):
        self.size = size  # Maximum number of slots in the hash table
        self.slots = [None] * self.size  # Creates empty storage slots

    # --------------------------------------------------------
    # HASH FUNCTION
    # --------------------------------------------------------
    # Calculates the index where a product should be stored.
    #
    # The modulo operator (%) returns the remainder after
    # dividing the product ID by the size of the hash table.
    #
    # Formula:
    # Hash Index = Product ID % Table Size
    #
    # Example:
    # Product ID = 1042
    # Table Size = 100
    # Hash Index = 1042 % 100 = 42
    #
    # Therefore, product 1042 will initially use slot 42.
    # --------------------------------------------------------

    def hash_function(self, key):
        return key % self.size

    # --------------------------------------------------------
    # INSERT FUNCTION
    # --------------------------------------------------------
    # Inserts a new pharmacy product into the hash table.
    #
    # Steps:
    # 1. Calculate the product's hash index.
    # 2. Check whether the calculated slot is empty.
    # 3. If occupied, compare the existing product ID.
    # 4. If the ID matches, replace the existing product.
    # 5. Otherwise, move to the next slot using linear probing.
    # 6. Continue until an empty slot is found.
    #
    # The modulo operation allows probing to wrap around
    # to the beginning of the table after reaching the end.
    #
    # If every slot is occupied, an exception is raised.
    # --------------------------------------------------------

    def insert(self, product):

        # Calculates the initial index based on the product ID.
        index = self.hash_function(product.product_id)

        # Remembers the starting position to detect a full table.
        start_index = index

        # Repeats while the current slot already contains a product.
        while self.slots[index] is not None:

            # Checks whether the existing product has the same ID.
            # If it does, the existing product is updated.
            if self.slots[index].product_id == product.product_id:
                self.slots[index] = product
                return index

            # Linear probing: move forward by one slot.
            # Modulo ensures that the index stays within table size.
            index = (index + 1) % self.size

            # If probing returns to the original position,
            # all slots have been checked and the table is full.
            if index == start_index:
                raise Exception("Hash Table is Full!")

        # Stores the product in the first available empty slot.
        self.slots[index] = product

        # Returns the slot number where the product was inserted.
        return index

    # --------------------------------------------------------
    # SEARCH FUNCTION
    # --------------------------------------------------------
    # Searches for a pharmacy product using its product ID.
    #
    # The search begins at the index generated by the
    # hash function.
    #
    # If the product is not at the initial index, linear
    # probing checks the following slots one by one.
    #
    # The process stops when:
    # 1. The matching product is found.
    # 2. An empty slot is reached.
    # 3. The search returns to its starting index.
    #
    # If found, the function returns the product and slot.
    # Otherwise, it returns None and -1.
    # --------------------------------------------------------

    def search(self, product_id):

        # Calculates the starting hash index.
        index = self.hash_function(product_id)

        # Saves the starting index to prevent an infinite loop.
        start_index = index

        # Continues searching while the current slot is occupied.
        while self.slots[index] is not None:

            # Compares the stored product ID with the requested ID.
            if self.slots[index].product_id == product_id:

                # Returns the matching product and its slot index.
                return self.slots[index], index

            # Moves to the next slot when the ID does not match.
            index = (index + 1) % self.size

            # Stops when every possible slot has been checked.
            if index == start_index:
                break

        # Indicates that the requested product was not found.
        return None, -1


# ============================================================
# FUNCTION 3: LINEAR SEARCH USING ARRAY
# ============================================================
# This function searches for a product in a normal Python list.
#
# Unlike a hash table, an array-based linear search checks
# products sequentially from the beginning of the list.
#
# Each product ID is compared with the requested ID.
#
# The search stops when the matching product is found.
# If no matching product exists, the function returns None.
#
# This function is used to compare the search performance
# of an array against the linear probing hash table.
#
# Time complexity:
# Best case: O(1) - Product is the first element.
# Worst case: O(n) - Product is last or not present.
# ============================================================

def search_array(array, product_id):

    # Loops through each product stored in the array.
    for product in array:

        # Checks whether the current product ID matches.
        if product.product_id == product_id:

            # Returns the product immediately if found.
            return product

    # Returns None if no matching product exists.
    return None


# ============================================================
# FUNCTION 4: INPUT VALIDATION
# ============================================================
# This helper function ensures the user enters a valid number.
#
# It accepts two parameters:
# prompt - The message displayed to the user.
# num_type - The required numerical data type (int or float).
#
# The try-except block prevents the program from crashing
# when the user accidentally enters invalid input.
#
# For example:
# Enter Product ID: abc
# Result: Invalid input message is displayed.
#
# The function continues asking until a valid number is given.
#
# This improves reliability and makes the system easier to use.
# ============================================================

def get_valid_number(prompt, num_type):

    # Repeats until the user enters a valid numeric value.
    while True:
        try:

            # Reads the input and converts it into int or float.
            # Returns the converted value if successful.
            return num_type(input(prompt))

        except ValueError:

            # Handles invalid numerical input without terminating
            # the program and asks the user to try again.
            print("Invalid input! Please enter numbers only (no letters or symbols).")


# ============================================================
# FUNCTION 5: MAIN PROGRAM
# ============================================================
# This is the main function that controls the entire
# Pharmacy Inventory System.
#
# Main responsibilities:
# 1. Initialize the hash table and array storage.
# 2. Insert predefined sample pharmacy products.
# 3. Display the inventory menu.
# 4. Allow the user to insert new products.
# 5. Allow the user to search for existing products.
# 6. Compare hash table and array search execution times.
# 7. Exit the program when requested.
# ============================================================

def main():

    # Creates a hash table containing 100 storage slots.
    hash_table = LinearProbeHashTable(size=100)

    # Creates an empty Python list for array-based storage.
    # This list is used for search performance comparison.
    array_storage = []

    # --------------------------------------------------------
    # INITIAL SAMPLE PRODUCTS
    # --------------------------------------------------------
    # Four predefined pharmacy products are created.
    #
    # These products allow the system to demonstrate
    # insertion and searching immediately after startup.
    #
    # Each product includes:
    # Product ID, Name, Price, and Stock Quantity.
    # --------------------------------------------------------

    sample_products = [
        PharmacyProduct(1042, "Paracetamol 500mg", 5.90, 120),
        PharmacyProduct(1005, "Amoxicillin 250mg", 12.50, 45),
        PharmacyProduct(1088, "Ibuprofen 400mg", 8.20, 80),
        PharmacyProduct(1012, "Cetirizine 10mg", 6.00, 60),
    ]

    # Stores every sample product in both data structures.
    # This ensures the same products are available when
    # comparing hash table search with array linear search.
    for prod in sample_products:

        # Inserts the product into the linear probing hash table.
        hash_table.insert(prod)

        # Adds the same product object to the normal Python list.
        array_storage.append(prod)

    # --------------------------------------------------------
    # MAIN MENU LOOP
    # --------------------------------------------------------
    # The menu runs continuously until the user chooses Exit.
    # The while True loop keeps the system active so users
    # can perform multiple operations during one session.
    # --------------------------------------------------------

    while True:

        # Displays the available inventory management options.
        print("\n==== Pharmacy Inventory System ====")
        print("1. Insert Product")
        print("2. Search Product")
        print("3. Exit")

        # Reads the user's menu selection.
        # strip() removes unnecessary spaces around the input.
        choice = input("Enter choice: ").strip()

        # ====================================================
        # OPTION 1: INSERT PRODUCT
        # ====================================================
        # Allows users to enter the details of a new product.
        #
        # The product ID, price, and stock quantity are
        # checked using the numerical validation function.
        #
        # After creating the product object, the program
        # inserts it into the hash table and array storage.
        # ====================================================

        if choice == '1':

            # Accepts the product ID as an integer.
            # Invalid input causes the program to ask again.
            pid = get_valid_number("Enter Product ID: ", int)

            # Accepts the product name as text.
            name = input("Enter Product Name: ")

            # Accepts the product price as a floating-point number.
            price = get_valid_number("Enter Price: ", float)

            # Accepts the quantity of available stock as an integer.
            stock = get_valid_number("Enter Stock Quantity: ", int)

            try:

                # Creates a new product object using user input.
                new_product = PharmacyProduct(pid, name, price, stock)

                # Inserts the product into the hash table.
                # The returned value indicates its storage slot.
                slot = hash_table.insert(new_product)

                # Also adds the product to the array so both
                # structures can be used for searching.
                array_storage.append(new_product)

                # Displays confirmation and the assigned hash slot.
                print(f"Product inserted successfully into slot [{slot}]")

            except Exception as e:

                # Displays an error if insertion fails,
                # such as when the hash table is full.
                print(f"Error: {e}")

        # ====================================================
        # OPTION 2: SEARCH PRODUCT
        # ====================================================
        # Allows the user to find a product by its unique ID.
        #
        # The same product is searched for in two structures:
        # 1. Linear probing hash table
        # 2. Normal Python array
        #
        # time.perf_counter() records high-resolution time
        # measurements before and after each search.
        #
        # Execution Time = End Time - Start Time
        #
        # These measurements help demonstrate the performance
        # differences between hash table and linear search.
        # ====================================================

        elif choice == '2':

            # Requests a product ID and ensures it is an integer.
            search_id = get_valid_number("Enter Product ID to search: ", int)

            # ------------------------------------------------
            # HASH TABLE SEARCH PERFORMANCE
            # ------------------------------------------------

            # Records the time immediately before searching.
            start_hash = time.perf_counter()

            # Searches the hash table using linear probing.
            # Returns the matching product and hash slot.
            found_ht, slot = hash_table.search(search_id)

            # Records the time immediately after searching.
            end_hash = time.perf_counter()

            # Calculates the hash table search execution time.
            time_hash = end_hash - start_hash

            # ------------------------------------------------
            # ARRAY LINEAR SEARCH PERFORMANCE
            # ------------------------------------------------

            # Records the time before starting the array search.
            start_arr = time.perf_counter()

            # Performs sequential linear search through the list.
            found_arr = search_array(array_storage, search_id)

            # Records the time after the array search finishes.
            end_arr = time.perf_counter()

            # Calculates the array search execution time.
            time_arr = end_arr - start_arr

            # ------------------------------------------------
            # DISPLAY SEARCH RESULTS
            # ------------------------------------------------

            # Checks whether the product was found in the hash table.
            if found_ht:

                # Displays a success message.
                print("\nProduct Found!")

                # Displays the product's complete information.
                # The __str__ method formats the output.
                print(found_ht)

                # Displays the hash table search execution time.
                # Six decimal places are shown for precision.
                print(f"Search completed in {time_hash:.6f} seconds (Hash Table)")

                # Displays the array linear search execution time.
                # Both timings can be compared to evaluate speed.
                print(f"Search completed in {time_arr:.6f} seconds (Array - same record)")

            else:

                # Displays a message when the product ID
                # cannot be found in the hash table.
                print("\nProduct not found!")

        # ====================================================
        # OPTION 3: EXIT PROGRAM
        # ====================================================
        # Terminates the main menu loop and ends the program.
        # ====================================================

        elif choice == '3':

            # Displays a farewell message before exiting.
            print("Exiting Inventory System. Goodbye!")

            # Stops the while True loop.
            break

        # ====================================================
        # INVALID MENU SELECTION
        # ====================================================
        # Handles menu inputs other than 1, 2, or 3.
        # The menu is displayed again for another attempt.
        # ====================================================

        else:
            print("Invalid choice, try again.")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================
# The condition below checks whether this Python file
# is being executed directly.
#
# If the file is run directly, the main() function starts.
#
# If this file is imported into another Python program,
# main() will not execute automatically.
#
# This is a standard Python programming practice.
# ============================================================

if __name__ == "__main__":
    main()
