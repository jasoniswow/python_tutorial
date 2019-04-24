# python 3.6
import numpy as np
import pandas as pd
import math


# calculate the combinations
def combinations(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)


# get subsets with 2 elements
def subsets(list1):
    sublist, sub = [], []
    # first element index
    for i in range(len(list1)):
        # second element index 
        for j in range(1,len(list1),1):
            if (i+j)<len(list1):
                sub = [ list1[m] for m in [i,i+j] ]
                sublist.append(sub)
    return sublist


# Input data set
df = pd.DataFrame({'Product':['Apple','Apple','Apple','Orange','Orange','Banana','Banana'], 'Origin':['Japan','China','USA','Mexico','USA','Philippines','Malaysia'], 'Price':[10,9,8,5,4,7,7]})
df = df.sort_values(['Product', 'Price'], ascending=[True, False]) # make sure Origin1 > Origin2
print ('Original dataset: \n', df)


# prepare values
count = df.groupby(['Product']).size() # count column based on 'Product'
#print (count)
total_rows_new = 0 # total rows in output
for i in range(len(count)):
    total_rows_new += combinations(count.values[i],2)
total_rows_new = int(total_rows_new)
#print (total_rows_new)


# create new dictionary to hold differences (one can also use dataframe)
cols_new = ['Product', 'Origin1', 'Origin2', 'Difference']
vals_new = [ [0 for i in range(total_rows_new)] for j in range(4) ]
dict_new = dict(zip(cols_new, vals_new))
#print (dict_new)


# fill new dictionaty with differences
ilist = [] # hold indices for one Product
iilist = [] # hold combinations of indices 
product_new, origin1_new, origin2_new, difference_new = [], [], [], [] # hold new values
num_ = 0 # loop count
for key, value in count.items():
    for index, row in df.iterrows():
        if row['Product']==key:
            ilist.append(index)
    iilist = subsets(ilist)
    if len(iilist)==combinations(count.values[num_],2): # cross check
        for i in range(len(iilist)):
            product_new.append(key)
            origin1_new.append(df.iloc[iilist[i][0]]['Origin'])
            origin2_new.append(df.iloc[iilist[i][1]]['Origin'])
            difference_new.append(abs(float(df.iloc[iilist[i][0]]['Price'])-float(df.iloc[iilist[i][1]]['Price'])))
    ilist, iilist = [], []
    num_ = num_ + 1


# update dictionary and output new data
dict_new['Product'] = product_new
dict_new['Origin1'] = origin1_new
dict_new['Origin2'] = origin2_new
dict_new['Difference'] = difference_new
df_new = pd.DataFrame.from_dict(dict_new)
print ('New dataset: \n', df_new)






