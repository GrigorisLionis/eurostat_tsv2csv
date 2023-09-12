#!/usr/bin/python3.5
import sys
from os.path import exists
from os import getcwd
import requests 
import gzip


n = len(sys.argv)

if(n==1):
    print("Error. Table name necessary")
    sys.exit(-1)

table_name=sys.argv[1]
base_link="https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/"
link=base_link+table_name+".tsv.gz"
response = requests.get(link)
if response.status_code !=200:
   print("Error.Invalid url. Table does not exist in database")
   sys.exit(-2)
with open(table_name+".tsv.gz", "wb") as tsv_gz_file:
    tsv_gz_file.write(response.content)
    print('Download completed.')
    with gzip.open(table_name+".tsv.gz", 'rb') as f:
        file_content = f.read()
        with open(table_name+".tsv","wb") as f:
            f.write(file_content)
            sys.exit(1)

print("Error.File was not decoded correctly")
sys.exit(-3)
