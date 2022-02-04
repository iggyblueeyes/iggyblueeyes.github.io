import os
import utilities
import pprint

root = ".."

directoryPaths = utilities.getDirectoriesInside(root)

pprint.pprint(directoryPaths)

for path in directoryPaths:
    os.system('git add ' + path + '*')
    
os.system('git commit -m "Update"')
os.system('git push')
