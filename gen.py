# script to generate a folder and blank file for each day of the Advent of Code 2019 event
# https://adventofcode.com/ to find this years puzzles as well as previous years challenges

import os

path = os.getcwd()

print("Current dir: %s" % path)

dir_path = ''
folderName = ''

# function to create a directory for the day of the challenge
def collectInfo() -> dict:
	# collect inputs from the user
	# the day of the challenge
	day = str(input("Please enter the day of the challenge (eg: 1, 2, 3, ... ): "))
	# ask if the file will need an input file to handle data from challenge
	dataInput = str(input("Does todays challenge require an input? (Y/n): "))
	# make sure the data is as expected
	userInputCheck = input("Are these values correct? %s %s (y/N):" % (day, dataInput))
	print(userInputCheck)

	# self check
	# if userInputCheck != 'y' or userInputCheck != 'yes' or userInputCheck != 'Y':
	# 	return False

	# assign data to be passed along, default has txt creation
	cleanedData = {"day": day, "input": 'y'}

	# check for not needing txt
	if dataInput == 'n' or dataInput == 'no' or dataInput == 'N':
		cleanedData['input'] = 'n'

	return cleanedData
		
# function to create folder for each day
def createFolder(day: str) -> bool:
	path = os.getcwd()
	global folderName
	folderName = "day" + day
	print(folderName)
	
	global dir_path
	dir_path = path + "/" + folderName

	print("path here -> %s" % dir_path)
	try:
	    os.mkdir(path)
	except OSError:
	    print ("Creation of the directory %s failed" % path)
	else:
	    print ("Successfully created the directory %s " % path)

	return False


# function to create the individual files for each day.
# create a python file for the day always, sometimes a txt

# add default imports for python
# conditional imports for when a txt is created (txt parsing, numpy ...)
def createFile(imports: list, txt: bool = False) -> bool:
	standalone_imports = {
				"csv": "lines = open('input.txt').read().split('\\n')",
				"numpy": "import numpy as np",
				"collections": "from collections import *",
				"itertools": "from itertools import *",
				"math": "from math import *",
				
				}
	imports = {
				"re": "re",
				"dateutil": "dateutil",
				"pprint": "pprint",
				"datetime": "datetime",

				}
	# test_path = folderName + "/first.py"
	f = open("first.py", "w")

	s = open("second.py", "w")

	# txt will be true when also making a txt file for data inport
	# therefor want all the parsing imports
	if txt == True:
		# create text file and close it out
		test_str = folderName + "/input.txt"
		t = open(test_str, "w+")
		t.close()

		# import the txt file into the py file and the parsing imports
		L = [standalone_imports['csv'] + '\n', standalone_imports['numpy'] + '\n', standalone_imports['itertools'] + '\n']
		f.writelines(L)

	
	for i in standalone_imports:
		# write lines to the imports

		pass

	f.close()
	s.close()
	return False


def main():
	info = collectInfo()
	print(info)
	if info is False:
		print("File creation aborted...")
		return

	# create the folder for the day
	createFolder(info['day'])

	if info['input'] == 'y':
		createFile([],True)
	return


if __name__ == '__main__':
	main()

