#!/usr/bin/env python
# coding: utf-8

# In[1]:


import glob
import shutil


x=8863

while x < 16897:
  
    files1 = glob.glob(r'C:\Users\source_directory/'+str(x)+'/0\*.png')

    destination1=(r'C:\Users\target_directory\0')

    for file_path in files1:
        print (file_path)
        shutil.copy(file_path, destination1)
    
    files2 = glob.glob(r'C:\Users\hp\Desktop\BREASTCANCER\DATASET\BREAST_DATA/'+str(x)+'/1\*.png')

    destination2=(r'C:\Users\hp\target_directory\1')

    for file_path in files2:
        print (file_path)
        shutil.copy(file_path, destination2)
        
    x += 1






