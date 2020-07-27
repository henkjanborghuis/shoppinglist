import unittest
from shoppinglist import ShoppingList

# TODO: Use the setUp() method

class SimpleListTestCase(unittest.TestCase):

    def setUp(self):
        name = "Test"
        self.item = "Bread"
        self.test_list = ShoppingList(name)

    def test_empty_list(self):
        self.assertEqual(self.test_list.shopping_list, [])

    def test_standard_text_empty_list(self):
        self.assertEqual(self.test_list.text, "")

    def test_single_item_list(self):
        self.test_list.shopping_list.append(self.item)
        self.assertEqual(self.test_list.shopping_list, ['Bread'])

    def test_print_ask_empty_list(self):
        out = self.test_list.print_ask()
        self.assertEqual(out, "What should we take from the store?")

    def test_print_ask_items_on_list(self):
        self.test_list.shopping_list.append(self.item)
        out = self.test_list.print_ask()
        self.assertEqual(out, "What else should we take from the store?")

if __name__ == '__main__':
    unittest.main()
