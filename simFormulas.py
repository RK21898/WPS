"""This Module contains the formulas used to calculate certain
values used in the simulation heatpumpSim 
in the process of the program"""

###FUNCTION SECTION###

##misschien overbodig
def WattToJoules(watt):
    """Convert kWh to joules
    Returns the equivalent of x kWh as y joules"""
    return watt * 1000

##misschien overbodig
def PowerRequirementForRoom(length, width, height, InsulationTypeInformation):
    """Calculate the power requirement for a room using
    Length, Width and Height in Meters
    RoomType like dictionary
    Length * Width * Height * WattPerM2
    Returns the PowerRequirementForRoom"""
    return length * width * height * InsulationTypeInformation

def COP(powerOutput, addedPower):
    """Calculate the COP coefficient of the heat pump
    powerOutput / addedPower
    Returns the COP coefficient"""
    return powerOutput / addedPower

##misschien overbodig
def WaterFlow(power, density, specific_heat, deltaT):
    """Calculates the volume flow rate
    Used for both Intake and Output sides in heat pump
    power in watts
    Density in kg/m^3
    Specific_heat in Joule/Kg.K
    DeltaT in Kelvin
    Returns the volume flow rate in m^3/s"""
    return power / (density * specific_heat * deltaT)

def SPF(Qw, Qk, E, G):
    """Seasonal Performance Factor
    Qw = warmth delivered to building by heat pump in MWh
    Qk = cold delivered to building by heat pump in MWh
    E = electricity used by the pump system in MWh
    G = electric equivalent of natural gas used by the pump system
    #Returns Seasonal Performance Factor"""
    return (Qw + Qk) / (E + G)

def SubstanceMass(m, rho):
    """True mass in kg of the substance calculated using the 
    capacity in cubic meters and specific mass of a substance"""
    return m * rho

##misschien betere naam voor functie
def PowerRequiredToHeatSubstance(m, c, DeltaT):
    """Calculate the power needed to heat up a substance, like air
    M = mass of substance
    C = specific heat
    DeltaT = Desired temp - started temp in K
    Returns the amount of power required to heat up substance"""
    return (m * c * DeltaT) / 3600000

def TransititionTime(requirement, power):
    """Calculate the time needed to heat up a substance, like air
    Power = the output of the device used to heat up the substance in kW
    Requirement = the power needed to heat up the substance in kWh
    Returns the time requirement in hours"""
    return requirement / power

def HeatTransfer(transferCoefficient, surface, deltaT):
    """Calculate the power needed to transfer the heat from
    item A to item B so that they become the same temperature"""
    return transferCoefficient * surface * deltaT

def TransferCoefficient(velocity):
    """Calculate the transfer coefficient in watts per square meter
    per kelvin using the airflow in meters per second => 12*sqrt(v)"""
    return 12 * velocity

##misschien overbodig
def CelsiusToKelvin(celsius):
    """Convert temperature in celsius to temperature in kelvin
    Celsius = degrees in Celsius
    Returns the degrees in Kelvin"""
    return celsius + 273



