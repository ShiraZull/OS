import os
USERLOGIN = os.getlogin()
DIRECTORY = 'C:/Users/' + USERLOGIN + '/Downloads'
SORTFOLDERS = {
    "_Folders":{},
    "Documents":{".pdf", ".doc"},
    "Images":{".gif", ".png", ".jpg"},
    }

entries = os.scandir(DIRECTORY)
for entry in entries:
    if entry.is_dir():
        print(entry.name)

print(SORTFOLDERS)
for thing in SORTFOLDERS:
    for thinginthing in SORTFOLDERS[thing]:
        print(thinginthing)

for dir in SORTFOLDERS:
    dirfull = DIRECTORY + '/' + dir
    if os.path.exists(dirfull) == 0:
        os.mkdir(dirfull)
        print("created", dir)