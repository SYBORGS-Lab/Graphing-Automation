

import numpy as np
from numpy import mean, append, concatenate, empty, stack, zeros, std
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import scatter, errorbar
from PIL import Image as im
import time as tm
from time import *
from math import log10

filepathod = r'C:\Users\jacob\Desktop\Syborgs\Jithran Data\11.23.20 NAL pAJM.337 - OD2.csv'
filepathfl = r'C:\Users\jacob\Desktop\Syborgs\Jithran Data\11.23.20 NAL pAJM.337 - FL2.csv'

np.seterr(divide='ignore', invalid='ignore')

file_1 = np.genfromtxt(filepathod, 
                          delimiter=',', dtype=str)

top_1 = file_1[0,:].tolist()
omit_1_0 = file_1[1:,:]
pre_time = omit_1_0[:,0]
float_array_1 = omit_1_0[:,2:]
array_od =  float_array_1.astype(np.float)
ncol = float_array_1.shape[1]
nrow = float_array_1.shape[0]
time = np.empty((nrow,1))
usable_names = top_1[2:]

file_2 = np.genfromtxt(filepathfl, 
                          delimiter=',', dtype=str, skip_header=1)

top_2 = file_2[0,:].tolist()
omit_2_0 = file_2[0:,:]
float_array_2 = omit_2_0[:,2:]
array_fl =  float_array_2.astype(np.float)

i = 0
for i in range(nrow):
    
    split_up = (pre_time[i]).split(":")
    hr = float(split_up[0])
    mn = float(split_up[1])
    sc = float(split_up[2])
    time_as_float =  float((hr*60) + (mn))
    time[i] = time_as_float

"""
number_of_experiments = int(input("How many experiments does this dataset contain?: ")) 
number_of_letters = int(input("How many letters are used in this experiment?: ")) 
number_of_wells = int(input("How many wells are there per letter in each experiment?: ")) 
number_per_replicate = int(input("How many wells are there per replicate?: ")) 
"""

number_of_experiments = 1
number_of_letters = 8
number_of_wells = 12
number_per_replicate = 3

replicate_array_od = np.empty((nrow,number_per_replicate), dtype = float)
replicate_array_fl = np.empty((nrow,number_per_replicate), dtype = float)
wells_array = np.empty((nrow,number_of_wells), dtype = float)
experiment_array = np.empty((nrow,number_of_letters), dtype = float)
how_many_to_go = int((number_of_letters)*(int(number_of_wells/number_per_replicate))) #bascialy a paramaterized way of saying twice as many letters... its the number of wells divided by the number of replicates times the number of letters, assuimng you have three replicates and six wells that equals two times how many letters used


i = 0
j = 0      
for i in range(int(number_per_replicate)):
    for j in range(int(how_many_to_go)):
        index_value = ((int(number_per_replicate)*j)+i)
        val = array_od[:,index_value]
        plt.plot(time,val, label = str(usable_names[index_value]))
    label = str(int(i+1))
    plt.title("OD" +  " " + "Replicates" + ":" + label + " vs " + "Time(min)")
    plt.ylabel("OD")
    plt.xlabel("Time (min)")
    #plt.legend()
    save_od= r'C:\Users\jacob\Desktop\Syborgs\Jithran Data\Graphs\10.9.20\OD'
    suff = '\OD'
    plt.savefig(save_od + suff + " " + "Replicate" + " " + label)
    plt.show()
    plt.close()     


i = 0
j = 0      
for i in range(int(number_per_replicate)):
    for j in range(int(how_many_to_go)):
        index_value = ((int(number_per_replicate)*j)+i)
        val = array_fl[:,index_value]
        plt.plot(time,val, label = str(usable_names[index_value]))
    label = str(int(i+1))
    plt.title("FL" +  " " + "Replicates" + ":" + label + " vs " + "Time(min)")
    plt.ylabel("FL")
    plt.xlabel("Time (min)")
    #plt.legend()
    save_od= r'C:\Users\jacob\Desktop\Syborgs\Jithran Data\Graphs\10.9.20\FL'
    suff = '\FL'
    plt.savefig(save_od + suff + " " + "Replicate" + " " + label)
    plt.show()
    plt.close()



columns_over_replicates = int(number_of_wells/number_per_replicate)

am_col = number_of_wells
num_let = number_of_letters
num_sec = number_per_replicate
amount_of_experiments = int((num_let) * (am_col/num_sec))

od_chosn = float(input("What OD value would you like to analyze?: ")) 
    
gr_ncol = array_od.shape[1]
gr_nrow = array_od.shape[0]

rep = int(gr_ncol/num_sec)
amount_per_letter = int(am_col/number_per_replicate)
broken_up = int(number_per_replicate*number_of_letters)

