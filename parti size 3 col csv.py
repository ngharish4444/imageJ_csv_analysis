# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 14:08:41 2018

@author: hari

for the particle size analysis from the csv files created from
the imagej software

"""
import os
import numpy as np
import pandas as pd
import glob

global y,x
global a,imgs_row,row_tot,mean_el
tot =int(input('Enter total number of images: '))
y=tot
imgs_row = int(input('\nEnter number of images per row: '))
row_tot = int(input('\nEnter number of rows: '))

ir = imgs_row
nam =['gr_0.79','gr_12.57','gr_38.48','gr_95.03','gr_176.71','gr_314.16','gr_490.87','gr_1452.2','gr_101787.6']



def df_creating():
    x = [i for i in range(y)]
    path =r''
    #path can also be defined but we paste it in folder
    all_files = glob.glob(os.path.join(path, "*.csv"))     # advisable to use os.path.join as this makes concatenation OS independent
    df = (pd.read_csv(f,names = 'abc',header =0) for f in all_files)
    global con_df # declaring as global variable for further usage
    con_df   = pd.concat(df, axis = 1)
    con_df = con_df.drop(['a','c'],axis=1)
    d = len(con_df)
    #print(len(con_df))
    #con_df1 = con_df
    con_df2 = con_df
    if d>=1000:
        con_df = con_df.loc[:500]
    
    con_df.columns = x
    con_df2.columns = x
    str1=os.getcwd()
    str2=str1.split('\\')
    n=len(str2)
    x=str2[n-1]
    a= (x+' step1concat.xlsx')
    #lk = (x+' concat1.xlsx')
    con_df2.to_excel(a)
    #con_df1.to_excel(lk)
    #print("\nConcat file created \n\nNow grouping particles by size")
    return con_df,x




def df_particle_group():
    global df_grouped,df_grouped2,nam
    df_grouped = pd.DataFrame()
    nam =['gr_0.79','gr_12.57','gr_38.48','gr_95.03','gr_176.71','gr_314.16','gr_490.87','gr_1452.2','gr_101787.6']
    append_data2 = []
    i=0
    z=0
    global df_con_particle,gra2
    for i in range(y):# call by col index
        gr079 = 0 #here we also intialise and empty every time the loop starts
        gr1257 = 0
        gr3848 = 0
        gr9503 = 0
        gr17671 = 0
        gr31416 = 0 #here we empty the variables again for each col
        gr49087 = 0 
        gr14522 = 0
        gr1017876= 0
        grgarb =0
        for z in range(int(len(con_df))):#call by row index
            
            u = float(con_df[i][z])
            if u<= 0.79:
                gr079+=1
            elif u<=12.57:
                gr1257+=1
            elif u<=38.48:
                gr3848+=1
            elif u<=95.03:
                gr9503+=1
            elif u<=176.71:
                gr17671+=1
            elif u<=314.16:
                gr31416+=1
            elif u<=490.87:
                gr49087+=1
            elif u<=1452.2:
                gr14522+=1
            elif u<=101787.6:
                gr1017876+=1
            
            else:
                grgarb+=1
            
            z+=1
            gra2 = pd.DataFrame([int(gr079),int(gr1257),int(gr3848),int(gr9503),int(gr17671),int(gr31416),int(gr49087),int(gr14522),int(gr1017876)])
        
        i+=1
        append_data2.append(gra2)
        df_grouped2 = pd.concat(append_data2,axis=1,ignore_index=True)
    
    
    str1=os.getcwd()
    str2=str1.split('\\')
    n=len(str2)
    x=str2[n-1]
    aa = (x+'step2group.xlsx')
    df_grouped2.to_excel(aa)
    
    #print('\nThe grouped excel file created')
    return df_grouped



def group_sort_in_order():
    zz= int(9*row_tot)
    new_index = range(zz)
    global t_df
    arr =[]
    t_df =pd.DataFrame()
    temp_df =pd.DataFrame()
    df = df_grouped2
    df1 =[]
    dfx =[]
    for e in range(row_tot):
        ind = int(((tot*e)/row_tot))
        arr.append(ind)
    global p
    p =0
    for h in range(int(len(arr))):
        p =arr[h]
        # Here we run loops to the number of times needed´in a row i.e 'ir'
        if h==0:
            for l in range(ir):
                df1.append(df[l])
                
            temp_df = pd.concat(df1,axis=1,ignore_index=True)
            df1=[]
            t_df = t_df.append(temp_df)
            
        elif h%2==0:
            for m in range(ir):
                df1.append(df[m+p])
            temp_df = pd.concat(df1,axis=1,ignore_index=True)
            df1=[]
            t_df= t_df.append(temp_df)
    
        elif h%2!=0:
            for k in range(ir):
                dfx.append(df[k+p])
                
            dfx.reverse()
            temp_df = pd.concat(dfx,axis=1,ignore_index=True)
            t_df= t_df.append(temp_df)
            dfx =[]
    t_df.index= new_index
    
    str1=os.getcwd()
    str2=str1.split('\\')
    n=len(str2)
    x=str2[n-1]
    b=(x+' step3group.xlsx')
    t_df.to_excel(b)
    
    return t_df

def print_factors(x):
   # This function takes a number and prints the factors

   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)
    
   return




def row_del():
    global mean_el,tp_df
    tp_df =t_df
    rep = input('\nDo u want to delete some images (y/n): ')
    if rep =="y":
        print('\nThe total number of rows evenly deleted both sides')
        idel =int(input('\nEnter number of rows to be deleted: '))
        nero = imgs_row-(2*idel)
        print('\nThus available row after deletion: '+str(nero))
        fac = print_factors(nero)
        print('\nFactors: '+str(fac))
        mean_an =int(input('\nEnter mean elements in a row: '))
        mean_el = mean_an
        st = int(0+idel)
        fi = int(imgs_row-idel)
        
        # we are assigning the remaining columns
        tp_df = tp_df.iloc[:,st:fi]
        #print(tp_df.columns)
        ni = range(int(nero))
        tp_df.columns = ni
    elif rep =="n":
        mean_el = int(input('\nNumber of elements to take mean in a row: '))
        
        
    
    return


def group_mean_byrow():
    jk=0
    app = []
    global df_app
    df_app = pd.DataFrame()
    t_df = tp_df
    for y in range(9):
        b=y
        if row_tot == 5:
            jk = t_df.loc[b]+t_df.loc[b+9]+t_df.loc[b+18]+t_df.loc[b+27]+t_df.loc[b+36]
        elif row_tot == 4:
            jk =t_df.loc[b]+t_df.loc[b+9]+t_df.loc[b+18]+t_df.loc[b+27]
        elif row_tot == 3:
            jk = t_df.loc[b]+t_df.loc[b+9]+t_df.loc[b+18]
        elif row_tot == 2:
            jk = t_df.loc[b]+t_df.loc[b+9]
        
        jk = jk/row_tot
        app.append(jk)
        df_app = pd.concat(app,axis=1,ignore_index=True)
        
    
    str1=os.getcwd()
    str2=str1.split('\\')
    n=len(str2)
    x=str2[n-1]
    b=(x+' step4group.xlsx')
    df_app.to_excel(b)
    
    #print('\nMean of rows file created')
    return df_app



def mean_final():
    ti = int(imgs_row/mean_el)
    tapp =[]
    tapp1=[]
    df_fin = pd.DataFrame()
    df_fin1 = pd.DataFrame()
    yy=0
    kk=0
    jj=0
    sub = mean_el-1
    #print(df_app.rolling(window=2,axis=1))
    
    for h in range(ti):
        yy= df_app.loc[kk:kk+sub].mean(axis=0)
        jj= df_app.loc[kk:kk+sub].std(axis=0)
        kk= kk+mean_el
        tapp.append(yy)
        tapp1.append(jj)
        df_fin = pd.concat(tapp,axis=1,ignore_index=True)
        df_fin1 = pd.concat(tapp1,axis=1,ignore_index=True)
    
    #df_fin = pd.concat(df_fin1,axis=1,ignore_index=True)
    #df_fin.index = nam
    ind =[]
    nam1=[]
    nam2=[]
    [ind.append(str(g))for g in range(int(len(df_fin.columns)))]
    [nam1.append(nam[g]+'_mean')for g in range(int(len(nam)))]
    [nam2.append(nam[g]+'_std')for g in range(int(len(nam)))]
    """
    for ww in range(int(len(ind))):
        ind3.append(ind1[ww])
        ind3.append(ind2[ww])
    """
    
    
    df_fin.index =nam1
    df_fin1.index =nam2
    fra = [df_fin,df_fin1]
    res =pd.concat(fra)
    print(len(ind))
    #res.columns = ind
    str1=os.getcwd()
    str2=str1.split('\\')
    n=len(str2)
    x=str2[n-1]
    b=(x+' step5final.xlsx')
    res.to_excel(b)
    
    return df_fin




        
















# Calling groups by order
print('\nStep 1:')
df_creating()
print("\nConcat file created \n\nNow grouping particles by size")


print('\nStep 2:')
df_particle_group()
print('\nThe grouped excel file created')


print('\nStep 3:')
group_sort_in_order()
print('\nThe sorted group file created')

print('\nSelection:')
row_del()

print('\nStep 4:')
group_mean_byrow()
print('\nMean of rows file created')


print('\nStep 5:')
mean_final()
print('\nFinal mean file created')


input("\nPress enter to exit")