#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line


# In[3]:


a=[]
for x in range(2000 , 3200) :
    if (x%7==0) and (x!=0):
        a.append(str(x))
print(','.join(a))


# In[ ]:


#Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.


# In[4]:


firstname =input()
secondname=input()
print(firstname[::-1] ," ",secondname[::-1])


# In[ ]:


#Write a Python program to find the volume of a sphere with diameter 12 cm. Formula: V=4/3 * π * r 3


# In[5]:


d=12
r=d/2
v=(4/3)*(22/7)*(pow(r,3))
print(v)


# In[6]:


########Task 2:#######


# In[ ]:


#Create the below pattern using nested for loop in Python. ** * * * * * * * * * * * * * * * * * * * * * * *


# In[7]:


a=5
for i in range(1,a+1):
    print("*"*(i)+" "*(a-i))
for i in range(1,a+1):
    print("*"*(a-i)+" "*(i))    


# In[ ]:


#Write a Python program to reverse a word after accepting the input from the user.


# In[8]:


a=str(input())
print(a[::-1])


# In[ ]:


#Write a program which accepts a sequence of comma-separated numbers from console and generate a list.


# In[1]:


a=input().split(',')
print(list(a))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




