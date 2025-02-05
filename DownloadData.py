import xml.etree.ElementTree as ET

class DownloadData:
    def __init__(self):
        pass

    def download(self, path):
        tree = ET.parse(path)
        fileroot = tree.getroot()
        return fileroot