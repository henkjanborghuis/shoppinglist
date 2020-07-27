import shoppinglist
import json

my_shopping_list = shoppinglist.ShoppingList("")

# Name shopping list
print("Give the shopping list a name")
my_shopping_list.name = input(">  ")

# Add items to shopping list
shoppinglist.show_help()
while True:
    print(my_shopping_list.print_ask())
    my_shopping_list.item = input("> ").capitalize()

    if (my_shopping_list.item.lower() == 'nothing'
    or my_shopping_list.item.lower() == 'n'):
        break
    elif (my_shopping_list.item.lower() == 'help'
    or my_shopping_list.item.lower() == 'h'):
        shoppinglist.show_help()
        continue
    elif (my_shopping_list.item.lower() == 'show'
    or my_shopping_list.item.lower() == 's'):
        my_shopping_list.show_list()
        continue
    else:
        my_shopping_list.add_to_list(my_shopping_list.item)
        print("{} added to the list.".format(my_shopping_list.item))
        print(my_shopping_list.print_items_on_list())

# Print shopping list to screen
my_shopping_list.print_list()

# Write shopping list to disk in txt format
filename_txt = './lists/{}.txt'.format(my_shopping_list.name)
filename_json = './lists/{}.json'.format(my_shopping_list.name)

with open(filename_txt, 'w') as file_object:
    for item in my_shopping_list.shopping_list:
        file_object.write(str(item) + "\n")


with open(filename_json, 'w') as f:
        json.dump(my_shopping_list.shopping_list, f)
