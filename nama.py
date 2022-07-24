# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 07:32:49 2021

@author: LENOVO
"""
import pandas as pd
import numpy as np
import os
#import fnmatch

files = pd.read_csv('e:/2021/KNMIPA 2021/Koreksi Wilayah/wil16.csv')

files = np.array(files)
#print(files)


for i in range(files.shape[0]):
    str1 = str(files[i,0])
    #print(str1)
    for filename in os.listdir('e:/2021/KNMIPA 2021/Koreksi Wilayah/Wilayah 16'):
        if filename.startswith(str1):
            nama = 'e:/2021/KNMIPA 2021/Koreksi Wilayah/Wilayah 16/'+str(files[i,1])+'_'+files[i,2]+'_'+str1+'_U4.pdf'
            old_name = 'e:/2021/KNMIPA 2021/Koreksi Wilayah/Wilayah 16/'+ filename
            print(filename)
            print(nama)
            print('-----')
            print('')
            os.rename(old_name, nama)
            


