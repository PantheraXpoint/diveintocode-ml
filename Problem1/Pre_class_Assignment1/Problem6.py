
import matplotlib.pyplot as plt
list = []

THICKNESS = 0.00008
folded_thickness = THICKNESS
for i in range(1,44):
    folded_thickness *= 2
    list.append(folded_thickness)


plt.title("thickness of folded paper")
plt.xlabel("number of folds")
plt.ylabel("thickness[m]")
plt.plot(list) # Enter the variable name of the list in "List name"
plt.show()

# The time of the graph as we can see, it is 2 times increment after each folding. However in the
# graph, we see a very dramatic change at the end of a graph, that is because the init of the graph is large.
# So as the fold increases to 43, it reaches the standard unit in the graph which is 1e8. Before that, the scale is 
# small compared to even the based 1 of the 1e8 unit.
