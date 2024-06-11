import os
import random
import shutil

data_folder = "F:/total_dataset\data_20230918/thanthan\coco120\images/"  # 이미지 데이터셋이 있는 폴더 경로
output_folder = "F:/total_dataset\data_20230918/thanthan/coco120/train/"  # 분할된 데이터셋을 저장할 폴더 경로

# 각 데이터셋의 비율 설정 (전체 데이터를 기준으로)
train_ratio = 0.8
val_ratio = 0.2
# test_ratio = 0.1

def split_dataset(data_folder, output_folder):
    # 분할된 데이터셋 폴더 생성
    os.makedirs(output_folder, exist_ok=True)

    # 이미지 파일과 레이블 파일 리스트 생성
    image_files = [filename for filename in os.listdir(data_folder) if filename.endswith('.jpg')]  # 이미지 파일 확장자에 맞게 수정
    label_files = [filename for filename in os.listdir(data_folder) if filename.endswith('.txt')]  # 레이블 파일 확장자에 맞게 수정

    # 데이터를 무작위로 섞음
    random.shuffle(image_files)

    # 분할할 인덱스 계산
    total_samples = len(image_files)
    train_end = int(total_samples * train_ratio)
    val_end = train_end + int(total_samples * val_ratio)

    # 각 데이터셋에 이미지와 레이블 파일 복사
    for i, filename in enumerate(image_files):
        source_image_path = os.path.join(data_folder, filename)
        source_label_path = os.path.join(data_folder, filename.replace('.jpg', '.txt'))  # 이미지와 레이블 파일 이름 대응되도록 수정
        dest_folder = "train" if i < train_end else ("val" if i < val_end else "test")
        dest_image_path = os.path.join(output_folder, dest_folder, filename)
        dest_label_path = os.path.join(output_folder, dest_folder, filename.replace('.jpg', '.txt'))

        os.makedirs(os.path.dirname(dest_image_path), exist_ok=True)
        shutil.copy(source_image_path, dest_image_path)
        shutil.copy(source_label_path, dest_label_path)

        print(f"Copied {filename} to {dest_folder} dataset")

split_dataset(data_folder, output_folder)
