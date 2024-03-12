class Item:
    def __init__(self, itemID: int, itemName: str, itemType: str, itemCat:str, ammount: int):
        self.itemID = itemID
        self.itemName = itemName
        self.itemType = itemType
        self.itemCat = itemCat
        self.ammount = ammount
    
    def print(self):
        print(f"ID\t: {self.itemID}")
        print(f"Name\t: {self.itemName}")
        print(f"Type\t: {self.itemType}")
        print(f"Category: {self.itemCat}")
        print(f"Ammount\t: {self.ammount}\n")