

import pandas as pd




folderName = r"C:/Users/Thang/Desktop/Tutor/Tutor spring 2023/csv converted/"
# folderName = r"data\ASC Individual_FA23_0815.xlsx"

tutorName = r"Individual_SP23_finalized - Thang.csv"

import os

for file in os.listdir(r"C:/Users/Thang/Desktop/Tutor/Tutor spring 2023/csv converted"):
    if not file.startswith("~") and file.endswith(".xlsx"):
        print(file)


path = folderName + tutorName
# read by default 1st sheet of an excel file
dataframe1 = pd.read_csv(path, header=2, index_col=None)

print(dataframe1)



# read by default 1st sheet of an excel file
dataframe2 = pd.read_csv(path)
dataframe2.columns = dataframe2[2]
print(dataframe2)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# import openpyxl
#
# # Define variable to load the dataframe
# dataframe = openpyxl.load_workbook(path)
#
# # Define variable to read sheet
# dataframe1 = dataframe.active
#
# # Iterate the loop to read the cell values
# for row in range(0, dataframe1.max_row):
#     for col in dataframe1.iter_cols(1, dataframe1.max_column):
#         print(col[row].value)





