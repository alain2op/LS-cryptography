#!/bin/bash
zip_files=$(find . -type f -name "*.zip")
while [ -n "$zip_files" ]; do
    for zip_file in $zip_files;do
        unzip $zip_file
        rm $zip_file
    done
    zip_files=$(find . -type f -name "*.zip")
done