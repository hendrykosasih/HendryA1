"""
This program is to load all of the items for the csv file and will show to the user how many items are loaded. Next,
user can choose either to list all of the items, hire an item, return an item, or add new item to stock. All of the
user's input are error-checked and error messages are shown if user enters the wrong input. Lastly, if the user quits
the program, it will then show how many items left in the csv file and terminate itself.
"""

"""
By : Hendry
Github URL : https://github.com/hendrykosasih/HendryA1.git
"""

def load_item():    #This function is to load all items from the csv file
    item_import=open("inventory.csv","r")   #Import items from csv file
    item_no=0   #number of items
    item_stock = [] #To make a list for all items
    for each_line in item_import:
        item_name, item_description, item_price, availability = each_line.strip().split(",")
        item = [item_no, item_name, item_description, float(item_price), availability]
        item_no += 1
        item_stock.append(item) #To add the item to item stock
    item_import.close() #Close the file
    return item_stock   #Return the stock of the item

def list_item(item):    #This function is to arrange the list structure
    list_of_item = ("{} - {:<40s} = ${:>7.2f}".format(item[0], item[1] + "(" + item[2] + ")", item[3]))#Print list of available items
    return list_of_item #Return list of the item


print("Items for Hire - by Hendry") #Welcome messages
item_stock = load_item()    #item stock assigns to load item
print("{} items loaded from inventory.csv".format(len(item_stock))) #Showing how many items are loaded from the csv file
while True:
    print("Menu:\n(L)ist all items\n(H)ire an item\n(R)eturn an item\n(A)dd new item to stock\n(Q)uit") #Displaying menu
    menu_choice=input(">>>").upper()    #automatically changes the input to capital letters
    if menu_choice == "L":  #If user input equals to L
        for item in item_stock:
            list_of_item = list_item(item)
            if item[4] == "in":
                print("{}{}".format(list_of_item, " ")) #List all items
            elif item[4] == "out":
                print("{}{}".format(list_of_item, "*"))#List all items
    elif menu_choice == "H":    #If user input equals to H
        item_to_hire = [item for item in item_stock if item[4] == "in"]
        if len(item_to_hire) == 0:
            print("No items are currently available")   #No items are currently available to hire
        elif len(item_to_hire) != 0:
            item_available_to_hire = [] #To make a list for all available items for hire
            all_item = []   #To show all items
            for item in item_stock:
                if item[4] == "in": #if items are available
                    print(list_item(item))
                    item_available_to_hire.append(item[0])  #To add items to available item to hire
                    all_item.append(item[0])    #To add items to all items
                elif item[4] == "out":  # if items are not available
                    all_item.append(item[0])  # To add items to all items
            print("Please enter the number of item to hire")
            while True:
                try:
                    hire_item = int(input(">>>"))
                    if hire_item in item_available_to_hire:
                        for item in item_stock:
                            if item[0] == hire_item:
                                item[4] = "out"
                                print("{} hired for $ {:.2f}".format(item[1],item[3]))
                        break  # Exit the while loop
                    elif hire_item not in item_available_to_hire and hire_item in all_item:
                        print("That item is not available for hire")    #Error message for unavailable item for hire
                        break  # Exit the while loop
                    elif hire_item not in all_item:
                        print("Invalid item number")  # Error message for invalid input
                except ValueError:  # To check if the user entered a string or the input is blank
                    print("Invalid input; enter a number")  # Error message for invalid input
    elif menu_choice == "R":    #If user input equals to R
        item_to_return = [item for item in item_stock if item[4] == "out"]
        if len(item_to_return) == 0:
            print("No items are currently on hire")
        elif len(item_to_return) != 0:
            item_available_to_return = []
            all_item = []   #To make a list for all item
            for item in item_stock:
                if item[4] == "out":
                    print(list_item(item))
                    item_available_to_return.append(item[0])
                    all_item.append(item[0])
                elif item[4] == "in":
                    all_item.append(item[0])
            print("Please enter the number of item to hire")
            while True:
                try:
                    return_item = int(input(">>>"))
                    if return_item in item_available_to_return:
                        for item in item_stock:
                            if item[0] == return_item:
                                item[4] = "in"
                                print("{} returned".format(item[1]))
                        break  # Exit the while loop
                    elif return_item not in item_available_to_return and return_item in all_item:
                        print("That item is not available for hire")    #Error message for unavailable item for hire
                    elif return_item not in all_item:
                        print("Invalid item number")  # Error message for invalid input of item number
                except ValueError:  # To check if the user entered a string or the input is blank
                    print("Invalid input; enter a number")  # Error message for invalid input
    elif menu_choice == "A":    #If user input equals to A
        while True:
            new_item_name = input("Item name:") #Asking for name of the new item
            if new_item_name == "":
                print("Input can not be blank") #Error message for blank input
            else:
                break  # Exit the while loop
        while True:
            new_item_description = input("Item description:")   #asking for the description of the new item
            if new_item_description == "":
                print("Input can not be blank") #Error message for blank input
            else:
                break  # Exit the while loop
        while True:
            try:
                new_item_price = float(input("Price per day:")) #Asking for the price of the new item
                if new_item_price < 0:  #if the price of the new item is under 0
                    print("Price must be >= $0")    #Price cannot be negative
                    print("Invalid input; enter a valid number")  # Error message for invalid input
                elif new_item_price >= 0:   #if the price of the new item is equals or more than 0
                    break  # Exit the while loop
            except ValueError:  # To check if the user entered a string or the input is blank
                print("Invalid input; enter a valid number")  # Error message for invalid input
        item = [len(item_stock), new_item_name, new_item_description, float(new_item_price), "in"]  # To put all the input into a list with the len
        item_stock.append(item) #To add item to item stock
        print("{} ({}), {} now available for hire".format(item[1],item[2],item[3])) #Showing available item for hire
    elif menu_choice == "Q":    #If user input equals to Q
        print("Have a nice day")    #Goodbye Message
        break   #Exit the while loop
    else:
        print("Invalid menu choice")    #Error message for invalid input
output_file = open("inventory.csv","w")  # To open the file for writing, thus overwrite the previous data
for item in item_stock:
    item="{},{},{},{}".format(item[1],item[2],item[3],item[4])
    print(item,file=output_file)
output_file.close() #To close the file
print("{} items saved to inventory.csv".format(len(item_stock)))    #Shows how many items are in the csv file