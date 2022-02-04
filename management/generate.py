"""
This file will allow me to update all the html files at the same time.
"""

import re
import os

#folders = [e for e in os.listdir() if "." not in e]
#htmlFiles = [e for e in os.listdir() if ".html" in e]

root = ".."

os.chdir(root)

print(os.listdir())


#print(folders)
#print(htmlFiles)

#f = open(htmlFiles[0], "r")
#print(f.read())

#os.chdir("tutoring")
