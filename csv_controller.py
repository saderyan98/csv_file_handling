'''
IMDB data transformation
The task is to transform the IMDB data using the below criteria:

x only the films from 2010 onwards should be selected
x movies should be the only title type
x only the primary title should be used
x remove the end date and isadult fields entirely
'''
from csv_file_handling_transform import transform_user_details

transform_user_details('imdbtitles.csv')
