import os
import sys, argparse

parsers = argparse.ArgumentParser()
parsers.add_argument("-i", "--index", default=1, help="Please enter begin index")
parsers.add_argument("-f", "--folder", help="Please enter folder path")
args = parsers.parse_args()
def changeFileName(oldName, newName):
    os.rename(oldName, newName)

def changeAllFileName(beginIndex, folder):
    for file in os.listdir(folder):
        
        changeFileName(folder + '/' + file, folder + '/' + str(beginIndex) + '.png')
        beginIndex = int(beginIndex)+1
    
changeAllFileName(args.index, args.folder)
print(args.index)
print(args.folder)
# "C:/Users/haime/Downloads/New folder\hàm_răng