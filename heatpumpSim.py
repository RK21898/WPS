###IMPORT SECTION###
import simFormulas as f
from datadump import SpecificHeat, SpecificMass, StartingTemps, DesiredTemps

###VARIABLES SECTION###


###MAIN PROGRAM###
#simulation input values 

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

#deltaT 
print("Temperatuur kan niet hoger dan 35 graden in verband met de vloerverwarming.")
startTemp = float(input("Voer een begintemperatuur in: "))
roomDesiredTemp = float(input("Voer een eindtemperatuur in: "))
roomDeltaT = roomDesiredTemp - startTemp
floorDesiredTemp = DesiredTemps.get("Desired Temp Floor")
floorDeltaT = floorDesiredTemp - startTemp
print("Het temperatuurverschil in de kamer is",roomDeltaT,"graden.")
print("Het temperatuurverschil in de vloer is",floorDeltaT,"graden.")

print("Berekenen van de hoeveelheid energie benodigd om de vloer en kamer te verwarmen.")
floorRequirement = f.PowerRequiredToHeatSubstance(
    f.TrueSubstanceMass(floorCapacity,SpecificMass.get("Gewapend Beton")),
    SpecificHeat.get("Beton"), floorDeltaT
)
print("De energie benodigd om de vloer te verwarmen is",floorRequirement)
roomRequirement = f.PowerRequiredToHeatSubstance(
    f.TrueSubstanceMass(roomCapacity,SpecificMass.get("Lucht")),
    SpecificHeat.get("Lucht"), roomDeltaT
)
print("De energie benodigd om de kamer te verwarmen is",roomRequirement)

##tijdsfunctie zodat het lijkt alsof de kamer echt warm wordt > simulatie
##van deltaT delen door benodigde tijd = temperatuur increment
##startTemp + increment totdat desiredTemp is bereikt
