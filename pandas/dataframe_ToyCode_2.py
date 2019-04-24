# python 3.6
import numpy as np
import pandas as pd
import math


# Input data set
df = pd.DataFrame({'Product':['Apple','Apple','Apple','Orange','Orange','Banana','Banana'], 'Origin':['Japan','China','USA','Mexico','USA','Philippines','Malaysia'], 'Price':[10,9,8,5,4,7,7]})
df = df.sort_values(['Product', 'Price'], ascending=[True, False])
print ('Original dataset: \n', df)


# input data info
count = df.groupby(['Product']).size() # count based on 'Product'


# create new output data
df_new = pd.DataFrame(None, index=np.arange(len(df)), columns=['Product', 'Origin', 'Price_diff', 'Product_compare', 'Origin_compare'])


# loop over events
price_diff, product_diff, origin_diff = [], [], []
for i in range(len(df)):
    price_diff.append([])
    product_diff.append([])
    origin_diff.append([])
    for index, row in df.iterrows():
        price_diff[i].append( float(df.iloc[i]['Price']) - float(row['Price']) )
        product_diff[i].append( row['Product'] )
        origin_diff[i].append( row['Origin'] )


# find proper match for each event
def find_match(df, price_diff):
    out_pricediff = price_diff # modified price diff
    pricediff_min = np.zeros(len(df)) # price diff min for each event
    candidates = [] # hold indices for more comparison with conditions
    index_chosen = np.zeros(len(df)) # output chosen target indices
    # event loop
    for i in range(len(df)):
        candidates.append([])
        # list loop
        for j in range(len(df)):
            if product_diff[i][j]==df.iloc[i]['Product']:
                out_pricediff[i][j] = float("inf")
        # modify values and get min
        out_pricediff[i] = [abs(x) for x in out_pricediff[i]]
        pricediff_min[i] = min(out_pricediff[i])

        # if there is only one match
        if out_pricediff[i].count(pricediff_min[i])==1:
            index_chosen[i] = out_pricediff[i].index(pricediff_min[i])

        # if there is more than one match
        else:
            for m in range(len(df)):
                if out_pricediff[i][m]==pricediff_min[i]:
                    candidates[i].append(m)
            # find the lower price if the difference is the same
            temp_pricediff = price_diff[i][candidates[i][0]]
            for n in range(len(candidates[i])):
                if price_diff[i][candidates[i][n]] < temp_pricediff:
                    index_chosen[i] = candidates[i][n]
                else:
                    index_chosen[i] = candidates[i][0]
    return index_chosen


# target event index for each event
index_chosen = find_match(df, price_diff)
index_chosen = list(map(int, index_chosen))


# update output data
for i in range(len(df)):
    df_new.iloc[i]['Product'] = df.iloc[i]['Product']
    df_new.iloc[i]['Origin'] = df.iloc[i]['Origin']
    df_new.iloc[i]['Price_diff'] = float(df.iloc[i]['Price']) - float(df.iloc[index_chosen[i]]['Price'])
    df_new.iloc[i]['Product_compare'] = df.iloc[index_chosen[i]]['Product']
    df_new.iloc[i]['Origin_compare'] = df.iloc[index_chosen[i]]['Origin']
print ('New dataset: \n', df_new)



