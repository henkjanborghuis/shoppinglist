class ShoppingList:

    def __init__(self, name):
        self.name = name
        self.shopping_list = []
        self.text = ''
        self.list = ''

    def add_to_list(self, item, verbose=False):
        self.shopping_list.append(item)

    def remove_from_list(self, item):
        self.shopping_list.remove(item)

    def items_on_list(self):
        number_of_items = len(self.shopping_list)
        return number_of_items

    def print_ask(self):
        if self.items_on_list() == 0:
            self.text = "What should we take from the store?"
            return self.text
        else:
            self.text = "What else should we take from the store?"
            return self.text

    def print_items_on_list(self):
        if self.items_on_list() == 0:
            self.text = "The list is empty!"
            return self.text
        elif self.items_on_list() == 1:
            self.text = ("There is now {} item on the list.\n"
            .format(self.items_on_list()))
            return self.text
        else:
            self.text = ("There are now {} items on the list\n"
            .format(self.items_on_list()))
            return self.text

    def print_list(self):
        self.list = print(self.name + ": ", *self.shopping_list, sep='\n- ')
        return self.list

class Item:
    def __init__(self, name):
        self.name = name
        self.quantity = 1



def show_help():
    print("""
Enter 'HELP' / 'H' to show this help.
Enter 'NOTHING' / 'N' to stop adding items.
Enter 'SHOW' / 'S' to show the current shopping list.
""")
