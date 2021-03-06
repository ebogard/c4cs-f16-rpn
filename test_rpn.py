import unittest
import rpn
class TestBasics(unittest.TestCase):
	def test_subtract(self):
		result = rpn.calculate("5 3 -")
		self.assertEqual(2, result)
	def test_add(self):
		result = rpn.calculate("1 1 +")
		self.assertEqual(2, result)
	def test_exponent(self):
		result = rpn.calculate("2 2 ^")
		self.assertEqual(4, result)
	def test_toomanythings(self):
		with self.assertRaises(TypeError):
			rpn.calculate("1 2 3 +")
	
