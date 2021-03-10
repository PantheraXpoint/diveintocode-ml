
import matplotlib.pyplot as plt
list = []

THICKNESS = 0.00008
folded_thickness = THICKNESS
for i in range(1,44):
    folded_thickness *= 2
    list.append(folded_thickness)


plt.tick_params(labelsize=20) # This will increase the letter size of label in the graph.
plt.title("thickness of folded paper")
plt.xlabel("number of folds")
plt.ylabel("thickness[m]")

plt.plot(list, color='red') # This will change the color of the graph

plt.show()
