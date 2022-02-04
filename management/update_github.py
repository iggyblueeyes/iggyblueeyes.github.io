import os
import utilities
import pprint

root = ".."

directoryPaths = utilities.getDirectoriesInside(root)

pprint.pprint(directoryPaths)

for path in directoryPaths:
    for filename in os.listdir(path):
        print(path + filename)
        if '~' in filename:
            print("remove")
            os.system('rm ' + path + filename)
        else:
            print("add")
            os.system('git add ' + path + filename)
    
os.system('git commit -m "Update"')
os.system('git push')
