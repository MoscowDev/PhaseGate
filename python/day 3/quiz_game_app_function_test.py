import unittest

from quiz_game_app_function import*



class quiz_game_app_function_test(unittest.TestCase):
	def test_that_function_returns_true_or_false(self):

		expected = "Correct"
		actual =  get_question_one("tinubu")

		self.assertEqual(actual,expected)
