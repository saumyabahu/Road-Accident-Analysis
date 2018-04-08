file=open("xyz.csv")

l=[]
k=[]
t=file.readlines()

for i in t :
	k=i.strip().split(",")
	l.append(k)

	

def distance(i,j):
	d=0
	for k in range(0,len(l[0])):
		if(l[i][k]!=l[j][k]):
			 d+=1
	return d


print distance(3,4)
