###IMPORT SECTION###
import VariableTempRequestModule as v
import readerModule as rm
import bufferModule as bm
import rewardModule as rewardM
import Formulas as f
import numpy as np
import plot as p
from datetime import datetime, timedelta

def _CalculateNeeds(action):
    """"CalculateNeeds calculates the needs"""
    innerData = rm.OpenTemperatureModel("InsideRequestTemp")
    outerData = rm.OpenTemperatureModel("OutsideTemp")

    innerTemp, outerTemp, energyNeed = [], [], []

    for array in innerData:
        innerTemp.append(array[1])

    for array in outerData:
        outerTemp.append(array[1])

    for i in range(0, len(innerTemp)):
        space = action['Space'][0] * action['Space'][1] * action['Space'][2]
        #space2 = action['Space'][0] * action['Space'][1] * action['Space'][3]
        #print((innerTemp[i] - innerTemp[i-1]))
        energyNeed.append(f.EnergyRequired(f.SubstanceMass(space, 1.29), 1005, (innerTemp[i] - outerTemp[i])))
                            #+f.EnergyRequired(f.SubstanceMass(space2, 2500), 920, (innerTemp[i] - innerTemp[i-1])))
    
    return energyNeed

def _CalculateSpace(action):
    """CalculateSpace calculates space"""
    action_space = {}
    
    action_space['surface'] = action['Space'][0] * action['Space'][1]
    action_space['capacity'] = action['Space'][0] * action['Space'][1] * action['Space'][2]

    return action_space

class Sim(): #receives an action in the form of action = {'start temp' : x, 'desired temp' : y, 'Space' : [l, b, h, d]}
###VARIABLE SECTION###

###FUNCTION SECTION###
    def __init__(self, action):
        self.action = action
        self.energyNeed = _CalculateNeeds(self.action)
        self.action_space = _CalculateSpace(self.action)
        self.space_output = f.FloorWarmingPower(self.action_space['surface'])
        self.powerlevel = 0
        self.desiredTemp = 20 #Get from dataset based on time (userinput values)
        self.currentTemp = 20 #Get from dataset based on time (imaginary sensor)
        self.time = datetime.now()
        self.fulfilledNeedsData = {}

    def _step(self, action, stepNum=0):
        """The _step does a _step"""
        #If we're debugging we want to simulate a custom time scale
        if (__debug__):
            #Add a minute to the current time so the step has progressed.
            self.time += timedelta(0,60)

        #Get the desired and current temperature
        #For debug reasons just now 2 static values. Desired temperature should be retrieved from the dataset.
        #The current temperature should be retrieved through a temperature sensor.
        self.desiredTemp = 21
        self.currentTemp = 20

        #Get the current values of the Buffer
        bufferValues = bm.Buffer.GetValues(buff)

        #Check if the action is heat water inside the buffervat
        if (action["Action"] == "1"): #Heat buffervat             
            #If the buffer IS EMPTY
            if (bufferValues[3]):
                #Make the AI choose a valid power level for the heatpump
                self.powerlevel = self.ai(bufferValues)
            #If the buffer IS NOT EMPTY
            elif (not bufferValues[3]):
                #Make the AI choose a valid power level for the heatpump
                self.powerlevel = self.ai(bufferValues)
            #Check if the goal has been reached
            elif (bufferValues[1] == bufferValues[0] and bufferValues[2] == action["Desired Temp"]):
                ...

        elif (action["Action"] == "2"): #Heat room            
            #If the current temp is under the desired temp
            if (self.desiredTemp < self.currentTemp):
                #Make the AI choose a valid power level for the heatpump OR buffervat
                self.ai(bufferValues)
            #If the current temp is above the desired temp
            elif (self.desiredTemp > self.currentTemp):
                #Make the AI choose a valid power level for the heatpump OR buffetvat
                self.ai(bufferValues)
            #If the buffer is empty
            if (bufferValues[3]):
                #Make the AI fill the buffervat
                self.ai(bufferValues)

        reward = self._reward()
        electricityUsage = 50

        #This print summarises the values that are within the current step.
        print("Time: ", self.time, "\nStep: ", stepNum, "\nPowerlevel: ", self.powerlevel, "\nStepReward: ", reward, "\nCurrent temperature: ", self.currentTemp, "\Desired temperature: ", self.desiredTemp, "\nEnergy usage: ", electricityUsage, "\nBuffetvat temp: ", bufferValues[2], "\nBuffervat inhoud: ", bufferValues[1], "\nAction: ", action)

        #figure out the energy we can use in joule/sec
        #if bm.Buffer.isEmpty:
        #    self.energyInput = 10000 #joule/sec
        #elif not bm.Buffer.isEmpty:
        #    self.energyInput = f.EnergyInside(bm.Buffer.currContent, 4187, action['DesiredTemp'] - bm.Buffer.currTemp)
        
    def calculateEnergy(self, stepNum):
        stepTime = (self.energyNeed[stepNum] / self.space_output) #outcome in seconds
        self.fulfilledNeedsData["Iteration {0}".format(stepNum)] = [stepTime] #


    def _reward(self):
        return rewardM.GetRewards()

    def policyExport(self):
        ...

    def ai(self, bufferValues):
        """"The ai function does ai functions"""
        #If the step does not pass any extra values onto the AI it has 
        if (bufferValues[0] and bufferValues[1] and bufferValues[2] == None):
            if (bufferValues[3]):
                return 100
            return 50


###MAIN SECTION###

action = {}

#startingTemp = float(input("Starting Temperature of room: "))
#desiredTemp = float(input("Desired Temperature of room: "))
startHours = [0, 6, 9, 12, 15, 18, 21]
endHours = [6, 9, 12, 15, 18, 21, 23]
wantedTemps = [-3, -2, 0, 1, -1, -2, -3]
v.createCSV(startHours,endHours,wantedTemps,'OutsideTemp')

startHours = [0, 6, 8, 16, 18, 22]
endHours = [6, 8, 16, 18, 22, 23]
wantedTemps = [18, 20, 18, 20, 21, 18]
v.createCSV(startHours,endHours,wantedTemps,'InsideRequestTemp')

buff = bm.Buffer()

action["Action"] = input("Type the number for the option you choose, 1: Heat water, 2: Heat room: ")

if action["Action"] == '1':
    action["Desired Temp"] = float(input("Desired temperature inside buffer: "))
    
    sim = Sim(action)

    #make loop so it keeps doing step until complete
    sim._step(action)

elif action["Action"] == '2':
    l = float(input("Length of room (in meters): "))
    b = float(input("Width of room (in meters): "))
    h = float(input("Height of room (in meters): "))
    d = float(input("Depth of floor (in centimeters): ")) / 100

    #action['StartingTemp'] = startingTemp
    #action['DesiredTemp'] = desiredTemp
    action['Space'] = [l,b,h,d] 

    p.DeltaTemperatureGraph("OutsideTemp","InsideRequestTemp")
    p.EnergyNeedGraph("OutsideTemp","InsideRequestTemp",action)

    sim = Sim(action)

    for i in range(0, len(sim.energyNeed)):
        sim._step(action, i)

    print(sim.fulfilledNeedsData)
    print(sim.energyNeed)