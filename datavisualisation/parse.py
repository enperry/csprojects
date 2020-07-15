import csv

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

def main():
    newData = parse(MY_FILE, ",")

    print(newData)

main()