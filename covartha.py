'''l=[1,4,7,9,3,7,4,7]
for i in l:
    p=l.count(i)
    print(i,p)
'''
###Duplicates remove in list::
#logic::1
'''l=[1,4,3,7,8,3,7,9,7]
l1=[]
for i in l:
    if i not in l1:
        l1=l1+[i]
print(l1)
'''
#logic2::
'''l=[1,4,3,7,8,3,7,9,7]
l1=[]
for i in l:
    if l.count(i)<=1:
        l1=l1+[i]
print(l1)
'''
#logic 3::
'''l=[1,4,3,7,8,3,7,9,7]
l1=[]
s=set(l)
print(list(s))
'''
##REVERSE LIST ::
#logic:1
'''l=[1,3,5,7,9]
l1=[]
for i in l:
    l1=[i]+l1
print(l1)
'''
#logic 2:
'''l=[1,3,5,7,9]
print(l[::-1])'''
##GETTING ODD NUMBERS AND EVEN NUMBER SUM::
'''l=[1,3,5,4,6,7,8]
l1=[]
s=0
for i in l:
    if i%2==1:
        l1+=[i]
    else:
        if i%2==0:
            s=s+i
print("odd numbers:",l1)
print("total even:",s)
'''
##FACTORIAL::
#LOGIC:1
'''s=int(input())
f=1
n=1
while s>=n:
    f=f*n
    n=n+1
print(f)'''
#LOGIC::2
'''s=int(input())
f=1
for i in range(1,s+1):
    f=f*i
print(f)'''
#GET COMMON ELIMENTS IN LIST::
'''l=[1,3,5,7,3,7,8,4,7]
l1=[]
for i in l:
    if l.count(i)>=2:
        l1+=[i]
print(l1)'''
#ANAGRAM:::
'''a=input("enter a string")
b=input("enter a string")
s=sorted(a)
c=sorted(b)
if s==c:
    print("anagram")
else:
    print("not angram")'''
'''l=[2,4,25,26,78,42]
sum=0
count=0
for i in range(len(l)):
    if i%2!=0:
        sum=sum+l[i]
        count=count+1
if count==0:
    print("no odd number in list")
else:
    mean=sum/count
    print("l:",mean)
     '''   

'''l=[2,4,25,26,78,42]
sum=0
count=0
for i in range(len(l)):
    if i%2!=0:
        sum=sum+l[i]
        count=count+1
if count==0:
    print("no odd numbers:")
else:
    mean=sum/count
    print("l:",mean)'''

'''a=list(map(int,input().split()))
c=[]
for i in range(len(a)):
    if i%2==1:
        c=c+[a[i]]
print(sum(c)/len(c))'''


'''l=['g','y','p','q','r']
s=['q','t','i','p']
for i in l:
    for j in s:
        if i==j:
            print(j)
'''
'''s=input("enter a str:")
s1=''
for i in s:
    if i.isalnum()==False:
        s1+=i
print(s1)
'''
'''a=input()
c=''
for i in a:
    if i.isdigit():
        continue
    else:
        c=c+i
print(c)'''
#MAX STR::
'''a=input()
a=a.split()
c=[]
for i in a:
    c=c+[len(i)]
print(a[c.index(max(c))])
'''
'''s=input()
a=s.split()
c=[]
for i in a:
    c=c+[len(i)]
print(a[c.index(max(c))])'''
'''l=[1,2,3,4,5,2,4,2,7,4]
l1=[]
for i in l:
    l1=l1+[(i,l.count(i))]
print(sorted(list(set(l1))))'''
'''for i in l:
    if i not in l1:
        l1=l1+[i]
print(l1)
'''
'''for i in l:
    if l.count(i)>=2:
        l1=l1+[i]
print(l1)'''
'''x=int(input("enter a number:"))
y=int(input("enter a number:"))
while x<=y:
    i=1
    c=0
    while i<=x:
        if x%i==0:
            c=c+1
        i=i+1
    if c==2:
        print(x)
    x=x+1

'''
'''s=input()
s1=input()
a=sorted(s)
b=sorted(s1)
if a==b:
    print("anagram")
else:
    print("not anagram")'''

'''l=[2,4,25,26,78,42]
sum=0
c=0
for i in range(len(l)):
    if i%2==1:
        sum=sum+l[i]
        c=c+1
if c==0:
    print("no odd:")
else:
    mean=sum/c
    print(mean)'''

'''v=input()
l=input()
for i in v:
    for j in l:
        if i==j:
            print(i)
'''
'''a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in a:
    if i in b:
        print(a)


'''
'''l=input()
l1=''
for i in l:
    if i.isalpha():
        l1+=i
print(l1)
'''
'''s=input()
s=s.split()
c=[]
for i in s:
    c=c+[len(i)]
print(s[c.index(max(c))])'''
'''s-input()
s=s.split()
c=[]
for i in s:
    c=c+[l[i]]
    print(s[c.index(max(c))])'''
