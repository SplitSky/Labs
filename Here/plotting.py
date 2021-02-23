import matplotlib.pyplot as plt
import numpy as np


def linearPlotData(title, xAxisTitle, yAxisTitle, x, y, error_y, label):
    figure = plt.figure()
    axes_1 = figure.add_subplot(111)
    axes_1.plot(x, y, "b+", label=label)
    #axes_1.errorbar(x, y, error_y, fmt="b+")
    plt.xlabel(xAxisTitle)  #
    plt.ylabel(yAxisTitle)  # edit from axes
    plt.title(title)
    #y_weights = (1 / error_y) * np.ones(np.size(y))
    #y_errors = error_y * np.ones(np.size(y))

x = np.array([10,8,6,5,4,3,2,20]) # etcone20 cuts (GeV)



N_sel = [53344.93257793784,
         53342.16887140274,
         53311.75044631958,
         53087.201599121094,
         52208.81396484375,
         50083.82696533203,
         44663.3271484375,
         53345.4446053803] # from the cut
#N_total = [19630128.89,19630128.89] # from TotExp
N_total = np.ones(len(x)) * 19630128.89

eff = np.array(N_sel)/N_total # N selected/ N total

linearPlotData("Efficiency vs Energy cut", "Energy cut (MeV)", "Efficiency", x, eff, [], "")
print()
plt.show()

