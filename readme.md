# Directory Zipper Script

## Description

This Python script takes a directory path as input and compresses all subdirectories within that directory into individual zip files. Each zip file is named after its respective subdirectory and is saved in the root directory provided as input.

## How to Use

1. **Input Path**: The script prompts the user to enter the root directory path.
2. **Processing**: It iterates through each item in the root directory:
   - If an item is a subdirectory, it creates a zip file with the same name as the subdirectory.
   - The contents of the subdirectory are added to the zip file, maintaining the directory structure.
3. **Output**: The zip files are saved in the root directory with the `.zip` extension appended to the subdirectory names.