'''
a=[9,3,2,7,4,8,1,6,5]
b=['a','c','e','i','p','k','o','w','j']
for i in range(len(a)-1):
    for j in range(len(a)-1):
        if a[j]<a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            b[j],b[j+1]=b[j+1],b[j]
print(a)
print(b)
'''
'''a=[1,23,43,23,5,45,6,7,8,3,2,3,5,3,4,5,5,6,4,3,6,3,2,4,2,3,5]
b=[]
c=[]
d=[]
for i in a:
    if len(b)==0:
        b=b+[i]
    elif(b[-1]+1==i):
        b=b+[i]
    else:
        c=c+[b]
        b=[i]
for i in c:
    if len(i)>1:
        d=d+[i]
print(d)'''


'''a = [9, 3, 2, 7, 4, 8, 1, 6, 5]
b = ["a", "c", "e", "i", "p", "k", "o", "w", "j"]

v=zip(a,b)
print(v)
r=list(v)
print(r)
r.sort()
c,d=zip(*r)
A=list(c)
B=list(d)
A.reverse()
B.reverse()
print(A)
print(B)'''















'''
a = [9, 3, 2, 7, 4, 8, 1, 6, 5]
b = ["a", "c", "e", "i", "p", "k", "o", "w", "j"]
s=list(zip(a,b))
d=sorted(s)
t,b=zip(*d)
d=list(t)
c=list(b)
d.reverse()
c.reverse()
print(d)
print(c)'''
'''for i in range(len(a)-1):
    for j in range(len(a)-1):
        if a[j]<a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            b[j],b[j+1]=b[j+1],b[j]
print(a)
print(b)'''

'''a = [9, 3, 2, 7, 4, 8, 1, 6, 5]
b = ["a", "c", "e", "i", "p", "k", "o", "w", "j"]
d={}
for i in range(len(a)):
    d1={}.fromkeys([a[i]],b[i])
    d.update(d1)
print(d)
a.sort()
a.reverse()
x=list(d.keys())
y=list(d.values())
for i in range(len(a)):
    for j in range(len(x)):
        if a[i]==x[j]:
            b[i]=y[j]
print(a)
print(b)
'''
'''s=input()
s=s.split()
c=[]
for i in s:
    c=c+[len(i)]
print(s[c.index(max(c))])'''
'''s=[2,4,25,26,78,42]
sum=0
c=0
for i in range(len(s)):
    if i%2==1:
        sum=sum+s[i]
        c=c+1
if c==0:
    print("no odd index:")
else:
    mean=sum/c
    print(mean)
'''

'''a = [9, 3, 2, 7, 4, 8, 1, 6, 5]
b = ["a", "c", "e", "i", "p", "k", "o", "w", "j"]
for i in range(len(a)-1):
    for j in range(len(a)-1):
        if a[j]<a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            b[j],b[j+1]=b[j+1],b[j]
print(a)
print(b)
'''

'''s=[2,4,25,26,78,42]
sum=0
c=0
for i in range(len(s)):
    if i%2==1:
        sum=sum+s[i]
        c=c+1
if c==0:
    print("no odd index")
else:
    mean=sum/c
    print(mean)
'''
'''s='spcys into named enterd recognition has been onedNote'
s=s.split()
c=[]
for i in s:
    c=c+[len(i)]
print(s[c.index(max(c))])'''
'''        
s=input()
s1=input()
a=sorted(s)
b=sorted(s1)
if a==b:
    print("anagram")
else:
    print("not anagram")'''
'''s=input()
l=len(s)
x=s[0]
y=s[l-1]
z=x!=y
print(z)'''
'''s=input()
x=int(s[0])
y=int(s[1])
r=x+y
z=r<10
print(z)'''


##111:
'''s=input()
c=input()
a=sorted(s)
b=sorted(c)
if a==b:
    print("ANAGRAM")
else:
    print("NOT ANAGRAM")'''
'''s=[2,4,25,26,78,42]
sum=0
c=0
for i in range(len(s)):
    if i%2==1:
        sum=sum+s[i]
        c=c+1
else:
    mean=sum/c
    print(mean)'''
'''s=['p','e','t','s','c']
s1=['d','r','h','s','c']
for i in s:
    for j in s1:
        if i==j:
            print(i)'''
'''s='spays named has been noted ricognition lens the print'
s=s.split()
c=[]
for i in s:
    c=c+[len(i)]
print(s[c.index(max(c))])'''

'''s=[9,4,6,3,7,2,0,1,5,8]
c=['B','K','I','L','Y','E','U','Q','X','Z']
for i in range(len(s)-1):
    for j in range(len(s)-1):
        if s[j]<s[j+1]:
            s[j],s[j+1]=s[j+1],s[j]
            c[j],c[j+1]=c[j+1],c[j]
print(s)
print(c)
'''
'''s=[9,4,6,3,7,2,0,1,5,8]
c=['B','K','I','L','Y','E','U','Q','X','Z']
p=list(zip(s,c))
l=sorted(p)
d,c=zip(*l)
y=list(d)
x=list(c)
x.reverse()
y.reverse()
print(y)
print(x)
'''







x = [2,5,1,2,3,6,5,7,8,9,6,5,6]
i=0
l,l1,count=[],[],0
while i<len(x)-1:
    if x[i+1]-x[i]==1:
        l.append(x[i])
        count+=1
    elif count>=1:
        l.append(x[i])
        l1.extend([l])
        l=[]
        count=0
    if i+2 ==len(x):
        if x[-1]-x[i]==1:
            l.append(x[i+1])
            l1.extend([l])
    i+=1
print(l1)





























































































































            












































