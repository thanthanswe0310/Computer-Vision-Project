import json
import os

# Load the JSON file containing polygon annotations
folder_path =  r'..\hatch_open_close_passing\test\test_json'
all_annotated_file=[]

def flatten_list(nested_list):
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened
# Process each item in the list
modified_list = []
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

                saved_folder_path  = r'..\hatch_open_close_passing\test\test_label'
                
                for shape in shapes:
                    if shape["shape_type"] == "polygon":
                        # Convert polygon to bounding box
                        center_x, center_y, width, height = calculate_bounding_box(shape, image_width, image_height)
                        #scaffolding , worker, box, hatch_close, hatch_open : In mobile_scaffolding dataset, we have five classes
                        if shape["label"]== "scaffolding": 
                            all_annotated_file.append([0]+[center_x]+[center_y]+[width]+[height]) # normalize bounding box
                            
                        elif shape['label'] =="worker":
                            all_annotated_file.append([1]+[center_x]+[center_y]+[width]+[height]) # normalize bounding box
                            
                        elif shape["label"]== "hatch_open":
                            all_annotated_file.append([7]+[center_x]+[center_y]+[width]+[height])# normalize bounding box
                            
                        elif shape['label'] =="hatch_close":
                            all_annotated_file.append([8]+[center_x]+[center_y]+[width]+[height])# normalize bounding box
                            
                        elif shape["label"]== "box":
                            all_annotated_file.append([9]+[center_x]+[center_y]+[width]+[height]) # normalize bounding box
                        else: continue
               
                flat_list = flatten_list(all_annotated_file)
                print(type(all_annotated_file))
                if polygon_data['imagePath']:
                    file_name =polygon_data['imagePath'].split(".")[0]
                    file_type = file_name+".txt"          
                    full_file_path = f"{saved_folder_path}\{file_type}"


                    with open(full_file_path,'w') as file:
                        for item in all_annotated_file:
                            s = " ".join(map(str, item))
                            file.write(s+'\n')
                

            except json.JSONDecodeError as e:
                print(f"Error reading JSON file {json_file}: {e}")





