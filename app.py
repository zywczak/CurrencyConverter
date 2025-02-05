from UserInterface import UserInterface
from CurrencyList import CurrencyList
from DownloadData import DownloadData
from Parser import Parser

if __name__ == "__main__":

    data=DownloadData()
    root=data.download("./lasta.xml")
    list=CurrencyList()

    parser=Parser()
    parser.parse(root,list)

    ui = UserInterface()
    print(ui.convert_and_display_result(list))