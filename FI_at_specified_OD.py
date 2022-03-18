import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# for each column ,find the point that's closest to a user-specified OD value (i.e. 0.4).
# every column represents a different inducer concentration
# make a plot of EYFP vs inducer concentration.

# Basically, look for the optical density reading for each column on the OD sheet that is closest to the
# desired value. Then look up the time. Then go to the FI sheet and find the EYFP reading at that time.
# Do that for every column

# read Excel file
filepath = '030422_R1R2.xlsx'
fi_data = pd.read_excel(filepath, sheet_name='EYFP')
od_data = pd.read_excel(filepath, sheet_name='OD')

# user can pick desired OD value as well as replicates to plot
desired_OD_val = float(input('What OD value would you like to analyze? '))
replicates_to_plot = input(
    'Which replicates do you want to see? Enter in the format A1:A3 (bounds are inclusive) ')
starting_replicate, ending_replicate = replicates_to_plot.split(':')  # start and end plots to draw

# a list of all recorded times in the OD spreadsheet
od_times_raw = np.array(od_data['Time'])
od_times_raw = np.array([i.hour * 3600 + i.minute * 60 + i.second for i in od_times_raw])
fi_times_raw = np.array(fi_data['Time'])
fi_times_raw = np.array(
    [i.hour * 3600 + i.minute * 60 + i.second for i in fi_times_raw])  # convert timestamp to seconds to make math possible

# some data is incorrectly formatted such that after 24 hours, the time resets to 0 hours.
# this part fixes that by adding 24 hours every time the day resets
od_times = []
for t in od_times_raw:
    if len(od_times) > 0:
        if t < od_times[-1]:  # beginning of the next day
            while t < od_times[-1]:
                t += 86400
    od_times.append(t)

fi_times = []
for t in fi_times_raw:
    if len(fi_times) > 0:
        if t < fi_times[-1]:  # beginning of the next day
            while t < fi_times[-1]:
                t += 86400
    fi_times.append(t)

# convert to arrays to allow element-wise operations
od_times = np.array(od_times)
fi_times = np.array(fi_times)

# Step 1: for each column (A-H), find the OD that is closest to the user-input OD value
OD_times_by_column = {}  # a dictionary containing the times for the OD closest to the desired OD for each column

columns = od_data.columns[2:]  # ignore the time column and the one right after that

for column in columns:
    od_column_data = np.array(od_data[column])  # read the OD data for one column at a time

    # find the OD that is closest to the user-input OD value
    closest_od_index = (np.abs(od_column_data - desired_OD_val)).argmin()
    time_for_closest_od = od_times[closest_od_index]  # look up the time at which that reading was taken
    OD_times_by_column[column] = time_for_closest_od  # save the time at which the closest OD reading was taken

# Step 2: look up the EYFP value at the time identified above for each column
EYFP_concentrations_by_column = {}
for column, time in OD_times_by_column.items():
    # find the time in the FI spreadsheet that is closest to the time in the OD spreadsheet
    closest_time_index = (np.abs(fi_times - time)).argmin()
    EYFP_column = np.array(fi_data[column])  # read EYFP data for the desired column
    EYFP_reading_at_desired_time = EYFP_column[closest_time_index]
    EYFP_concentrations_by_column[
        column] = EYFP_reading_at_desired_time  # save the EYFP reading at the desired time for each column

num_replicates = 3  # the number of replicates in a set of replicates (determines when to make a new plot)
fig_number = 1  # this helps to draw new figures for each set of replicates
column_name_and_EYFP_dict = {}  # contains the replicates that we want to plot; resets after the plot is made

# make the plots
for column_name, eyfp_concentration in EYFP_concentrations_by_column.items():
    # make a new figure for each set of replicates
    col_letter = column_name[0]
    col_number = int(column_name[1:])  # number after the column letter. ex: C1 => column #1

    # skip replicates before the desired starting replicate
    if col_letter < starting_replicate[0]:
        continue
    elif col_letter == starting_replicate[0] and col_number < int(starting_replicate[1:]):
        continue

    # stop after the user-specified end replicate
    if col_letter > ending_replicate[0]:
        break
    elif col_letter == ending_replicate[0] and col_number > int(ending_replicate[1:]):
        break

    column_name_and_EYFP_dict[column_name] = eyfp_concentration
    if col_number % num_replicates == 0:  # make a plot after each replicate set is processed
        col_names = list(column_name_and_EYFP_dict.keys())
        eyfp = list(column_name_and_EYFP_dict.values())
        plt.figure(fig_number)  # create the figure
        plt.bar(col_names, eyfp)  # draw the bar plot
        plt.title("EYFP for Columns {}:{}\n(OD = {})".format(f'{col_letter}{col_number - num_replicates + 1}',
                                                            f'{col_letter}{col_number}', desired_OD_val))
        plt.xlabel("Column Name")  # will need to convert column names (A7, B7, etc.) to actual numbers
        plt.ylabel("EYFP Value")
        column_name_and_EYFP_dict.clear()  # reset for the next group of replicates
        fig_number += 1  # make a new figure for the next replicate set

plt.show()
