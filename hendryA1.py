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