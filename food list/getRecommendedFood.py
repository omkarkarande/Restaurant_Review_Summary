import os
import sys
if len(sys.argv) != 3:
        print ('USAGE: python preprocessor.py <path to menufile.txt> <path to review_sentiments folder>')
        sys.exit(0)
directory_menus = os.path.dirname('food/')
if not os.path.isdir(directory_menus):
	os.makedirs(directory_menus)
foodlist=eval(open(sys.argv[1],"r").read())
files=os.listdir(sys.argv[2])
for f in files:		
		fooddict={}
		positive={}
		negative={}
		#if not os.path.isfile(os.path.splitext("menu/"+f)[0]+".txt"):
		#	continue
		#foodlist=eval(open(os.path.splitext("menu/"+f)[0]+".txt","r").read())
		print("Processing file "+f)
		sfile=open(sys.argv[2]+f,"r")
		sentences=eval(sfile.read())
		for s in sentences:
			ngrams=[]
			words=s[1].split()
			for i in range(0,len(words)):
				w=words[i].lower()
				for j in range(i+1,len(words)):
					ngrams.append(w)
					w=w+" "+words[j].lower()
			#print(str(ngrams)+"\n")
			for x in ngrams:
				if x in foodlist:
					if x in fooddict:
						fooddict[x][0]=fooddict[x][0]+s[0]
						fooddict[x][1]=fooddict[x][1]+1
					else:
						fooddict[x]=[s[0],1]
				#if x in foodlist and s[0]>0:
				#	positive.append(x)
				#if x in foodlist and s[0]>1:
				#	negative.append(x)
		for x in fooddict:
			if((fooddict[x][0]/fooddict[x][1])>0):
				positive[x]=fooddict[x][0]/fooddict[x][1]
			if((fooddict[x][0]/fooddict[x][1])<0):
				negative[x]=fooddict[x][0]/fooddict[x][1]
		if not(len(fooddict)==0):
			outputfile=open(os.path.splitext("food2/"+f)[0]+".txt","w")
		if len(positive)!=0:
			outputfile.write("Recommended Food Dishes:\n")
			#print(positive)
			positivelist=sorted(positive.items(), key=lambda x: x[1])
			
			if(len(positivelist)>5):
				positivelist=positivelist[5:]
			#print(positivelist)
			for f in positivelist:
				outputfile.write(f[0]+"\n")
		if len(negative)!=0:
			outputfile.write("\nDishes to avoid:\n")
			negativelist=sorted(negative.items(), key=lambda y: y[1])
			print(negative)
			if(len(negativelist)>5):
				negativelist=negativelist[5:]
			print(negativelist)
			for f in negativelist:
				outputfile.write(f[0]+"\n")
		
		if len(positive)!=0 and len(negative)!=0:
			outputfile.close()

