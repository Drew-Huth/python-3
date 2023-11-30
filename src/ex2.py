import csv

def find_total_visits():
    weeks = ["files\week-1.csv", "files\week-2.csv", "files\week-3.csv"]
    total = 0

    for week in weeks:
        with open(week) as file:
            row = csv.reader(file)
            next(row, None)
            for person in row:
                total += sum(map(lambda x: int(x), person[1:]))
    
    return total


def ex2():
    total = find_total_visits()
    print(f"Total visits: {total}.")

ex2()