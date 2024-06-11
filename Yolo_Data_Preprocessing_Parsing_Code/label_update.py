import os
import glob
import shutil

folder_path = r"..\labels"  
save_folder_path = r"..\labels_update"  

# 라벨 번호 
# label_mapping = {'0': '9', '1':'3', '2':'5', '3':'0', '4':'1' }   #    ['box','hardhat', 'hook', 'scaffolds', 'worker'] 
# 2 : hardhat , 4: box
label_mapping = {'2': '3', '4':'9' }  
file_paths = glob.glob(os.path.join(folder_path, '*.txt'))

for file_path in file_paths:
    with open(file_path, 'r') as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        parts = line.split(' ')
        if parts[0] in label_mapping:
            parts[0] = label_mapping[parts[0]]
        
        if parts[0]!='10':
            new_line = ' '.join(parts)
            new_lines.append(new_line)
        else: continue

    save_file_path = os.path.join(save_folder_path, os.path.basename(file_path))
    with open(save_file_path, 'w') as f:
        for line in new_lines:
            f.write(line)

           