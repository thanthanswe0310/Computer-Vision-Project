import os

def extract_filename_without_extension(file_path):
    base_name = os.path.basename(file_path)
    file_name, _ = os.path.splitext(base_name)
    return file_name

def main():
    image_dir = r'..\dataset\val2017\images'
    text_dir = r'..\dataset\val2017\labels'
    image_files = os.listdir(image_dir)
    text_files = os.listdir(text_dir)

    for image_file in image_files:
        image_name = extract_filename_without_extension(image_file)
        matching_text_file = f"{image_name}.txt"

        if matching_text_file in text_files:
            print(f"Image file '{image_file}' has a matching text file '{matching_text_file}'.")
        else:
            print(f"No matching text file found for image file '{image_file}'.")

if __name__ == "__main__":
    main()
