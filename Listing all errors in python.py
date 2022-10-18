#!/usr/bin/env python
# coding: utf-8

# In[6]:


#A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. 
import re

#dir(--builtins__) helps in producing all types of errors that we face in python
# match() function of re in Python will search the regular expression pattern and return the first occurrence.
for i in dir(__builtins__):
     if re.match(r'^[A-Z]',i):
        print(i)


# In[ ]:




