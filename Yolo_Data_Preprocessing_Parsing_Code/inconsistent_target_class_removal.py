import os

def remove_classes_and_coordinates(folder_path, target_classes):
   # Import all txt files within a folder
    txt_files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]

   # Perform actions for each file
    for file_name in txt_files:
        file_path = os.path.join(folder_path, file_name)

       # Read the file
        with open(file_path, 'r') as file:
            lines = file.readlines()

       # List to save new content
        new_lines = []

       # Inspect each line to remove specific class numbers and coordinate values
        for line in lines:
            parts = line.split(' ')
            current_class = parts[0]

           # Add if you do not match the class number you want to remove
            if current_class not in target_classes:
                new_lines.append(line)

       # Write new content to a file
        with open(file_path, 'w') as file:
            file.writelines(new_lines)

if __name__ == "__main__":
    # Folder path to work with
    folder_path = "../../labels/"

   # Class Numbers to Remove
    target_classes = ["2","4","6"]

   # Function call
    remove_classes_and_coordinates(folder_path, target_classes)

   print(f"Class {', '.join(target_classes)} and its coordinate values have been removed.")
