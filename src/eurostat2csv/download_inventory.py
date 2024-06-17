import requests
from os.path import exists

def download_inventory(filename,force_update):
 
#    filename=path+"inventory.txt"
    if exists(filename) and force_update==False:
        return(2)
        
    link="https://ec.europa.eu/eurostat/api/dissemination/files/inventory?type=data&lang=en"
    response = requests.get(link)
    if response.status_code !=200:
        print("Error.Cannot download Inventory")
        return(-1)
    with open(filename, "wb") as inventory_file:
        inventory_file.write(response.content)
        print('Download completed.')
        inventory_file.close()
    return(1)
