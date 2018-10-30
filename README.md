
Insight CC - Susanna McDonald
=======

## Problem
An an overview, the challenge was to take a CSV of H1B visa applications from various years and write a program which returns the top 10 occupations and states based off of the number of certified applicants and the corresponding percentage of total certified applicants. There were a number of considerations with this challenge. 

* size of csv files - all above 150 MB
* reusable for different years and column labels
* proper format of output file

## Approach

For the meat of the code, I used Python 3 and shell scripting in order to make it reusable. I also used python classes to seperate different tasks into different modules.
    
To be able to process the large amount of input data, I used Python's standard library `csv.DictReader()` which creates an iterable object from a csv file. Each row becomes essentially a hash table. This allows for quick iteration when looking for specific attributes as needed in this challenge. 

Next, the program iterates through the DictReader object. First, it verifies that the entry is `CERTIFIED`. It increments the Class count attribute, so as to keep track of the overall count of certified entries. Next, it checks if that entry's occupation or state name exists as a key in the particular query dictionary. If it does not, the key is added and the value for the key is set as an array with an integer to count how many instances that key appears. If the key does already exist then it increments the integer. I opted for the program to create dictionaries for two different query values at the same time so as to save time on iterating through the DictReader object. This process returns two query dictionaries which require substantially less memory than the entire DictReader. 

Then, the dictionaries are sorted first by the value integer, then, alphabetically by key and returned as a list. Those lists are then sliced down to the top 10 entries. Each top 10 list is then iterated through and for each entry the percentage of its count compared to the count of certified entries overall is calculated and added to the entry's list.

Finally, the .txt file is written using the top 10 lists and column labels, the first of which is created based off of the desired name of the output file.

To make the code resuable and fully executable using just `run.sh` I scripted an interactive mode for the command interface. This allows the user to specify the input file name, column labels specific to that particular year and the desired output file name. This will allow the user to compute the top 10 list for any 2 columns, not just state and occupation.

## Run Instructions
* To run on the default settings, meaning the tester file `h1b_input.csv`, simply execute `.\run.sh`
* To alter the default settings add the `-i` flag to `.\run.sh` to enter interactive mode.

        .\run.sh -i
        >starting interactive mode
        >Enter name of input CSV file >
Enter the name of the csv file which you have put into the input file. such as `H1B_FY_2014.csv`

        >Enter name of input CSV file > "H1B_FY_2014.csv"
        >you entered H1B_FY_2014.csv
        >enter column name of application status ex STATUS >>
Enter the column name which reflects the current status of the visa application.

        >enter column name of application status ex STATUS >> "STATUS"
        >you entered STATUS
        >enter name of desired output file, ex top_10_states >>
Here you'll name one of the output files you want, no .txt needed

        >enter name of desired output file, ex top_10_states >> "top_10_states"
        >you entered top_10_states
        >enter name of csv column to evaluate, ex WORKSITE_STATE >>
Enter the name of the corresponding column label to the output file you just named

        >enter name of csv column to evaluate, ex WORKSITE_STATE >> "WORKSITE_STATE"
        >you entered WORKSITE_STATE

It will then ask you for the second query file name and column name. After the second column name is inputted, it will execute.