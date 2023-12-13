count=$(awk -F';' '{print NF-1}' "$1" | sort | uniq | wc -l)
if [ "$count" -ne 1 ]; then
  echo "Error: $1 has different number of columns" >&2
  exit 1
fi
exit 0
