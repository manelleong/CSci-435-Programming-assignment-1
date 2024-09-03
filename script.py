import re
import os
from PIL import Image, ImageDraw

"""
Returns a set of all file base names from a provided directory
"""
def GetBaseNames(directory):
    base_names = set()

    for filename in os.listdir(directory):
        base_name = os.path.splitext(filename)[0]

        base_names.add(base_name)

    return base_names

"""
Given the path to an xml file, returns a list of tuples of ints representing bounds of leaf nodes

[(x1, y1, x2, y2), ...]
"""
def GetLeafNodeBounds(filePath):
    leafNodePattern = r'node[^>]+bounds="([^"]+)"[^>]*?(?:\/>|>\s*<\/node>)'

    with open(filePath, 'r') as file:
        content = file.read()

    matches = re.findall(leafNodePattern, content)

    boundsList = []
    for match in matches:
        parts = match.replace('[', '').replace(']', ',').split(',')[:-1]

        boundsList.append(tuple(map(int, parts)))

    return boundsList

"""
Given a path to a png file, a list of bounds, and a base name this function
draws and saves a new png with bounds delimited in yellow in the output folder
"""
def DrawYellowBoxes(filePath, boundsList, baseName):
    image = Image.open(filePath)

    draw = ImageDraw.Draw(image)

    for bounds in boundsList:
        draw.rectangle(bounds, outline = 'yellow', width = 5)

    image.save(f'output/{baseName}.annotated.png')

"""
Reads and parses the xml for the bounds of leaf nodes and then
produces new pngs with those bounds delmited in yellow
"""
def main():
    directory = 'Programming-Assignment-Data'
    baseNames = GetBaseNames(directory)

    for baseName in baseNames:
        xmlFilePath = f'{directory}/{baseName}.xml'
        pngFilePath = f'{directory}/{baseName}.png'

        leafNodeBounds = GetLeafNodeBounds(xmlFilePath)

        DrawYellowBoxes(pngFilePath, leafNodeBounds, baseName)

if __name__ == '__main__':
    main()
