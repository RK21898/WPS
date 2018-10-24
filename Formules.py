
#Watt To Joules function
def WattToJoules(watt):
    return watt * 1000

def PowerRequirementForRoom(length, width, height, watt):
    return length * width * height * watt

def COP(powerOutput, addedPower):
    return powerOutput / addedPower

def WaterFlow(power, density, specific_heat, deltaT):
    return power / (density * specific_heat * deltaT)

def SPF(Qw, Qk, E, G):
    return (Qw + Qk) / (E + G)

def PowerRequirementToHeatUpSubstance(m, c, DeltaT):
    return (m * c * DeltaT) / 3600000

def TimeRequirementToHeatUpSubstance(power, requirement):
    return (requirement / power) * 3600
