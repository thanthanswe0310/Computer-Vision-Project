import os
import shutil
label_dir = 'F:/coco128_last/val2017\labels/'

# Iterate through label files
for filename in os.listdir(label_dir):
    with open(os.path.join(label_dir, filename), 'r') as file:
        lines = file.readlines()
        # Check for empty or improperly formatted files
        if len(lines) == 0 or any(line.strip() == '' for line in lines):
            print(f'Corrupted label file: {filename}')