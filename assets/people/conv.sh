#!/bin/bash

# Get the directory name from the user
read -p "Enter the directory name: " dir_name

# Loop through all files in the directory
for file in $dir_name/*; do
    # Check if the file is an image
    if [[ $(file -b --mime-type "$file") == image/* ]]; then
        # Get the filename and extension
        filename=$(basename "$file")
        extension="${filename##*.}"

        # Crop the image to 100x100 px and save as PNG with the same name
        convert "$file" -resize 150x150^ -gravity center -crop 150x150+0+0 +repage "$dir_name/output/${filename%.*}.png"
    fi
done

echo "Done!"