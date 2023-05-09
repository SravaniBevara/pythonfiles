'''
x=int(input("enter a number:"))
y=int(input("enter a number:"))
while x<=y:
    i=1
    c=0
    while x>=i:
        if x%i==0:
            c=c+1
        i=i+1
    if c==2:
        print(x)
    x=x+1
'''
'''x=int(input("enter a number:"))
i=1
c=0
while x>=i:
    if x%i==0:
        c=c+1
    i=i+1
if c==2:
    print("prime number")
else:
    print("not prime")
'''
#s={key: value for key, value in zip(['key1','key2','key3'],['value1','value2','value3'])}
'''x=int(input())
l=[]
for i in range(1,x+1):
    y = int(input())
    l+=[y]
print(l[:2]+l[-2:])
'''
'''d=int(input())
l=[]
for i in range(1,d+1):
    y=int(input())
    if y%5==0:
        l+=[y]
print(l)
'''
'''l=[1,2,3,5,7,9,5]
x=int(input())
y=int(input())
a=l[x]
b=l[y]
l[x]=b
l[y]=a
print(l)'''

#with open(r'C:\Users\CHINNI\Desktop\web_scrapp\fun.txt','r') as vani:
    #print(vani.read())
'''
import random
import math
a='0123456789'
b='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
c=a+b
def otp_gen():
    otp=''
    for i in range(6):
        otp=otp+c[math.floor(random.random()*len(c))]
    print(otp)
otp_gen()

'''
#dynamic dict::
'''dict={}
n=int(input("enter items:"))
for i in range(n):
    a,s=input().split()
    dict[a]=s
print(dict)
'''
'''l=[1,1,2,3,1,2,3,1,7]
c=[]
for i in l:
    c=c+[(i,l.count(i))]
print(sorted(list(set(c))))
'''
'''l=[1,1,2,3,1,2,3,1]
l1=[]
for i in l:
    if i not in l1:
        l1=l1+[i]
print(l1)
'''
'''print(list(set(l)))'''

'''a='xyzabcxyz'
c=[]
d=[]
for i in a:
    c=c+[(i,a.count(i))]
for i in c:
    if i not in d:
        d=d+[i]
print(d)    
'''
'''a=input("enter str:")
c=[]
d=[]
for i in a:
    c=c+[(i,a.count(i))]
for i in c:
    if i not in d:
        d=d+[i]
print(d)
'''
'''l=input()
c=[]
d=[]
for i in l:
    c=c+[(i,l.count(i))]
    for i in c:
        if i not in d:
            d=d+[i]
print(d)
'''
'''a=input()
b=input()
c=sorted(a)
d=sorted(b)
if c==d:
    print("anagram")
else:
    print("not anagram")'''
'''l=list(map(int,input().split()))
c=[]
for i in len(a):
    if i%2==1:
        c=c+[a[i]]
print(sum(c)/len(c))
'''
'''a=list(map(int,input().split()))
c=[]
for i in range(len(a)):
    if i%2==1:
        c=c+[a[i]]
print(sum(c)/len(c))'''

'''l=[2,4,25,26,78,42]
sum=0
c=0
for i in range(len(l)):
    if i%2==1:
        sum= sum+l[i]
        c=c+1
else:
    mean=sum/c
    print(mean)'''
'''import random
import math
a='0123456789'
b='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
c=a+b
def otp_gen():
    otp=''
    for i in range(6):
        otp=otp+c[math.floor(random.random()*len(c))]
    print(otp)
otp_gen()'''
'''l=int(input("enter a number"))
x=int(input("enter a number"))
while l<=x:
    i=1
    c=0
    while i<=l:
        if l%i==0:
            c=c+1
        i=i+1
    if c==2:
        print(l)
    l=l+1'''

##python test::
'''x=int(input("enter a number:"))
a=1
b=0
i=1
while i<=x:
    d=a+b
    a=b
    b=d
    i=i+1
    print(a)'''
#factorial:"
'''x=int(input("enter a number:"))
n=1
f=1
while x>=n:
    f=f*n
    n=n+1
    print(f)'''
'''x=int(input("enter a number:"))
for i in range(1,x):
    x=x*i
    print(x)'''
'''dict={}
n=int(input("enter a items:"))
for i in range(n):
    a,p=input().split()
    dict[a]=p
print(dict)'''
'''dict={}
n=int(input("enter a items:"))
for i in range(n):
    a,p=input().split()
    dict[a]=p
print(dict)'''

































































