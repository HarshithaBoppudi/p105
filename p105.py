import csv
import math


with open("data1.csv") as k:
    data_read=csv.reader(k)
    data1=list(data_read)
    
data=data1[0]

def mean(data):
    n=len(data)
    sum=0
    for d in data:
        sum=sum+int(d)
    mean=sum/n

    return mean

squared_list=[]
for i in data:
    a=int(i)-mean(data)
    a=a**2
    squared_list.append(a)
    
total=0
for j in squared_list:
    total=total+int(j)
    
result=total/(len(data)-1)

std_deviation=math.sqrt(result)
print(std_deviation)

