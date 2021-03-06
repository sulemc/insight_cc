# import from standard library
import csv

class ReadFile:
    def __init__(self, filename):
        # csv file
        self.filename = str(filename)
        # will be ordered dictionary from csv
        self.data = None
         # build ordered dictionary
        self.read_it()

    def read_it(self):
        #check that filename is in proper format
        self.check_csv()
        # create custom dialect to be able to parse the semi-colons
        csv.register_dialect('read_semi','excel', delimiter=';')
        # create ordered dictionary 
        self.data = csv.DictReader(open("./input/"+self.filename), dialect='read_semi')

    def check_csv(self):
        # check that file includes .csv
        index = self.filename.find(".csv")
        #if file doesn't contain it, add it
        if index == -1:
            self.filename = self.filename + ".csv"