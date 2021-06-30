

import numpy as np
from numpy import *
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import scatter, errorbar
from PIL import Image as im
import time as tm
from time import *
from math import log10

#################### Below Here

filepathod = r'C:\Users\jacob\Desktop\Syborgs\Syborgs Coding\RM 6.30.21 OD1.csv'
filepathfl = r'C:\Users\jacob\Desktop\Syborgs\Syborgs Coding\RM 6.30.21 FL1.csv'

X_ax = [0.00, 1.00, 5.00, 10.00, 20.00, 40.00, 80.00, 160.00, 240.00, 320.00, 380.00, 480.00, 600.00, 1200.00, 2000.00, 3000.00]

#################### Above Here

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

#################### Below Here

number_of_experiments = 1
number_of_letters = 8
number_of_wells = 6
number_per_replicate = 3


#################### Above Here


replicate_array_od = np.empty((nrow,number_per_replicate), dtype = float)
replicate_array_fl = np.empty((nrow,number_per_replicate), dtype = float)
wells_array = np.empty((nrow,number_of_wells), dtype = float)
experiment_array = np.empty((nrow,number_of_letters), dtype = float)
how_many_to_go = int((number_of_letters)*(int(number_of_wells/number_per_replicate))) #bascialy a paramaterized way of saying twice as many letters... its the number of wells divided by the number of replicates times the number of letters, assuimng you have three replicates and six wells that equals two times how many letters used


columns_over_replicates = int(number_of_wells/number_per_replicate)

am_col = number_of_wells
num_let = number_of_letters
num_sec = number_per_replicate
amount_of_experiments = int((num_let) * (am_col/num_sec))

while (i != 1):
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
    
    legend = "OD" + " " + str(od_chosn) + " " + "Simple Regulation"
        
    #Where you save values to
    np.savetxt(r'C:\Users\jacob\Desktop\Syborgs\SYBORGS Coding\Values' + " " + legend + ".csv", group_X, delimiter=",")
        
    #Where you save standard devations to
    np.savetxt(r'C:\Users\jacob\Desktop\Syborgs\SYBORGS Coding\Deviation' + " " + legend + ".csv", group_Y, delimiter=",")
    
    plt.scatter(X_ax[1:], group_X[0,1:], label = legend)
    plt.xscale('log')
    plt.legend()
    #plt.ylim(0)
    plt.errorbar(X_ax[1:], group_X[0,1:], group_Y[0,1:], linestyle='None', capsize=5.0)
    plt.grid(True)
    plt.xlabel("Log of DHBA Concentration uM")
    plt.ylabel("Per Cell Fluoresence")
    plt.title("Log Per Cell Fluoresence" + " " + "vs" + " " + "IPTG Concentration uM")
    save_err = r'C:\Users\jacob\Desktop\Syborgs\Jithran Data\Graphs\10.9.20\BARS'
    suff = '\ERR'
    plt.savefig(save_err + suff + ".png")
    #Extends left of graph to account for cropping error 
    plt.gcf().subplots_adjust(left = 0.15)
    
    
    cont = str(input("Run Again? (Y) or (N) ")) 
    
    if (cont == "Y" or cont == "y" or cont == "Yes" or cont == "yes"):
        i = 0
        
    else:
        i = 1
        
plt.show()
plt.close()
