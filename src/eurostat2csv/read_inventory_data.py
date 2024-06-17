from datetime import datetime
import time

def read_inventory_data(table_name,inventory_lines):
    table_name=table_name.upper()
    table_name=table_name.strip()
    for line in inventory_lines:
        elements=line.split("\t")
        table_found=False
        if (elements[0].strip())==table_name:
            #time format is YYYY-MM-DDTHH:MM:SS+ab00
            #ab00 is offset from GMT
            last_data_change_datetime=elements[3].split("+")
            last_structural_change_datetime=elements[4].split("+")
            last_data_change=datetime.strptime(last_data_change_datetime[0],"%Y-%m-%dT%H:%M:%S")
            last_data_change_gmtoffset=last_data_change_datetime[1]
            last_sturcutral_change=datetime.strptime(last_structural_change_datetime[0],"%Y-%m-%dT%H:%M:%S")
            last_structual_change_gmtoffset=last_structural_change_datetime[1]
            table_found=True
            break
    if (table_found==False):
        return False,None,None
    return True,last_data_change,last_sturcutral_change

