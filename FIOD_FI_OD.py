import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

replicates_to_plot = input(
    'Which replicates do you want to see? Enter in the format A1:A3 (bounds are inclusive) ')
starting_replicate, ending_replicate = replicates_to_plot.split(':')  # start and end plots to draw

excel_file_name = '030422_R1R2.xlsx'  # change this to read a different file (OD and EYFP must be separate sheets)

# read Excel file
fi_data = pd.read_excel(excel_file_name, sheet_name='EYFP')
od_data = pd.read_excel(excel_file_name, sheet_name='OD')

# desired_OD_val = float(input('What OD value would you like to analyze? '))
ODs = np.linspace(0.1, 1, 11)

# a list of all recorded times (in seconds) in the OD spreadsheet
od_times_raw = od_data['Time'].to_numpy()
od_times_raw = np.array([i.hour * 3600 + i.minute * 60 + i.second for i in od_times_raw])
fi_times_raw = fi_data['Time'].to_numpy()
fi_times_raw = np.array(
    [i.hour * 3600 + i.minute * 60 + i.second for i in
     fi_times_raw])  # convert timestamp to seconds to make math possible

# some data is incorrectly formatted such that after 24 hours, the time resets to 0 hours.
# if that is the case, ignore data beyond 24 hours
# basically, if a subsequent time stamp is smaller than the previous time stamp, then
# stop the clock at the previous time stamp value
od_times = []
for t in od_times_raw:
    if len(od_times) > 0:
        if t < od_times[-1]:  # beginning of the next day
            t += 86400
    od_times.append(t)

fi_times = []
for t in fi_times_raw:
    if len(fi_times) > 0:
        if t < fi_times[-1]:  # beginning of the next day
            t += 86400
    fi_times.append(t)

# convert to arrays to allow element-wise operations
od_times = np.array(od_times)
fi_times = np.array(fi_times)

# column labels
column_labels = fi_data.columns[
                2:]  # ignore the time column and T degree column, since they don't contain EYFP data.

fig_number = 1
num_replicates = 3  # number of replicates for each inducer condition
replicate_EYFP_over_OD_dict = {}  # list of all replicates that we want to plot
replicate_EYFP_dict = {}
replicate_OD_dict = {}

for index, column_label in enumerate(column_labels):
    # make a new figure every time the column letter changes
    col_letter = column_label[0]
    col_number = int(column_label[1:])  # number after the column letter. ex: C1 => column #1

    # skip replicates before the desired starting replicate
    if col_letter < starting_replicate[0]:
        continue
    elif col_letter == starting_replicate[0] and col_number < int(starting_replicate[1]):
        continue

    # stop after the user-specified end replicate
    if col_letter > ending_replicate[0]:
        break
    elif col_letter == ending_replicate[0] and col_number > int(ending_replicate[1]):
        break

    od_column_data = od_data[column_label].to_numpy()  # read the OD data for one column at a time
    times_and_ODs_list = [[od_times[i], od_column_data[i]] for i in
                          range(len(od_times))]  # get the OD reading at each time

    # Step 2: look up the EYFP value at each time
    EYFP_concentrations_at_times = {}

    for X in times_and_ODs_list:
        time, od = X

        # find the time in the FI spreadsheet that is closest to the time in the OD spreadsheet
        closest_time_index = (np.abs(fi_times - time)).argmin()
        EYFP_column = fi_data[column_label].to_numpy()  # read EYFP data for the desired column
        EYFP_reading_at_desired_time = EYFP_column[closest_time_index]
        EYFP_concentrations_at_times[
            time] = EYFP_reading_at_desired_time  # save the EYFP reading at the desired time for each column

    times = np.array([i[0] for i in times_and_ODs_list])
    ods = np.array([i[1] for i in times_and_ODs_list])
    eyfps = np.array(list(EYFP_concentrations_at_times.values()))

    # EYFP over od, EYFP, OD
    eyfp_over_od = eyfps / ods  # y axis
    replicate_EYFP_over_OD_dict[f'{col_letter}{col_number}'] = eyfp_over_od
    replicate_EYFP_dict[f'{col_letter}{col_number}'] = eyfps
    replicate_OD_dict[f'{col_letter}{col_number}'] = ods


    # convert seconds to hh:mm:ss
    nicer_formatted_times = []
    for t in times:
        m, s = divmod(t, 60)
        h, m = divmod(m, 60)
        nicer_formatted_times.append(f'{h:d}:{m:02d}:{s:02d}')

    if col_number % num_replicates == 0:  # make a plot after each replicate set is processed
        plt.figure(fig_number)  # make a new figure
        for column_ID, data in replicate_EYFP_over_OD_dict.items():
            plt.plot(nicer_formatted_times, data, label=f'{column_ID} EYFP/OD')  # plot data
            plt.xticks([i for i in range(len(nicer_formatted_times)) if i % 70 == 0])  # show every nth time stamp
            plt.legend()
            plt.title(f'{column_ID} EYFP/OD')
            plt.xlabel("Time")  # will need to convert column names (A7, B7, etc.) to actual numbers
            plt.ylabel("EYFP/OD")
        fig_number += 1

        plt.figure(fig_number)  # make a new figure
        for column_ID, data in replicate_EYFP_dict.items():
            plt.plot(nicer_formatted_times, data, label=f'{column_ID} EYFP')  # plot data
            plt.xticks([i for i in range(len(nicer_formatted_times)) if i % 70 == 0])  # show every nth time stamp
            plt.legend()
            plt.title(f'{column_ID} EYFP')
            plt.xlabel("Time")  # will need to convert column names (A7, B7, etc.) to actual numbers
            plt.ylabel("EYFP")
        fig_number += 1

        plt.figure(fig_number)  # make a new figure
        for column_ID, data in replicate_OD_dict.items():
            plt.plot(nicer_formatted_times, data, label=f'{column_ID} OD')  # plot data
            plt.xticks([i for i in range(len(nicer_formatted_times)) if i % 70 == 0])  # show every nth time stamp
            plt.legend()
            plt.title(f'{column_ID} OD')
            plt.xlabel("Time")  # will need to convert column names (A7, B7, etc.) to actual numbers
            plt.ylabel("OD")
        fig_number += 1  # so that the next plot shows up in a separate figure

        replicate_EYFP_over_OD_dict.clear()  # reset for a new group of replicates
        replicate_EYFP_dict.clear()
        replicate_OD_dict.clear()

plt.show()
