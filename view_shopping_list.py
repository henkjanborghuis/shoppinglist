import shoppinglist

my_shopping_list = shoppinglist.ShoppingList(" ")


print("Provide the name of the shopping list you want to view:")
my_shopping_list.name = input(">  ")


filename_txt = './lists/{}.txt'.format(my_shopping_list.name)

with open(filename_txt) as file_object:
    for line in file_object:
        my_shopping_list.add_to_list(line.rstrip())

print("")
my_shopping_list.print_list()
