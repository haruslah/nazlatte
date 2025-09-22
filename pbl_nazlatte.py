# Program-ID: pbl_nazlatte.py
# Author: Adlie Hadif, Nik Haris, Mohamad Naim
# OS: Windows 11
# Interpreter: Python 3
# Note: Ensure that menus.txt is in the same folder as the program. If the file is missing, the program will still display the menu using the built-in dictionary.

_file = "menus.txt"

try:
    with open(_file, "r") as f:
        Menu = {}   # menu dictionary: key=item number, value=(item name, item price)
                    # new syntax (dictionary literal)
        # build menu dictionary from menus.txt
        for line in f:
            item_number, item_name, item_price = line.strip().split(",")
            Menu[int(item_number)] = (item_name, float(item_price))
            
except FileNotFoundError:
    print("\nFile 'menus.txt' not found.")


#initialize quantity of each item to zero
Quantities = {key: 0 for key in Menu.keys()} 
#new syntax (dictionary comprehension)

# list to store orders
Orders = []               
#new syntax (list literal)

print("Welcome to Nazlatte Cafe!")

while True:
    print("\nSelect an option:")
    print("A = Display menu")
    print("B = Order food")
    print("C = Generate bill")
    print("Q = Quit")

# get user option and convert to uppercase to make it case-insensitive
    option = input("Enter option: ").upper() 

    # option A: display menu from file if exists
    if option == "A":
        print('\n--- MENU ---')
        try:
            with open("menus.txt", "r") as f:
                for line in f:
                    item_number, item_name, item_price = line.strip().split(",")
                    print(f"{item_number}. {item_name} - RM{item_price}")
        except FileNotFoundError:
            print("\nFile 'menus.txt' not found.")
    
 
    # option B: order food
    elif option == "B":
        print("\n--- MENU ---")
        for key, (item, price) in Menu.items():
            print(f"{key}. {item} - RM {price:.2f}")

        while True:
            # get user choice and convert to lowercase to make it case-insensitive
            choice = input("\nEnter item number to order (or type 'done' to finish): ").lower()
            if choice == "done":
                break
            try:
                choice = int(choice)
                if choice in Menu:
                    Orders.append(Menu[choice])
                    print(f"{Menu[choice][0]} added to order.")
                    #add quantity
                    Quantities[choice] += 1
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Please enter a valid number or 'done'.")
                 # option C: generate bill
                 
                 
    elif option == "C":
        if not Orders:
            print("\nNo items ordered yet.")
        else:
            print("\n--- BILL ---")
            total = 0
            for key in Menu:
                qty = Quantities[key]
                if qty > 0:
                    item, price = Menu[key]
                    subtotal = price * qty
                    print(f"{item} x {qty} - RM {subtotal:.2f}")
                    total += subtotal
            print(f"\nTOTAL = RM {total:.2f}")

    # option Q: quit program
    elif option == "Q":
        print("\nThank you for visiting Nazlatte Cafe!")
        break

    # invalid option
    else:
        print("Invalid option. Please try again.")
