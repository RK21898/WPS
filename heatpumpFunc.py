"""Module that contains the functions that simulate
the actual transitions in temperature desired by the simulator

!NOT FUNCTIONAL!"""

###IMPORT SECTION###
import math as m
import time as t

###VARIABLE SECTION###

###FUNCTION SECTION###
def optimal_realism_transitioning(
    deltaT, time, startingTemps, desiredTemps, speedup):
    increment = deltaT / time

    sFt = startingTemps["Starting Floor Temperature"]
    sRT = startingTemps["Starting Room Temperature"]
    dFT = desiredTemps["Desired Floor Temperature"]
    dRT = desiredTemps["Desired Room Temperature"]

    while sRT < dRT:
        
        sRT += increment * speedup


##tijdsfunctie zodat het lijkt alsof de kamer echt warm wordt > simulatie
##van deltaT delen door benodigde tijd = temperatuur increment
##startTemp + increment totdat desiredTemp is bereikt
