# script to generate an entry for each day of the Advent of Code 2019 event
# https://adventofcode.com/ to find this years puzzles as well as previous years challenges

import os

path = os.getcwd()

print("Current dir: %s" % path)


# function to create a directory for the day of the challenge
def collectInfo() -> dict:
	day = str(input("Please enter the day of the challenge (eg: 1, 2, 3, ... ): "))
	dataInput = str(input("Does todays challenge require a csv? (Y/n): "))
	userInputCheck = input("Are these values correct? %s %s :" % (day, dataInput))

	# self check
	if userInputCheck != 'Y' or userInputCheck != 'yes':
		return False

	# assign data to be passed along, default has csv creation
	cleanedData = {"day": day, "input": 'y'}

	# check for not needing csv
	if not userInputCheck or userInputCheck == "n" or userInputCheck =="no":
		cleanedData['input'] = 'n'

	return cleanedData
		

def createFolder(day: str) -> bool:
	folderName = "day" + day
	print(folderName)
	try:
	    os.mkdir(path)
	except OSError:
	    print ("Creation of the directory %s failed" % path)
	else:
	    print ("Successfully created the directory %s " % path)

	return False


# function to create the individual files for each day.
# create a python file for the day always, sometimes a CSV

# add default imports for python
# conditional imports for when a csv is created (csv parsing, numpy ...)
def createFile(fileType: str) -> bool:
	f = open("guru99.txt","w+")
	f.close()

	return False


def main():
	info = collectInfo()
	if info == False:
		print("File creation aborted...")
		return
	print(info)
	createFolder(info['day'])

	if info['input'] == 'y':
		pass
	return


if __name__ == '__main__':
	main()

