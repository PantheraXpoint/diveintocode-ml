import time


#start = time.time()
#time.sleep(0.5)


#THICKNESS = 0.00008
#A =  2**4444444
#folded_thickness = 2**43 * THICKNESS
   


#elapsed_time = (time.time() - start - 0.5)
#print("time for 1st method: {}[s]".format(elapsed_time))



start = time.time()
time.sleep(0.5)


THICKNESS = 0.00008
folded_thickness = THICKNESS
for i in range(1,4444444):
    folded_thickness *= 2
   


elapsed_time = (time.time() - start - 0.5)
print("time for 2nd method: {}[s]".format(elapsed_time))


## As I tested, the 1st method is nearly 10 times faster than the 2nd method if the data size increases to millions of numbers.
# With the 1st method, I always record its execution time under 0.1 seconds (always around 0.04s). However, with 2nd method, I record with 
# a range from 0.3s to 0.5s.
# The reason I use sleep is because it make the time delay and so the calculation of execution time of the code results in higher accuracy.
# I still don't know why.