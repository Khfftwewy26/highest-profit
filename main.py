import csv, json

jsonFilePath = r'data2.json'
csvFilePath = r'profitData.csv'

#Takes the filename in the function and reads/prints the csv
def readData(filename):
    with open(filename) as profitInfo:
        readProfit = csv.DictReader(profitInfo, delimiter = ',')
        rows = len(list(readProfit))
        print(rows)


def readValidData(filename):
    finalValidList = []
    with open(filename) as profitInfo:
        readProfit = csv.reader(profitInfo, delimiter = ',')
        for row in readProfit:
            if row[4].isdigit():
                finalValidList.append(row)
            else:
                try:
                    float(row[4])
                    finalValidList.append(row)
                except ValueError:
                    continue

        validData = len(list(finalValidList))
        print(validData)

        finalValidList.sort(key = lambda x: (float(x[4])), reverse= True)

def createJSON(validFinalData, jsonFilePath):
    data = []

    with open(validFinalData) as csvFile:
        csvRead = csv.DictReader(csvFile)
        for rows in csvRead:
            if rows['Profit (in millions)'].isdigit():
                data.append(rows)
            else:
                try:
                    float(rows['Profit (in millions)'])
                    data.append(rows)
                except ValueError:
                    continue

        data.sort(key = lambda x: float(x['Profit (in millions)']), reverse = True)

    with open(jsonFilePath, 'w',encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

def getJsonValues(jsonFile):
    with open(jsonFile) as dataFile:
        data = json.load(dataFile)
        for i in range(21):
            print(data[i])

# Calls the read function
if __name__ == '__main__':
    readData('profitData.csv')
    readValidData('profitData.csv')
    createJSON('profitData.csv','data2.json')
    getJsonValues('data2.json')

