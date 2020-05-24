import sys

infile = sys.argv[1]

content = open(infile,'r',encoding='utf-8').readlines()
unique_file = open("unique_"+infile,"w")

unique_content = list(set(content))

for line in unique_content:
    unique_file.write(str(line) )

unique_file.close()    
