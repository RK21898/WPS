###IMPORT SECTION###
import VariableTempRequestModule as v
import readerModule as rm
import bufferModule as bm
import rewardModule as rewardM
import Formulas as f
import numpy as np
import plot as p

from datetime import datetime, timedelta
from decimal import Decimal as d

def _CalculateNeeds(action):
    """Calculates the energy need per datapoint in the dataset"""
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
    """calculates the capacity and surface of the room and returns it
    as the action space of the environment"""
    action_space = {}
    
    action_space['surface'] = action['Space'][0] * action['Space'][1]
    action_space['capacity'] = action['Space'][0] * action['Space'][1] * action['Space'][2]

    return action_space

def GetDesiredTemp():
    #currdata = rm.OpenTemperatureModel("CurrentInsideTemp")
    desireddata = rm.OpenTemperatureModel("InsideRequestTemp")

    desiredTemp = []
    #currTemp, desiredTemp = [], []

    #for array in currdata:
    #    currTemp.append(array[1])
    
    for array in desireddata:
        desiredTemp.append(array[1])

    return desiredTemp #[currTemp, desiredTemp]


class Sim(): #receives an action in the form of action = {'start temp' : x, 'desired temp' : y, 'Space' : [l, b, h, d]}
    """
    Description:
        A heatpump is used to heat up a room of size x,y,z
    Source:
        This problem represents the assignment for the heatpump case provided by Hogeschool Zuyd and CGI for the minor AI
    Observation: 
        Type: Box(3)
        Num	Observation                 Min             Max
        0	room temperature            15C°            24C° 
        1	temperature change          -.05C°          .05C°
        2	floor output                -920*10m2j/s    920*10m2j/s
        
    Actions:
        Type: Discrete(2)
        Num	Action
        0	Heat up with x degrees per second
        1	Cool down with x degrees per second
        
        Note: a state exists where it's no longer heating but the temperature
              still increases, at this point it starts deducting points
    Reward:
        Reward is 0.02 for every minute in the dataset it manages to have the correct desired temperature
        and is deducted by a value between 0 and .05 depending on the temperature change when it over- or undershoots
    Starting State:
        room temperature = 16C°
        heating state = heating towards goal
    Episode Termination:
        The temperature boundary is crossed
        Episode length is greater than 1440 ticks 
        (each tick equals a minute and a day lasts 1440 minutes)
        Solved Requirements
        considered solved when it magages to receive the same total reward several times in a row
    """
###VARIABLE SECTION###

