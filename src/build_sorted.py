class BuildSorted:
    def __init__(self,data,q1, q2,status_label):
        self.data = data
        self.q1_dict = {}
        self.q2_dict = {}
        self.q1 = str(q1)
        self.q2 = str(q2)
        self.status_label = str(status_label)
        self.count = 0
        self.build_Dicts()

    def check_Dict(self, dict, key_val):
        if key_val not in dict:
            dict[str(key_val)]= [1]
        else:
            dict[str(key_val)][0] += 1

    def build_Dicts(self):
        for row in self.data:
            if row[self.status_label] == 'CERTIFIED':
                self.count += 1
                value_1 = row[self.q1]
                value_2 = row[self.q2]
                self.check_Dict(self.q1_dict,value_1)
                self.check_Dict(self.q2_dict,value_2)
        self.q1_dict = sorted(self.q1_dict.items(), key=lambda t: (-t[1][0], t[0]))
        self.q2_dict = sorted(self.q2_dict.items(), key=lambda t: (-t[1][0],t[0]))