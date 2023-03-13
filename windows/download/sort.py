import os
USERLOGIN = os.getlogin()
DIRECTORY = 'C:/Users/' + USERLOGIN + '/Downloads'
DIR_RULES = {
    "_Folders":{},
    "Documents":{".pdf", ".docx"},
    "Images":{".gif", ".png", ".jpg"},
    "Videos":{".mp4", ".mkv", ".webm"},
    "Sound":{".mp3", ".wav", ".webm"},
    "Executables":{".exe", ".msi"},
    "Compressed":{".zip", ".rar", ".7z", ".tar.gz"},
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

for dir_name in DIR_RULES:
    dir_full = DIRECTORY + '/' + dir_name
    rule_count = len(DIR_RULES[dir_name])
    if os.path.exists(dir_full) == 0:
        os.mkdir(dir_full)
        print("created", dir_name)
    if rule_count:
        print(rule_count)
    elif dir_name == '_Folders':
        if folder_count > len(DIR_RULES):
            print(file_count, '-', folder_count, ':', len(DIR_RULES))