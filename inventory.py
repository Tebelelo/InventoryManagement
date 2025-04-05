class InventoryManagement():
    
    def __init__(self,store_name:str):
        self.items_list = []
        self.quantity_and_item = {}
        self.store_name = store_name
        
        
    def add_item(self) -> dict:
        
        print("Add item and price")
        
        #data validation
        while True:
            item = input("Item: ").lower().strip()
            if item.isalnum():
                break
            else:
                print("Enter correct item name")
        
        while True:
            try:
                price = int(input("Price: "))
                break
            except ValueError:
                print("Enter correct price,try again")
        
        self.items_list.append(item)
        
        
        #checking if the item already exist in the a dictionary, if it does only update the quantity.
        for product in self.items_list:
            if product in self.quantity_and_item.keys():
                self.quantity_and_item[product] = {'Quantity':self.items_list.count(product),'Price':self.quantity_and_item[product]['Price']}
            else:
                self.quantity_and_item[product] = {'Quantity':self.items_list.count(product),'Price':price}  
                
        return self.quantity_and_item
    
    
    def update_item_price(self) ->dict:
        #Checking if the item exist in the a dictionary before updating it
        print("Update item price")
        try:
            item = input("Item: ")
            new_price = int(input("Price: "))
            self.quantity_and_item[item.lower()]['Price'] = new_price
        except KeyError:
            print('Item does not exist')
            
        return self.quantity_and_item
    
    
    def delete_item(self) -> dict:
        print("Delete item")
        while True:
            try:
                if self.quantity_and_item:
                    self.item_to_be_deleted = input('Which item do you want to remove from inventory? ')
                    self.quantity_and_item.pop(self.item_to_be_deleted.lower().strip())
                    print(f"Item deleted!")
                    break
                else:
                    print("There is nothing in the shelf,add first")
                    break
            except KeyError:
                print('Item not found,try again')   
                  
        return self.quantity_and_item
    

    def inventory_summary(self) ->str:
        #Display all the items and total revenue
        self.total_revenue = 0
        if self.quantity_and_item:
            print('Here is the inventory list')
            for key,values in self.quantity_and_item.items():
                print(f'{key[0].upper()+key[1:]}:{values}')
                print(" ")
                
            for key,values in self.quantity_and_item.items():
                self.total_revenue += (values['Quantity'] * values['Price'])
            
            print(f"The total revenue is: R{self.total_revenue}")
        else:
            print(f"{self.store_name} shelf is empty, add some items")
            


def main():
    store_input = input("What is your store name: ").lower().strip()
    store_name = InventoryManagement(store_input)
    
    functionalies = ["add item","update item price","delete item","display products","exit"]
    functionalies_ = ["Add Item","Update Item Price","Delete Item","Display Products","Exit"]
    functions_num = ["1","2","3","4","5"]
    print("Here are the options")
    for num,item in enumerate(functionalies_):
        print(f"{num+1}:{item}")
        
    open = True
    while open:
        print()
        option = input("Your option:").lower().strip()
        if option in functionalies or option in functions_num:
            if option == "add item" or option == "1":
                store_name.add_item()
                continue
                
            elif option == "update item price" or option == "2":
                store_name.update_item_price()
                continue
                
            elif option == "delete item" or option =="3":
                store_name.delete_item()
                continue
               
            elif option == "display products" or option == "4":
                store_name.inventory_summary()
                continue
                
            elif option == "exit" or option == "5":
                break
        else:
            print("Choose the correct functionality")
            continue
    
    
if __name__ == "__main__":
    main()
    