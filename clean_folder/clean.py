import os
import sys
import shutil
import re
from pathlib import Path



def normalize(name):
    translit = str.maketrans("абвгдеёзийклмнопрстуфхъыьэАБВГДЕЁЗИЙКЛМНОПРСТУФХЪЫЬЭ",
                             "abvgdeezijklmnoprstufh'y'eABVGDEEZIJKLMNOPRSTUFH'Y'E")
    name = name.translate(translit)
    name = re.sub(r'[^a-zA-Z0-9]', '_', name)

    return name



def process_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = file.split('.')[-1].upper()

            if file_extension in ('JPEG', 'PNG', 'JPG', 'SVG'):
                target_folder = 'images'
            elif file_extension in ('AVI', 'MP4', 'MOV', 'MKV'):
                target_folder = 'video'
            elif file_extension in ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'):
                target_folder = 'documents'
            elif file_extension in ('MP3', 'OGG', 'WAV', 'AMR'):
                target_folder = 'audio'
            elif file_extension in ('ZIP', 'GZ', 'TAR'):
                target_folder = 'archives'
                extract_folder = os.path.join(target_folder, file.replace('.' + file_extension, ''))
                shutil.unpack_archive(file_path, extract_folder)
                continue
            else:
                target_folder = 'unknown'

            target_folder_path = os.path.join(folder_path, target_folder)
            Path(target_folder_path).mkdir(parents=True, exist_ok=True)

            new_file_name = normalize(file.split('.')[0]) + '.' + file_extension
            new_file_path = os.path.join(target_folder_path, new_file_name)

            shutil.move(file_path, new_file_path)



if len(sys.argv) != 2:
    print("Usage: python sort.py <folder_path>")
    sys.exit(1)

folder_path = sys.argv[1]

if not os.path.exists(folder_path):
    print(f"Folder '{folder_path}' doesn't exist.")
    sys.exit(1)