#!/bin/bash
while read text
do
echo $text | cut -c 2-7
done
