
import matplotlib.pyplot as plt


    list_n_grains = []
    list_total_grains = []
    grain_d = 1
    list_n_grains.append(grain_d)
    list_total_grains.append(grain_d)
    for i in range(1,100):
        grain_d *= 2
        list_n_grains.append(grain_d)
        list_total_grains.append(list_total_grains[i - 1] + (list_n_grains[i])
                                 
    plt.title("the change in the number of rice grains on x day")
    plt.xlabel("number of days")
    plt.ylabel("number of rice")
    plt.plot(list_n_grains)
    plt.plot(list_total_grains)
    plt.show()
    pass
