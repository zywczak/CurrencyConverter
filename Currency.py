class Currency:
    def __init__(self, name, code, factor, rate):
        self.name = name
        self.code = code
        self.factor = factor
        self.rate = rate

    def __eq__(self, other):
        return isinstance(other, Currency) and self.code == other.code
   
    def getFactor(self):
        return self.factor
    
    def getName(self):
        return self.name
    
    def getCode(self):
        return self.code
    
    def getRate(self):
        return self.rate
    
    def setName(self, name):
        self.name = name

    def setCode(self, code):
        self.code = code

    def setFactor(self, factor):
        self.factor = factor
    
    def setRate(self, rate):
        self.rate = rate