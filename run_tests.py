import unittest
from src.convert import kilometers_to_miles, miles_to_kilometers, \
	years_to_minutes, minutes_to_years

class TestConvert(unittest.TestCase):

	def test_km_2_mi(self):
		actual = kilometers_to_miles(1)
		expected = 0.621 # From Brian, from Google
		self.assertAlmostEqual(actual, expected, delta = 0.01)

	def test_mi_2_km(self):
		actual = miles_to_kilometers(1)
		expected = 1.609
		self.assertAlmostEqual(actual, expected, delta = 0.01)

	def test_yrs_2_min(self):
		self.assertEqual(525600, years_to_minutes(1))

	def test_min_2_yrs(self):
		self.assertEqual(1, minutes_to_years(525600))

# To run the function this is needed here.

if __name__ == '__main__':
	uniittest.main()