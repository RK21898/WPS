"""Create the graphs with the usage patterns and outside temperatures and inside requested temperatures."""

import matplotlib.pyplot as plt
import readerModule as rm
import numpy as np
import Formulas as f

def DeltaTemperatureGraph(f1, f2, f3=0,):
    outerdata = rm.OpenTemperatureModel(f1)
    innerdata = rm.OpenTemperatureModel(f2)
    if f3 == "CurrentInsideTemp":
        currdata = rm.OpenTemperatureModel(f3)

    x_1_axis, x_2_axis, x_3_axis = [], [], []
    y_1_axis, y_2_axis, y_3_axis = [], [], []


    for array in outerdata:
        x_1_axis.append(array[0])
        y_1_axis.append(array[1])

    for array in innerdata:
        x_2_axis.append(array[0])
        y_2_axis.append(array[1])

    if f3 == "CurrentInsideTemp":
        currdata = rm.OpenTemperatureModel(f3)
        for array in currdata:
            x_3_axis.append(array[0])
            y_3_axis.append(array[1])

    fig = plt.figure()
    fig.show()  
    ax = fig.add_subplot(111)

    ax.plot(x_1_axis, y_1_axis, label="OutsideTemp", fillstyle="none")
    ax.plot(x_2_axis, y_2_axis, label="RequestedInsideTemp", fillstyle="none")
    if f3 == "CurrentInsideTemp":
        ax.plot(x_3_axis, y_3_axis, label="CurrentInsideTemp", fillstyle="none", linestyle="dashed")
    elif f3 == 0:
        pass
    else:
        for array in f3:
            x_3_axis.append(array[0])
            y_3_axis.append(array[1])
        ax.plot(x_3_axis, y_3_axis, label="CurrentInsideTemp", fillstyle="none", linestyle="dashed")

    plt.xlabel("Time (hours)")
    plt.gcf().autofmt_xdate()
    plt.ylabel("Temperature (C°)")
    plt.legend(loc=0)
    plt.draw()
    plt.show()

    #OUTSIDE TEMPERATURE CODE EXISTS NOW, ADD INSIDE REQUESTED TEMPERATURES AND MAKE A DELTA GRAPH
    #OPTIONALLY ADD SMOOTHING CODE

def EnergyNeedGraph(f1, f2, action):
    outerdata = rm.OpenTemperatureModel(f1)
    innerdata = rm.OpenTemperatureModel(f2)

    innerTemp, outerTemp, energyNeed, x_axis = [], [], [], []

    for array in innerdata:
        innerTemp.append(array[1])
        x_axis.append(array[0])

    for array in outerdata:
        outerTemp.append(array[1])

    for i in range(0,len(innerTemp)):
        space = action['Space'][0] * action['Space'][1] * action['Space'][2]
        #space2 = action['Space'][0] * action['Space'][1] * action['Space'][3]
        energyNeed.append(f.EnergyRequired(f.SubstanceMass(space, 1.29), 1005, (innerTemp[i] - outerTemp[i])))
                          #+f.EnergyRequired(f.SubstanceMass(space2, 2500), 920, (innerTemp[i] - innerTemp[i-1])))

    fig = plt.figure()
    fig.show()  
    ax = fig.add_subplot(111)

    ax.plot(x_axis, energyNeed, label="EnergyNeed", fillstyle="none")

    plt.xlabel("Time (hours)")
    plt.gcf().autofmt_xdate()
    plt.ylabel("Energy Need (Q in Joules)")
    plt.legend(loc=0)
    plt.draw()
    plt.show()

def policyGraph(policy):
    x_axis = []
    y_1_axis, y_2_axis, y_3_axis = [], [], []

    for array in policy:
        x_axis.append(array[0])
        y_1_axis.append(array[1])
        y_2_axis.append(array[2])
        y_3_axis.append(array[3])
    
    fig = plt.figure()
    fig.show()
    ax = fig.add_subplot(111)

    ax.plot(x_axis, y_1_axis, label="tickReward", fillstyle="none")
    ax.plot(x_axis, y_2_axis, label="tickTemperatureChange", fillstyle="none",linestyle="dashed")
    ax.plot(x_axis, y_3_axis, label="TotalReward", fillstyle="none")

    plt.xlabel("Time (hours)")
    plt.gcf().autofmt_xdate()
    plt.ylabel("Policy Values")
    plt.legend(loc=0)
    plt.draw()
    plt.show()

#USAGE   
#DeltaTemperatureGraph("OutsideTemp","InsideRequestTemp","CurrInsideTemp")
#EnergyNeedGraph("OutsideTemp","InsideRequestTemp")