
import cv2
import os

video_folder = "..\..\data/"
output_folder = "..\..\data/"

# video_files = [f for f in os.listdir(video_folder) if f.endswith(('.mp4', '.avi', '.mkv'))]


# for video_file in video_files:
#     video_path = os.path.join(video_folder, video_file)
#     cap = cv2.VideoCapture(video_path)

#     if not cap.isOpened():        
#         print(f"{video_path} not working")
#         continue

#     video_name = os.path.splitext(video_file)[0]

#     video_output_folder = os.path.join(output_folder, video_name)
#     os.makedirs(video_output_folder, exist_ok=True)

#     frame_count = 1

#     while True:
#         ret, frame = cap.read()

#         if not ret:
#             break

#         image_name = f'{video_name}_{frame_count:03d}.jpg'
#         image_path = os.path.join(video_output_folder, image_name)

#         cv2.imwrite(image_path, frame)
#         print(f'{image_name} save.')

#         frame_count += 1

#     cap.release()
#     cv2.destroyAllWindows() 
# print ("Work Done")
# 5 Frame 1
# video_files = [f for f in os.listdir(video_folder) if f.endswith(('.mp4', '.avi', '.mkv'))]

# for video_file in video_files:
#     video_path = os.path.join(video_folder, video_file)
#     cap = cv2.VideoCapture(video_path)

#     if not cap.isOpened():        
#         print(f"{video_path} not working")
#         continue

#     video_name = os.path.splitext(video_file)[0]

#     video_output_folder = os.path.join(output_folder, video_name)
#     os.makedirs(video_output_folder, exist_ok=True)

#     frame_count = 1
#     image_count = 1

#     while True:
#         ret, frame = cap.read()

#         if not ret:
#             break

#         if frame_count % 5 == 1:
#             image_name = f'{video_name}_{image_count:03d}.jpg'
#             image_path = os.path.join(video_output_folder, image_name)
#             cv2.imwrite(image_path, frame)
#             print(f'{image_name} saved.')
#             image_count += 1

#         frame_count += 1

#     cap.release()
#     cv2.destroyAllWindows() 

# print ("Work Done")


# 2 images per second
desired_fps = 1  # 1 / 2 = 0.5

video_files = [f for f in os.listdir(video_folder) if f.endswith(('.mp4', '.avi', '.mkv'))]

for video_file in video_files:
    video_path = os.path.join(video_folder, video_file)
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"{video_path} not working")
        continue

    video_name = os.path.splitext(video_file)[0]

    video_output_folder = os.path.join(output_folder, video_name)
    os.makedirs(video_output_folder, exist_ok=True)

    frame_count = 1
    image_count = 1

    fps = int(cap.get(cv2.CAP_PROP_FPS)) # Get the frame rate of the video

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        if frame_count % (fps / desired_fps) == 1:
            image_name = f'{video_name}_{image_count:03d}.jpg'
            image_path = os.path.join(video_output_folder, image_name)
            cv2.imwrite(image_path, frame)
            print(f'{image_name} saved.')
            image_count += 1

        frame_count += 1

    cap.release()
    cv2.destroyAllWindows()
print ("Work Done")
