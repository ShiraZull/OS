import os
import shutil
import time

DELAY = 60*60*24*7
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

entries = os.scandir(DIRECTORY)
folder_count = 0
file_count = 0
for entry in entries:
    if entry.is_dir():
        folder_count += 1
    elif entry.is_file():
        file_count += 1

print(DIR_RULES)
for thing in DIR_RULES:
    for thinginthing in DIR_RULES[thing]:
        print(thinginthing)

def group_folders(folder_count):
    if folder_count > len(DIR_RULES):
        for entry in os.scandir(DIRECTORY):
            valid = False
            if entry.is_dir():
                for white_listed_entry in DIR_RULES:
                    if entry.name == white_listed_entry:
                        valid = True
                        break
                if valid:
                    continue
                else:
                    move(entry.path, DIRECTORY+'/_Folders', "")
                    print("moved", entry.path, "to", DIRECTORY+'/_Folders')

def group_files(dir_name):
    for entry in os.scandir(DIRECTORY):
        if entry.stat().st_ctime + DELAY < time.time():
            for dir_rule in DIR_RULES[dir_name]:
                if entry.name.endswith(dir_rule):
                    move(entry.path, DIRECTORY+'/'+dir_name, dir_rule)
                    break

def move(src, dst, dir_rule):
    filename = os.path.basename(src)
    newfilename = filename
    count = 0
    while True:
        if os.path.exists(dst+'/'+newfilename):
            count += 1
            extention = " ("+str(count)+")"
            newfilename = filename[:(-len(dir_rule)) if len(dir_rule) else (len(filename)) ] + extention + dir_rule
        else:
            break
    if count:
        parentpath = src[:-len(filename)]
        os.rename(parentpath+filename, parentpath+newfilename)
        src = parentpath+newfilename
    shutil.move(src, dst)

for dir_name in DIR_RULES:
    dir_full = DIRECTORY + '/' + dir_name
    rule_count = len(DIR_RULES[dir_name])
    if os.path.exists(dir_full) == 0:
        os.mkdir(dir_full)
        print("created", dir_name)
    if rule_count:
        group_files(dir_name)
    elif dir_name == '_Folders':
        group_folders(folder_count)
