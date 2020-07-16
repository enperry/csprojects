from collections import Counter

import csv
import matplotlib.pyplot as plt
import numpy as np

MY_FILE = "/Users/kuro/Documents/GitHub/csprojects/datavisualisation/sample_sfpd_incident_all.csv"

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
    
    plt.plot(dataList)
    plt.xticks(range(len(dayTuple)), dayTuple)
    plt.savefig("Days.png")
    plt.clf()

def visualizeType():
    dataFile = parse(MY_FILE, ",")

    counter = Counter(item["Category"] for item in dataFile)
    labels = tuple(counter.keys())
    xLocations = na.array(range(len(labels))) + 0.5

    width = 0.5

    plt.bar(xLocations, counter.values(), width = width)
    plt.xticks(xLocations + width / 2, labels, rotation = 90)
    plt.subplots_adjust(bottom = 0.4)
    plt.rcParams["figure.figsize"] = 12, 8
    plt.savefig("Type.png")
    plt.clf()

def main():
    visualizeDays()
    visualizeType()

main()