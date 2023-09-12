#!/bin/bash
len=$#
if [ $len -ne 1 ]; then
    echo "Usage: eurostat table_name"
    exit
fi
./eurostat_get_tsv.py $1
if [ $? -ne 1 ]; then
   echo "Error fetching table"
   echo $?
   exit
fi
tsv_file=$1".tsv"
./eurostat_tsv2csv.py $tsv_file
if [ $? -ne 1 ]; then
   echo "Error reading file"
   echo $?
   exit
fi
echo "csv,sql file ready"

