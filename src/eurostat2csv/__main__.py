import sys
from os.path import exists
from os import getcwd
import requests 
import gzip
from .eurostat_get_tsv import eurostat_get_tsv
from .eurostat_tsv2csv import eurostat_tsv2csv
from .args import parse_args
from .download_inventory import download_inventory
from .read_inventory_data import read_inventory_data

def main():

    n = len(sys.argv)

    if(n==1):
        print("Error. Table name necessary")
        sys.exit(-1)
    arguments,tables=parse_args(sys.argv)
    table_name=tables[0]
    if(arguments["use_custom_path"]["use"]==True):
        path=arguments["use_custom_path"]["path"]
    else:
        path=getcwd()
    inventory_file=path+"inventory.txt"

    download_inventory(inventory_file,arguments["update_inventory"])
    inventory = open(inventory_file, 'r')
    lines = inventory.readlines()
    for table_name in tables:
        found_table,last_data_change,last_sturcutral_change=read_inventory_data(table_name,lines)
        if found_table==False:
            print("Error. Table", table_name," does not exist")
            continue
        else:
            print(last_data_change,last_sturcutral_change)
        last_change=max(last_data_change,last_sturcutral_change)
        return1=eurostat_get_tsv(table_name,path,last_change, arguments["force_update_tsv"])
        if(return1==2):
           print("TSV file already present",return1)
        if(return1!=1 and return1!=2):
           print("Error downloading file. Error no",return1)
           continue
           #do now go over tsv
       

        return2=eurostat_tsv2csv(table_name,path)
        if(return2!=1):
           print("Error decoding tsv file")
           continue
        print("csv,sql files for ",table_name," ready")
        print("To import use: mysql -e \"source "+path+"/"+table_name+".sql\"")

if __name__=="__main__":
    main()
