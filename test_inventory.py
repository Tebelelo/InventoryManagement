import unittest
from inventory import *
from unittest.mock import patch
from io import StringIO

class MyTestCases(unittest.TestCase):
    
    
    @patch('builtins.input', side_effect=['Door', '400'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_add_item(self, mock_stdout, mock_input):
        store_name = "OK Furnitures"
        shelf1 = InventoryManagement(store_name)
        expected = {'door': {'Quantity': 1, 'Price': 400}}
        result = shelf1.add_item()
        self.assertEqual(result, expected)
        
    
    @patch('builtins.input', side_effect=['Door', '500'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_update_item(self,mock_stdout,mock_input):
        store_name:str = "OK Furnitures"
        shelf2 = InventoryManagement(store_name)
        shelf2.quantity_and_item = {'door':{'Quantity':1,'Price':400}}
        expected = {'door':{'Quantity':1,'Price':500}}
        result = shelf2.update_item_price()
        self.assertEqual(result,expected)
        
    @patch("sys.stdout", new_callable=StringIO)
    @patch('builtins.input', side_effect=['Chair', '500'])
    def test_update_non_exist_item(self, mock_input, mock_stdout):
        shelf1 = InventoryManagement("OK Furnitures")
        shelf1.quantity_and_item = {'door': {'Quantity': 1, 'Price': 5000}}
        shelf1.update_item_price() 
        expected = "Update item price\nItem does not exist"
        result = mock_stdout.getvalue().strip()
        self.assertEqual(result, expected)

    
    @patch('builtins.input',return_value = 'door')
    def test_delete_item(self,mock_input):
        self.shelf1 = InventoryManagement("OK Furnitures")
        self.shelf1.quantity_and_item = {'door':{'Quantity':1,'Price':400},'chair':{'Quality':1,'Price':250}}
        self.assertEqual(self.shelf1.delete_item(),{'chair':{'Quality':1,'Price':250}})
        
    @patch('builtins.input',side_effect =['Coffee','door'])
    @patch('sys.stdout',new_callable=StringIO)
    def test_delete_non_exist_item(self,mock_stdout,mock_input):
        self.shelf1 = InventoryManagement("OK Furnitures")
        self.shelf1.quantity_and_item ={'door':{'Quantity':1,'Price':400}}
        self.shelf1.delete_item()
        self.assertIn('Item not found,try again',mock_stdout.getvalue().strip())
        self.assertIn('Item deleted!',mock_stdout.getvalue().strip())

    
if __name__ == '__main__':
    unittest.main()
    
    
    
    
    