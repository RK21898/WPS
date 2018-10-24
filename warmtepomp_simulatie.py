#import section
import time as t
import math as m
import _simulatie_formules as f

#simulation input values 
roomWidth = int(input("Breedte van de ruimte in meters: "))
roomLength = int(input("Lengte van de ruimte in meters: "))
roomHeight = int(input("Hoogte van de ruimte in meters: "))
insulationType = input("Isolatiekwaliteit van de ruimte\n(slecht/standaard/goed/excellent): ")
roomPowerRequirement = f.PowerRequirementForRoom(roomLength, roomWidth, roomHeight, insulationType)

#deltaT 
startTemp = int(input("Voer een begintemperatuur in: "))
desiredTemp = int(input("Voer een eindtemperatuur in: "))
deltaT = desiredTemp - startTemp

