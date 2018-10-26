import csv

#create custom dialect to be able to parse the semi-colons
#csv.register_dialect('read_semi','excel', delimiter=';')
#create ordered dictionary 
#input_file = csv.DictReader(open("../input/tester.csv"),dialect='read_semi')

class ReadFile:
    def __init__(self, filename):
        self.filename = str(filename)
        #self.file = None
        self.data = None
        self.read_it()

    def read_it(self):
        csv.register_dialect('read_semi','excel', delimiter=';')
        #self.file = open("./input/"+ self.filename)
        self.data = csv.DictReader(open("./input/"+self.filename), dialect='read_semi')
        #self.file.close()
