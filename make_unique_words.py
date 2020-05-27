import sys
import re
import tamil

infile = sys.argv[1]

spechal_charecers = ["~","`","!","@","#","$","%","^","&","*","(",")","_","-","+","=","[","{","]","}",'\\',"|",";",":","\'",'\"',"<",">",".","?","/",',',"’","\’",'“','”']
numbers = [1,2,3,4,5,6,7,8,9,0]
sandhi_chars = ['க்','ச்', 'த்', 'ப்']

unique_content = set()

def is_tamil(word):
    lower_unicode_value = 2944
    upper_unicode_value = 3071
    first_char = word[:1]
    lang_number = ord(first_char)
    if lang_number >=int(lower_unicode_value) and lang_number <=int(upper_unicode_value):
        return True


with open(infile,'r',encoding='utf-8') as fp:
   line = fp.readline()
   cnt = 1
   while line:
   #    print("Line {}: {}".format(cnt, line.strip()))
       #words = re.split('; |, |\*|\n',line)
#       words = re.split('; |, | |\n |- |_ |',line)
#       line = line.replace(","," ").replace(";"," ").replace("-"," ").replace("_"," ")
       for item in spechal_charecers:
           line = line.replace(item," ")

       for item in numbers:
           line = line.replace(str(item)," ")

           
       words = line.split(" ")    
#       print(words)
       for word in words:
           print(word)
           word = word.strip()
           
           if len(word) > 1:
               if is_tamil(word):
#                   if tamil.utf8.get_letters(word)[-1] in sandhi_chars:
#                       print(word)
#                       word = ''.join(word[:-2])
#                       print(word)
#                       sys.exit()
                   unique_content.add(word)
              
       line = fp.readline()
       cnt += 1
    
unique_file = open("unique_"+infile,"w")

#unique_content = set(content)

for line in unique_content:
    unique_file.write(str(line) + "\n")

unique_file.close()    
