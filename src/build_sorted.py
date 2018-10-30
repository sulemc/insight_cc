class BuildSorted:
    def __init__(self,data,q1, q2,status_label):
        # ordered dictionary from csv
        self.data = data
        # dictionaries for query 1 and 2
        self.q1_dict = {}
        self.q2_dict = {}
        # column labels that are being evaluated
        self.q1 = str(q1)
        self.q2 = str(q2)
        # csv specific column status label
        self.status_label = str(status_label)
        # count of how many entries are certified
        self.count = 0
        self.build_Dicts()

    #helper function to check the query dictionary 
    def check_Dict(self, dict, key_val):
        # does key_val exist in the query dictionary?
        if key_val not in dict:
            # if no - add the key_val as a key and the value as a list with 1 at index 0
            dict[str(key_val)]= [1]
        else:
            # if yes - increment the value at index 0
            dict[str(key_val)][0] += 1

    def build_Dicts(self):
        # iterate through each row of the dictionary
        for row in self.data:
            # check if the entry is certified
            if row[self.status_label] == 'CERTIFIED':
                # increment certified count
                self.count += 1
                # set the value for the 2 column queries
                value_1 = row[self.q1]
                value_2 = row[self.q2]
                # call helper function using those values
                self.check_Dict(self.q1_dict,value_1)
                self.check_Dict(self.q2_dict,value_2)
        # Now sorted lists are built based off of number value and then alphabetically
        self.q1_dict = sorted(self.q1_dict.items(), key=lambda t: (-t[1][0], t[0]))
        self.q2_dict = sorted(self.q2_dict.items(), key=lambda t: (-t[1][0],t[0]))
