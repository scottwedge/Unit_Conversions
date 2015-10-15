# Command line script to convert a given number from one unit, to another. 
# Assigns multiple units to given number and converts them all.

import argparse
from src.convert import kilometer_to_miles, miles_to_kilometer, years_to_minutes, minutes_to_years

# Command line parse options
parser = argparse.ArgumentParser()
parser.add_argument('value', type = float, help = "Enter the number to be converted.")
args = parser.parse_args()

#km to miles
km_2_miles = kilometers_to_miles(ars.value)
