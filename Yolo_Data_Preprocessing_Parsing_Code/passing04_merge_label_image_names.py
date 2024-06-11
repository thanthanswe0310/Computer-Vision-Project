import os
import shutil

folder1_path = 'F:/coco128_last/val2017/images/'  
folder2_path = 'F:/coco128_last/val2017/labels/' 
destination_folder = 'F:/coco128_last/last01/' 

def merge_matching_files(folder1, folder2, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)
    
    for root1, _, filenames1 in os.walk(folder1):
        for root2, _, filenames2 in os.walk(folder2):
            for filename1 in filenames1:
                base_name1, extension1 = os.path.splitext(filename1)
                if extension1 == '.txt':
                    jpg_filename1 = base_name1 + '.jpg'
                    txt_path1 = os.path.join(root1, filename1)
                    jpg_path1 = os.path.join(root1, jpg_filename1)
                    for filename2 in filenames2:
                        base_name2, extension2 = os.path.splitext(filename2)
                        if extension2 == '.txt' and base_name2 == base_name1:
                            txt_path2 = os.path.join(root2, filename2)
                            jpg_path2 = os.path.join(root2, base_name2 + '.jpg')
                            if os.path.exists(txt_path2) and os.path.exists(jpg_path2):
                                destination_txt = os.path.join(destination, filename1)
                                destination_jpg = os.path.join(destination, jpg_filename1)
                                shutil.copy(txt_path1, destination_txt)
                                shutil.copy(jpg_path1, destination_jpg)
                                break

merge_matching_files(folder1_path, folder2_path, destination_folder)
print("done")
