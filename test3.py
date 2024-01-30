import random

import pandas as pd


# folderName = r"C:/Users/Thang/Desktop/Tutor/Tutor spring 2023/Individual_SP23_finalized.xlsx"
folderName = r"data\ASC Individual_FA23_0815.xlsx"
# tutorName = r"Individual_SP23_finalized - Thang.csv"

headerRow = 2

path = folderName
# read by default 1st sheet of an excel file
dataframe1 = pd.read_excel(path, sheet_name="Thang", header=headerRow, index_col=None)

# print(dataframe1)

column = dataframe1.drop(columns=['Time'])
# print(column)
#
#
# timeColumn = dataframe1['Time']
# print(timeColumn)

mondayColumn = dataframe1['Monday']
notna_monday = mondayColumn.notna()

# add column
column["new Monday"] = notna_monday

# print(dataframe1[]  notna_monday)
# print(column)





dataframe2 = pd.read_excel(path, sheet_name=None, header=headerRow, index_col=None, nrows=14)
tutors = []


for sheet_name, df in dataframe2.items():
    strippedSheetName = sheet_name.replace(" ", "")
    exec(f"{strippedSheetName} = df")   # store table to variable with same tutor's name, each varibale is a dataFrame obj
    tutors.append(strippedSheetName)    # create list of tutors' name



print(len(tutors))
print(tutors)

#Abood




def check_conflict_by_day(dayOfTheWeek, tutor1, tutor2):
    conflicted = False
    conflictColumn = []
    for timeBlock1, timeBlock2 in zip( eval(tutor1)[dayOfTheWeek].notna() , eval(tutor2)[dayOfTheWeek].notna()):
        if timeBlock1 and timeBlock2:
            conflicted = True
        conflictColumn.append(timeBlock1 and timeBlock2)
    return conflicted

def check_conflict_by_week(tutor1, tutor2):
    listOfConflicts = {}
    for day in eval(tutor1).drop(columns=["Time"]):
        if check_conflict_by_day(day, tutor1, tutor2):
            listOfConflicts[day] = "conflicted"
    return listOfConflicts

def hasNoConflict(tutor1, tutor2):
    listOfConflicts = check_conflict_by_week(tutor1, tutor2)
    if len(listOfConflicts) == 0:
        print(True)
        return True
    else:
        print(listOfConflicts)
        return listOfConflicts

# check_conflict_by_week("Abood", "Maryam")

# print(hasNoConflict("Abood", "Maryam"))

# for sheet_name, df in Thang.drop(columns=["Time"]).items():
#     print("kaka ", sheet_name)
#     # print("Items", dataframe1.items())




listOfGoodPairs = {}
goodPairs = []
# find pairs not conflict
for i, item1 in enumerate(tutors):
    for j, item2 in enumerate(tutors):
        if i < j:

            # if hasNoConflict(item1, item2):
            #     print(item1, "  ", item2)
            listConflicts = check_conflict_by_week(item1, item2)

            # bad pairs
            # if len(listConflicts) != 0:
            #     print(item1, item2, listConflicts.keys())

            # good pairs
            if len(listConflicts) == 0:
                # listOfGoodPairs[item1].append(item2)

                # listOfGoodPairs.setdefault(item1, []).append(item2)
                goodPairs.append([item1, item2])
                # print(item1, item2)

            # print(hasNoConflict(item1, item2))
print("Good pairs: \n", listOfGoodPairs)
print(len(listOfGoodPairs))

# ______________________________________________________________________

IPAD_ASSIGNMENT_LIST = {}


# assign ipad for the first guy, find the second guy to assign.
# if found second guy  --> then move on to next tutors without BOTH of these 2 that just have been assigned
# if not then assign first guy, then move on to next tutors without this one that just have been assigned
# break when the list is filled, means everybody has an ipad assigned to them

def assign_ipad(ipad_list, names, ipad_number, maxTutors):
    if len(ipad_list) == maxTutors:
        return 0
    count = 1
    firstTutor = names[0]
    ipad_list[firstTutor] =  ipad_number
    namesWithThoutTutor1 = [name for name in names if name != firstTutor]

    for secondTutor in namesWithThoutTutor1 :
        if [firstTutor , secondTutor] in goodPairs and count > 0:
            ipad_list[secondTutor] = ipad_number
            count -= 1
            namesWithThoutBoth = [name for name in namesWithThoutTutor1 if name != secondTutor]
            assign_ipad(ipad_list, namesWithThoutBoth, ipad_number + 1, maxTutors)
    assign_ipad(ipad_list, namesWithThoutTutor1, ipad_number + 1, maxTutors)


assign_ipad(IPAD_ASSIGNMENT_LIST, tutors, 1, len(tutors))

IPAD_ASSIGNMENT_LIST_SORTED = dict(sorted(IPAD_ASSIGNMENT_LIST.items(), key=lambda x: (x[1])))

print("please work: ", IPAD_ASSIGNMENT_LIST_SORTED)



# unit test
print(check_conflict_by_week('Abood', 'Huong'))
print(check_conflict_by_week('Afifah', 'Dorsa'))
print(check_conflict_by_week('Alexandra', 'Isaac'))
print(check_conflict_by_week('Arham', 'Elena'))
print(check_conflict_by_week('Ariel', 'Ethan'))

print(check_conflict_by_week('Cheryl', 'Helen'))
print(check_conflict_by_week('Cliff', 'Fransia'))
print(check_conflict_by_week('Danna', 'Keidy'))
print(check_conflict_by_week('Frank', 'MariemC'))
print(check_conflict_by_week('Ha', 'Khadijah'))

print(check_conflict_by_week('Maryam', 'Shreyan'))
print(check_conflict_by_week('Saja', 'Tram'))


# ______________________________________________________________________
# unit test
print(hasNoConflict('Abood', 'Huong'))
print(hasNoConflict('Afifah', 'Dorsa'))
print(hasNoConflict('Alexandra', 'Isaac'))
print(hasNoConflict('Arham', 'Elena'))
print(hasNoConflict('Ariel', 'Ethan'))

print(hasNoConflict('Cheryl', 'Helen'))
print(hasNoConflict('Cliff', 'Fransia'))
print(hasNoConflict('Danna', 'Keidy'))
print(hasNoConflict('Frank', 'MariemC'))
print(hasNoConflict('Ha', 'Khadijah'))

print(hasNoConflict('Maryam', 'Shreyan'))
print(hasNoConflict('Saja', 'Tram'))

exportDataFrame = pd.DataFrame(data=IPAD_ASSIGNMENT_LIST_SORTED, index=[0])
exportDataFrame = exportDataFrame.T
print(exportDataFrame)
exportDataFrame.to_excel("Finalize_Ipad_Assigning_Form.xlsx")