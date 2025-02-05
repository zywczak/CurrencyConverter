from Currency import Currency

class Parser:
    def __init__(self):
        pass

    def parse(self, fileroot, list_currency): 
        for pozycja in fileroot.findall(".//pozycja"):
            name = pozycja.find("nazwa_waluty").text
            factor = int(float(pozycja.find("przelicznik").text))
            code = pozycja.find("kod_waluty").text
            rate = float(pozycja.find("kurs_sredni").text.replace(',', '.'))
            list_currency.addCurrency(Currency(name, code, factor, rate))
