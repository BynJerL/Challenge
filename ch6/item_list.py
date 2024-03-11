import json
from item import Item
from tabulate import tabulate

class ItemApp:
    def __init__(self):
        self.items = []
        self.recordNumber = 0
        self.load_items()
    
    def load_items(self):
        try:
            with open("items.json", "r") as file:
                data = json.load(file)
                for item_data in data:
                    item = Item(item_data['itemID'], item_data['itemName'], item_data['itemType'], item_data['itemCat'], item_data['ammount'])
                    self.items.append(item)

        except FileNotFoundError:
            # print("Fail to load file")
            pass
    
    def update_recordNum(self):
        tempNumber = 1
        numbers = []

        try:
            for item in self.items:
                numbers.append(item.itemID)

        except Exception:
            pass
        
        numbers.sort()
        for number in numbers:
            if number != tempNumber:
                break
            else:
                tempNumber += 1

        self.recordNumber = tempNumber

    def record_items(self):
        with open("items.json", "w") as file:
            recordedData = []
            for item in self.items:
                recordedData.append({'itemID': item.itemID, 'itemName' : item.itemName, 'itemType' : item.itemType, 'itemCat': item.itemCat, 'ammount' : item.ammount})
            json.dump(recordedData, file)

    def add_item(self, itemName: str, itemType: str, itemCat: str, ammount: int):
        self.update_recordNum()
        new_item = Item(self.recordNumber, itemName, itemType, itemCat, ammount)
        self.items.append(new_item)
        self.record_items()
        print("Add item: Success!\n")
    
    def view_item(self):
        table = []
        head = ["ID", "Item Name", "Type", "Category", "Ammount"]
        for item in self.items:
            table.append([item.itemID, item.itemName, item.itemType, item.itemCat, item.ammount])
        print(tabulate(table, headers=head, tablefmt="grid"))
    
    def update_item(self):
        # Will be added soon
        pass
    
    def delete_item(self):
        # Will be added soon
        pass

def main():
    app = ItemApp()
    while True:
        print("\nItem List App:")
        print("1. Add Item")
        print("2. View Item")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            itemName = input("Enter item name: ")
            itemType = input("Enter item type: ")
            itemCat = input("Enter item category: ")
            ammount = input("Enter item ammount: ")
            app.add_item(itemName, itemType, itemCat, ammount)

        elif choice == '2':
            app.view_item()

        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()