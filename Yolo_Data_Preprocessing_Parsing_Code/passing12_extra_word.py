import os

def remove_suffix_and_extra(file_name, suffix):
    index = file_name.find(suffix)
    if index != -1:
        cleaned_name = file_name[:index] 
        return cleaned_name
    else:
        return file_name

folder_path = 'F:/total_dataset\data_20230918/thanthan\coco120/valid/test/'

suffix_to_remove = "_jpg"
file_names = os.listdir(folder_path)

for old_name in file_names:
    new_name = remove_suffix_and_extra(old_name, suffix_to_remove)

    old_path = os.path.join(folder_path, old_name)
    new_path = os.path.join(folder_path, new_name)
    
    os.rename(old_path, new_path)

print("done")


# import os

# def remove_suffix_and_extra(file_name):
#     # 파일 이름에서 마지막 "_"를 찾음
#     last_underscore_index = file_name.rfind("_")
    
#     # 확장자 포함 "_" 이후의 문자열을 제거
#     if last_underscore_index != -1:
#         cleaned_name = file_name[:last_underscore_index]
#         return cleaned_name
#     else:
#         # "_"가 없는 파일 이름은 그대로 유지
#         return file_name

# # 폴더 경로 설정
# folder_path = 'F:/total_dataset\data_20230918/thanthan\coco120/valid/test/'

# # 폴더 내의 모든 파일 목록 가져오기
# file_names = os.listdir(folder_path)

# # 각 파일 이름 수정 및 이동
# for old_name in file_names:
#     # 수정된 파일 이름 생성
#     new_name = remove_suffix_and_extra(old_name)
    
#     # 새 파일 이름으로 파일 이동
#     old_path = os.path.join(folder_path, old_name)
#     new_path = os.path.join(folder_path, new_name)
    
#     os.rename(old_path, new_path)

# print("파일 이름 수정이 완료되었습니다.")