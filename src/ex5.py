from pprint import pprint
import csv
import re

def Convert (tuples, dicts):
    dicts = dict(tuples)
    return dicts

def build_car_list():
    
    miles = []
    makes = []
    ids = []
    both = []
    
    with open("files/input.txt") as file_input:
        file_reader = csv.reader(file_input)
        next(file_reader, None)
        for row in file_reader:
            num = row[1]
            if '.' in num:
                continue
            num = int(num)
            miles.append(num)
        
    with open("files/car-ids.txt") as file_input:
        file_reader = csv.reader(file_input)
        for row in file_reader:
            if row[0] == '4':
                continue
            car_ids = int(row[0])
            ids.append(car_ids)
        
    with open("files/car-ids.txt") as file_input:
        file_reader = csv.reader(file_input)
        for row in file_reader:
            if row[0] == '4':
                continue
            word = row[1].strip()
            makes.append(word)

    count = 0
    while count != len(ids):
        car = {'id': ids[count],
               'miles': miles[count],
               'model': makes[count]}
        both.append(car)
        count += 1

        
    return both

    

                
def ex5():
    car_list = build_car_list()
    pprint(car_list)

ex5()
