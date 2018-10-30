"""Module that contains the functions that simulate
the actual transitions in temperature desired by the simulator

!NOT FUNCTIONAL!"""

###IMPORT SECTION###
import math as m
import time as t

###VARIABLE SECTION###

###FUNCTION SECTION###
def realism_transitioning(deltaT, time, speedup):
    return None

###basic bitch oplossing
##tijdsfunctie zodat het lijkt alsof de kamer echt warm wordt > simulatie
##van deltaT delen door benodigde tijd = temperatuur increment
##startTemp + increment totdat desiredTemp is bereikt
###advanced coolguy oplossing
##deltaT verkleinen en de berekeningen iedere keer opnieuw uitvoeren,
##zodat het verwarmen van de vloer invloed heeft op het verwarmen
##van de kamer vanaf het begin van de simulatie.
###ultieme baas oplossing
##pak de advanced coolguy oplossing en laat hierop alle
##verliezen en winsten uit de omgeving op los voor ultrarealism simulatie
###EINDE ENZO