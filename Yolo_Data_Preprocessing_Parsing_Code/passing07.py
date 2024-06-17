import cv2
import os
video_path = 'F:/total_dataset\data_20230918/1.mp4'

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Unable to open the video file.")
    exit()

output_path = '..\..\data_20230918\image/'

frame_count = 1

base_name = "A_20230918_"

while True:
   # Read the frame
    ret, frame = cap.read()

    if not ret:
        break

    # Create Image File Name
    image_name = f'{base_name}{frame_count:04d}.jpg'
    image_path = os.path.join(output_path, image_name)

    cv2.imwrite(image_path, frame)
    print(f'{image_name} 이미지로 저장.')

    frame_count += 1

# Release after completion of the job
cap.release()
cv2.destroyAllWindows()
