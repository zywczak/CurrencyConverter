class CurrencyConverter:
    _instance = None  

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CurrencyConverter, cls).__new__(cls)
            
        return cls._instance

    def convert(self, amount, source, target):    
        if source is not None and target is not None and amount>=0:
            sourceFactor = source.getFactor()
            targetFactor = target.getFactor()  
            return amount * (targetFactor/sourceFactor) * (source.getRate()/target.getRate())
        else:
            return None