###IMPORT SECTION###

#import modules
import simFormulas as f

#import tables
from tableDump import SpecificHeat, SpecificMass, StartingTemps, DesiredTemps

###VARIABLES SECTION###
specificHeat = SpecificHeat
specificMass = SpecificMass

###MAIN PROGRAM###
print("We gaan de verwarming van een kamer simuleren. . .")

#simulation input values 
#find the capacity of the area that needs to be warmed up
print("Bepalen van de inhoud van te verwarmen ruimte. . .")
roomWidth = float(input("Breedte van de ruimte in meters: "))
roomLength = float(input("Lengte van de ruimte in meters: "))
roomHeight = float(input("Hoogte van de ruimte in meters: "))
roomCapacity = roomWidth * roomLength * roomHeight
print("De inhoud van de kamer is",roomCapacity,"kubieke meters")

print("Bepalen van de inhoud van te verwarmen vloer. . .")
floorWidth = float(input("Breedte van de vloer in meters: "))
floorLength = float(input("Lengte van de vloer in meters: "))
floorDepth = float(input("Diepte van de vloer in meters: "))
floorCapacity = floorWidth * floorLength * floorDepth
print("De inhoud van de vloer is",floorCapacity,"kubieke meter")
#insulationType = input("Isolatiekwaliteit van de ruimte\n(slecht/standaard/goed/excellent): ")
#roomPowerRequirement = f.PowerRequirementForRoom(roomLength, roomWidth, roomHeight, insulationType)

#deltaT (floor startTemp is a fixed 35 degrees due to regulations)
print("Bepalen van temperatuursverschillen. . .",
      "\nTemperatuur kan niet hoger dan 35 graden, in verband met de",
      "vloerverwarming. . .")

startTemp = float(input("Voer een begintemperatuur in: "))
desiredTemp = float(input("Voer een eindtemperatuur in: "))

roomDeltaT = desiredTemp - startTemp
floorDeltaT = 35 - startTemp

StartingTemps["Starting Floor Temperature"] = startTemp
StartingTemps["Starting Room Temperature"] = startTemp
DesiredTemps["Desired Room Temperature"] = desiredTemp
print("Het temperatuurverschil van de kamer is",roomDeltaT,
      "Graden Kelvin/Celsius",
      "\nHet temperatuurverschil van de vloer is",floorDeltaT,"Graden")

print("Berekenen hoeveel vermogen er nodig is voor de verwarming",
      "\nvan een kamer op basis van de hierboven ingevulde gegevens. . .")

floorRequirement = f.PowerRequiredToHeatSubstance(
    f.SubstanceMass(floorCapacity,specificMass.get("Gewapend Beton")),
    specificHeat.get("Water"),
    floorDeltaT
)
print("Het benodigde vermogen om de vloer te verwarmen is:",
      floorRequirement,"kWh")

roomRequirement = f.PowerRequiredToHeatSubstance(
    f.SubstanceMass(roomCapacity,specificMass.get("Lucht")),
    specificHeat.get("Lucht"),
    roomDeltaT
)
print("Het benodigde vermogen om de vloer te verwarmen is:",
      roomRequirement,"kWh")
