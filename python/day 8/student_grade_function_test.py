

import unittest
from student_grade import*

class TestStudentGrades(unittest.TestCase):

	
	def test_that_function_takes_addition_of_scores(self):
		scores = [[85, 90, 78],[75, 88, 92] ]
		student1_total = 85 + 90 + 78

		self.assertEqual(student1_total, 253)


	def test_that_function_returns_average_of_scores(self):
		scores = [[85, 90, 78],[75, 88, 92] ]
		student2_total = 75 + 88 + 92
		student2_avg = student2_total / 3

		self.assertEqual(student2_total, 255)
		self.assertEqual(student2_avg, 255/3)

