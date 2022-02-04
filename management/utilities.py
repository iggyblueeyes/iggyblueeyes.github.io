'''
utilities.py
'''

import os

def getDirectoriesInside(path, directoryPaths = []):
    if (path[-1] != '/'):
        path += '/'
    directoriesInside = [x for x in os.listdir(path) if '.' not in x]
    if (len(directoriesInside) > 0):
        for directory in directoriesInside:
            newPath = path + directory
            directoryPaths.append(newPath)
            getDirectoriesInside(newPath, directoryPaths)

    return directoryPaths;