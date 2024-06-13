import sys
from os.path import exists
from os import getcwd
import requests 
import gzip


def eurostat_get_tsv(table_name):

    #base_link="https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/"
    #link=base_link+table_name+".tsv.gz"
    base_link="https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/"
    #<CODELIST_CODE>"/latest?format=TSV&lang=en
    link=base_link+table_name+"/?format=TSV"
    #link="https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/LFSI_EMP_A/?format=TSV"
    response = requests.get(link)
    if response.status_code !=200:
        print("Error.Invalid url. Table does not exist in database")
        return(-2)
    with open(table_name+".tsv", "wb") as tsv_gz_file:
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




