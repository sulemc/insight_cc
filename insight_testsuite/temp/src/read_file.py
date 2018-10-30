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
        # create custom dialect to be able to parse the semi-colons
        csv.register_dialect('read_semi','excel', delimiter=';')
        # create ordered dictionary 
        self.data = csv.DictReader(open("./input/"+self.filename), dialect='read_semi')