###FUNCTION SECTION###
    def __init__(self):#, action):
    #    self.action = action
    #    self.energyNeed = _CalculateNeeds(self.action)
        self.state = None
        self.observation_space = [[15,24],
                                  [-.05,.05]]
    #    self.space_output = f.FloorWarmingPower(self.action_space['surface'])
    #    self.powerlevel = 0
        self.desiredTemp = GetDesiredTemp() #Get from dataset based on time (userinput values)
        self.currTemp = 16 #Get from dataset based on time (imaginary sensor)
        self.change = round(d(.05),2)
        self.heatingState = "TowardsGoal"
        self.tick = 0
    #    self.time = datetime.now()
    #    self.fulfilledNeedsData = {}

    def _step(self, tick):
        if not (np.isnan(self.desiredTemp[tick]) or self.state == "Terminated"):
            self.currTemp += d(self.change)

            #awards 0 points for heating up towards the goal
            if self.currTemp < self.desiredTemp[tick] - 0.025 and self.change > 0 and self.heatingState == "UpTowardsGoal":
                reward = 0
                self.change += d(self.change * d(1.05))

            #awards 0 points for cooling down towards the goal
            elif self.currTemp > self.desiredTemp[tick] + 0.025 and self.change < 0 and self.heatingState == "DownTowardsGoal":
                reward = 0
                self.change += d(self.change * d(1.05))
            
            #awards 0 points for transitioning into the TowardsGoal states
            elif (self.currTemp < self.desiredTemp[tick] - 0.025) or (self.currTemp > self.desiredTemp[tick] + 0.025) and (self.change > -0.001 or self.change < 0.001):
                if  (self.currTemp < self.desiredTemp[tick]):
                    self.heatingState = "UpTowardsGoal"
                elif (self.currTemp > self.desiredTemp[tick]):
                    self.heatingState = "DownTowardsGoal"
                reward = 0
            
            #is no longer heating up towards the goal, has however reached the OnGoal critera,
            #but the temperature change is still higher than expected, therefore entering the NotTowardsGoal state and starting penalization
            elif (self.currTemp > self.desiredTemp[tick] - 0.025 or self.currTemp < self.desiredTemp[tick] + 0.025 ) and (self.change > 0 or self.change < 0):
                self.heatingState = "NotTowardsGoal"
                if self.change < 0:
                    reward = -d(-self.change)
                else:
                    reward = -d(self.change)
                self.change -= d(self.change * d(0.05))

            #is no longer cooling down towards the goal, and penalizes for the negative effect
            elif self.currTemp < self.desiredTemp[tick] - 0.025 and (self.change > 0 or self.change < 0) and self.heatingState == "NotTowardsGoal":
                if self.change < 0:
                    reward = -d(-self.change)
                else:
                    reward = -d(self.change)
                self.change -= d(self.change * d(0.05))

            #is no longer heating up towards the goal, and penalizes for the negative effect
            elif self.currTemp > self.desiredTemp[tick] + 0.025 and (self.change < 0 or self.change > 0) and self.heatingState == "NotTowardsGoal":
                if self.change < 0:
                    reward = -d(-self.change)
                else:
                    reward = -d(self.change)
                self.change -= d(self.change * d(0.05))
            
            #is no longer truly heating up, but staying around the desired temperature, therefore it has reached the OnGoal state
            elif (self.currTemp > self.desiredTemp[tick] - 0.025 or self.currTemp < self.desiredTemp[tick] + 0.025 ) and (self.change < 0.001 or self.change > -0.001):
                self.heatingState = "OnGoal"
                reward = d(.02)           

            #sets the lower and upper bounds that may not be crossed when cooling down or heating up
            lowerBound, upperBound = self.observation_space[0][0], self.observation_space[0][1]

            #terminates when it crosses a boundary and returns necessary information
            if lowerBound > self.currTemp or self.currTemp > upperBound+1:
                self.state = "Terminated"
                return reward, self.state, self.heatingState
            
            #hasn't terminated so continues to feed necessary information
            else:
                self.state = "NoTermination" 
                return reward, self.state, self.heatingState

    #def calculateEnergy(self, stepNum):
    #    stepTime = (self.energyNeed[stepNum] / self.space_output) #outcome in seconds
    #    self.fulfilledNeedsData["Iteration {0}".format(stepNum)] = [stepTime]

    #def _reward(self):
    #    return rewardM.GetRewards()

    #def policyExport(self):
    #    ...

    #def ai(self, bufferValues):
    #    """"The ai function does ai functions"""
    #    #If the step does not pass any extra values onto the AI it has 
    #    if (bufferValues[0] and bufferValues[1] and bufferValues[2] == None):
    #        if (bufferValues[3]):
    #            return 100
    #        return 50

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


#action["Action"] = input("Type the number for the option you choose, 1: Heat water, 2: Heat room: ")
#
#if action["Action"] == '1':
#    action["Desired Temp"] = float(input("Desired temperature inside buffer: "))
#    
#    sim = Sim(action)
#
#    #make loop so it keeps doing step until complete
#    sim._step(action)
#
#elif action["Action"] == '2':
#    l = float(input("Length of room (in meters): "))
#    b = float(input("Width of room (in meters): "))
#    h = float(input("Height of room (in meters): "))
#    d = float(input("Depth of floor (in centimeters): ")) / 100
#
#    #action['StartingTemp'] = startingTemp
#    #action['DesiredTemp'] = desiredTemp
#    action['Space'] = [l,b,h,d] 
#
#    p.DeltaTemperatureGraph("OutsideTemp","InsideRequestTemp","CurrentInsideTemp")
#    p.EnergyNeedGraph("OutsideTemp","InsideRequestTemp",action)
#
#    sim = Sim(action)
#
#    for i in range(0, len(sim.energyNeed)):
#        sim._step(action, i)
#
#    print(sim.fulfilledNeedsData)
#    print(sim.energyNeed)

day = GetDesiredTemp()

sim = Sim()

for i in range (0, len(day)):
    if not np.isnan(day[i]):
        #if i == 40:
        #   input()
        if(sim.state != "Terminated"):
            print("Iteration {0} of {1}".format(i, len(day)))
            reward, state, heatingState = sim._step(i)
            print(reward, state, heatingState)