import csv

#Takes the filename in the function and reads/prints the csv
def readData(filename):
    with open(filename) as profitInfo:
        readProfit = csv.reader(profitInfo, delimiter = ',')
        rows = len(list(readProfit))
        print(rows)

def readValidData(filename):
    finalData = []
    with open(filename) as profitInfo:
        readProfit = csv.reader(profitInfo, delimiter = ',')
        for row in readProfit:
            if row[4].isdigit():
                finalData.append(row[4])
            else:
                try:
                    float(row[4])
                    finalData.append(row[4])
                except ValueError:
                    continue

        validData = len(list(finalData))
        print(validData)






# Calls the read function
if __name__ == '__main__':
    readData('profitData.csv')
    readValidData('profitData.csv')

