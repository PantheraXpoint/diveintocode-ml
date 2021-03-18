import numpy as np
import matplotlib.pyplot as plt
def calculation(sprinkle_obj_volume,fillup_obj_volume):
    sprinkle_obj = []
    fillup_obj = []
    doubling_times = 0
    sprinkle_obj.append(sprinkle_obj_volume)
    fillup_obj.append(fillup_obj_volume)
    sprinkle = sprinkle_obj_volume
    while (sprinkle < fillup_obj_volume):
        sprinkle *= 2
        doubling_times += 1
        fillup_obj.append(fillup_obj_volume)
        sprinkle_obj.append(sprinkle)
        print(sprinkle_obj)
        print(fillup_obj)
    return fillup_obj,sprinkle_obj,doubling_times
sprinkle_obj_volume = float(input("Enter the volume of the sprinkled object: (in cubic meters)"))
fillup_obj_volume = float(input("Enter the radius of the object you want to fill up: (in cubic meters)"))
fillup_obj,sprinkle_obj,doubling_times = calculation(sprinkle_obj_volume,fillup_obj_volume)
how_long = (doubling_times * 5) / 60
plt.plot(sprinkle_obj, label = "Sprinkled Object's Volume")
plt.plot(fillup_obj, label = "Given Object's Volume")
plt.legend(loc = 'best')
plt.title("How Long Will It Take For A Sprinkled Object's Volume To Reach The Given Object's Volume")
plt.ylabel("Volume(cubic meters)")
plt.xlabel("time(minutes)")
plt.show()
