file = open(r"C:/Users/haime/Downloads/leaf_list.txt", "r", encoding="utf8")
outString = ""
for line in file:
    

    print(line)
    line = line.rstrip('\r\n')
    outString = outString + line + ","

writeFile = open(r"C:/Users/haime/Downloads/leaf_list_one_line.txt", "w", encoding="utf8")
writeFile.write(outString)
writeFile.close()
