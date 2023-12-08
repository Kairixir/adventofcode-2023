#!/bin/sh

if (( $# != 1 )); then
    >&2 echo "Illegal number of arguments"
    exit 1
fi

if ! [[ $1 =~ ^[1-9]?[0-9]$ ]]; then
    >&2 echo "Input is not in correct format\nUse format [1-9]?[0-9]"
    exit 1
fi

source "config.get-input"

folder=$(printf '%02d' $1)

mkdir $folder

curl "https://adventofcode.com/2023/day/$1/input" \
  -H 'authority: adventofcode.com' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8' \
  -H 'accept-language: en-GB,en;q=0.9' \
  -H 'cache-control: no-cache' \
  -H "cookie: session=${COOKIE_SESSION}" \
  --compressed >> $folder/input.txt



cp $folder/input.txt $folder/part1-solution.txt
cp $folder/input.txt $folder/part2-solution.txt
