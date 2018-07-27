#!/bin/bash
while read text
do
echo $text | cut -c3 -
done
