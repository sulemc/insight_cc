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