import os

def remove_suffix_and_extra(file_name, suffix):
    index = file_name.find(suffix)
    if index != -1:
        cleaned_name = file_name[:index] 
        return cleaned_name
    else:
        return file_name

folder_path = '..\coco120/valid/test/'

suffix_to_remove = "_jpg"
file_names = os.listdir(folder_path)

for old_name in file_names:
    new_name = remove_suffix_and_extra(old_name, suffix_to_remove)

    old_path = os.path.join(folder_path, old_name)
    new_path = os.path.join(folder_path, new_name)
    
    os.rename(old_path, new_path)

print("done")


# import os

# def remove_suffix_and_extra(file_name):
#    # Find the last "_" in the file name
#     last_underscore_index = file_name.rfind("_")
    
#    # Remove string after "_" with extension
#     if last_underscore_index != -1:
#         cleaned_name = file_name[:last_underscore_index]
#         return cleaned_name
#     else:
#        # Keep file names that don't have "_"
#         return file_name

# # Set folder path
# folder_path = 'F:/total_dataset\data_20230918/thanthan\coco120/valid/test/'

# # Get a list of all files within a folder
# file_names = os.listdir(folder_path)

# # Modify and move each file name
# for old_name in file_names:
#    # Create a Revised File Name
#     new_name = remove_suffix_and_extra(old_name)
    
#    # Move files to new file name
#     old_path = os.path.join(folder_path, old_name)
#     new_path = os.path.join(folder_path, new_name)
    
#     os.rename(old_path, new_path)

# print ("File name modification completed.")
