import csv

def readData(filename):
    with open(filename) as profitInfo:
        readProfit = csv.reader(profitInfo, delimiter = ',')
        for row in readProfit:
            print(row)


if __name__ == '__main__':
    readData('profitData.csv')

