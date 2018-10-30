import matplotlib.pyplot as mpl
import tempfile as tmp
import dataport as dpt
import numpy as numpy
import os 
from numpy import genfromtxt

tempdir = tmp.gettempdir()

def ShowGraph(filename):
    #data = dpt.importCSV(os.path.abspath(".\\"+filename+".csv"))
    data = genfromtxt(os.path.abspath(".\\"+filename+".csv"), delimiter=';', encoding="utf8")
    mpl.plot(numpy.array(data[0]), numpy.array(data[1]))
    mpl.ylabel("Warmtepomp verbruik (percentage)")
    #mpl.yticks(numpy.arange(len(numpy.array([0,10,20,30,40,50,60,70,80,90,100]))))
    mpl.xlabel("Tijdstip (uren)")
    mpl.xticks(numpy.arange(0, 2500, 100.0), rotation='vertical')
    mpl.show()

ShowGraph("dummydata")