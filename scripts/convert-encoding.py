import csv
import sys

old_translations = sys.argv[1]
new_translations = sys.argv[2]
output_file = sys.argv[3]

old_translations_f = open(old_translations, 'r', encoding='utf-8')
new_translations_f = open(new_translations, 'r', encoding='windows-1252', errors='ignore')
output_file_f = open(output_file, 'w', encoding='utf-8')

english_new_lang_mapping = {}

new_translations = [l.split(';')[-1] for l in new_translations_f.readlines()]

with old_translations_f as old_file, output_file_f as output_file:
    reader = csv.reader(old_file, delimiter=';')
    writer = csv.writer(output_file, delimiter=';')

    for i, row in enumerate(reader):
        new_value = new_translations[i]
        new_row = row + [new_value.strip()]
        writer.writerow(new_row)

