#!/bin/bash
while read text
do
echo $text | cut -d $'\t' -f 1,2,3
done
