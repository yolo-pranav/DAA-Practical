import os
import csv
import random
from time import time
from types import FunctionType
import matplotlib.pyplot as plt
from Empirical_Analysis.Sorting import quick_sort

NAME = 'name'
CSVHEADER = 'csvHeader'
CSVAPPEND = 'csvAppend'
ARGS = 'args'

class Analysis:
    def __init__(self):
        self._testCase = []
        self._target = 0
        self._timeArray = [[], [], []] # Average | Best | Worst
        self._funcTypeDict = {
            0: {
                NAME: lambda: 'Sorting',
                CSVHEADER: lambda: ['Run', 'Input Size', 'TIme of Execution'],
                ARGS: lambda: [self._testCase],
                CSVAPPEND: lambda: [self._timeArray[0]]
            },
            1: {
                NAME: lambda: 'Searching',
                CSVHEADER: lambda: ['Run', 'Input Size', 'TIme of Execution (Average)', 'TIme of Execution (Best)', 'TIme of Execution (Worst)'],
                ARGS: lambda: [self._testCase, self._target],
                CSVAPPEND: lambda: [*self._timeArray]
            },
        }


    def analyse(
        self,
        algorithm: FunctionType,
        dataRange: list = [0, 100],
        lenArray: list = [100, 500, 1000, 2000, 3000, 5000, 8000, 10000],    
        csvSave: bool = False,
        csvPath: str = "results.csv"
    ):
        print(f"Choose the type of function to be analysed:")
        for x in range(self._funcTypeDict.__len__()):
            print(str(x) + ' -> ' + self._funcTypeDict.get(x).get(NAME)())


        variables = self._funcTypeDict.get(int(input()))
       
        if csvSave:
            if os.path.exists(csvPath):
                inp = input("The provided csv file path is already existing. Do you wish to overwrite the existing file? (Y/N): ")
                while(['Y','N'].__contains__(inp) == False):
                    inp = input("Enter a valid input. (Y/N): ")
                if inp == 'N':
                    csvSave = False


        if csvSave:
            while True:
                try:
                    with open(csvPath, 'w', newline='') as csvFile:
                        csv.writer(csvFile).writerow(variables.get(CSVHEADER)())
                    break
                except FileExistsError:
                    print("The file opened in exclusive creation mode ('x') already exists.")
                except InterruptedError:
                    print("System call is interrupted by an incoming signal.")


        if algorithm.__name__ == 'linear_search':
            linear = True
        else:
            linear = False
        for i,n in enumerate(lenArray):
            targets = [
                lambda: self._testCase[n//2] if linear else self._testCase[n - n//4],
                lambda: self._testCase[0] if linear else self._testCase[n//2],
                lambda: dataRange[1] + 1
            ]
           
            cases = ['Average', 'Best', 'Worst']
            self._testCase = create_list(n, dataRange)
           
            for x in range(3):
                self._target = targets[x]()
                print(self._target)
                case_time = algo_average_time(algorithm, variables.get(ARGS)())
                self._timeArray[x].append(case_time)
                print(f"Execution {i+1} with length={n} ({cases[x]})\t: {self._timeArray[x][i]}")
           
            if csvSave:
                csvAppend = [i, n]
                for list in variables.get(CSVAPPEND)():
                    csvAppend.append(list[i])
                csv.writer(open(csvPath, 'a', newline='')).writerow(csvAppend)


        generate_graph(lenArray, variables.get(CSVAPPEND)())


def algo_average_time(algorithm: FunctionType, arguments) -> float:
    exec_time = []
    average_time:float = 0
    for i in range(5):
        intial_time = time()
        algorithm(*arguments)  
        final_time = time()
        exec_time.append(final_time-intial_time)


    for et in exec_time:
        average_time += et


    return average_time/5


def create_list(length: int, dataRange: list[int] = [0, 100]) -> list[int]:
    '''
    Create a list of random whole numbers less than 100 of length n.


    Parameters:
        length (int): The length of the list to be created.
        dataRange (list[int]): Range of data with index 0 as minimum value and index 1 as maximum value.


    Returns:
        list[int]: A list with random generated numbers.
    '''
    numbers = []
    for i in range(length):
        numbers.append(random.randint(dataRange[0], dataRange[1]))
    return numbers


def generate_graph(lenarray: list, timeArray: list[list]):
    '''
    Plot a graph from the given csv .FIle


    Parameter:
    csvFile (str): The system path to the file with input values.
    '''
    # Extract x and y values from the data
    x_values = lenarray
    y_values = timeArray[0]
    try:
        y1_values = timeArray[1]
        y2_values = timeArray[2]
    except IndexError:
        pass        


    # Create a line plot
    plt.plot(x_values, y_values, label='Average Case', color='blue', marker='.')
    try:
        plt.plot(x_values, y1_values, label='Best Case', color='green', marker='.')
        plt.plot(x_values, y2_values, label='Worst Case', color='red', marker='.')
    except NameError:
        pass


    # Add labels and title
    plt.xlabel('Length of Array')
    plt.ylabel('Time of Execution')
    plt.title('Execution TIme v/s Array Length')


    # Add gridlines
    plt.grid()


    # Show the plot
    plt.legend()
    plt.show()