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



tutors = dataframes.keys()


#%%

tutors_this_sem = {key: value for key, value in dataframes.items() if (lambda k: k not in retired_tutors)(key)}
each_tutor_with_schedule_object = list(tutors_this_sem.items())

from_list = []
to_list = []
node_list = list(tutors_this_sem.keys())

#%%
# Iterate through each person
pairs_set = set()
pairs = set()
for i in range(len(each_tutor_with_schedule_object)):
    tutor, schedule = each_tutor_with_schedule_object[i]

    for j in range(i + 1, len(each_tutor_with_schedule_object)):
        another_tutor, another_schedule = each_tutor_with_schedule_object[j]

        if tutor == 'Mariem Cherif' and another_tutor == 'Thang' or tutor == 'Thang' and another_tutor == 'Mariem Cherif':
            print('hello')

        if not conflicts(schedule, another_schedule, tutor, another_tutor):
            # tempt = tuple(([tutor, another_tutor]))
            # pairs_set.add(tempt)

            from_list.append(tutor)
            to_list.append(another_tutor)

            # from_list.append(another_tutor)
            # to_list.append(tutor)

# pairs = tuple(pairs_set)
# for pair in pairs:
#     from_list.append(pair[0])
#     to_list.append(pair[1])

import testNewGraph as plot
# a = from_list.copy()
# a.extend(to_list)
# b = to_list.copy()
# b.extend(from_list)
# node_list = ['Thang', 'Mariem Cherif']
# from_list = ['Thang', 'Mariem Cherif']
# to_list = ['Mariem Cherif', 'Thang']
plot.draw_graph(node_list, from_list, to_list)






