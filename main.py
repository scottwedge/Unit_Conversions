# Command line script to convert a given number from one unit, to another. 
# Assigns multiple units to given number and converts them all.

import argparse
from src.convert import kilometer_to_miles, miles_to_kilometer, years_to_minutes, minutes_to_years

# Command line parse options
parser = argparse.ArgumentParser()
parser.add_argument('value', type = float, help = "Enter the number to be converted.")
args = parser.parse_args()

# Unit conversions below here

#km to miles
km_2_mi = kilometers_to_miles(args.value)
print("{0} kilometers is {1} miles.".format(args.value, km_2_miles))

# Miles to km
mi_2_km = miles_to_kilometers(args.value)
print("{0} miles is {1} kilometers.".format(args.value, mi_2_km))

# Years to minutes
yrs_2_min = years_to_minutes(args.value)
print("{0} years is {1} minutes.".format(args.value, yrs_2_min))

# Minutes to years
min_2_yrs = minutes_to_years(args.value)
print("{0} minutes is {1} years.".format(args.value, min_2_yrs))