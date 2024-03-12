from item_list import ItemApp

def main():
    app = ItemApp()
    while True:
        print("\nItem List App:")
        print("1. Add Item")
        print("2. View Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Clear Item")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            itemName = input("Enter item name: ")
            itemType = input("Enter item type: ")
            itemCat = input("Enter item category: ")
            ammount = input("Enter item ammount: ")
            app.add_item(itemName, itemType, itemCat, ammount)

        elif choice == '2':
            app.view_item()
            print()

        elif choice == '3':
            app.update_item()

        elif choice == '4':
            app.delete_item()

        elif choice == '5':
            app.clear_item()

        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()