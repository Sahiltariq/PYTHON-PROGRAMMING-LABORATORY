import os.path
import sys
fname = input("Enter the filename: ")
if not os.path.isfile(fname):
    print("File", fname, "doesn't exist")
    sys.exit(1)
with open(fname, "r") as infile:
    lineList = infile.readlines()
num_lines = len(lineList)
for i in range(min(20, num_lines)):
    print(i + 1, ":", lineList[i])
word = input("Enter a word: ")
cnt = 0
for line in lineList:
    cnt += line.count(word)
print("The word", word, "appears", cnt, "times in the file")
