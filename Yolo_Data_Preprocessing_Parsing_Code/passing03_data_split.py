import os
import random
import shutil

data_folder = "..\..\coco120\images/"  # The path to the folder where the image dataset resides
output_folder = "../../coco120/train/"  # The path to the folder where you want to store the segmented data set

# Set the percentage of each dataset (based on total data)
train_ratio = 0.8
val_ratio = 0.2
# test_ratio = 0.1

def split_dataset(data_folder, output_folder):
   # Creating a Split Dataset Folder
    os.makedirs(output_folder, exist_ok=True)

   # Create a list of image files and label files
    image_files = [filename for filename in os.listdir(data_folder) if filename.endswith('.jpg')]  # Modify image file to fit the extension
    label_files = [filename for filename in os.listdir(data_folder) if filename.endswith('.txt')] # Modify to fit label file extensions

  # Mixing data at random
    random.shuffle(image_files)

   # Index calculating index calculation
    total_samples = len(image_files)
    train_end = int(total_samples * train_ratio)
    val_end = train_end + int(total_samples * val_ratio)

   # Copy images and label files to each dataset
    for i, filename in enumerate(image_files):
        source_image_path = os.path.join(data_folder, filename)
        source_label_path = os.path.join(data_folder, filename.replace('.jpg', '.txt'))# Modify image to correspond to label file name
        dest_folder = "train" if i < train_end else ("val" if i < val_end else "test")
        dest_image_path = os.path.join(output_folder, dest_folder, filename)
        dest_label_path = os.path.join(output_folder, dest_folder, filename.replace('.jpg', '.txt'))

        os.makedirs(os.path.dirname(dest_image_path), exist_ok=True)
        shutil.copy(source_image_path, dest_image_path)
        shutil.copy(source_label_path, dest_label_path)

        print(f"Copied {filename} to {dest_folder} dataset")

split_dataset(data_folder, output_folder)
