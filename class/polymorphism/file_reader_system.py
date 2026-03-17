import os
from pathlib import Path
import csv
import json


class FileReader:
    def read(self, file):
       with open(file, "r") as f:
            for line in f:
                print(line.strip())               
        
class PDFReader(FileReader):
    def read(self, file):
        super().read(file)

        
class CSVReader(FileReader):
    def read(self, file):
        with open(file, mode ='r')as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                print(lines)

class JSONReader(FileReader):
    def read(self, file):
        with open(file, "r") as f:
            data = json.load(f)
            for key,values in data.items():
                print(f"{key}: {values}")

filename = input("Enter the file name: ")
file_location = os.path.abspath(filename)
#file_extension = filename.split(".")[1] #issue in case file nale file.txt.csv
file_extension = Path(filename).suffix.lower()


if file_extension == ".pdf":
    reader = PDFReader()
    reader.read(file_location)
elif file_extension == ".csv":
    reader = CSVReader()
    reader.read(file_location)
elif file_extension == ".json":
    reader = JSONReader()
    reader.read(file_location)
elif file_extension == ".txt":
    reader = FileReader()
    reader.read(file_location)
else:
    print("Unsupported file format")
