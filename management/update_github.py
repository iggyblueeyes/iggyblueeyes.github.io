import os
import utilities

root = ".."

#directoryPaths = [];

'''
def getDirectoriesInside(path):
    if (path[-1] != '/'):
        path += '/'
    directoriesInside = [x for x in os.listdir(path) if '.' not in x]
    if (len(directoriesInside) > 0):
        for directory in directoriesInside:
            newPath = path + directory
            directoryPaths.append(newPath)
            getDirectoriesInside(newPath)
'''

directoryPaths = utilities.getDirectoriesInside(root)

print(directoryPaths)

for path in directoryPaths:
    os.system('git add ' + path + '*')
    
os.system('git commit -m "Update"')
os.system('git push')
