#!/usr/bin/env python
# coding: utf-8

# In[55]:


import numpy as np
def knapsack(W,a,n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif int(a[i-1][1])<= w:
                K[i][w]=max(int(a[i-1][2])+K[i-1][w-int(a[i-1][1])],K[i-1][w])
            else:
                K[i][w]=K[i-1][w]
    res=K[n][W]
    w=W
    for i in range(n,0,-1):
        if res <= 0:
            break
        if res==K[i-1][w]:
            continue
        else:
            print(a[i-1][0])
            res=res-a[i-1][2]
            w=w-a[i-1][1]
    value=K[n][W]
    return value
def notes(amt,cur,l):
    arr=[]
    max1=max(cur)
    while(amt>0):
        if(amt-max1>=0):
            arr.append(max1)
            amt-=max1
        elif(amt-max1<0):
            cur.remove(max1)
    print("2000X",arr.count(2000))
    print("500 X",arr.count(500))
    print("200 X",arr.count(200))
    print("100 X",arr.count(100))
    print("50 X",arr.count(50))
    print("20 X",arr.count(20))
    print("10 X",arr.count(10))
cur=[10,20,50,100,200,500,2000]
l=len(cur)
price=int(input("enter the price of the weight per kg of extra luggage"))
n=int(input("enter the number of items"))
W=int(input("enter the maximum luggage allowance"))
a=np.zeros((n,3),dtype=object)
for i in range(n):
    item,weight=input().split()
    a[i][0]=item
    a[i][1]=int(weight)
    a[i][2]=int(weight)*price
print(a)
sum=0
for i in range(n):
    sum+=int(a[i][1])
print(sum)
value=knapsack(W,a,n)
print("The amount of money/profit maximised",value)
amt=sum*price-value
if(amt==0):
    print("Your luggage is of optimal weight,you do not have to pay anything")
else:
    print("Amount to be paid to carry the extra luggage",amt)
    print("This can be paid optimally with")
    notes(amt,cur,l)


# In[ ]:


import numpy as np  #importing library numpy to create a 2D matrix,as np is used to cut short the name
def knapsack(W,a,n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif int(a[i-1][1])<= w:
                K[i][w]=max(int(a[i-1][2])+K[i-1][w-int(a[i-1][1])],K[i-1][w])
            else:
                K[i][w]=K[i-1][w]
    res=K[n][W]
    w=W
    for i in range(n,0,-1):
        if res <= 0:
            break
        if res==K[i-1][w]:
            continue
        else:
            print(a[i-1][0])
            res=res-a[i-1][2]
            w=w-a[i-1][1]
    value=K[n][W]
    return value
def notes(amt,cur,l):
    arr=[]
    max1=max(cur)
    while(amt>0):
        if(amt-max1>=0):
            arr.append(max1)
            amt-=max1
        elif(amt-max1<0):
            cur.remove(max1)
    print("2000X",arr.count(2000))
    print("500 X",arr.count(500))
    print("200 X",arr.count(200))
    print("100 X",arr.count(100))
    print("50 X",arr.count(50))
    print("20 X",arr.count(20))
    print("10 X",arr.count(10))
cur=[10,20,50,100,200,500,2000]  #array denoting the denomination of currency
l=len(cur)  #calculates the length of array
price=int(input("enter the price of the weight per kg of extra luggage"))  #takes input
n=int(input("enter the number of items"))  #takes input
W=int(input("enter the maximum luggage allowance"))  #takes input
a=np.zeros((n,3),dtype=object)  #creates a np array of n rows and 3 columns filled with zeros and can contain any type of onject
for i in range(n):
    item,weight=input().split()
    a[i][0]=item  #changing the values in array to the values we are going to use
    a[i][1]=int(weight)
    a[i][2]=int(weight)*price
print(a)
sum=0
for i in range(n):
    sum+=int(a[i][1])  #calculates the total weight that the person wnts to carry
print(sum)
value=knapsack(W,a,n)  #calling the knapsack function
print("The amount of money/profit maximised",value)
amt=sum*price-value  #this is the amount that the person has to pay at the airport
if(amt==0):
    print("Your luggage is of optimal weight,you do not have to pay anything")
else:
    print("Amount to be paid to carry the extra luggage",amt)
    print("This can be paid optimally with")
    notes(amt,cur,l)  #calling function notes to find the optimal amount of notes to give

