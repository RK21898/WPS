###IMPORT SECTION
import simFormulas as f
from datadump import SpecificHeat

###CLASS SECTION###
class Buffer():
    """This is a Buffer object"""
    ###OBJECT VARIABLES
    maxContent = float(300) #capacity of buffer in liters
    currContent = float(150) #current content of buffer in liters
    currTemp = float(20) #current temperature inside the buffer
    isEmpty = "" #whether the buffer is empty

    #OBJECT FUNCTIONS
    def EmptyCheck(self):
        """Check whether the buffer is empty or not"""
        if(self.currContent > 0):
            return False
        else:
            return True
    
    def DesiredTempEstimate(self, DesiredTemp, HeatElementInput):
        """Check how long it will take until
        DesiredTemperature in degrees
        HeatElementInput in kW"""
        return f.TransititionTime(f.PowerRequiredToHeatSubstance(self.currContent,SpecificHeat.get("Water"),DesiredTemp-self.currTemp),HeatElementInput)