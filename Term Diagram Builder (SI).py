# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 14:58:55 2015

@author: cpc14
"""

""
import matplotlib.pyplot as plt
import matplotlib.patches as ptch
import csv

box_width = 1.
i = 0

plt.ylabel('Energy (cm-1)')
plt.xlabel('ML')
plt.axis([0, 12, -10000, 200000])
plt.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')

plt.text(1.8, 12000, '3d9')  # Parent term labels
plt.text(3.8, 157000, '3F')
plt.text(5.8, 170000, '1D')
plt.text(7.8, 172500, '3P')
plt.text(9.8, 179500, '1G')

plt.plot((4, 4), (8393.9, 146541.56), 'black', zorder = 1)  # Vertical lines
plt.plot((6, 6), (23796.18, 160573.16), 'black', zorder = 1)
plt.plot((8, 8), (23108.28, 163203.16), 'black', zorder = 1)
plt.plot((10, 10), (32499.53, 169650.26), 'black', zorder = 1)

plt.plot((0, 12), (146541.56, 146541.56), 'k--', zorder = 1)  # Ionisation dashed line


f = open('Ni II Singly Ionised.csv', 'rt')  # Data format [Parent term, Energy, x coord, height of level]

try: 
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        if i % 2 ==0:  # Skip every other line
            x = float(row[2]) - (box_width/2)
            y = float(row[1])
            height = float(row[3])
            
            box = ptch.Rectangle((x,y), box_width, height, fc='white', ec='black', zorder=2)
            plt.gca().add_patch(box)
        else:
            continue
finally:
    f.close()

figure = plt.gcf()
figure.set_size_inches(19.2, 12)
    
plt.savefig('Ni II Singly Ionised Term Diagram.png', dpi=1000)

plt.show()

