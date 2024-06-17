import sys
from datetime import datetime
import os
import time
import requests

link="https://ec.europa.eu/eurostat/api/dissemination/files/inventory?type=data&lang=en"
response = requests.get(link)
print(response)
exit()
if response.status_code !=200:
    print("Error.Cannot download Inventory")
with open("inventory.txt", "wb") as inventory_file:
        inventory_file.write(response.content)
        print('Download completed.')
        inventory_file.close()        
n = len(sys.argv)
table_name=sys.argv[1]
table_name=table_name.upper()
table_name=table_name.strip()
print(table_name)
inventory = open("inventory.txt" , 'r')
lines = inventory.readlines()
for line in lines:
    elements=line.split("\t")
    #print(elements[0])
    if (elements[0].strip())==table_name:
        #time format is YYYY-MM-DDTHH:MM:SS+ab00
        #ab00 is offset from GMT
        last_data_change_datetime=elements[3].split("+")
        last_structural_change_datetime=elements[4].split("+")
        last_data_change=datetime.strptime(last_data_change_datetime[0],"%Y-%m-%dT%H:%M:%S")
        last_data_change_gmtoffset=last_data_change_datetime[1]
        last_sturcutral_change=datetime.strptime(last_structural_change_datetime[0],"%Y-%m-%dT%H:%M:%S")
        last_structual_change_gmtoffset=last_structural_change_datetime[1]
        
        print(last_data_change,last_sturcutral_change)
        
path = "estat_"+table_name.lower()+".tsv.gz" 
ti_m = os.path.getmtime(path)    
m_ti = time.ctime(ti_m)
print(last_data_change,last_sturcutral_change,m_ti)
if( datetime.fromtimestamp(ti_m)>last_data_change and datetime.fromtimestamp(ti_m)>last_sturcutral_change):
    print("File up to date")
else:
    print("File needs to reload")