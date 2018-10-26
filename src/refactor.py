import csv

#create custom dialect to be able to parse the semi-colons
#csv.register_dialect('read_semi','excel', delimiter=';')
#create ordered dictionary 
#input_file = csv.DictReader(open("../input/tester.csv"),dialect='read_semi')

class ReadFile:
    def __init__(self, filename):
        self.filename = str(filename)
        self.file = None
        self.data = None
        self.read_it()

    def read_it(self):
        csv.register_dialect('read_semi','excel', delimiter=';')
        self.file = open("../input/"+ self.filename)
        self.data = csv.DictReader(open("../input/"+ self.filename), dialect='read_semi')
        self.file.close()

class BuildSorted:
    def __init__(self,data,q1, q2):
        self.data = data
        self.q1_dict = {}
        self.q2_dict = {}
        self.q1 = str(q1)
        self.q2 = str(q2)
        self.count = 0
        self.build_Dicts()

    def check_Dict(self, dict, key_val):
        if key_val not in dict:
            dict[str(key_val)]= [1]
        else:
            dict[str(key_val)][0] += 1

    def build_Dicts(self):
        for row in self.data:
            if row['CASE_STATUS'] == 'CERTIFIED':
                self.count += 1
                value_1 = row[self.q1]
                value_2 = row[self.q2]
                self.check_Dict(self.q1_dict,value_1)
                self.check_Dict(self.q2_dict,value_2)
        self.q1_dict = sorted(self.q1_dict.items(), key=lambda t: (-t[1][0], t[0]))
        self.q2_dict = sorted(self.q2_dict.items(), key=lambda t: (-t[1][0],t[0]))

class Top10:
    def __init__(self,sorted_1,sorted_2,count):
        self.top_10_1= sorted_1[:10]
        self.top_10_2= sorted_2[:10]
        self.count = count
        self.calc_percent(self.top_10_1)
        self.calc_percent(self.top_10_2)
    
    def calc_percent(self, top_10):
        for row in top_10:
            num = row[1][0]
            percent = (num*100)/self.count
            row[1].append(percent)

class WriteText:
    def __init__(self, name, titles, info):
        self.name = name
        self.titles = titles
        self.info = info
        self.write()

    def write(self):
        with open("../output/"+self.name, "w+") as f:
            f.writelines(self.titles)
            f.write('\n')
            for row in self.info:
                string = str(row[0])+';'+str(row[1][0])+";"+str(row[1][1])+'%'
                f.write(string+"\n")
            f.close()

class MakeLabels:
    def __init__(self, title, num):
        self.title = title
        self.num = str(num)
        self.labels = [';NUMBER_CERTIFIED_APPLICATIONS;', 'PERCENTAGE']
        self.make_first_label()

    def make_first_label(self):
        index = self.title.find(self.num)
        new_string = (self.title[:index-1]+self.title[len(self.num)+index:]).upper()
        self.labels.insert(0,new_string)

def main(file, title1, title2, category1, category2):
    x = ReadFile(file)
    x = BuildSorted(x.data,category1,category2)
    x = Top10(x.q1_dict,x.q2_dict,x.count)
    y = MakeLabels(title1, 10)
    y_2 = MakeLabels(title2, 10)
    WriteText(title1, y.labels, x.top_10_1)
    WriteText(title2, y_2.labels, x.top_10_2)

main('tester.csv', 'top_10_employers', 'top_10_states', 'EMPLOYER_NAME', 'WORKSITE_STATE')