import matplotlib.pyplot as plt
import readerModule as rm
import numpy as np
import Formulas as f

def DeltaTemperatureGraph(f1, f2):
    outerdata = rm.OpenTemperatureModel(f1)
    innerdata = rm.OpenTemperatureModel(f2)

    x_1_axis, x_2_axis = [], []
    y_1_axis, y_2_axis = [], []

    for array in outerdata:
        x_1_axis.append(array[0])
        y_1_axis.append(array[1])

    for array in innerdata:
        x_2_axis.append(array[0])
        y_2_axis.append(array[1])

    fig = plt.figure()
    fig.show()  
    ax = fig.add_subplot(111)

    ax.plot(x_1_axis, y_1_axis, label="OutsideTemp", fillstyle="none")
    ax.plot(x_2_axis, y_2_axis, label="InsideTemp", fillstyle="none")

    plt.xlabel("Time (hours)")
    plt.gcf().autofmt_xdate()
    plt.ylabel("Temperature (C°)")
    plt.legend(loc=0)
    plt.draw()
    plt.show()

    #OUTSIDE TEMPERATURE CODE EXISTS NOW, ADD INSIDE REQUESTED TEMPERATURES AND MAKE A DELTA GRAPH
    #OPTIONALLY ADD SMOOTHING CODE

def EnergyNeedGraph(f1, f2):
    outerdata = rm.OpenTemperatureModel(f1)
    innerdata = rm.OpenTemperatureModel(f2)

    innerTemps, outerTemps, energyNeeds, x_axis = [], [], [], []

    for array in innerdata:
        innerTemps.append(array[1])
        x_axis.append(array[0])

    for array in outerdata:
        outerTemps.append(array[1])

    for i in range(0,len(innerTemps)):
        energyNeeds.append(f.EnergyRequired(f.SubstanceMass(6*6*2.5, 1.29), 1005, (innerTemps[i] - outerTemps[i])))

    fig = plt.figure()
    fig.show()  
    ax = fig.add_subplot(111)

    ax.plot(x_axis, energyNeeds, label="OutsideTemp", fillstyle="none")

    plt.xlabel("Time (hours)")
    plt.gcf().autofmt_xdate()
    plt.ylabel("Energy Need (Q in Joules)")
    plt.legend(loc=0)
    plt.draw()
    plt.show()
    
DeltaTemperatureGraph("OutsideTemp","InsideRequestTemp")
EnergyNeedGraph("OutsideTemp","InsideRequestTemp")