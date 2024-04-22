import sys

translations = sys.argv[1]

with open(translations, 'r') as f:
    lines = f.readlines()

keys = set()
for line_no, line in enumerate(lines, start=1):
    key = line.split(',')[0]
    if key in keys:
        print(f'Duplicate key found in line {line_no}: {key}')
    keys.add(key)
