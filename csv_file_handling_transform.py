import csv

def transform_user_details(csv_file):

    new_user_data = []

    try:
        with open("imdbtitles.csv", newline='') as csv_file:
            csvreader = csv.reader(csv_file, delimiter=',')

            next(csvreader)
            for movie in csvreader:
                if movie[0] == "movie" and movie[4].isdigit() and int(movie[4]) >= 2010:
                    new_list = [movie[0], movie[1], movie[4], movie[6], movie[7]]
                    print(new_list)

                    new_user_data.append(new_list)

        return new_user_data

    except FileNotFoundError as errmsg:
        print('File not found')
        print(errmsg)