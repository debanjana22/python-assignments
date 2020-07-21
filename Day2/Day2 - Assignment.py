#!/usr/bin/env python
# coding: utf-8

# In[1]:


print ("Hello\npython")


# In[2]:


print ("Hello        python")


# In[3]:


print ("Hello\tpython")


# In[2]:


print ("Hello\apython")


# In[3]:


print ("""……..@*@*
….@*……..@* …………………………@*
..@*……………@* ………………@*……..@*
.@*……………….@*……….@*……………..@*
@*…………………..@*…@*………………….@*
@*………………………*……………………..@*
.@*…………………………………………….@*
..@*………………………………………..@*
….@*…………………………………..@*
……..@*…………………………..@*
………..@*……………………@*
…………….@*…………..@*
……………….@*……@*
………………….*..@*
……………………@
……………………*
……………………@
……………………*
""")
#prints the text as it is - used for text art


# In[4]:


"""Without print used for documentation"""


# In[5]:


a = """sql statement"""


# In[6]:


print ("Python's world")


# In[5]:


print ('Python\'s world')


# In[9]:


name = "Debanjana"
marks = 90.867
age = 29
print ("The name of person is", name, ", marks is", marks, "and age is", age)


# In[15]:


print ("The name of person is %8s, marks is %10.2f and age is %10d"%(name, marks, age))


# In[17]:


print (f"The name of person is {name}, marks is {marks} and age is {age}") #For python > 3.7


# In[18]:


x = 20
id(x) #RAM address


# In[22]:


x = y = 10
x=20
id(x)


# In[23]:


id(y)


# In[25]:


y=20
id(y) #Interpreter checks memory and points y to a memory that already has a value of 20 (range of -5 to 256), if it is not present then it will allocate a fresh memory cell


# In[8]:


10 ** 3


# In[9]:


10 * 3


# In[26]:


10 / 3


# In[28]:


10 % 3


# In[10]:


10 + 3


# In[11]:


10 - 3


# In[27]:


10 // 3 #Floor division, returns floor value


# In[12]:


x = 1.5
y = 1.5
x == y


# In[13]:


a = 10
b = 20
a < b


# In[14]:


a > b


# In[15]:


a <= b


# In[16]:


a >= b


# In[17]:


a != b


# In[19]:


a = b
b


# In[21]:


a += b
a


# In[22]:


a -= b
a


# In[23]:


a *= b
a


# In[25]:


a /= b
a


# In[26]:


a **= b
a


# In[27]:


a = 10
bin(a)


# In[28]:


b = 20
bin(b)


# In[29]:


a | b


# In[30]:


bin(30)


# In[31]:


a & b


# In[33]:


a > 20 or 10 > 9


# In[35]:


a > 20 and 10 > 9


# In[37]:


a > 20 or 10 > M


# In[38]:


a > 20 and 10 > M


# In[39]:


a < 20 or 10 > M


# In[ ]:




