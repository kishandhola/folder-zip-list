import zipfile, os
import os.path as path
root_dir = str(input("Please enter Path :"))
for file_name in os.listdir(root_dir):
    # print(file_name)
    d = os.path.join(root_dir, file_name)
    if os.path.isdir(d):
        # print(file_name)
        myzip=zipfile.ZipFile(os.path.join(root_dir, file_name+'.zip'),'w',zipfile.ZIP_DEFLATED)
        for folder,subfolder,file in os.walk(os.path.join(d,'')):
            for each in subfolder+file:
                # print(each)
                source = os.path.join(folder,each)
                arcname = source[len(root_dir):].lstrip(os.sep)
                myzip.write(source,arcname=arcname)

        print(file_name+'.zip')
