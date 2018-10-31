"""Module that contains the functions that simulate
the actual transitions in temperature desired by the simulator

!NOT FUNCTIONAL!"""

###IMPORT SECTION###
import math as m
import time
import simFormulas as f
import csv as c

from datetime import datetime as t
from datetime import timedelta
from datadump import DesiredTemps, SpecificHeat, SpecificMass

###VARIABLE SECTION###

###FUNCTION SECTION###
def realism_transitioning(currTemp, surface, roomCapacity, floorCapacity, speedup):
    with open("..\\WPS\\simData",t.now(),".csv", "w") as file:
        wrt = c.writer(file, dialect="excel", delimiter=";")
        
        ticker = 0
        timestart = t(2018, 10, 1, 0, 0, 0, 0)

        currRoomTemp = currTemp
        currFloorTemp = currTemp
        
        while currRoomTemp <= DesiredTemps["Desired Temp Room"]:
            
            currFloorDeltaT = f.CurrentDeltaT(f.FloorWarmingPower(surface),f.TrueSubstanceMass(floorCapacity, SpecificMass["Gewapend Beton"]),SpecificHeat["Beton"])
            currFloorTemp += currFloorDeltaT 
            
            currRoomDeltaT = f.CurrentDeltaT(f.HeatTransfer(f.TransferCoefficient(0.25),surface,f.CurrentDeltaT(f.WarmthRequired(f.TrueSubstanceMass(floorCapacity, SpecificMass["Gewapend Beton"]),SpecificHeat["Beton"],currFloorDeltaT),SpecificMass["Lucht"],SpecificHeat["Lucht"])),f.TrueSubstanceMass(roomCapacity,SpecificMass["Lucht"]),SpecificHeat["Lucht"])
            if currFloorTemp > currRoomTemp:
                currRoomTemp += currRoomDeltaT
            
            time.sleep(1 / speedup)

            if(ticker % 60 == 0):
                timestart += timedelta(seconds=60)
                row = [currFloorTemp,currRoomTemp,timestart]
                wrt.writerow(row)

            ticker+=1
            

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