import matplotlib.pyplot as mpl
import tempfile as tmp
import dataport as dpt
import os 

tempdir = tmp.gettempdir()

def ShowGraph(filename):
    data = dpt.importCSV(os.path.abspath(".\\"+filename+".csv"))
    mpl.plot(data)
    mpl.ylabel("Tijd")
    mpl.xlabel("Data")
    mpl.show()

ShowGraph("dummydata")