import sys
from os.path import exists
from os import getcwd
import requests 
import gzip
from .eurostat_get_tsv import eurostat_get_tsv
from .eurostat_tsv2csv import eurostat_tsv2csv

def main():

    n = len(sys.argv)

    if(n==1):
        print("Error. Table name necessary")
        sys.exit(-1)

    table_name=sys.argv[1]
    return1=eurostat_get_tsv(table_name)
    if(return1!=1):
       print("Error reading tsv from database.Error ",return1)

    tsv_file=table_name+".tsv"
    return2=eurostat_tsv2csv(tsv_file)
    if(return2!=1):
       print("Error decoding tsv file")
    print("csv,sql files ready")
    print("To import use: mysql -e \"source ./"+table_name+".sql\"")

if __name__=="__main__":
    main()
