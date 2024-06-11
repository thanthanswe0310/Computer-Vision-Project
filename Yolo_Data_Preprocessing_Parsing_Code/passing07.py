import cv2
import os
video_path = 'F:/total_dataset\data_20230918/1.mp4'

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("동영상 파일을 열 수 없습니다.")
    exit()

output_path = 'F:/total_dataset\data_20230918\image/'

frame_count = 1

base_name = "A_20230918_"

while True:
    # 프레임 읽기
    ret, frame = cap.read()

    if not ret:
        break

    # 이미지 파일 이름 생성
    image_name = f'{base_name}{frame_count:04d}.jpg'
    image_path = os.path.join(output_path, image_name)

    cv2.imwrite(image_path, frame)
    print(f'{image_name} 이미지로 저장.')

    frame_count += 1

# 작업 완료 후 해제
cap.release()
cv2.destroyAllWindows()