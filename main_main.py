#%%

import pandas as pd
import random

folderName = r"data/ASC Individual_SP2024.xlsx"

# read by default 1st sheet of an excel file
dataframes = pd.read_excel(folderName, sheet_name=None,  header=2, nrows=14, usecols="B:F")
# dataframe2 = pd.read_excel(folderName, header=2, index_col=None, nrows=14, usecols="A:F")
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

tutors = dataframes.keys()
print(tutors)
ipad_pointer = 1 # plan to move up if ipad is full, but i'm too lazy to implement

MAX_TUTORS_FOR_ONE_IPAD = 5

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
        14: []
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

    # random_tutors = dataframes.items()
    # random.seed(random.randint(0, 200))
    # random_tutors = dataframes.items()
    # random.shuffle(dataframes.items())



    for tutor, dataframe in reversed(random_tutors):
        if tutor in retired_tutors:
            continue
        current_ipad = ipad_pointer
        while current_ipad <= MAX_IPAD:
            if len(ipads[current_ipad]) == 0:
                ipads[current_ipad].append(tutor)
                break
            elif len(ipads[current_ipad]) < MAX_TUTORS_FOR_ONE_IPAD:  #
                AVAILABLE_IPAD = True
                for t in ipads[current_ipad]:
                    df = dataframes[t]
                    if conflicts(df, dataframe, t, tutor):
                        AVAILABLE_IPAD = False
                        current_ipad += 1
                        break
                if AVAILABLE_IPAD:
                    ipads[current_ipad].append(tutor)
                    break
            else:
                current_ipad += 1
            if current_ipad > MAX_IPAD:
                print(f"ipad is full for {tutor}")

    print(ipads)
    # for sheet_name, dataframe in dataframes.items():
    #     # dataframe.drop(columns=["Time"])
    #     if sheet_name == "Arham" or sheet_name == "Thang":
    #         print(sheet_name)
    #         print(dataframe)
    #


    # print("________________________________________________________________________________________")
    #
    # # for testing
    # sheet_name1 = "Suong"
    # sheet_name2 = "Preston"
    #
    #
    # df1 = dataframes[sheet_name1]
    # df2 = dataframes[sheet_name2]
    # print(dataframes[sheet_name1])
    # print(dataframes[sheet_name2])
    #
    # print(f"{sheet_name1} vs {sheet_name2}is conflict: ", conflicts(df1, df2, sheet_name1, sheet_name2))
    # print("_____________________________________________________________________________________________________")



    # exportDataFrame = pd.DataFrame.from_dict(ipads, orient='index')
    # exportDataFrame = exportDataFrame.T
    # print(exportDataFrame)
    # exportDataFrame.to_excel("Finalize_Ipad_Assigning_Form_v2.xlsx")

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



#%% Export excel file

import numpy as np
# find the maximum length of lists in the dictionary
max_len = max(len(v) for v in ipads.values())

# fill the shorter lists with np.nan
ipads = {k: v + [np.nan] * (max_len - len(v)) for k, v in ipads.items()}


exportDataFrame = pd.DataFrame.from_dict(ipads)
exportDataFrame = exportDataFrame.T
print(exportDataFrame)
exportDataFrame.to_excel("Finalize_Ipad_Assigning_Form_v2.xlsx")



