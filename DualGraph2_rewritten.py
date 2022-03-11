import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
        if t < od_times[-1]:
            break
    od_times.append(t)

fi_times = []
for t in fi_times_raw:
    if len(fi_times) > 0:
        if t < fi_times[-1]:
            break
    fi_times.append(t)

# convert to arrays to allow element-wise operations
od_times = np.array(od_times)
fi_times = np.array(fi_times)

# column labels
column_labels = fi_data.columns[
                2:]  # ignore the time column and T degree column, since they don't contain EYFP data.

letters = set()  # make a new plot for each column letter, just so that the figure isn't too crowded
for col_number, column_label in enumerate(column_labels):
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
    eyfp_over_od = eyfps / ods  # y axis

    # make a new figure every time the column letter changes
    col_letter = column_label[0]
    if col_letter not in letters:
        letters.add(col_letter)  # use this to keep track of when to make a new figure for plotting
        plt.figure(len(letters))

    plt.title("EYFP/OD vs Time, {} columns".format(col_letter))
    plt.xlabel("Time")  # will need to convert column names (A7, B7, etc.) to actual numbers
    plt.ylabel("EYFP/OD")

    # convert seconds to hh:mm:ss
    nicer_formatted_times = []
    for t in times:
        m, s = divmod(t, 60)
        h, m = divmod(m, 60)
        nicer_formatted_times.append(f'{h:d}:{m:02d}:{s:02d}')

    plt.plot(nicer_formatted_times, eyfp_over_od, label=column_label)  # plot data
    plt.xticks([i for i in range(len(nicer_formatted_times)) if i % 50 == 0])  # show every 50th time stamp
    plt.legend()

plt.show()
