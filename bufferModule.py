###IMPORT SECTION

###CLASS SECTION###
class Buffer():
    """This is a Buffer object"""
    ###OBJECT VARIABLES
    maxContent = float(300) #capacity of buffer in liters
    currContent = float(280) #current content of buffer in liters
    currTemp = float(40) #current temperature inside the buffer
    isEmpty = False #whether the buffer is empty

    #OBJECT FUNCTIONS
    def EmptyCheck(self):
        """Check whether the buffer is empty or not"""
        if(self.currContent > 0):
            return False
        else:
            return True