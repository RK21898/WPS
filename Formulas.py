"""This Module contains the formulas used throughout the
Simulation."""
###IMPORT SECTION###
import math as m

###FUNCTION SECTION###
def EnergyRequired(m, c, dT):
    """Calculate the Energy needed to heat up a substance, like air
    @param m: mass of substance
    @param c: specific heat
    @param dT: Desired temp - start temp in K
    @return: the amount of Energy required to heat up substance"""
    return (m*c*dT)

def EnergyInside(m, c, dT):
    return (m*c*dT)

def CurrentDeltaT(Q,m,c):
    """Calculate the current temperature difference using the warmth formula
    @param Q: heat in joules
    @param m: mass of substance
    @param c: specific heat
    @return: current temp difference"""
    return Q / (m * c)

def SubstanceMass(m, rho):
    """True mass in kg of the substance calculated 
    @param m: capacity in cubic meters
    @param rho: specific mass of a substance
    @return: true mass"""
    return m * rho

def COP(powerOutput, addedPower):
    """Calculate the COP coefficient of the heat pump
    powerOutput / addedPower
    Returns the COP coefficient"""
    return powerOutput / addedPower

def FloorWarmingPower(surface):
    """Calculate the power the floor warming can deliver
    @param surface: the surface of the floor the warming is placed in
    @return: the power in increments of 970 watts per 10 square meters"""
    return m.ceil((surface / 10)) * 970 #in watts