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
plt.axis([0, 18, -10000, 400000])
plt.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')

plt.text(1.8, 305000, '4F')  # Parent term labels
plt.text(3.8, 325000, '4P')
plt.text(5.8, 326000, '2G')
plt.text(7.8, 332000, '2P')
plt.text(9.8, 335000, '2H')
plt.text(11.7, 335000, '2D2')
plt.text(13.8, 350000, '2F')
plt.text(15.8, 375000, '2D1')

plt.plot((2, 2), (51045.46, 283800), 'black', zorder = 1)  # Vertical lines
plt.plot((4, 4), (67880.16, 301918.6), 'black', zorder = 1)
plt.plot((6, 6), (70358.94, 303629.6), 'black', zorder = 1)
plt.plot((8, 8), (73893.73, 307448.9), 'black', zorder = 1)
plt.plot((10, 10), (76727.36, 310449.1), 'black', zorder = 1)
plt.plot((12, 12), (77332.47, 310896.5), 'black', zorder = 1)
plt.plot((14, 14), (92373.45, 327237.5), 'black', zorder = 1)
plt.plot((16, 16), (115870.28, 351160), 'black', zorder = 1)

plt.plot((0, 18), (283800, 283800), 'k--', zorder = 1)  # Ionisation dashed line


f = open('Ni II Doubly Ionised.csv', 'rt')  # Data format [Parent term, Energy, x coord, height of level]

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
    
plt.savefig('Ni II Doubly Ionised Term Diagram.png', dpi=1000)
    
plt.show()

