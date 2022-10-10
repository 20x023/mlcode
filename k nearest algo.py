import math

f=open('Z:\SEM 5\ML\Knear.txt','r')
files=f.readlines()
array=[]
for i in files:
    j = i.split(',')
    array.append(j)

n=len(array)  
x1=[]
x2=[]
x3=[]
x4=[]
c1=[]
real=[]

a=0
b=0
c=0
d=0
e=0
f=0
dp=0
dpx=0
k=0
data=[]
svalue=[]
sreal=[]
for i in array:
    a=float(i[0])
    x1.append(a)
    b=float(i[1])
    x2.append(b)
    c=float(i[2])
    x3.append(c)
    d=float(i[3])
    x4.append(d)
    e=float(i[4])
    c1.append(e)
    f=float(i[5])
    real.append(f)
    
for i in range(0,5):
   
    dp=((x1[i]-x1[5])**2)+((x2[i]-x2[5])**2)+((x3[i]-x3[5])**2)+((x4[i]-x4[5])**2)
    dpx=math.sqrt(dp)
    #print(dpx)
    data.append(float(dpx))
       
mapping = {key:value for key, value in zip(data,c1)}
rmapping = {key:value for key, value in zip(data,real)}
print("\nThe data point values and their corresponding classes are:",mapping)

sortbkey={k: v for k,v in sorted(mapping.items())}
sortbrealkey={k: v for k,v in sorted(rmapping.items())}
#print(sortbrealkey)
out = dict(list(sortbkey.items())[0: 3])
print("\n\nThe selected datapoint values:",out)

rout = dict(list(sortbrealkey.items())[0: 3])
print("\n\nThe selected datapoint values:",rout)

#for key,value in out.items():
	#print(value)
for key,value in out.items():
    svalue.append(float(value))
#print(svalue)

for key,value in rout.items():
    sreal.append(float(value))

res = max(set(svalue), key = svalue.count)
avg = sum(sreal)/len(sreal)
print("\nThe average is ", round(avg,2))
print("\nValue of the new query point:",res)
