import csv

def find_total_visits():
    all_weeks = ["files\week-1.csv", "files\week-2.csv", "files\week-3.csv"]
    total = 0

    for week in all_weeks:
        with open(week) as file_input:
            row = csv.reader(file_input)
            next(row, None)
            for person in row:
                total += sum(map(lambda x: int(x), person[1:]))
    
    return total


def ex2():
    total = find_total_visits()
    print(f"Total visits: {total}.")

ex2()