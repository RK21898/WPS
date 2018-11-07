###IMPORT SECTION###
import VariableTempRequestModule as v
import readerModule as rm
import bufferModule as bm
import Formulas as f
import numpy as np
import plot as p

def _CalculateNeeds(action):
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
        self.fulfilledNeedsData = {}

    def _step(self, action, stepNum):
        #figure out the energy we can use in joule/sec
        #if bm.Buffer.isEmpty:
        #    self.energyInput = 10000 #joule/sec
        #elif not bm.Buffer.isEmpty:
        #    self.energyInput = f.EnergyInside(bm.Buffer.currContent, 4187, action['DesiredTemp'] - bm.Buffer.currTemp)
        
        stepTime = (self.energyNeed[stepNum] / self.space_output) #outcome in seconds

        self.fulfilledNeedsData["Iteration {0}".format(stepNum)] = [stepTime] #

    def _reward(self):
       # if "Good":
       #     return 10
       # elif "Mediocre":
       #     return 0
       # elif "Bad":
       #     return -5
       # elif "Very Bad":
       #     return -10 
        pass

    def policyExport(self):
        ...


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

