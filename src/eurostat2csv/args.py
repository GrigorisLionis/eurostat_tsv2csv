import sys

#simple and extremely lightweight parser
#no error checking

def parse_args(argvs):
    arguments={}
    arguments["update_inventory"]=True
    arguments["force_update_tsv"]=False
    arguments["use_custom_path"]={"use":False,"path":""}
    tables=[]
    use_custom_path=False
    
    for arg in argvs[1:]:
        arg_decomp=arg.split("=")
        if len(arg_decomp)==1:
            if arg=="-v":
                arguments["update_inventory"]=False
            elif arg=="-f":
                arguments["force_update_tsv"]=True
            else:
                tables.append(arg)
        else:
            if arg_decomp[0]=="-p":
                arguments["use_custom_path"]={"use":True,"path":arg_decomp[1]}

    return arguments,tables

