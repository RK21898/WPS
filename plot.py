import matplotlib as mpl
import tempfile as tmp
import dataport as dpt
import numpy as numpy
import os 
from numpy import genfromtxt

tempdir = tmp.gettempdir()

def ShowGraph(filename):
    #data = dpt.importCSV(os.path.abspath(".\\"+filename+".csv"))
    data = genfromtxt(os.path.abspath(".\\"+filename+".csv"), delimiter=';', encoding="utf-8")
    
    mpl.pyplot.plot(numpy.array(data[2]), numpy.array(data[0]))
    mpl.pyplot.ylabel("Warmtepomp verbruik (percentage)")
    #mpl.yticks(numpy.arange(len(numpy.array([0,10,20,30,40,50,60,70,80,90,100]))))
    mpl.pyplot.xlabel("Tijdstip (uren)")
    mpl.pyplot.xticks(numpy.arange(0, 25, 1.0), rotation='vertical')
    mpl.pyplot.show()

ShowGraph("simData")