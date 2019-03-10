#!/bin/bash

while read -r line 
do
    curl -o $line https://cdn.assets.scratch.mit.edu/internalapi/asset/$line/get/
done < "costumes.txt"