import os
import utilities
import pprint

root = ".."

directoryPaths = utilities.getDirectoriesInside(root)

pprint.pprint(directoryPaths)

for path in directoryPaths:
    for filename in os.listdir(path):
        if '~' != filename[-1] and '_' != filename[0] and '.' != filename[0]:
            print(path + filename)
            os.system('git add ' + path + filename)
    
os.system('git commit -m "Update"')
os.system('git push')
