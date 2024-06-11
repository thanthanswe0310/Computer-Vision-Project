import json

json_data = r'..\coco_json_txt\roboflowtest.json'

# Read JSON data from the input JSON file
with open(json_data, "r") as json_file:
    json_data = json.load(json_file)

cat_temp=[]
cat_dictList =[]
img_dictList =[]
annot_dictList =[]  
# Iterate through the nested dictionaries
for key, val in json_data.items():
    if key=='categories':
        for val_category in json_data['categories']:
            cat_dictList.append(val_category)
    elif key=='images':
        for val_images in json_data['images']:
            img_dictList.append(val_images)
    elif key=='annotations':
        for val_annotation in json_data['annotations']:
            annot_dictList.append(val_annotation)
            

saved_folder_path  = r'..\Label'

for annot_list in annot_dictList:
    for img_list in img_dictList:
        for cat_list in cat_dictList:            
            if annot_list['image_id'] == img_list['id'] and annot_list['category_id'] == cat_list['id']:
                image_width=  1920
                image_height = 1080
                for index,ann_val in enumerate(annot_list['bbox']):
                    if index ==0: x =ann_val
                    elif index==1: y = ann_val
                    elif index ==2: x_max = x + ann_val
                    elif index ==3: y_max = y+ann_val
                
            # Normalize the coordinates to range [0,1]
                    
                # center_x = x/image_width
                # center_y= y/image_height
                # width = x_max/image_width
                # height = y_max/image_height
        
                # all_annotated_file = [cat_list['id']]+[center_x]+[center_y]+[width]+[height] # normalize bounding box
                all_annotated_file = [cat_list['id']]+[x]+[y]+[x_max]+[y_max]  # Coco bounding box
                # all_annotated_file= [cat_list['id']]+annot_list['bbox']
                if img_list['file_name']:
                    file_name =img_list['file_name'].split(".")[0]
                    file_type = file_name+".txt"          
                    full_file_path = f"{saved_folder_path}\{file_type}"
                #save an image file name
                    with open(full_file_path,'w') as file:
                        file.write(' '.join(map(str, all_annotated_file)))
                else: print('image already exit.')
            


            