# Start with an empty shopping list
shopping_list = []

def display_menu():
<<<<<<< HEAD
    print(f"--- Shopping List Manager ---")
=======
    print("Shopping List Manager")
>>>>>>> 7be34fce93b1598af5a21076facc6c99d4d44b9e
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

def main():
<<<<<<< HEAD
    global shopping_list 
    while True:      

       display_menu()
       choice = input("Enter your choice (1-4): ").strip()

=======
    while True:
        display_menu()
        choice = input("Enter your choice: ")
>>>>>>> 7be34fce93b1598af5a21076facc6c99d4d44b9e
       if choice == '1':
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)
            print(f"'{item}' has been added to your shopping list.")
        elif choice == '2':
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")
        elif choice == '3':
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                print("Your Shopping List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    if __name__ == "__main__":
        main()
    

