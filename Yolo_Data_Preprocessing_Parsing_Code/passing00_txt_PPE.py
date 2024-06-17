import os
import glob
import shutil

# names: ['0', '1', '2', '3']
# names: ['scaffolds', 'worker', 'hardhat', 'hook']
# names: [ "scaffolds","worker","boots","hardhat","safety_vest","hook","robot_dog","opened_hatch","closed_hatch"]names: ['0', '1', '3', '5']


# 2 : 3
# 3 : 5
# 4 : 7
# 5 : 8
folder_path = "../../test\labels/"  
save_folder_path = "../../test\dsds/"    

# label_mapping = {'2': '3', '3':'5', '4':'7', '5':'8'}
label_mapping = {'2': '3', '3':'5', '4':'7','5':'8',}    
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
