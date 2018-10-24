###IMPORT SECTION###
import time as t
import math as m
import simulatieformules as f

###VARIABLES SECTION###
#Insulation Type Information
#Watts per square meter used to warm a room of x m^3 at
#a standard of 22 degrees prior to corrections
#Column 1: Insulation type
#Column 2: Watt per m²
InsulationTypeInformation = {
    "Excellent": 50,
    "Goed": 60,
    "Normaal": 70,
    "Slecht": 80} #!!Compleet

#Horizontal Collector Soil Type Information
#Watts per square meter collected by horizontal collector
#Column 1: Soil type
#Column 2: Watt per m²
HorizontalSoilTypeInformation = {
    "Droge zanderige bodem": 50,
    "Goed": 60,
    "Normaal": 70,
    "Slecht": 80} #!!Nog niet compleet, twijfel of overbodig.

#Vertical Collector Soil Type Information
#Watts per square meter collected by vertical collector
#Column 1: Soil type
#Column 2: Watt per m²
VerticalSoilTypeInformation = {
    "Droge zanderige bodem": 50,
    "Goed": 60,
    "Normaal": 70,
    "Slecht": 80} #!!Nog niet compleet, twijfel of overbodig.

###MAIN PROGRAM###
#simulation input values 

#find the capacity of the area that needs to be warmed up
roomWidth = int(input("Breedte van de ruimte in meters: "))
roomLength = int(input("Lengte van de ruimte in meters: "))
roomHeight = int(input("Hoogte van de ruimte in meters: "))
roomCapacity = roomWidth * roomLength * roomHeight
print ("De inhoud van de kamer is",roomCapacity,"kubieke meters")
#insulationType = input("Isolatiekwaliteit van de ruimte\n(slecht/standaard/goed/excellent): ")
#roomPowerRequirement = f.PowerRequirementForRoom(roomLength, roomWidth, roomHeight, insulationType)

#deltaT 
startTemp = int(input("Voer een begintemperatuur in: "))
desiredTemp = int(input("Voer een eindtemperatuur in: "))
deltaT = desiredTemp - startTemp

##tijdsfunctie zodat het lijkt alsof de kamer echt warm wordt > simulatie
##van deltaT delen door benodigde tijd = temperatuur increment
##startTemp + increment totdat desiredTemp is bereikt
