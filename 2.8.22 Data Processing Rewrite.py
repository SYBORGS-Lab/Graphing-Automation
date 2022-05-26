# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 10:10:26 2022

@author: jacob
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



#The location of the excel file to be read
loc = (r'C:\Users\jacob\Desktop\Syborgs\Jithran Data\Spring 2022\1.13.22.xlsx') 

#Converts the excel file to a PANDAS dataframe (df)
df = df = pd.read_excel(loc)

#Isolates the first two rows of the dataframe to be processed for determining where to find the OD and FL reads
indices = df.iloc[:,:].to_numpy(dtype = str)

#Looks for where the Excel file starts the OD read
OdStart = np.char.find(indices[:,0], "Read 1") #Finds where the file says Read 1
OdStart = np.asarray(np.where(OdStart == 0)) #Returns the above location as an integer in an array
OdStart = OdStart[0,0] + 3 #Converts the above array into an integer value and adjusts the value to the beginning row of data

OdEnd = np.char.find(indices[OdStart:,1], "nan")
OdEnd = np.asarray(np.where(OdEnd == 0))
OdEnd = OdEnd[0,0] + OdStart - 1


#Looks for where the Excel file starts the FL read
FlStart = np.char.find(indices[:,0], "Read 2") #Finds where the file says Read 2
FlStart = np.asarray(np.where(FlStart == 0)) #Returns the above location as an integer in an array
FlStart = FlStart[0,0] + 3 #Converts the above array into an integer value and adjusts the value to the beginning row of data

FlEnd = np.char.find(indices[FlStart:,1], "nan")
FlEnd = np.asarray(np.where(FlEnd == 0))
FlEnd = FlEnd[0,0] + FlStart - 1


#Creating Indices for the Dataframes
Time = (df.iloc[OdStart:OdEnd, 1]) #Pulls out the time series
Header = (df.iloc[OdStart - 1, 3:]) #Pulls out the cell headers

Od = df.iloc[OdStart:OdEnd, 3:] #Creates the OD dataframe
Od.columns = Header #Sets the column names as the matching wells
Od.index = Time #Sets the row names as the matching time

Fl = df.iloc[FlStart:FlEnd, 3:] #Creates the FL dataframe
Fl.columns = Header #Sets the column names as the matching wells
Fl.index = Time #Sets the row names as the matching time

LetterStart = np.char.find(indices[:,0], "Layout")
LetterStart = np.asarray(np.where(LetterStart == 0))
LetterStart = LetterStart[0,0] + 3

LetterEnd = np.char.find(indices[LetterStart:,2], "nan")
LetterEnd = np.asarray(np.where(LetterEnd == 0))
LetterEnd = LetterEnd[0,0] + LetterStart

NumberEnd = np.char.find(indices[LetterStart,:], "Well ID")
NumberEnd = np.asarray(np.where(NumberEnd == 0))
NumberEnd = NumberEnd[0,0]

Layout = df.iloc[(LetterStart -1):LetterEnd, 1:NumberEnd]
Layout = np.array(Layout, dtype = str)
Layout = np.delete(Layout,np.where(Layout[:,0] == "nan"), axis = 0)
Letters = Layout[:,0]
Layout = np.delete(Layout,(0), axis = 1)


Amount = df.iloc[(LetterStart -1):LetterEnd, 1:NumberEnd]
Amount = np.array(Amount, dtype = str)
Amount = np.delete(Amount,np.where(Amount[:,0] != "nan"), axis = 0)
Amount = np.delete(Amount,(0), axis = 1)
Numbers = Amount[0,:]
Amount = np.delete(Amount,(0), axis = 0)

Labels = np.empty((len(Letters),len(Numbers)),dtype = 'U224') #U224 is the datatype needed to have both numbers and letters as a string

for i in range(int(len(Letters))):
    for j in range(int(len(Numbers))):
        Labels[i,j] = Letters[i] + Numbers[j]

Labels = np.concatenate(list(Labels))
Amount = np.concatenate(list(Amount))
Layout = np.concatenate(list(Layout))

Plate = pd.DataFrame({'Layout':Layout, 'Amount':Amount, 'Labels':Labels})
Plate.index = Labels
Plate.Amount = Plate.Amount.astype(float)
Plate.sort_values(by = ['Amount','Labels'], inplace = True)

Od = Od.transpose()
Od = Od.reindex(index=Plate.index)

Fl = Fl.transpose()
Fl = Fl.reindex(index=Plate.index)
Fl = Fl.replace(to_replace = 'OVRFLW', value = np.NaN)

FlOd = Fl/Od
GroupedOd = Od.groupby(Plate['Layout'])
GroupedFl = Fl.groupby(Plate['Layout'])
GroupedFlOd = FlOd.groupby(Plate['Layout'])

Layout = pd.unique(Plate['Layout']) #Gets unique value for list

for i in range(len(Layout)): #Rework the plotting method to account for the data issue
    #GroupedOd.get_group(Layout[i]).transpose().plot(xlabel = 'Time (HH,MM,SS)', ylabel = 'Optical Density', title = 'OD vs Time for ' + Layout[i])
    #GroupedFl.get_group(Layout[i]).transpose().plot(xlabel = 'Time (HH,MM,SS)', ylabel = 'Fluorescence', title = 'FL vs Time for ' + Layout[i])
    GroupedFlOd.get_group(Layout[i]).transpose().plot(xlabel = 'Time (HH,MM,SS)', ylabel = 'Per Cell Fluorescence', title = 'FL/OD vs Time for ' + Layout[i])


ErrorGraph = np.empty((len(Layout),2))
Average = np.empty((Plate.shape[1],1)) #values to be averaged
Amount = np.unique(Amount.astype(float))

"""
od_chosn = 0.4
    
for i in range(len(Layout)):
    OdSet = GroupedOd.get_group(Layout[i]).transpose()
    FlOdSet = GroupedFlOd.get_group(Layout[i]).transpose()
        
        
    for j in range(OdSet.shape[1]):
        index = abs(pd.to_numeric(OdSet.iloc[:,j]) - od_chosn).idxmin()
        Average[j] = FlOdSet.iloc[:,j].loc[index]
    ErrorGraph[i,0] = Average.mean()
    ErrorGraph[i,1] = Average.std()
        
plt.scatter(ErrorGraph[:,0], Amount)
xlabel = 'Log of Inducer Concentration (uM)', 
ylabel = 'Per Cell Fluorescence', 
xscale = 'log',
title = 'FL/OD vs Inducer Concentration at OD ' + str(od_chosn)  
plt.errorbar(ErrorGraph[:,0], Amount, ErrorGraph[:,1], linestyle='None', capsize=5.0)



    cont = str(input("Run Again? (Y) or (N) ")) 

    if (cont == "Y" or cont == "y" or cont == "Yes" or cont == "yes"):
        k = 0
            
    else:
        k = 1
"""      
