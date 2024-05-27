# Directory Zipper Script

This Python script compresses all subdirectories within a specified directory into individual zip files. Each zip file is named after its respective subdirectory and is saved in the root directory provided as input.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Features

- Compresses each subdirectory in the given root directory into a separate zip file.
- Maintains the directory structure within each zip file.
- Easy to use with a simple input prompt for the directory path.

## Requirements

- Python 3.x
- Standard Python libraries: `zipfile`, `os`

## Usage

1. **Clone the Repository**

    ```sh
    git clone https://github.com/your-username/directory-zipper.git
    cd directory-zipper
    ```

2. **Run the Script**

    ```sh
    python zipper.py
    ```

3. **Input the Directory Path**

    When prompted, enter the path to the root directory containing the subdirectories you wish to compress.

## Example

Assume the following directory structure in `root_dir`:


root_dir/
├── subdir1/
│ ├── file1.txt
│ └── file2.txt
├── subdir2/
│ ├── file3.txt
│ └── file4.txt
└── file5.txt

After running the script and entering the path to `root_dir`, the script will create the following zip files in `root_dir`:

root_dir/
├── subdir1.zip
├── subdir2.zip
└── file5.txt

Each zip file will contain the respective subdirectory's contents, maintaining the directory structure.
