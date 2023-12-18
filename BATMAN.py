#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a=1
while(a<10):
    if(a==6):
        continue
    print(a)
    a=a+1


# In[16]:


a=0
if(a>5):
    pass
print(a)


# In[2]:


import random
x=0
sysscore=0
userscore=0
while(x<=5):
    a = ['rock','paper','scissor']
    sys = random.choice(a)
    user = input("select rock / paper / scissor : ")
    print("system choose : ",sys)
    if  sys == 'rock' and user == 'paper':
        print("user Wins")
        userscore=userscore+1
    elif  sys == 'paper' and user == 'scissor':
        print("user Wins")
        userscore=userscore+1
    elif  sys == 'scissor' and user == 'rock':
        print("user Wins")
        userscore=userscore+1
    elif  sys == ' paper' and user == 'rock':
        print("sys Wins")
        sysscore=sysscore+1
    elif  sys == 'scissor' and user == 'paper':
        print("sys Wins")
        sysscore=sysscore+1
    elif  sys == 'rock' and user == 'scissor':
        print("sys Wins")
        sysscore=sysscore+1
    elif user == sys:
        print("draw")
        x=x+1
        print("system score=",sysscore)
        print("user score=",userscore)
        


# In[ ]:





# In[6]:


n=int(input("Enter the number:"))
a=0
b=1
c=0
print(a)
print(b)
while c<n:
    c=a+b
    print(c)
    a=b
    b=c
    n=n-1


# In[11]:


a=1
while (True):
    if a==10:
        break
    print(a)
    a=a+1


# In[ ]:


def sum(a ,b):
    c = a + b
    return c

def sub(a ,b):
    c = a - b
    return c
def mul(a ,b):
    c = a * b
    return c
def div(a ,b):
    c = a / b
    return c
def fact(n):
    fact = 1
    while(a<=n):
        fact = fact*a
        a +=1
    return fact
def fact2(n):
    fact = 1
    while():
        fact = fact*a
        a +=1
    return fact


# In[1]:


x = int(input("Enter a number : "))
y = int(input("Enter a number : "))

a = sum(x,y)
print(a)
a = sub(x,y)
print(a)
a = mul(x,y)
print(a)
a = div(x,y)
print(a)


# In[26]:


z = fact(5)
print(z)


# In[6]:


month = int(input("enter a num corresponding month : "))
match month:
    case 1: print("january")
    case 2: print("feb")
    case 3: print("march")
    case 2: print("april")
    default:


# In[ ]:





# In[ ]:




