import unittest
from src.convert import km_2_mi, mi_2_km, yrs_2_min, min_2_yrs

class TestConvert(unittest.TestCase):

	def test_km_2_mi(self):
		actual = km_2_mi(1)
		expected = 0.621 # From Brian, from Google
		self.assertAlmostEqual(actual, expected, delta = 0.01)

	def test_mi_2_km(self):
		actual = mi_2_km(1)
		expected = 1.609
		self.assertAlmostEqual(actual, expected, delta = 0.01)

	def test_yrs_2_min(self):
		self.assertEqual(525600, yrs_2_min(1))

	def test_min_2_yrs(self):
		self.assertEqual(1, min_2_yrs(525600))

# To run the function this is needed here.

if __name__ == '__main__':
	unittest.main()
