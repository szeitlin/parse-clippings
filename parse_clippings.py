__author__ = 'szeitlin'

#script to clean up exported 'clippings.txt' file from kindle annotations
#removes repetition of title and date from each annotation

import re

myfile = 'My Clippings.txt'

title = 'Memoir draft Feb2015 (Samantha Zeitlin)'

p = re.compile('[|]\s\w*') #remove the dates after '|' symbol, don't need them

with open ('cleaned_clippings.txt', 'w') as clipped:

    with open (myfile, 'r') as clips:
        for line in clips:
            if title in line:
                continue
            elif p.findall(line)!=[]:
                q = p.split(line)
                clipped.write(q[0])
            elif p.findall(line)==[]:
                clipped.write(line)

