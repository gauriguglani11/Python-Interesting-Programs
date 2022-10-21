#!/usr/bin/env python
# coding: utf-8

# In[9]:


get_ipython().system('pip install pillow')


# In[10]:


from PIL import Image


# In[15]:


def Images_pdf(filename, output):
    images=[]
    
    for file in filename:
        im = Image.open(file)
        im = im.convert('RGB')
        images.append(im)
        
        images[0].save(output, save_all=True, append_images=images[1:])
        
#imagespath, output pdf
Images_pdf(["C:\\Users\\gguglani\\desktop\\gg.jpg"], "C:\\Users\\gguglani\\desktop\\output.pdf")


# In[ ]:




