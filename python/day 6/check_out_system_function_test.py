import unittest

from check_out_system_function import*

class check_out_system_function_test(unittest.TestCase):


	def test_that_function_returns_total(self):
		expected = [4,999.925]
		actual = compute_totals({5000,0.15,0.075})
		self.assertEqual(actual,expected)



	def test_that_product_can_be_added_to_cart(self):
		
		expected = add_to_cart(5000)
		actual =  add_to_cart(5000,2000,1000)
		self.assertEqual(actual,expected)

		

