import sys
import re

# Checks if all sentences have no leading or trailing whitespace, and if all words are separated by a single space.
# Prints the first sentence of the line which made the line not pass.

whitespace_regex = re.compile(r"(\s+)")
regex_hit = False
with open(sys.argv[1], mode = 'r', encoding = "utf-8") as f:
    for row_num, line in enumerate(f, start = 1):
        for sentence in line.rstrip("\n").split(";"):
            stripped_sentence = sentence.strip()
            if stripped_sentence != sentence or any(match.group(1) != " " for match in whitespace_regex.finditer(stripped_sentence)):
                print(f'Incorrect whitespace formatting at line {row_num} of "{sentence}"')
                regex_hit = True
                break

if regex_hit:
    sys.exit(1)
sys.exit(0)
