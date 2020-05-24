import csv
import glob
import tamil

files = glob.glob("girl-old/*")

for input_file in files:
    lines = open(input_file,'r').readlines()
    line_count = 1
    for line in lines:
        print(line)
        print(line_count)
        if not line_count == 1:
            start_letter = line.split(",")[0]
            content = line.split(",")[1]
            new_file = open(start_letter + ".txt","a")
            new_file.write(content + "\n")
            new_file.close()
        line_count = line_count + 1
