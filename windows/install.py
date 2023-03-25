import sys
import os
import shutil

def aph(path: str):
    return os.path.abspath(path)
startupfolder = aph(sys.argv[1])
workfolder = aph(os.curdir)

def py2startup(name):
    script = aph(f"./startup/{name}.py")
    if not os.path.exists(aph(f"{startupfolder}/{name}.pyw")):
        shutil.copy(script, script+'w')
        shutil.move(script+'w', startupfolder)

py2startup("sort")
