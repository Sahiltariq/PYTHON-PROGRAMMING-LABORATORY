import os
from zipfile import ZipFile

# Create object of ZipFile
with ZipFile('Zipped file.zip', 'w') as zip_object:
    for folder_name, sub_folders, file_names in os.walk('E:/python files'):
        for filename in file_names:
            file_path = os.path.join(folder_name, filename)
            zip_object.write(file_path, os.path.basename(file_path))

if os.path.exists('Zipped file.zip'):
    print("ZIP file created")
else:
    print("ZIP file not created")

