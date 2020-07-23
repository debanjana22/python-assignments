#!/usr/bin/env python
# coding: utf-8

# In[9]:


str1="what we think we become; we are Python programmer"
searchStr="we"

countOfSearchStr = str1.count(searchStr)
lengthOfSearchStr = len(searchStr)
#print(countOfSearchStr)
counter = 0
while (counter < countOfSearchStr):
    print (str1)
    index = str1.find(searchStr)
    print (f"Index of occurence {counter}: {index}")
    counter += 1
    str1 = str1[index+lengthOfSearchStr:]


# In[ ]:




