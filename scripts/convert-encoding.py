import csv
import sys

old_translations = sys.argv[1]
new_translations = sys.argv[2]
output_file = sys.argv[3]

old_translations_f = open(old_translations, 'r')
new_translations_f = open(new_translations, 'r', encoding='ascii', errors='ignore')
output_file_f = open(output_file, 'w', encoding='utf-8')

english_new_lang_mapping = {}

with new_translations_f as new_file:
    reader = csv.reader(new_file, delimiter=';')

    for row in reader:
        english_value = row[0]
        new_value = row[-1].encode('utf-8').decode('utf-8')
        english_new_lang_mapping[english_value] = new_value


with old_translations_f as old_file, output_file_f as output_file:
    reader = csv.reader(old_file, delimiter=';')
    writer = csv.writer(output_file, delimiter=';')

    for row in reader:
        english_value = row[0]
        new_value = english_new_lang_mapping.get(english_value, '')
        new_row = row + [new_value.strip()]
        writer.writerow(new_row)

