###IMPORT SECTION###
import simFormulas as f
import heatpumpFunc as func
from datadump import SpecificHeat, SpecificMass, StartingTemps, DesiredTemps

###VARIABLES SECTION###


###MAIN PROGRAM###
#simulation input values 
if __debug__:
    roomWidth = 4
    roomLength = 4
    roomHeight = 3
    roomCapacity = roomWidth * roomLength * roomHeight
    floorWidth = roomWidth
    floorLength = roomLength
    floorDepth = 0.18
    floorCapacity = floorWidth * floorLength * floorDepth
    print ("De inhoud van de kamer is",roomCapacity,"kubieke meters")
else:
    #find the capacity of the area that needs to be warmed up
    roomWidth = float(input("Breedte van de ruimte in meters: "))
    roomLength = float(input("Lengte van de ruimte in meters: "))
    roomHeight = float(input("Hoogte van de ruimte in meters: "))
    roomCapacity = roomWidth * roomLength * roomHeight
    print ("De inhoud van de kamer is",roomCapacity,"kubieke meters")
    floorWidth = float(input("Breedte van de vloer in meters: "))
    floorLength = float(input("Lengte van de vloer in meters: "))
    floorDepth = float(input("Dikte van de vloer in meters: "))
    floorCapacity = floorWidth * floorLength * floorDepth

print ("De inhoud van de vloer is",floorCapacity,"kubieke meters")



#insulationType = input("Isolatiekwaliteit van de ruimte\n(slecht/standaard/goed/excellent): ")
#roomPowerRequirement = f.PowerRequirementForRoom(roomLength, roomWidth, roomHeight, insulationType)
print("Temperatuur kan niet hoger dan 35 graden in verband met de vloerverwarming.")
if __debug__:
    #deltaT     
    roomStartTemp = 18
    roomDesiredTemp = 21
    floorStartTemp = 18
    floorDesiredTemp = 26

else:
#deltaT
    roomStartTemp = float(input("Voer een begintemperatuur voor de kamer in: "))
    roomDesiredTemp = float(input("Voer een eindtemperatuur voor de kamer in: "))
    floorStartTemp = float(input("Voer een begintemperatuur voor de vloer in: "))
    floorDesiredTemp = float(input("Voer een eindtemperatuur voor de vloer in: "))

roomDeltaT = roomDesiredTemp - roomStartTemp
floorDeltaT = floorDesiredTemp - floorStartTemp
StartingTemps["Starting Temp Floor"] = floorStartTemp
StartingTemps["Starting Temp Room"] = roomStartTemp
DesiredTemps["Desired Temp Floor"] = floorDesiredTemp
DesiredTemps["Desired Temp Room"] = roomDesiredTemp
print("Het temperatuurverschil in de kamer is",roomDeltaT,"graden.",
      "\nHet temperatuurverschil in de vloer is",floorDeltaT,"graden.")

print("Berekenen van de hoeveelheid energie benodigd om de vloer en kamer te verwarmen.")
floorRequirement = f.PowerRequiredToHeatSubstance(
    f.TrueSubstanceMass(floorCapacity,SpecificMass.get("Gewapend Beton")),
    SpecificHeat.get("Beton"), floorDeltaT)
print("De energie benodigd om de vloer te verwarmen is",floorRequirement,"kWh")
roomRequirement = f.PowerRequiredToHeatSubstance(
    f.TrueSubstanceMass(roomCapacity,SpecificMass.get("Lucht")),
    SpecificHeat.get("Lucht"), roomDeltaT)
print("De energie benodigd om de kamer te verwarmen is",roomRequirement,"kWh")

print("Individuele tijd berekenen voor de verwarming van vloer en kamer.")
print(roomRequirement, (f.HeatTransfer(6,roomCapacity/roomHeight,floorDeltaT)/1000),roomCapacity,roomHeight,floorDeltaT)
print(floorRequirement, f.FloorWarmingPower(floorLength*floorWidth))
roomTransition = f.TransititionTime(roomRequirement, (f.HeatTransfer(6,roomCapacity/roomHeight,floorDeltaT)/1000))
floorTransition = f.TransititionTime(floorRequirement, (f.FloorWarmingPower(floorLength*floorWidth)/1000))
print("Benodigde tijd om de kamer op te warmen:",roomTransition,"uur",
      "\nBenodigde tijd om de vloer op te warmen:",floorTransition,"uur")
func.realism_transitioning(StartingTemps["Starting Temp Floor"],(floorWidth*floorLength),roomCapacity,floorCapacity,1024)



