# csv - comma separated values
import csv
with open("C:/Users/hazfr/OneDrive/Desktop/Code/PythonLearning/D19REF_Csv_Ex.txt") as c:
    my_csv = csv.reader(c)
    for item in my_csv:
        print(item)
# xlsx - excell files
# xml looks like html