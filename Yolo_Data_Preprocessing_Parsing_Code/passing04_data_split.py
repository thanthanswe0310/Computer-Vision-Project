#%% Kütüphanelerin Yüklenmesi
from IPython.display import Image  
import os 
import random
import shutil
from sklearn.model_selection import train_test_split
import xml.etree.ElementTree as ET
from xml.dom import minidom
from tqdm import tqdm
from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt
import glob

images = [os.path.join('images', x) for x in os.listdir('images')]
annotations = [os.path.join('annotations', x) for x in os.listdir('annotations') if x[-3:] == "txt"]
images.sort()
annotations.sort()
train_images, val_images, train_annotations, val_annotations = train_test_split(images, annotations, test_size = 0.2, random_state = 1)
val_images, test_images, val_annotations, test_annotations = train_test_split(val_images, val_annotations, test_size = 0.5, random_state = 1)

#%% Yolov5 Formatında Veri Setini Ayalarma

root_path = 'C:/data/coco128/train2017/images/'
folders = ['train','test/','val']
for folder in folders:
    os.makedirs(os.path.join(root_path,folder))
    
root_path = 'C:/data/coco128/train2017/labels/'
folders = ['train','test/','val']
for folder in folders:
    os.makedirs(os.path.join(root_path,folder))    

#%% Resim ve Labelleri Dosyalara Taşıma

def move_files_to_folder(list_of_files, destination_folder):
    for f in list_of_files:
        try:
            shutil.move(f, destination_folder)
        except:
            print(f)
            assert False

move_files_to_folder(train_images, 'C:/data/train_image/')
move_files_to_folder(test_images, 'C:/data/test_image/')
move_files_to_folder(val_images, 'C:/data/val_image/')
move_files_to_folder(train_annotations, 'C:/data/train_label/')
move_files_to_folder(test_annotations, 'C:/data/test_label/')
move_files_to_folder(val_annotations, 'C:/data/val_label/')