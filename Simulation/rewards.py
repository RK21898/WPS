import numpy as np

#Reward multipliers
rewardMultiplierEnergyOver = 1.5
rewardMultiplierEnergyUnder = 1.5
rewardMultiplierUser = 2
rewardMultiplierTemperatureHot = 1.2
rewardMultiplierTemperatureCold = 1.2

#Debug values
energyUndershoot = 50 #in KWh
energyOvershoot = 0 #in KWh
userSatisfaction = 100
deltaTHot = 2
deltaTCold = 0.2

def GetRewards():
    return CalculateRewardTotal()

def CalculateRewardTotal():
    #Get the individual rewards from their respective reward calculations
    energy = CalculateRewardEnergy(energyOvershoot, energyUndershoot)
    user = CalculateRewardUser(userSatisfaction)
    temperature = CalculateRewardTemperature(deltaTHot, deltaTCold)

    #Total all the reward values and return this to the AI
    return (energy + user + temperature)


#Calculate the Reward that the AI should get for the values of the undershoot and overshoot.
#The under- and overshoot values are given based on KWh.
#To normalize the rewards these values are divided by 100 before any calculations are made.
#The vaue of 100 is a wet finger value. If you read this, please contact Bram and tell him to change it. Seriously.
def CalculateRewardEnergy(energyOvershoot, energyUndershoot):
    #Default energyReward
    energyReward = 1

    #Overshoot calculations
    if (energyOvershoot == 0):
        energyReward += (1 * rewardMultiplierEnergyOver)
    if (energyOvershoot > 0):
        energyReward -= ((energyOvershoot / 100) * rewardMultiplierEnergyOver)

    #Undershoot calculations
    if (energyUndershoot == 0):
        energyReward += (1 * rewardMultiplierEnergyUnder)
    if (energyUndershoot > 0):
        energyReward -= ((energyUndershoot / 100) * rewardMultiplierEnergyUnder)

    #Return the end result
    return energyReward


#Calculate the reward value that should be given to the AI by the user.
#The user can give a value from 0-100 as input. This will be their level of satisfaction.
#The reward multiplier for the user can be set in the configuration.
#If the value is above 50 (satisfied) then the reward the AI gets will be positive.
#If the value is under 50 (dissatisfied) then the reward the AI gets will be negative.
#If the value is exacty 50 (neutral) then the reward the AI gets will be neutral AKA zero.
def CalculateRewardUser(userValue):
    #The default value for the user is -50. This ensures that the default value for the reward is 0.
    #And then positive reward will be +50, and the negative reward will be -50.
    userValue -= 50

    #If the user gives a negative input we need to reward the AI negatively.
    if (userValue < 50):
        return (userValue * rewardMultiplierUser)

    #If the user gives a positive input we need to reward the AI positively.
    elif (userValue > 50):
        return (userValue * rewardMultiplierUser)
    
    #If the user does not give an input it will be received as a neutral input.
    else:
        return 0


#Calculate the reward value that should be given to the AI by the difference in temperature.
#The difference gets calculated in both too hot and too cold. Both of these have seperate multiplier values.
def CalculateRewardTemperature(hotDiff, coldDiff):
    #Default temperatureReward value
    temperatureReward = 1

    #If the difference for both hot and cold is 0 then we need to give the AI a positive reward.
    if (hotDiff == 0 and coldDiff == 0):
        return temperatureReward * (rewardMultiplierTemperatureCold * rewardMultiplierTemperatureHot)
    
    #If the hotDifference is more than 0 we need to give a negative reward to the AI based on the amount of hotDiff
    if (hotDiff > 0):
        temperatureReward -= (hotDiff * rewardMultiplierTemperatureHot)

    #If the coldDifference is more than 0 we need to give a negative reward to the AI based on the amount of coldDiff
    if (coldDiff > 0):
        temperatureReward -= (coldDiff * rewardMultiplierTemperatureCold)

    #Finally return the vaue for the temperature reward
    return temperatureReward