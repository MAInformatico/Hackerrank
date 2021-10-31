#!/bin/bash
while read text
do
echo $text | cut -c2,7
done
