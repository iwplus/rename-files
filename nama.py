import pandas as pd
import numpy as np
import os
#import fnmatch

files = pd.read_csv('e:/2021/KNMIPA 2021/Koreksi Wilayah/wil16.csv') ### you can change to your desired directory

files = np.array(files)
#print(files)


for i in range(files.shape[0]):
    str1 = str(files[i,0])
    #print(str1)
    for filename in os.listdir('e:/2021/KNMIPA 2021/Koreksi Wilayah/Wilayah 16'): ### you can change to your desired directory
        if filename.startswith(str1):
            nama = 'e:/2021/KNMIPA 2021/Koreksi Wilayah/Wilayah 16/'+str(files[i,1])+'_'+files[i,2]+'_'+str1+'_U4.pdf' ### you can change according to your desired directory
            old_name = 'e:/2021/KNMIPA 2021/Koreksi Wilayah/Wilayah 16/'+ filename ### you can change according to your desired directory
            print(filename)
            print(nama)
            print('-----')
            print('')
            os.rename(old_name, nama)
            


