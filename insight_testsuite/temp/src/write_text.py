class WriteText:
    def __init__(self, name, titles, info):
        self.name = name
        self.titles = titles
        self.info = info
        self.write()

    def write(self):
        with open("./output/"+self.name + ".txt", "w+") as f:
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