import sys
from os.path import exists,getmtime
from os import getcwd
from datetime import datetime
import requests 
import gzip


def eurostat_get_tsv(table_name,path,last_change,force_update):

    #base_link="https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/"
    #link=base_link+table_name+".tsv.gz"
    base_link="https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/"
    #<CODELIST_CODE>"/latest?format=TSV&lang=en
    link=base_link+table_name+"/?format=TSV"
    #link="https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/LFSI_EMP_A/?format=TSV"

    filename=path+table_name+".tsv"
    if exists(filename):
        ti_m = getmtime(filename)
        if(datetime.fromtimestamp(ti_m)>last_change):
            print("File more recent that last change")
            if (force_update==False):
                return(2)
                    
    response = requests.get(link)
    if response.status_code !=200:
        print("Error.Invalid url. Table does not exist in database")
        return(-2)
    with open(path+table_name+".tsv", "wb") as tsv_gz_file:
        tsv_gz_file.write(response.content)
        print('Download completed.')
        return(1)
    #    with gzip.open(table_name+".tsv.gz", 'rb') as f:
    #        file_content = f.read()
    #        with open(table_name+".tsv","wb") as f:
    #            f.write(file_content)
    #            sys.exit(1)

    print("Error.File was not decoded correctly")
    return(-3)




