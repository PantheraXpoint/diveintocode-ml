import time


start = time.time()
time.sleep(0.5)


THICKNESS = 0.00008
folded_thickness = THICKNESS
for i in range(1,44):
    folded_thickness *= 2
   


elapsed_time = (time.time() - start - 0.5)
print("time : {}[s]".format(elapsed_time))
