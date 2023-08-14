from normalize import normalize
from sys import argv
from pathlib import Path
import os

DEFAULT_PATH = Path(argv[1] if len(argv) >= 2 else './')

FOLDERS_DATA = {
        "archives": ('ZIP', 'GZ', 'TAR'),
        "video": ('AVI', 'MP4', 'MOV', 'MKV'),
        "audio": ('MP3', 'OGG', 'WAV', 'AMR'),
        "documents": ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX', 'CSV', 'XLS'),
        "images": ('JPEG', 'PNG', 'JPG', 'SVG')
    }

def create_directories(path):
    for name in FOLDERS_DATA:
        folder_path = f"{path.parent}/{path.name}/{name}"

        if not Path(folder_path).exists():
            os.mkdir(folder_path)

def handle_file(path): 
    parent_folder_name = None
    file = path.name.split('.')
    file_ext = file.pop()
    file_name = '.'.join(file)
    for name, list in FOLDERS_DATA.items():
        if file_ext.upper() in list:
            parent_folder_name = name
            break

    if parent_folder_name:
        file_name = f"{normalize(file_name)}{path.suffix}"
        new_path = f"{path.parent}/{parent_folder_name}/{file_name}"
        os.rename(path, new_path)
        print(path, '-->', new_path)

def arrange(path):
    if not path.exists():
        print(f"Folder '{path.name}' in '{path.parent}' doesn't exist!")
    elif path.is_file():
        print(f"'{path.name}' is not a folder!")
    else:
        create_directories(path)
        for i in path.iterdir():
            if i.is_dir() and i.name not in FOLDERS_DATA:
                arrange(i)
            elif i.is_file():
                handle_file(i)

arrange(DEFAULT_PATH)