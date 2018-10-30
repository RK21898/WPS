"""Module that contains the functions that simulate
the actual transitions in temperature desired by the simulator

!NOT FUNCTIONAL!"""

###IMPORT SECTION###
import math as m
from datetime import datetime as t
import time
import simFormulas as f
from datadump import DesiredTemps, SpecificHeat, SpecificMass

###VARIABLE SECTION###

###FUNCTION SECTION###
def realism_transitioning(currTemp, surface, roomCapacity, floorCapacity, speedup):
    currRoomTemp = currTemp
    currFloorTemp = currTemp
    start = t.now()
    while currRoomTemp <= DesiredTemps["Desired Temp Room"]:
        currFloorDeltaT = f.CurrentDeltaT(f.FloorWarmingPower(surface),f.TrueSubstanceMass(floorCapacity, SpecificMass["Gewapend Beton"]),SpecificHeat["Beton"])
        currFloorTemp += currFloorDeltaT 
        ##caution!!!! line below is flawed
        #currRoomDeltaT = f.CurrentDeltaT(f.HeatTransfer(f.TransferCoefficient(0.25),surface,currFloorDeltaT),f.TrueSubstanceMass(roomCapacity,SpecificMass["Lucht"]),SpecificHeat["Lucht"])
        currRoomDeltaT = f.CurrentDeltaT(f.HeatTransfer(f.TransferCoefficient(0.25),surface,f.CurrentDeltaT(f.WarmthRequired(f.TrueSubstanceMass(floorCapacity, SpecificMass["Gewapend Beton"]),SpecificHeat["Beton"],currFloorDeltaT),SpecificMass["Lucht"],SpecificHeat["Lucht"])),f.TrueSubstanceMass(roomCapacity,SpecificMass["Lucht"]),SpecificHeat["Lucht"])
        #this line below functions only for room temperature
        #currRoomDeltaT = f.CurrentDeltaT((f.WarmthRequired(f.TrueSubstanceMass(floorCapacity, SpecificMass["Gewapend Beton"]),SpecificHeat["Beton"],currFloorDeltaT)),f.TrueSubstanceMass(roomCapacity,SpecificMass["Lucht"]),SpecificHeat["Lucht"])
        currRoomTemp += currRoomDeltaT
        print("Current floor temperature: ",currFloorTemp,
              "\nCurrent room temperature: ",currRoomTemp)
        time.sleep(1 / speedup)
    end = t.now()
    print("Time Elapsed: ",(end-start)*speedup)

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