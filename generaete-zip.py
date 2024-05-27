import zipfile, os
import os.path as path

# Prompt the user to enter the root directory path
root_dir = str(input("Please enter Path :"))

# Iterate through each item in the root directory
for file_name in os.listdir(root_dir):
    # Construct the full path of the item
    d = os.path.join(root_dir, file_name)
    
    # Check if the item is a directory
    if os.path.isdir(d):
        # Create a zip file with the same name as the directory
        myzip = zipfile.ZipFile(os.path.join(root_dir, file_name + '.zip'), 'w', zipfile.ZIP_DEFLATED)
        
        # Walk through the directory structure
        for folder, subfolder, file in os.walk(os.path.join(d, '')):
            for each in subfolder + file:
                # Construct the source path of the current item
                source = os.path.join(folder, each)
                
                # Determine the archive name by stripping the root directory from the source path
                arcname = source[len(root_dir):].lstrip(os.sep)
                
                # Write the current item to the zip file
                myzip.write(source, arcname=arcname)
        
        # Print the name of the created zip file
        print(file_name + '.zip')
