'''def chinnu():
    print("hello")
    def sravs(sree):
        print("hello sravs")
    return sravs()
a=chinnu()
a()
'''
'''s='masthan'
print(s[0:2]+s[3:5]+s[6]+s[0]*3)
print(s[-7:-5]+s[-4:-2]+s[-1]+s[-7]*3)
print(s[0]+s[1]+s[3]+s[4]+s[6]+s[0]*3)
print(s[0]*3+s[6]+s[4:3]+s[1:0])
'''
'''l=[1,2,3,4]
l1=['a','b','c','d']
c=[]
p=dict(zip(l,l1))
c=c+[p]
print(c)
'''
'''s=int(input("enter a number"))
while s>0:
    d=s%10
    s=s//10
    if d%2==0:
        print(d)
'''
'''s=input("enter:")
s1=input("enter:")
a=sorted(s)
b=sorted(s1)
if a==b:
    print("anagram")
else:
    print("not anagram")
'''
'''s='aacecaaa'
s1=''
for i in s:
    s1=i[::-1]+s1
print(s1+i[0])'''

'''s='sravs'
s1=''
for i in s:
    s1=i+s1
print(s[0]+s1+s[0])
'''
'''s=input("enter a str:")
s1=''
for i in s:
    s1=i+s1
if s1==s:
    print("pal")
else:
    print("not pal")'''
'''
s=input("enter a str:")
s1=''
for i in s:
    s1=i[::-1]+s1
if s1==s:
    print("pal")
else:
    print("not pal")
'''
'''a=["1","12","123","1234","12345","123456","1234567","123456","12345","1234","123","12","1"]
print("\n".join(a))
'''
'''import calendar
year=int(input("enter a year"))
month=input()
x=calendar.month(year,month)
print(x)
'''
#single inh::
'''class sravs:
    x=10
    y=20
    def f1():
        print("hiii")
class chinnu(sravs):
    def f2():
        print("hello")

'''
# multi level::
'''class a:
    d=10
    def f1():
        print("nani")
class b(a):
    e=20
    def f2():
        print("chinnu")
class c(b):
    def f3():
        print("king")
'''
#multipule inh::
'''class a:
    def f1():
        print("hiii raaa")
class b:
    def f2():
        print("hello mam")
class c(a,b):
    def f3():
        print("i love my mom")
    
'''
#swaping::
'''s=input("enter a str:")
s1=''
for i in s:
    if i.isupper():
        s1=s1+i.lower()
    if i.islower():
        s1=s1+i.upper()
print(s1)
'''
#print(s.swapcase())
##anagram::
'''s=input("ent:")
s1=input("ent:")
a=sorted(s)
b=sorted(s1)
if a==b:
    print("this is anagram")
else:
    print("not anagram")
'''
##string palandrom::
'''s=input("ent:")
s1=''
for i in s:
    s1=i[::-1]+s1
if s1==s:
    print("pal")
else:
    print("not pal")
'''
'''l=[1,2,3,4,5]
s=tuple(enumerate(l,0))
print(s)
'''

#abstraction:::
'''class d:
    __c=10
    e=20
    def f1():
        print("hiii")

'''


### bank bal enq,withdraw ,deposite:::
'''class chinnu:
    balance=1500
    def balance_enq(self):
        print("ur balance is:",self.balance)
    def withdraw_amount(self,amount):
        self.amount=amount
        if self.amount>self.balance:
            print("insuf balance")
        else:
            print("collect cash:")
            yes=input("ur present balance:")
            if yes:
                print("ur present balanace:",self.balance-self.amount)
    def deposite(self,amount):
        global balance
        self.amount=amount
        print("now ur balance:",self.amount+self.balance)
        balance=self.amount+self.balance
s=chinnu()
sravs=int(input("BALANCE_ENQUERY PRESS :1 \n WITHDRAW_AMOUNT PRESS :2 \n DEPOSITE_AMOUNT PRESS :3 \n "))
if sravs==1:
          s.balance_enq()
elif sravs==2:
          amount=int(input("enter a amount:   "))
          s.withdraw_amount(amount)
elif sravs==3:
          amount=int(input("enter a deposite amount:   "))
          s.deposite(amount)

'''






































































































    