group = []
group = np.empty((gr_nrow,gr_ncol))
group_1 = []
group_1 = np.empty((gr_nrow,gr_ncol))

od_parsed = []
od_parsed = np.empty((gr_nrow,broken_up,amount_per_letter))
fl_parsed = []
fl_parsed = np.empty((gr_nrow,broken_up,amount_per_letter))


i = 0
j = 0
for i in range(amount_per_letter):
    what_number = (i * number_per_replicate)
    for j in range(number_of_letters):
        index_value_1 = int(what_number + number_of_wells * j)
        index_value_2 = int(index_value_1 + 1)
        index_value_3 = int(index_value_2 + 1)
        parsed_index_value_1 = int(j * number_per_replicate)
        parsed_index_value_2 = (parsed_index_value_1 + 1)
        parsed_index_value_3 = (parsed_index_value_1 + 2)
        od_parsed[:,(parsed_index_value_1,parsed_index_value_2,parsed_index_value_3),i] = array_od[:,(index_value_1,index_value_2,index_value_3)]
        fl_parsed[:,(parsed_index_value_1,parsed_index_value_2,parsed_index_value_3),i] = array_fl[:,(index_value_1,index_value_2,index_value_3)]
        j = 0

i = 0
for i in range(amount_per_letter):
    index_value_1 = int(broken_up * i)
    index_value_2 = int(index_value_1 + (broken_up))
    group[:,index_value_1:index_value_2] = od_parsed[:,:,i]
    group_1[:,index_value_1:index_value_2] = fl_parsed[:,:,i]
    
    
group_3 = []
group_3 = np.empty((1,rep))
group_5 = []
group_5 = np.empty((1,rep))
group_6 = []
group_6 = np.empty((1,int(number_per_replicate),2))
group_Y = []
group_Y = np.empty((1,int(amount_of_experiments)))

a = 0
l = 0
z = 0

for a in range(nrow):
    for l in range(rep):
        index_value_1 = int(number_per_replicate * l)
        index_value_2 = int(index_value_1 + 1)
        index_value_3 = int(index_value_2 + 1)
        group_2 = group[:,(index_value_1, index_value_2, index_value_3)]
        group_4 = group_1[:,(index_value_1, index_value_2, index_value_3)]
        
        z = 0
        1
        for z in range(number_per_replicate):
            od_clost = (np.abs(group_2[:,z] - od_chosn)).argmin()
            group_6[0,z,0] = group_2[int(od_clost),z]
            group_6[0,z,1] = group_4[int(od_clost),z]
            if (np.mean(group_2[range(0,9),z]) > int(od_chosn)):
                np.delete(group_6,[0,z,0])
                np.delete(group_6,[0,z,1])
                
                
        group_3[0,l] = np.mean(group_6[0,z,0])
        group_5[0,l] = np.mean(group_6[0,z,1])
        data = (group_6[0,:,1]/group_6[0,:,0])
        group_Y[0,l] = np.std(data)
        
    l = 0
       
group_X = group_5/group_3


X_ax = [0,1,2.5,5,7.5,10,12.5,15,17.5,20,25,35,50,65,80,100,150,200,250,300,350,400,450,500,600,700,800,900,1000,1500,2000,2500]  


 
plt.scatter(X_ax, group_X)
plt.errorbar(X_ax, group_X[0,:], group_Y[0,:],linestyle='None', capsize=5.0)
plt.xlabel("IPTG Concentration uM")
plt.ylabel("Per Cell Fluoresence")
plt.title("Per Cell Fluoresence" + " " + "vs" + " " + "IPTG Concentration uM")
save_err = r'C:\Users\jacob\Desktop\Syborgs\Jithran Data\Graphs\10.9.20\BARS'
suff = '\ERR'
plt.savefig(save_err + suff)
plt.show()
plt.close()     

"""
L_X_ax = []

for z in range(len(X_ax)-1):
    L_X_ax.append(log10(X_ax[z+1]))
"""



plt.scatter(X_ax[1:], group_X[0,1:])
plt.xscale('log')
plt.errorbar(X_ax[1:], group_X[0,1:], group_Y[0,1:], linestyle='None', capsize=5.0)
plt.grid(True)
plt.xlabel("Log of IPTG Concentration uM")
plt.ylabel("Per Cell Fluoresence")
plt.title("Log Per Cell Fluoresence" + " " + "vs" + " " + "IPTG Concentration uM")
save_err = r'C:\Users\jacob\Desktop\Syborgs\Jithran Data\Graphs\10.9.20\BARS'
suff = '\ERR'
plt.savefig(save_err + suff)
plt.show()
plt.close()     