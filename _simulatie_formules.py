
#Convert kiloWatthour to joules
#Returns the equivalent of x kWh as y joules
def WattToJoules(watt):
    return watt * 1000

#Calculate the power requirement for a room using
#Length, Width and Height in Meters
#RoomType like dictionary
#Length * Width * Height * WattPerM2
#Returns the PowerRequirementForRoom
def PowerRequirementForRoom(length, width, height, InsulationTypeInformation):
    return length * width * height * InsulationTypeInformation

#Calculate the COP coefficient of the heat pump
#powerOutput / addedPower
#Returns the COP coefficient
def COP(powerOutput, addedPower):
    return powerOutput / addedPower

#Calculates the volume flow rate
#Used for both Intake and Output sides in heat pump
#power in watts
#Density in kg/m^3
#Specific_heat in Joule/Kg.K
#DeltaT in Kelvin
#Returns the volume flow rate in m^3/s
def WaterFlow(power, density, specific_heat, deltaT):
    return power / (density * specific_heat * deltaT)

#Seasonal Performance Factor
#Qw = warmth delivered to building by heat pump in MWh
#Qk = cold delivered to building by heat pump in MWh
#E = electricity used by the pump system in MWh
#G = electric equivalent of natural gas used by the pump system
#Returns Seasonal Performance Factor
def SPF(Qw, Qk, E, G):
    return (Qw + Qk) / (E + G)

#Calculate the power needed to heat up a substance, like air
#M = mass of substance
#C = specific heat
#DeltaT = Desired temp - started temp in K
#Returns the amount of power required to heat up substance
def PowerRequirementToHeatUpSubstance(m, c, DeltaT):
    return (m * c * DeltaT) / 3600000

#Calculate the time needed to heat up a substance, like air
#Power = the output of the device used to heat up the substance in kWh
#Requirement = the power needed to heat up the substance in kWh
#Returns the time requirement in seconds
def TimeRequirementToHeatUpSubstance(power, requirement):
    return (requirement / power) * 3600

#Convert temperature in celsius to temperature in kelvin
#Celsius = degrees in Celsius
#Returns the degrees in Kelvin
def CelsiusToKelvin(celsius):
    return celsius + 273

#Insulation Type Information
#Watts per square meter used to warm a room of x m^3 at
#a standard of 22 degrees prior to corrections
#Column 1: Room type
#Column 2: Watt per m²
InsulationTypeInformation = {
    "Excellent": 50,
    "Goed": 60,
    "Normaal": 70,
    "Slecht": 80}

#Horizontal Collector Soil Type Information
#Watts per square meter collected by horizontal collector
#Column 1: Soil type
#Column 2: Watt per m²
HorizontalSoilTypeInformation = {
    "Droge zanderige bodem": 50,
    "Goed": 60,
    "Normaal": 70,
    "Slecht": 80}

#Vertical Collector Soil Type Information
#Watts per square meter collected by vertical collector
#Column 1: Soil type
#Column 2: Watt per m²
VerticalSoilTypeInformation = {
    "Droge zanderige bodem": 50,
    "Goed": 60,
    "Normaal": 70,
    "Slecht": 80}

