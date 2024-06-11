import os
import shutil

source_folder = 'F:/total_dataset\data_20230922\dataset\C_20230922_01/'
destination_folder = 'F:/total_dataset\data_20230922\dataset\C_scenario/'

file_list = os.listdir(source_folder)

image_extensions = ['.jpg', '.jpeg', '.png', '.gif']  
image_files = [file for file in file_list if any(file.endswith(ext) for ext in image_extensions)]

# 이미지 파일을 대상 폴더로 복사하고 이름 변경
for image_file in image_files:
    source_path = os.path.join(source_folder, image_file)
    destination_path = os.path.join(destination_folder, image_file) 
    shutil.move(source_path, destination_path) # 그냥 옮길때 
    # shutil.copy(source_path, destination_path)# 복사 할때 