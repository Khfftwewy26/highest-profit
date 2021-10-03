import csv, json
"""
Vanessa White 

I would like to thank you for giving me this opportunity.
I chose to write the program in a primitive way so I can talk about
the optimized version in the next part of the interview. No
amount of words can express how much I want to be apart of SADA.
I am really just happy that you gave me a chance. I always wanted 
to start my career in cloud computing and I believe in this. I am 
willing to do whatever it takes to get this position. 

Description
___________
This is a program that allows for information to be
read from a csv, sorted, placed in a json file, and 
printed.


"""


jsonFilePath = r'data2.json'
csvFilePath = r'profitData.csv'

def readData(filename):
    """
        Parameter
        __________
        filename : str
            The data csv file

        Function
        ________
        This method opens and reads data from the csv.
        Then it prints the amount of items in the csv.

        Returns
        _______
        Nothing

    """
    with open(filename) as profitInfo:
        readProfit = csv.DictReader(profitInfo, delimiter = ',')
        rows = len(list(readProfit))
        print(rows)

"_______________________________________________________________________________"

def readValidData(filename):
    """
        Parameter
        __________
        filename : str
            The data csv file

        Function
        ________
        This method opens and reads data from the csv.
        However,this time, the profit data is specifically
        being checked for validity. And, it eliminates all
        other data types if it is not a numerical value. It
        does this by checking if the profit data is a digit
        and if not it will try to see if it can be changed to
        a float. (as this is being converted from a csv file)
        If so, it appends it to the list. If not, it continues
        so it does not break the code. I then print out the
        amount of valid data and sort it by the profit data.

        Returns
        _______
        Nothing

    """

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

"_______________________________________________________________________________"

def createJSON(validFinalData, jsonFilePath):
    """
        Parameter
        __________
        validFinalData: str
            The data csv file

        jsonFilePath: str
            The json file



        Function
        ________
        This function also opens the csv and checks
        if the profit data is valid or not while
        leaving it in a dictionary form. It then
        appends the data to a list and sorts it. I
        then open the json file to write the data
        to that file.

        Returns
        _______
        Nothing

    """
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

"_______________________________________________________________________________"

def getJsonValues(jsonFile):
    """
        Parameter
        __________
        jsonFile : str
            The json file

        Function
        ________
        This method opens and loads the json file.
        It then proceeds to print the first 20 items
        in the file.

        Returns
        _______
        Nothing

    """
    with open(jsonFile) as dataFile:
        data = json.load(dataFile)
        for i in range(20):
            print(data[i])


#All these functions above are all called in the main function below
if __name__ == '__main__':
    readData('profitData.csv')
    readValidData('profitData.csv')
    createJSON('profitData.csv','data2.json')
    getJsonValues('data2.json')

