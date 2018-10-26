import sys

from read_file import ReadFile
from build_sorted import BuildSorted
from top_10 import Top10
from write_text import WriteText, MakeLabels


def main(file, title1, title2, category1, category2):
    x = ReadFile(file)
    x = BuildSorted(x.data,category1,category2)
    x = Top10(x.q1_dict,x.q2_dict,x.count)
    y = MakeLabels(title1, 10)
    y_2 = MakeLabels(title2, 10)
    WriteText(title1, y.labels, x.top_10_1)
    WriteText(title2, y_2.labels, x.top_10_2)

main('h1b_input.csv','top_10_occupations', 'top_10_states', 'SOC_NAME', 'WORKSITE_STATE')