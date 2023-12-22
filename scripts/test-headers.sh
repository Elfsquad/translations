#!/bin/bash
file="$1"
header=$(head -n 1 "$file" | tr -d '\r' | tr -d '\n' | tr -d '\r\n')
IFS=';' read -ra header_array <<< "$header"

declare -A header_map

for h in "${header_array[@]}"; do
  if [ ${#h} -ne 2 ]; then
    echo "Error: Header $h is not 2 characters long" >&2
    exit 1
  fi

  if [[ ${header_map[$h]} ]]; then
    echo "Error: Header $h is duplicated" >&2
    exit 1
  else
      header_map[$h]=1
  fi

  if [[ $h =~ [A-Z] ]]; then
    echo "Error: Header $h contains uppercase characters" >&2
    exit 1
  fi
done

