from Currency import Currency

class CurrencyList:
    def __init__(self):
        self.currencyList = []
        self.currencyList.append(Currency("polski złoty","PLN",1,1))

    def addCurrency(self,currency):
        self.currencyList.append(currency)

    def getCurrency(self, currencyCode):
        for currency in self.currencyList:
            if currency == currencyCode:
                return currency
        return None