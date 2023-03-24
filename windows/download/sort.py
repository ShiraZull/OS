# Project inspired by "Internet Made Coder"
# https://youtu.be/NCvI-K0Gp90

import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

DELAY = 60*60*24*7 #Time where files are accessable in downloads directly
DIRECTORY = 'C:/Users/' + os.getlogin() + '/Downloads'
DIR_RULES = {
    "_Folders":{},
    "Documents":{".pdf", ".docx"},
    "Images":{".gif", ".png", ".jpg"},
    "Videos":{".mp4", ".mkv", ".webm", ".mov"},
    "Sound":{".mp3", ".wav", ".webm"},
    "Executables":{".exe", ".msi", ".iso"},
    "Compressed":{".zip", ".rar", ".7z", ".tar.gz"},
    "DataSheets":{".csv", ".json", ".xlsx", ".xls", ".xlsm"},
    }

def group_folders():
    directories = list(entry for entry in os.scandir(DIRECTORY) if entry.is_dir())
    if len(directories) > len(DIR_RULES):
        for directory in directories:
            if directory.name not in DIR_RULES:
                move(directory.path, DIRECTORY+'/_Folders', "")
                print("moved", directory.path, "to", DIRECTORY+'/_Folders')

def group_files(dir_name):
    for file in os.scandir(DIRECTORY):
        if file.stat().st_ctime + DELAY < time.time():
            for dir_rule in DIR_RULES[dir_name]:
                if file.name.endswith(dir_rule):
                    move(file.path, DIRECTORY+'/'+dir_name, dir_rule)
                    break

# Move the file from src to dst, will add '(x)' if there is already a file of the same name in the destination
def move(src, dst, dir_rule):
    filename = os.path.basename(src)
    newfilename = filename
    count = 0
    while os.path.exists(dst+'/'+newfilename):
        count += 1
        extention = " ("+str(count)+")"
        newfilename = filename[:(-len(dir_rule)) if len(dir_rule) else (len(filename)) ] + extention + dir_rule
    if count:
        parentpath = src[:-len(filename)]
        os.rename(parentpath+filename, parentpath+newfilename)
        src = parentpath+newfilename
    shutil.move(src, dst)

def sort_download_directory():
    for dir_name in DIR_RULES:
        dir_full = DIRECTORY + '/' + dir_name
        rule_count = len(DIR_RULES[dir_name])
        if os.path.exists(dir_full) == 0:
            os.mkdir(dir_full)
            print("created", dir_name)
        if rule_count:
            group_files(dir_name)
        elif dir_name == '_Folders':
            group_folders()

class MoverHandler(FileSystemEventHandler):
    def on_modified(self, event):
        sort_download_directory()

if __name__ == "__main__":
    path = DIRECTORY
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()