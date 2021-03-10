import numpy as np

list = []

THICKNESS = 0.00008
folded_thickness = THICKNESS
for i in range(1,44):
    folded_thickness *= 2
    list.append(folded_thickness)
    print("Thickness after {} fold: {} meters".format(i,folded_thickness))
