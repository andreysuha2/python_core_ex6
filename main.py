from normalize import normalize
from sys import argv
from pathlib import Path

DEFAULT_PATH = Path(argv[1])

FOLDERS_DATA = [
    {
        "name": "archives",
        "extensions": ('ZIP', 'GZ', 'TAR')
    },
    {
        "name": "video",
        "extensions": ('AVI', 'MP4', 'MOV', 'MKV')
    },
    {
        "name": "audio",
        "extensions": ('MP3', 'OGG', 'WAV', 'AMR') 
    },
    {
        "name": "documents",
        "extensions": ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
    },
    {
        "name": "images",
        "extensions": ('JPEG', 'PNG', 'JPG', 'SVG')
    }
]

def arrange(path):
    if not path.exists():
        print(f"Folder '{path.name}' in '{path.parent}' doesn't exist!")

arrange(DEFAULT_PATH)