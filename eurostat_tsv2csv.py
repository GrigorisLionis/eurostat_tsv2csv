#!/usr/bin/python3.5
import sys

n = len(sys.argv)

if(n==1):
    print("Error. Filename of tsv necessary")
    quit()
filename=sys.argv[1]
file1 = open( filename, 'r')
filename_components=filename.split(".")
table_name=filename_components[0]
csv_filename=table_name+".csv"
csv_file=open(csv_filename,"w")
Lines = file1.readlines()
head=Lines[0]
head_br=head.split("\t")

for i in range(0,len(head_br)):
    head_br[i]=(head_br[i]).strip()

variables=head_br[0].split(",")
head_br.pop(0)
len_of_time=max(map(len,head_br))
last_entry=variables[len(variables)-1]
last_variables=last_entry.split("\\")
#print(head_br)
#print(variables)
#print(last_entry)

if(last_variables[1]!="time"):
    print("TSV wrong format")
    quit()
variables=variables[0:len(variables)-1]
len_of_fields=[0]*len(variables)
variables.append(last_variables[0])
len_of_fields=[0]*len(variables)
#count size of varchar data, to construct sql table

variables.append("time")
variables.append("value")
variables.append("flags")
for i in range(0,len(variables)-1):
    print(variables[i].strip(),",",end="",sep="",file=csv_file)
print(variables[len(variables)-1],file=csv_file)


Lines.pop(0)
for line in Lines:
    data=line.split("\t")
    row_vars=data.pop(0)
    row_vars_const=row_vars.split(",")
    for i in range(0,len(row_vars_const)):
         if len(row_vars_const[i])>len_of_fields[i]:
                len_of_fields[i]=len(row_vars_const[i])
    #print(row_vars)
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
#print(len_of_time)
#print(len_of_fields)

def sql_string(var_name,var_length):
    return(var_name+" VARCHAR("+str(var_length+5)+"),")


sql_string_vars=""
for i in range(0,len(variables)-3):
    sql_string_vars=sql_string_vars+sql_string(variables[i],len_of_fields[i]) 
sql_string_vars="CREATE TABLE "+table_name+" ("+sql_string_vars
sql_string_vars=sql_string_vars+sql_string("obs_time",len_of_time)
sql_string_vars=sql_string_vars+"value FLOAT,flags VARCHAR(6) );"
print(sql_string_vars)
    

