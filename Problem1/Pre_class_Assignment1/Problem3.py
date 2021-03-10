import numpy as np
THICKNESS = 0.00008
folded_thickness = THICKNESS
for i in range(1,44):
    folded_thickness *= 2
   
    
print("Thickness: {} meters".format(folded_thickness))
