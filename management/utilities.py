'''
Utilities
'''

import os

def getDirectoriesInside(path, directoryPaths = []):
    if (path[-1] != '/'):
        path += '/'
    if len(directoryPaths) == 0:
        directoryPaths.append(path);
    directoriesInside = [x for x in os.listdir(path) if not any((c in '._') for c in x)]
    if (len(directoriesInside) > 0):
        for directory in directoriesInside:
            newPath = path + directory + '/'
            directoryPaths.append(newPath)
            getDirectoriesInside(newPath, directoryPaths)
    return directoryPaths;

def getFilenamesInDirWithExt(path, extension):
    return [f[0:-len(extension)] for f in os.listdir(path) if f[-len(extension):] == extension]
