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
            json.dump(recordedData, file, sort_keys=False, indent=4, separators=(',', ': '))

    def add_item(self, itemName: str, itemType: str, itemCat: str, ammount: int):
        self.update_recordNum()
        new_item = Item(self.recordNumber, itemName, itemType, itemCat, ammount)
        self.items.append(new_item)
        self.record_items()
        print("Add item: Successful!\n")
    
    def view_item(self):
        self.load_items()

        table = []
        head = ["ID", "Item Name", "Type", "Category", "Ammount"]
        for item in self.items:
            table.append([item.itemID, item.itemName, item.itemType, item.itemCat, item.ammount])
        print(tabulate(table, headers=head, tablefmt="grid"))
    
    def update_item(self):
        id: int = None
        try:
            id = int(input("Item ID: "))
        except (TypeError, ValueError):
            return
        
        for item in self.items:
            if item.itemID == id:
                print("Old Informaton")
                item.print()

                item.itemName = str(input("New item name: "))
                item.itemType = str(input("New item type: "))
                item.itemCat = str(input("New item category: "))
                item.ammount = int(input("New item ammount: "))
                
                self.record_items()
                print(f"Update item (ID = {id}): Successful!")

                return
        
        print("Item not found!")
    
    def delete_item(self):
        id: int = None
        try:
            id = int(input("Item ID: "))
        except (TypeError, ValueError):
            return
        
        for item in self.items:
            if item.itemID == id:
                item.print()
                confirmation = str(input("Are you sure to delete this item? (Y/n): "))
                
                if confirmation.lower() in ['y', 'yes']:
                    self.items.remove(item)
                    self.record_items()
                    print(f"Delete item (ID = {id}): Successful!")

                elif confirmation.lower() in ['n', 'no']:
                    pass
                
                else:
                    print("Error: Invalid answer")
                
                return
        
        print("Item not found!")
    
    def clear_item(self):
        print("Warning!\nThis action will deleting all data from the list.")
        confirmation = str(input("Are you sure to continue? (Y/n): "))

        if confirmation.lower() in ['y', 'yes']:
            self.items = []
            self.record_items()

            print("Clear item(s): Successful")