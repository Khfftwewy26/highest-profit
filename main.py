import csv

#Takes the filename in the function and reads/prints the csv
def readData(filename):
    with open(filename) as profitInfo:
        readProfit = csv.reader(profitInfo, delimiter = ',')
        for row in readProfit:
            print(row)


# Calls the read function
if __name__ == '__main__':
    readData('profitData.csv')

