from collections import Counter

import csv
import matplotlib.pyplot as plt
import numpy as np

MY_FILE = "/Users/kuro/Desktop/school/cs projects/datavisualisation/sample_sfpd_incident_all.csv"

def parse(rawFile, delimiter):
    openedFile = open(rawFile)
    csvData = csv.reader(openedFile, delimiter = delimiter)
    parsedData = []
    fields = next(csvData)

    for row in csvData:
        parsedData.append(dict(zip(fields, row)))

    openedFile.close()

    return parsedData

def visualizeDays():
    dataFile = parse(MY_FILE, ",")
    counter = Counter(item["DayOfWeek"] for item in dataFile)

    dataList = [
        counter["Monday"],
        counter["Tuesday"],
        counter["Wednesday"],
        counter["Thursday"],
        counter["Friday"],
        counter["Saturday"],
        counter["Sunday"]
    ]
    dayTuple = tuple(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
    