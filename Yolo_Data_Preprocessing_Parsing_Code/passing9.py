import os

# Folder path to process
input_folder_path = "..\..\coco128/train\labels/"
output_folder_path = "..\..\coco128/train01/"
target_class = "9"
# Create if you don't have an output folder
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Import and process all .txt files in the input folder
for filename in os.listdir(input_folder_path):
    if filename.endswith(".txt"):
        input_file_path = os.path.join(input_folder_path, filename)
        output_file_path = os.path.join(output_folder_path, filename)

       # Create a list to read files and save new content
        new_lines = []

      # Read the file
        with open(input_file_path, "r") as file:
            lines = file.readlines()

      # extract class information and coordinate values only if necessary
        for line in lines:
            parts = line.strip().split()
            if len(parts) >= 5 and parts[0] != target_class:
                new_lines.append(line)
            elif len(parts) < 5:
               # Keep empty lines without class information
                new_lines.append(line)

      # Save a new content to file
        with open(output_file_path, "w") as file:
            file.writelines(new_lines)

        print("Done:", output_file_path)

print ("All files processed")
