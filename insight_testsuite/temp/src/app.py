import csv

#create custom dialect to be able to parse the semi-colons
csv.register_dialect('read_semi','excel', delimiter=';')
#create ordered dictionary 
input_file = csv.DictReader(open("../input/tester.csv"),dialect='read_semi')
print(input_file)
occupation_dict = {}
state_dict = {}
count = 0

def checkDict(dict, key_val):
    if key_val not in dict:
        dict[str(key_val)]= [1]
    else:
        dict[str(key_val)][0]= dict[str(key_val)][0] + 1

for row in input_file:
    if row['CASE_STATUS'] == 'CERTIFIED':
        count = count +1
        occupation_name = row["SOC_NAME"]
        state = row["WORKSITE_STATE"]
        checkDict(occupation_dict,occupation_name)
        checkDict(state_dict,state)
sort_state = sorted(state_dict.items(), key=lambda t: (-t[1][0], t[0]))
sort_occu = sorted(occupation_dict.items(), key=lambda t: (-t[1][0],t[0]))

top_10_state = sort_state[:10]
top_10_occu = sort_occu[:10]

def calc_percent(top_10, n):
    for row in top_10:
        num = row[1][0]
        percent = (num*100)/n
        row[1].append(percent)

calc_percent(top_10_state, count)
calc_percent(top_10_occu, count)


def write_text_file(name, titles, info):
    with open("../output/"+name, "w+") as f:
        f.writelines(titles)
        f.write('\n')
        for row in info:
            string = str(row[0])+';'+str(row[1][0])+";"+str(row[1][1])+'%'
            f.write(string+"\n")
        f.close()
            

#write_text_file("hello.txt", ["yo", "what_up"], top_10_occu)