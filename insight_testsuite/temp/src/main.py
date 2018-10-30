#imports from standard library
import sys

#import classes
from read_file import ReadFile
from build_sorted import BuildSorted
from top_10 import Top10
from write_text import WriteText, MakeLabels

def main(file, title1, title2, category1, category2, status_label):
    # read csv file and build ordered dictionary
    x = ReadFile(file)
    # build sorted lists of just the search categories
    x = BuildSorted(x.data,category1,category2,status_label)
    # build top 10 lists and add percentages
    x = Top10(x.q1_dict,x.q2_dict,x.count)
    # write category label based off of desired output file
    y = MakeLabels(title1, 10)
    y_2 = MakeLabels(title2, 10)
    #output text files
    WriteText(title1, y.labels, x.top_10_1)
    WriteText(title2, y_2.labels, x.top_10_2)

#call main() with command line inputs
if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])