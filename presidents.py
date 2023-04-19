#! /usr/bin/env python3

# import modules
import argparse
import csv


# create an ArgumentParser object
parser = argparse.ArgumentParser(description="This script parses presidents.csv file")

# add positional (required) arguments
parser.add_argument("data", help="Name of the presidents file to parse", type=str)

# access argument values via `args` variable
args = parser.parse_args()


#open the file
with  open(args.data) as file:

	#create a csv reader objecy
	reader = csv.reader(file)

	#loop over the lines in the file
	for line in reader:

	#skip blank lines
	if not line:
	continue

	#else its not a blank line
	else:
	print(line)



