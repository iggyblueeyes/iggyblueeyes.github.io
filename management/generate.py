"""
This file will allow me to update all the html files at the same time.
"""

import os
import re
import utilities

stylesFileName = "styles.css"

def writeHTMLFile(root, directoryPath, title):
    bodyText = open(directoryPath + title + ".txt", "r").read()
    # alternatively I could just count the number of fwd slashes instead of using re, but this works fine
    stylesPath = re.sub("/.*/","/../", directoryPath[len(root):]) + stylesFileName
    with open(directoryPath + title + ".html", "w") as file:
        file.write("<html>\n")
        file.write("<head>\n")
        file.write("<link rel='stylesheet' href='"+ stylesPath + "'>")
        file.write("</head>\n")
        file.write("<body>\n")
        file.write(bodyText)
        file.write("</body>\n")
        file.write("</html>")

root = "../"

directoryPaths = utilities.getDirectoriesInside(root)

for directoryPath in directoryPaths:
    for filename in utilities.getFilenamesInDirWithExt(directoryPath, ".txt"):
        writeHTMLFile(root, directoryPath, filename)
