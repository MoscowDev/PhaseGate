import unittest
from mini_parking_system_function import*


	
class mini_parking_system_function_test(unittest.TestCase):
	def test_that_cars_can_be_added(self):
		
		expected = ["volvo"]
		actual =  add_car("volvo")

		self.assertEqual(actual,expected)

"""
class mini_parking_system_function_test(unittest.TestCase):
	def test_that_multiple_cars_can_be_added(self):
		add_car("g-wagon")
		actual =  add_car("rav4")
		expected = ["g-wagon","rav4"]

		self.assertEqual(actual,expected)

class mini_parking_system_function_test(unittest.TestCase):

	def test_remove_nonexistent_cars(self):
        	add_car("hilux")
       		actual = remove_car("truck")  
        	expected = ["hilux"]         
        	self.assertEqual(actual, expected)
"""