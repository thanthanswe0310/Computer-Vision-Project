import os
import shutil


source_folder = "../../coco128/train2017/labels/"  
destination_folder = "../../Parsing_code/passing_val/"  

def find_files_with_label(label, folder_path):
    matching_files = []
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            full_path = os.path.join(folder_path, filename)
            with open(full_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    parts = line.strip().split()
                    if len(parts) > 0 and parts[0] == label:
                        matching_files.append(full_path)
                        break
    
    return matching_files

label_to_find = "5"
matching_files = find_files_with_label(label_to_find, source_folder)

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

if matching_files:
    print(f"label이 {label_to_find}The in-file {destination_folder}saveing..")
    for source_file in matching_files:
        filename = os.path.basename(source_file)
        destination_file = os.path.join(destination_folder, filename)
        shutil.copy(source_file, destination_file)
    print("done")
else:
    print(f"these's no file name {label_to_find} anymore.")
