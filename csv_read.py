import csv

def open_and_print_csv(file):
    try:
        with open(file,'r') as csv_file: #file.close() automatically
            csvreader = csv.reader(csv_file, delimiter=',')

            iterable_csv = iter(csvreader)
            next(iterable_csv)
            for row in iterable_csv:
                print(row)

    except FileNotFoundError as errmsg:
        print('File not found')
        print(errmsg)

    except FileExistsError as errmsg:
        print('File already exists')
        print(errmsg)