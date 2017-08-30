"""
Split multiple datasets from a single file and create each file for each dataset.
Author: Pairode Jaroensri
Last visited Feb 2017
"""


# Make a new file with file name "data" + i
new_file = lambda i: open("data" + str(i), 'w')

scr = open("data.txt", 'r')
i = 0

prev = "Initializing variable" # Keeping track of the previous line.

dest = new_file(0)

for line in scr:
    # Make a list of words in a line.
    words = line.split()

    # Make sure the line is not empty.
    if len(words) != 0:
        # At the beginning of a dataset, close the current destination file and create a new one.
        if prev.split()[0] != "dataValue" and words[0] == "dataValue":
            dest.close()
            dest = new_file(i)
            i = i + 1

        if words[0] == "dataValue":
            dest.write(line)

        prev = line

dest.close()
scr.close()