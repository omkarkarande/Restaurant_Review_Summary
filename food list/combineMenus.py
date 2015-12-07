import os
import sys
from collections import Counter
if len(sys.argv) != 2:
        print ('USAGE: python preprocessor.py <path to menus folder>')
        sys.exit(0)
files=os.listdir(sys.argv[1])
foodlist=[]
for f in files:
	file1=open(sys.argv[1]+f,"r")
	list1=eval(file1.read())
	for x in list1:
		foodlist.append(x.lower())
cnt = Counter(foodlist)
foodlist= [k for k, v in cnt.iteritems() if v > 1]
foodlist = [x for x in foodlist if not len(x.split())==1]
for x in foodlist:
	if(len(x.split())==1):
		print(x)
		foodlist.remove(x)
menufile=open("menufile.txt","w")
print(len(foodlist))
menufile.write(str(foodlist))
