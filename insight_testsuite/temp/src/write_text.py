class WriteText:
    def __init__(self, name, titles, info):
        #name of file to be outputted
        self.name = name
        #titles of each column
        self.titles = titles
        #the top 10 dictionary
        self.info = info
        self.write()

    def write(self):
        #open/ write to new file
        with open("./output/"+self.name + ".txt", "w+") as f:
            #write titles of columns
            f.writelines(self.titles)
            #new line
            f.write('\n')
            # iterate through top 10, writing each entry
            for row in self.info:
                string = str(row[0])+';'+str(row[1][0])+";"+str(row[1][1])+'%'
                f.write(string+"\n")
            f.close()

class MakeLabels:
    def __init__(self, title, num):
        #name of desired output file
        self.title = title
        #what top __ list are we making?
        self.num = str(num)
        #default labels
        self.labels = [';NUMBER_CERTIFIED_APPLICATIONS;', 'PERCENTAGE']
        self.make_first_label()

    def make_first_label(self):
        #find the index of the number
        index = self.title.find(self.num)
        #create a new string without the number and capitalize it
        new_string = (self.title[:index-1]+self.title[len(self.num)+index:]).upper()
        # add new string to the labels list
        self.labels.insert(0,new_string)