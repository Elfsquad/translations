import sys
import csv
import re

# helper script to transform a csv into a version with correct whitespace formatting according to the 'test-whitespace.py'
# creates a new csv named {old_name}_new.csv.
# only intended to be ran manually, with manual copy pasting of the new file into the old one.

oldfile = sys.argv[1]
newfile = oldfile[:-4] + "_new.csv"

normalise_regex = re.compile(r"\s+")

with open(oldfile, mode = 'r', encoding = 'utf-8') as f_in, open(newfile, mode = 'w', encoding = 'utf-8', newline = '') as f_out:
    reader = csv.reader(f_in, delimiter=";")
    writer = csv.writer(f_out, delimiter=";")
    for line in reader:
        writer.writerow([normalise_regex.sub(" ", sentence.strip()) for sentence in line])
