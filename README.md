# CSci-435-Programming-assignment-1

To run this program execute script.py through a python interpreter and have it be in the same directory as your "Programming-Assignment-Data" and "output" folders.

You will need the following python libraries: os, re, and PIL (Pillow==9.4.0). Run "pip install -r requirements.txt".

My solution works by first getting the basenames for all the files in the 
data folder.  This is so that even if the filenames change, or more are added, my program will still consider them.  Then I get the bounds for every leaf node within a given xml file.  This is done using a regular expression that checks for self-closing nodes or nodes that are closed immediatly after ending (<node blah blah > </node>).  I chose a regular expression over a xml parsing library because I think apalon.ringtones isn't valid xml, so it would run into an error.  I also use a capturing group to only grab the bounds as a string ("[0,0][1440,2368]") and then I do some string manipulation to convert it to a tuple of ints ((0, 0, 1440, 2368)).  Finally, I call the DrawYellowBoxes function that uses the PIL library to draw the rectangles based on the bounds given to it.  It saves it the new pngs in the output folder.  My program runs on the assumption that the data folder exists with pairs of matching png and xml files and that the output folder exists.  