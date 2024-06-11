import os

def remove_classes_and_coordinates(folder_path, target_classes):
    # 폴더 내의 모든 txt 파일 가져오기
    txt_files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]

    # 각 파일에 대해 작업 수행
    for file_name in txt_files:
        file_path = os.path.join(folder_path, file_name)

        # 파일 읽기
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # 새로운 내용을 저장할 리스트
        new_lines = []

        # 각 줄에 대해 검사하여 특정 클래스 번호와 좌표값 제거
        for line in lines:
            parts = line.split(' ')
            current_class = parts[0]

            # 제거할 클래스 번호와 일치하지 않으면 추가
            if current_class not in target_classes:
                new_lines.append(line)

        # 파일에 새로운 내용 쓰기
        with open(file_path, 'w') as file:
            file.writelines(new_lines)

if __name__ == "__main__":
    # 작업할 폴더 경로
    folder_path = "F:\yolov7-main\coco128/valid\labels/"

    # 제거할 클래스 번호들
    target_classes = ["2","4","6"]

    # 함수 호출
    remove_classes_and_coordinates(folder_path, target_classes)

    print(f"클래스 {', '.join(target_classes)}와 해당 좌표값을 제거하는 작업이 완료되었습니다.")
