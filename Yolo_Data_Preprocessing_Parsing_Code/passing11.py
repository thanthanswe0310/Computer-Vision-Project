import os
import shutil

source_folder = '..\..\dataset\C_20230922_01/'
destination_folder = '..\..\dataset\C_scenario/'

file_list = os.listdir(source_folder)

image_extensions = ['.jpg', '.jpeg', '.png', '.gif']  
image_files = [file for file in file_list if any(file.endswith(ext) for ext in image_extensions)]

# Copy the image file to the destination folder and rename it
for image_file in image_files:
    source_path = os.path.join(source_folder, image_file)
    destination_path = os.path.join(destination_folder, image_file) 
    shutil.move(source_path, destination_path)# When you move it
    # shutil.copy(source_path, destination_path)# When you copy,
