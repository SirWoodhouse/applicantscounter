## Imports
# regex for advanced string matching
import re

## Global variables
# Unique values in the start of the string
uncounters = {}
# Unique values, end of the string
nocounters = {}
# Total items
totalcount = 0

## Main program
def main(file):
    global totalcount
    next(file)  # Skip first entry (column header)
    for line in file:
        # Get all the letters at the start of the string
        un = re.search(r"^\D+", line).group()
        # Get the first number in the string
        no = re.search(r"\d{1}", line).group()
        # DEBUG: Print variables to verify
        # print(f"un:{un}, no:{no}")
        # Process un
        addtolist(un, uncounters)
        # Process no
        addtolist(no, nocounters)
        # Raise counter
        totalcount += 1
    #Print results
    print("===")
    print(f'The are a total of {totalcount} applicants.')
    print("===")
    printlist("Applicants per department", uncounters)
    printlist("Applicants per seniority level", nocounters)

## Helper functions
def addtolist(value, list):
    if value is not None:
        if value not in list:
            list[value] = 1
        else:
            list[value] += 1

def printlist(title, list):
    print(f"{title}:")
    for key, value in list.items():
        print(f"{key}:\t{value}")
    print("===")

## Intializer
if __name__ == "__main__":
    file = open('applicants.csv')
    main(file)
