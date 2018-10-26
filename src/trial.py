import csv
class ReadFile:
    def __init__(self, filename):
        self.filename = str(filename)
        #self.file = None
        self.data = None
        self.read_it()

    def read_it(self):
        csv.register_dialect('read_semi','excel', delimiter=';')
        #self.file = open("../input/"+ self.filename)
        #print(self.file)
        self.data = csv.DictReader(open("../input/"+ self.filename), dialect='read_semi')
        print(self.data)
        #self.file.close()

x = ReadFile('tester.csv')
print(x.data)