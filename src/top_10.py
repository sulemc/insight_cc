class Top10:
    def __init__(self,sorted_1,sorted_2,count):
        #take the sorted query lists and slice down to top 10
        self.top_10_1= sorted_1[:10]
        self.top_10_2= sorted_2[:10]
        #count of certified entries
        self.count = count
        #calculate percentages for each entry
        self.calc_percent(self.top_10_1)
        self.calc_percent(self.top_10_2)
    
    def calc_percent(self, top_10):
        #for each entry in top 10
        for row in top_10:
            #calculate percent of certified entries
            num = row[1][0]
            percent = round((num*100)/self.count, 2)
            #add it to the value array at index 1
            row[1].append(percent)