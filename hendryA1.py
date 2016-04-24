def load_item():
    item_import=open("inventory.csv","r")
    item_no=0
    item_stock = []
    for each_line in item_import:
        item_name, item_description, item_price, availability = each_line.strip().split(",")
        item = [item_no, item_name, item_description, float(item_price), availability]
        item_no += 1
        item_stock.append(item)
    item_import.close()
    return item_stock

def list_item(item):
    list_of_item = ("{} - {:<40s} = ${:>7.2f}".format(item[0], item[1] + "(" + item[2] + ")", item[3]))
    return list_of_item

print("Items for Hire - by Hendry")
item_stock = load_item()
print("{} items loaded from inventory.csv".format(len(item_stock)))
while True:
    print("Menu:\n(L)ist all items\n(H)ire an item\n(R)eturn an item\n(A)dd new item to stock\n(Q)uit")
    menu_choice=input(">>>").upper()
    if menu_choice == "L":
        for item in item_stock:
            list_of_item = list_item(item)
            if item[4] == "in":
                print("{}{}".format(list_of_item, " "))
            elif item[4] == "out":
                print("{}{}".format(list_of_item, "*"))
    elif menu_choice == "H":
        item_to_hire = [item for item in item_stock if item[4] == "in"]
        if len(item_to_hire) == 0:
            print("No items are currently available")
        elif len(item_to_hire) != 0:
            item_available_to_hire = []
            all_item = []
            for item in item_stock:
                if item[4] == "in":
                    print(list_item(item))
                    item_available_to_hire.append(item[0])
                    all_item.append(item[0])
                elif item[4] == "out":
                    all_item.append(item[0])
            print("Please enter the number of item to hire")
            hire_item = int(input(">>>"))
            if hire_item in item_available_to_hire:
                for item in item_stock:
                    if item[0] == hire_item:
                        item[4] = "out"
                        print("{} hired for $ {:.2f}".format(item[1],item[3]))
            elif hire_item not in item_available_to_hire and hire_item in all_item:
                print("That item is not available for hire")
            elif hire_item not in all_item:
                print("Invalid item number")
            elif ValueError:
                print("Invalid input; enter a number")
    elif menu_choice == "R":
        item_to_return = [item for item in item_stock if item[4] == "out"]
        if len(item_to_return) == 0:
            print("No items are currently on hire")
        elif len(item_to_return) != 0:
            item_available_to_return = []
            all_item = []
            for item in item_stock:
                if item[4] == "out":
                    print(list_item(item))
                    item_available_to_return.append(item[0])
                    all_item.append(item[0])
                elif item[4] == "in":
                    all_item.append(item[0])
            print("Please enter the number of item to hire")
            return_item = int(input(">>>"))
            if return_item in item_available_to_return:
                for item in item_stock:
                    if item[0] == return_item:
                        item[4] = "in"
                        print("{} returned".format(item[1]))
            elif return_item not in item_available_to_return and return_item in all_item:
                print("That item is not available for hire")
            elif return_item not in all_item:
                print("Invalid item number")
            elif ValueError:
                print("Invalid input; enter a number")