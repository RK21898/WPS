import matplotlib as mpl
import tempfile as tmp
import dataport as dpt
import numpy as np
import os 
from matplotlib import pyplot
from numpy import genfromtxt

tempdir = tmp.gettempdir()

def ShowGraph(filename):
    #data = dpt.importCSV(os.path.abspath(".\\"+filename+".csv"))
    data = genfromtxt(os.path.abspath(".\\"+filename+".csv"), delimiter=';', encoding="utf-8")
    
    mpl.pyplot.plot(np.array(data[2]), np.array(data[0]))
    mpl.pyplot.ylabel("Warmtepomp verbruik (percentage)")
    #mpl.yticks(numpy.arange(len(numpy.array([0,10,20,30,40,50,60,70,80,90,100]))))
    mpl.pyplot.xlabel("Tijdstip (uren)")
    mpl.pyplot.xticks(np.arange(0, 25, 1.0), rotation='vertical')
    mpl.pyplot.show()

def DeltaTemperatureGraph(f):
    data = genfromtxt(os.path.abspath(".\\"+f+".csv"), delimiter=';', encoding="utf-8")
    mpl.pyplot.plot(np.array(data[:1,:]), np.array(data[1:,:]))
    mpl.pyplot.xlabel("Time (hours)")
    mpl.pyplot.gcf().autofmt_xdate()
    mpl.pyplot.ylabel("Temperature (C°)")
    mpl.pyplot.xticks(np.arange(0,25,1))
    mpl.pyplot.show()

DeltaTemperatureGraph("OutsideTemp")