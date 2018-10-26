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

#specific heat of substance in joules per kilo per kelvin
SpecificHeat = {
    "Lucht":1005,
    "Water":2060
}

#specific mass of substance in kg per cubic meter
SpecificMass = {
    "Lucht":1.29,
    "Gewapend Beton":2500
}

#starting temperatures
StartingTemps = {
    "Starting Temp Floor":0,
    "Starting Temp Room":0
}

#desired temperatures
DesiredTemps = {
    "Desired Temp Floor":35,
    "Desired Temp Room":0
}