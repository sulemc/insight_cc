#!/bin/bash
filename=
output1=
output2=
category1=
category2=
certified=
if [ "$1" = "-i" ]
then 
    echo "starting interactive mode"
    response=
    echo -n "Enter name of input CSV file > "
    read response
     if [ -n "$response" ]; then
        filename=$response
        echo "you entered $filename"
        echo -n "enter column name of application status ex STATUS >>"
        read response  
        if [ -n "$response" ]; then
         certified=$response
        echo "you entered $certified"
        echo -n "enter name of desired output file, ex top_10_states >>"
        read response
        if [ -n "$response" ]; then
        output1=$response
        echo "you entered $output1"
        echo -n "enter name of csv column to evaluate, ex SOC_NAME >>"
        read response  
        if [ -n "$response" ]; then
         category1=$response
        echo "you entered $category1"
        echo -n "enter name of desired 2nd output file, ex top_10_states >>"
        read response  
        if [ -n "$response" ]; then
         output2=$response
        echo "you entered $output2"
        echo -n "enter name of 2nd csv column to evaluate, ex SOC_NAME >>"
        read response  
        if [ -n "$response" ]; then
         category2=$response
        echo "you entered $category2"
                    fi
                fi
            fi
        fi
    fi
fi
else
echo "using defaults"
filename="h1b_input.csv"
output1="top_10_occupations"
output2="top_10_states"
category1="SOC_NAME"
category2="WORKSITE_STATE"
certified="CASE_STATUS"
fi

python3 ./src/main.py "$filename" "$output1" "$output2" "$category1" "$category2" "$certified"