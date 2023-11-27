#!/usr/bin/python3.5
import sys
from os.path import exists
from os import getcwd
n = len(sys.argv)

if(n==1):
    print("Error. Filename of tsv necessary")
    sys.exit(-1)
filename=sys.argv[1]
if exists(filename):
     tsv_file = open( filename, 'r')
else:
     print("Error. Filename does not exist")
     sys.exit(-2)

current_working_directory = getcwd()    
filename_components=filename.split(".")
table_name=filename_components[0]
csv_filename=table_name+".csv"
csv_file=open(csv_filename,"w")
sql_filename=table_name+".sql"
sql_file=open(sql_filename,"w")
Lines = tsv_file.readlines()
head=Lines[0]
head_br=head.split("\t")

for i in range(0,len(head_br)):
    head_br[i]=(head_br[i]).strip()

variables=head_br[0].split(",")
head_br.pop(0) #head br contains now only time columns
len_of_time=max(map(len,head_br))  # find max len of time column.

last_entry=variables[len(variables)-1]
last_variables=last_entry.split("\\")

if(last_variables[1]!="time"):
    print("Error.TSV wrong format")  #extremely basic internal check of TSV structure
    sys.exit(-3)
variables=variables[0:len(variables)-1]
variables.append(last_variables[0])
len_of_fields=[0]*len(variables)
#count size of varchar data, to construct sql table

variables.append("time")
variables.append("value")
variables.append("flags")
for i in range(0,len(variables)-1):
    print(variables[i].strip(),",",end="",sep="",file=csv_file)
print(variables[len(variables)-1],file=csv_file)
#csv header

Lines.pop(0)
for line in Lines:
    data=line.split("\t")  #split rown on tab
    row_vars=data.pop(0)   
    row_vars_const=row_vars.split(",")
    for i in range(0,len(row_vars_const)):
         if len(row_vars_const[i])>len_of_fields[i]:
                len_of_fields[i]=len(row_vars_const[i])
    #check all rows to find length of fields
    
    for i in range(0,len(data)):
           val=data[i].strip() 
           flags="NULL"
           if(val==":"):
                val="NULL"
           val_seg=val.split(" ")
           if(len(val_seg)>1):
                val=val_seg[0]
                flags=""
                for j in range(1,len(val_seg)):
                      flags=flags+val_seg[j]
           print(row_vars,",",head_br[i],",",val,",",flags,end="\n",sep="",file=csv_file)

def sql_string(var_name,var_length):
    return(var_name+" VARCHAR("+str(var_length+5)+"),")
    
#SQL SCHEMA
#table name is the same as in tsv file
#all fields are varchar, with approrpiatte length= MAX(length of field in data+5)
#except of field value which is FLOAT
#we keep also a field FLAGS, as in some cases Eurostat assigns to data a (c or b) field
sql_string_vars=""
print("CREATE DATABASE IF NOT EXISTS Eurostat;",file=sql_file)
print("USE Eurostat;",file=sql_file)
print("DROP TABLE IF EXISTS "+table_name+";",file=sql_file)
for i in range(0,len(variables)-3):
    sql_string_vars=sql_string_vars+sql_string(variables[i],len_of_fields[i]) 
sql_string_vars="CREATE TABLE "+table_name+" ("+sql_string_vars
sql_string_vars=sql_string_vars+sql_string("obs_time",len_of_time)
sql_string_vars=sql_string_vars+"value FLOAT,flags VARCHAR(6) );"
print(sql_string_vars,file=sql_file)

sql_string="LOAD DATA INFILE \'"+current_working_directory+"/"+csv_filename+"\'  INTO TABLE "+table_name+"  FIELDS TERMINATED BY \',\' IGNORE 1 LINES;"    
print(sql_string,file=sql_file)
sys.exit(1)
