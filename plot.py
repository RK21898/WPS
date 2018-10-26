import numpy
import matplotlib.pyplot as mpl
import tempfile as tmp
import dataport as dpt

tempdir = tmp.gettempdir()

def ShowGraph(filename):
    data = dpt.importCSV('..//'+filename+'.csv')
    mpl.plot(data)
    mpl.ylabel('Tijd')
    mpl.xlabel('Data')
    mpl.show()

ShowGraph('WPS')