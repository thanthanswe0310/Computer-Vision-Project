import json
import os

# Load the JSON file containing polygon annotations
folder_path =  r'..\hatch_open_passing\hatch_open_passing_Json'

# Ensure the folder path exists
if os.path.exists(folder_path) and os.path.isdir(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)
    # Filter for JSON files (files with a .json extension)
    json_files = [file_name for file_name in files if file_name.endswith('.json')]
    
    # Iterate through the JSON files
    for json_file in json_files:
        # Construct the full file path
        file_path = os.path.join(folder_path, json_file)
        
        # Open and read the JSON file
        with open(file_path, 'r') as file:
            try:
                polygon_data = json.load(file)
                        # Initialize a list to store bounding boxes
                bounding_boxes = []
                # Extract the points data from the "shapes" section
                shapes = polygon_data["shapes"]

                points = []
                image_height= 1088
                image_width=  1920
                # Function to calculate the bounding box for a polygon
                def calculate_bounding_box(polygon, image_width, image_height):
                    
                    poly_points = polygon['points']
                    
                    min_x = min(poly_points, key=lambda point: point[0])[0]
                    max_x = max(poly_points, key=lambda point: point[0])[0]
                    min_y = min(poly_points, key=lambda point: point[1])[1]
                    max_y = max(poly_points, key=lambda point: point[1])[1]

                    # Calculate center_x, center_y, width, and height of the bounding box
                    center_x = ((max_x + min_x) / 2)
                    center_y = ((max_y + min_y) / 2)

                    x_normalized = (center_x ) / image_width
                    y_normalized = (center_y ) / image_height
                    width = (max_x - min_x) /image_width
                    height = (max_y - min_y) /image_height

                    return x_normalized, y_normalized, width, height

                saved_folder_path  = r'..\hatch_open_passing\hatch_open_passing_Label'

                for shape in shapes:
                    if shape["shape_type"] == "polygon":
                        # Convert polygon to bounding box
                        center_x, center_y, width, height = calculate_bounding_box(shape, image_width, image_height)
                        if shape["label"]== "hatch_open":
                            all_annotated_file = [7]+[center_x]+[center_y]+[width]+[height] # normalize bounding box
                            print("all_annoated hatched_close : ", all_annotated_file)

                if polygon_data['imagePath']:
                    file_name =polygon_data['imagePath'].split(".")[0]
                    file_type = file_name+".txt"          
                    full_file_path = f"{saved_folder_path}\{file_type}"
                #save an image file name
                    with open(full_file_path,'w') as file:
                        file.write(' '.join(map(str, all_annotated_file)))
                else: print('image already exit.')
                     
            except json.JSONDecodeError as e:
                print(f"Error reading JSON file {json_file}: {e}")





