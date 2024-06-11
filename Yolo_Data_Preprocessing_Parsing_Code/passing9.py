import os

# 처리할 폴더 경로
input_folder_path = "E:\yolov7-main\coco128/train\labels/"
output_folder_path = "E:\yolov7-main\coco128/train01/"
target_class = "9"
# 출력 폴더가 없으면 생성
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# 입력 폴더의 모든 .txt 파일을 가져와서 처리
for filename in os.listdir(input_folder_path):
    if filename.endswith(".txt"):
        input_file_path = os.path.join(input_folder_path, filename)
        output_file_path = os.path.join(output_folder_path, filename)

        # 파일을 읽어오고 새로운 내용을 저장할 리스트 생성
        new_lines = []

        # 파일 읽기
        with open(input_file_path, "r") as file:
            lines = file.readlines()

        # 클래스 정보와 좌표 값을 추출하고 필요한 경우에만 저장
        for line in lines:
            parts = line.strip().split()
            if len(parts) >= 5 and parts[0] != target_class:
                new_lines.append(line)
            elif len(parts) < 5:
                # 클래스 정보가 없는 빈 줄도 유지
                new_lines.append(line)

        # 새로운 내용을 파일로 저장
        with open(output_file_path, "w") as file:
            file.writelines(new_lines)

        print("Done:", output_file_path)

print("모든 파일 처리 완료")