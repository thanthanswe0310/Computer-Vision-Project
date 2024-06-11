import json

json_data = rjson_data = r'\ContilTrain.json' #put here your json file

# Read JSON data from the input JSON file
with open(json_data, "r") as json_file:
    json_data = json.load(json_file)

cat_temp = []
cat_dictList = []
img_dictList = []
annot_dictList = []

filter_cat_id = 0
# Iterate through the nested dictionaries
for key, val in json_data.items():
    if key == 'categories':
        for val_category in json_data['categories']:
            if val_category['name'] == "Y-34":
                filter_cat_id = val_category['id']
                print(filter_cat_id)
                cat_dictList.append(val_category)
    elif key == 'images':
        print("2")
        for val_images in json_data['images']:
            img_dictList.append(val_images)
    elif key == 'annotations':
        print("3")
        for val_annotation in json_data['annotations']:
            if filter_cat_id == val_annotation['category_id']:
                annot_dictList.append(val_annotation)
            

def polygon_to_bbox(polygon_points, image_width, image_height):
    
    # Find minimum and maximum x, y coordinates of the polygon
    min_x, min_y = min(polygon_points, key=lambda p: p[0])[0], min(polygon_points, key=lambda p: p[1])[1]
    max_x, max_y = max(polygon_points, key=lambda p: p[0])[0], max(polygon_points, key=lambda p: p[1])[1]

    # Calculate center_x, center_y, width, and height of the bounding box
    center_x = ((max_x + min_x) / 2)
    center_y = ((max_y + min_y) / 2)

    x_normalized = (center_x ) / image_width
    y_normalized = (center_y ) / image_height
    width = (max_x - min_x) /image_width
    height = (max_y - min_y) /image_height

    #print( "In function:  ",center_x, center_y, width, height)

    # Normalize the coordinates to range [0, 1]
    
    #width /= image_width
    #height /= image_height

    return x_normalized, y_normalized, width, height

saved_folder_path  = r'\label' # Save your desire location
print("parsing is started")
for annot_list in annot_dictList:
    for img_list in img_dictList:
        for cat_list in cat_dictList:            
            if annot_list['image_id'] == img_list['id'] and annot_list['category_id'] == cat_list['id']:
                image_width = 1920
                image_height = 1080
                print("image founded")
                # import pdb;pdb.set_trace()
            # Split the line into class and polygon points
                # polygon_line = (line.split(',') for line in annot_list['segmentation'])
                
                polygon_points = sum(annot_list['segmentation'], [])
            # Convert polygon points to a list of tuples
                polygon_points = [(polygon_points[i], polygon_points[i + 1]) for i in range(0, len(polygon_points)-1, 2)]
            # Convert polygon to bounding box
                center_x, center_y, width, height = polygon_to_bbox(polygon_points, image_width, image_height)
                #print( "function call: ", center_x, center_y, width, height)

             
          
        
                all_annotated_file = [cat_list['id']]+[center_x]+[center_y]+[width]+[height] # normalize bounding box
              
                if img_list['file_name']:
                    file_name =img_list['file_name'].split(".")[0]
                    file_type = file_name+".txt"          
                    full_file_path = f"{saved_folder_path}\{file_type}"
                #save an image file name
                    with open(full_file_path,'w') as file:
                        file.write(' '.join(map(str, all_annotated_file)))
                else: print('image already exit.')
        


            
