import os
import glob
import shutil

folder_path = "/labels/"  
save_folder_path = "/passing/"   

label_mapping = {'0':'5','1':'1','2':'0','3':'3'}  
file_paths = glob.glob(os.path.join(folder_path, '*.txt'))

for file_path in file_paths:
    with open(file_path, 'r') as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        parts = line.split(' ')

        if parts[0] in label_mapping:
            parts[0] = label_mapping[parts[0]]

        new_line = ' '.join(parts)
        new_lines.append(new_line)

    save_file_path = os.path.join(save_folder_path, os.path.basename(file_path))
    with open(save_file_path, 'w') as f:
        for line in new_lines:
            f.write(line)
