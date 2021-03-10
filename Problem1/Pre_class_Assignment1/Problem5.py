import numpy as np

list = []

THICKNESS = 0.00008
folded_thickness = THICKNESS
list.append(folded_thickness)
for i in range(1,44):
    folded_thickness *= 2
    list.append(folded_thickness)
    print("Thickness after {} fold: {} meters".format(i,folded_thickness))

print("There are total {} times of folding operation.".format(len(list)))