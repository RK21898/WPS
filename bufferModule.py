###IMPORT SECTION

###CLASS SECTION###
class Buffer():
    """This is a Buffer object"""
    
    def __init__(self):
        ###OBJECT VARIABLES
        self.maxContent = float(300) #capacity of buffer in liters
        self.currContent = float(280) #current content of buffer in liters
        self.currTemp = float(40) #current temperature inside the buffer
        self.isEmpty = False #whether the buffer is empty

    #OBJECT FUNCTIONS
    def EmptyCheck(self):
        """Check whether the buffer is empty or not"""
        if(self.currContent > 0):
            return False
        else:
            return True

    def GetValues(self):
        return ([self.maxContent, self.currContent, self.currTemp, self.isEmpty])