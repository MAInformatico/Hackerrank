#!/bin/bash

read caracter
if [[("$caracter" == "y") || ("$caracter" == "Y")]]; then
    echo "YES"
elif [[("$caracter" == "n") || ("$caracter" == "N")]]; then
    echo "NO"
fi
