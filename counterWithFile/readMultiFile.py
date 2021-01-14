import glob
import os

path = "C:/Users/haime/Downloads/mouthAno/"
all_files = os.listdir(path)
 
for file in all_files:
    content_file = open(path + file,"r")
    
    new_content = ""
    if (content_file.readline()[0:2]) == "15":
        content_file.seek(0)
        new_content = "0 " + content_file.readline()[3:]
        print(new_content)
    content_file.close()
    content_file = open(path + file,"w")
    content_file.write(new_content)
    content_file.truncate()
    # content_file.close()
    next