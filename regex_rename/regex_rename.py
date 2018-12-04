"""
Rename files with dates in the filenames to the particular format: YYYY.MM.DD_filename
Rename by copying rather than replacing.
Author: Pairode Jaroensri
Client: Zoe Ng
Last visited: August 26, 2017
"""

import os
import shutil
import re

def is_int(string):
    """Determines whether the string is a positive number without excessive characters.

    >>> is_int("123")
    True
    >>> is_int("-2")
    False
    >>> is_int(" 555")
    False
    """
    try:
        i = int(string)
        return i > 0 and len(str(i)) == len(string)
    except ValueError:
        return False

def new_name(name, regex):
    """Create a new file name where the date is moved to the front

    >>> new_name("xxxx -2.09.2017- v1l")
    "2017.09.02_xxxx - v1l"
    >>> new_name("Lab06-3.7.17.xlsx")
    "2017.07.03_Lab06.xlsx"
    """
    # Find the date segment of the file name

    matched = regex.search(name)
    # If there is no match (because either the file name does not contain a date,
    # or the program is not perfect), ask the user to manually input a new file name.
    if matched == None:
        print("Unable to automatically rename the following file: " + name)
        new_file_name = input("Please enter a new name for this file, or enter nothing to keep this name.\n")
        if new_file_name == "":
            return name
        else:
            return new_file_name

    # If there is a match, then change the format from d/m/y to y/m/d.
    date = matched.group(0)
    dmy = re.split("\.", date)

    # Clean up the date. Make sure day and month are in 2 digits, and year is in 4 digits.
    if len(dmy[0]) == 1:
        dmy[0] = "0" + dmy[0]
    elif len(dmy[0]) >= 2 and not is_int(dmy[0]):
        dmy[0] = "0" + dmy[0][-1]
    if len(dmy[1]) == 1:
        dmy[1] = "0" + dmy[1]
    if len(dmy[2]) == 2:
        dmy[2] = "20" + dmy[2]

    # Put the date back together in yyyy/mm/dd_ format.
    new_date = dmy[2] + "." + dmy[1] + "." + dmy[0] + "_"
    
    # Finally, put the date in front of the file name.
    name_segments = regex.split(name)
    return new_date + name_segments[0] + name_segments[1]

# Create a matcher using regular expression.
matcher = re.compile(".\d{1,2}\.\d{1,2}\.\d{2,4}")

# Create a new directory (folder) to store the renamed files.
proceed = True
try:
    os.makedirs("renamed_files")
except Exception:
    print("Warning: Directory 'renamed_files' already exists.")
    print("All existing files in the directory will be overwritten.")
    choice = input("Do you wish to proceed? (y/N): ")
    proceed = choice == 'y' or choice == 'Y'

# Copy every file in the current directory to the new directory while renaming them.
if proceed:
    for filename in os.listdir("."):
        if filename[-3:] != ".py" and os.path.isfile(filename):
            shutil.copy(filename, "renamed_files/" + new_name(filename, matcher))
else:
    print("Canceled.")
# Done.
