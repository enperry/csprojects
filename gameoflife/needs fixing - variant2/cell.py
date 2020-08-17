class Cell:
    def __init__(self):
        self.status = "DEAD"

    def setDead(self): 
        self.status = "DEAD"

    def setLive(self):
        self.status = "LIVE"
    
    def isAlive(self):
        if(self.status == "LIVE"):
            return True
        else: 
            return False
    
    def getPrintCharacter(self):
        if(self.isAlive == True):
            return "O"
        else:
            return " "
