#!/bin/bash
if ! file -bi "$1" | grep -q "utf-8"; then
    echo "Error: $1 is not encoded in UTF-8" >&2
    exit 1
fi

