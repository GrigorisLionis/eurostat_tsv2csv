#!/usr/bin/python3.5
import sys

n = len(sys.argv)

if(n==1):
    print("Error. Filename of tsv necessary")
    quit()
filename=sys.argv[1]
file1 = open( filename, 'r')
Lines = file1.readlines()
head=Lines[0]
head_br=head.split("\t")
for i in range(0,len(head_br)):
    head_br[i]=(head_br[i]).strip()
variables=head_br[0].split(",")
head_br.pop(0)
last_entry=variables[len(variables)-1]
last_variables=last_entry.split("\\")
#print(head_br)
#print(variables)
#print(last_entry)

if(last_variables[1]!="time"):
    print("TSV wrong format")
    quit()
variables=variables[0:len(variables)-1]
variables.append(last_variables[0])
variables.append("time")
variables.append("value")
variables.append("flags")
for i in range(0,len(variables)-1):
    print(variables[i],",",end="")
print(variables[len(variables)-1])

Lines.pop(0)
for line in Lines:
    data=line.split("\t")
    row_vars=data.pop(0)
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
           print(row_vars,",",head_br[i],",",val,",",flags,end="\n",sep="")
