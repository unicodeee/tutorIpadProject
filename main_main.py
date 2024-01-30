#%%

import pandas as pd
import random

folderName = r"data/ASC Individual_SP2024.xlsx"

# read by default 1st sheet of an excel file
dataframes = pd.read_excel(folderName, sheet_name=None,  header=2, nrows=14, usecols="B:F")
retired_tutors = ["Alexandra", "Arham", "Ariel", "Cheryl", "Cliff", "Frank", "Helen", "Keidy", "Khadijah", "Ha", "Huong", "Toey", "Omar"]
def conflicts(df1, df2, sheet_name1, sheet_name2):
    for index, row in df1.iterrows():
        for col in df1.columns:
            cell_value_df1 = row[col]
            cell_value_df2 = df2.loc[index, col]
            # compare cell values
            both_working = pd.notna(cell_value_df1) and pd.notna(cell_value_df2)
            both_work_at_asc_inperson_not_ET = cell_value_df1 == sheet_name1 and cell_value_df2 == sheet_name2
            if both_working and both_work_at_asc_inperson_not_ET:
                print(f'CONFLICT --> Cell ({index}, {col}) {sheet_name1} vs {sheet_name2}')
                return True
    return False

ipads = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
    10: [],
    11: [],
    12: [],
    13: [],
    14: [],
    15: []
}

MAX_IPAD = 14
MAX_TUTORS_FOR_ONE_IPAD = 5

tutors = dataframes.keys()
print(tutors)
ipad_pointer = 1 # plan to move up if ipad is full, but i'm too lazy to implement

#%%

node_list = []
from_list = []
to_list = []


AT_LEAST_ONE_TUTOR_HAS_NO_IPAD = True
while AT_LEAST_ONE_TUTOR_HAS_NO_IPAD:
    AT_LEAST_ONE_TUTOR_HAS_NO_IPAD = False

    ipads = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
        10: [],
        11: [],
        12: [],
        13: [],
        14: [],
        15: []
    }



    # This shuffling is not in-place
    # Set a fixed seed for reproducibility
    seed = random.randint(0, 2000)  # You can use any integer you like

    # Get a list of items from the dataframes dictionary
    l = list(dataframes.items())

    # Seed the random number generator
    random.seed(seed)

    # Shuffle the list using the seeded random generator
    random.shuffle(l)

    # Create a new dictionary with the shuffled items
    d_shuffled = dict(l)

    random_tutors = d_shuffled.items()



    tutors_this_sem = {key: value for key, value in dataframes.items() if (lambda k: k not in retired_tutors)(key)}

    node_list = list(tutors_this_sem.keys())

    for tutor, schedule in reversed(random_tutors):
        if tutor in retired_tutors:
            continue
        current_ipad = ipad_pointer
        while current_ipad <= MAX_IPAD:
            if len(ipads[current_ipad]) == 0:
                ipads[current_ipad].append(tutor)
                break
            elif len(ipads[current_ipad]) < MAX_TUTORS_FOR_ONE_IPAD:  #
                AVAILABLE_IPAD = True
                for already_assigned_tutor in ipads[current_ipad]:
                    df = dataframes[already_assigned_tutor]
                    if conflicts(df, schedule, already_assigned_tutor, tutor):
                        AVAILABLE_IPAD = False
                        current_ipad += 1
                        break
                    else:

                        tempt = sorted((already_assigned_tutor, tutor))
                        from_list.append(tempt[0])
                        to_list.append(tempt[1])

                if AVAILABLE_IPAD:
                    ipads[current_ipad].append(tutor)
                    break
            else:
                current_ipad += 1
            if current_ipad > MAX_IPAD:
                print(f"ipad is full for {tutor}")

    print(ipads)

    AT_LEAST_ONE_TUTOR_HAS_NO_IPAD = True

    import testNewGraph as plot

    plot.draw_graph(node_list, from_list, to_list)




    #%%

    # to make sure the tutors after IPAD assigning matches the number of tutors we have, right now we have 25 tutors
    count = 0
    for key in ipads:
        print(ipads[key])
        if (ipads[key]) != None:
            count += len(ipads[key])
    print(count)

    for tutor in dataframes.keys():
        if tutor in retired_tutors:
            continue
        NO_IPAD = True
        for small_group in ipads.values():
            if tutor in small_group:
                NO_IPAD = False
                break
        if NO_IPAD:
            AT_LEAST_ONE_TUTOR_HAS_NO_IPAD = True
            print(f"{tutor} has no ipad")
        # if tutor not in ipads.values():

    AT_LEAST_ONE_TUTOR_HAS_NO_IPAD = True


#%%

import testNewGraph as plot

plot.draw_graph(node_list, from_list, to_list)

#%% Export excel file

import numpy as np
# find the maximum length of lists in the dictionary
max_len = max(len(v) for v in ipads.values())

# fill the shorter lists with np.nan
ipads = {k: v + [np.nan] * (max_len - len(v)) for k, v in ipads.items()}


exportDataFrame = pd.DataFrame.from_dict(ipads)
exportDataFrame = exportDataFrame.T
print(exportDataFrame)
exportDataFrame.to_excel("/results/Finalize_Ipad_Assigning_Form_v2.xlsx")

# %%





