from Currency import Currency
from CurrencyConverter import CurrencyConverter

class UserInterface:
    def __init__(self,):
        self.converter = CurrencyConverter()

    def convert_and_display_result(self, rateTable):
        amount = float(input("Enter the amount of money: "))
        sourceCurrency = input("Enter the source currency: ").upper()
        targetCurrency = input("Enter the target currency: ").upper()
        
        source = rateTable.getCurrency(Currency("",sourceCurrency,0,0))
        target = rateTable.getCurrency(Currency("",targetCurrency,0,0))

        result = self.converter.convert(amount,source,target)

        if result is not None:
           return round(result,2)
        else:
            print("Wrong data!!!")
