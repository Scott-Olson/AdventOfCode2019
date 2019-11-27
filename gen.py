# script to generate an entry for each day of the Advent of Code 2019 event
# https://adventofcode.com/ to find this years puzzles as well as previous years challenges

import os

path = os.getcwd()

print("Current dir: %s" % path)

# function to create a directory for the day of the challenge

def collectInfo() -> dict:
	day = input("Please enter the day of the challenge (eg: 1, 2, 3, ... ): ")
	dataInput = input("Does todays challenge require a csv? (Y/N): ")
	print("Test values: %s %s " % (day, dataInput))

	cleanedData = {"day": day, "input": dataInput}

	return cleanedData

def createFolder(day: int) -> bool:

	return False

def createFile(fileType: str) -> bool:
	f = open("guru99.txt","w+")
	f.close()

	return False




def main():
	info = collectInfo()
	print(info)
	return


if __name__ == '__main__':
	main()

