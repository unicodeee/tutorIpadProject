import random

import pandas as pd


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
    strippedSheetName = sheet_name.replace(" ", "").replace("-", "")
    # strippedSheetName = sheet_name
    exec(f"{strippedSheetName} = df")   # store table to variable with same tutor's name
    tutors.append(strippedSheetName)    # create list of tutors' name

print(len(tutors))
print(tutors)

#Abood




def conflict_by_day(dayOfTheWeek, tutor1, tutor2):
    conflicted = False
    conflictColumn = []
    for timeBlock1, timeBlock2 in zip(eval(tutor1)[dayOfTheWeek].notna(), eval(tutor2)[dayOfTheWeek].notna()):
        try:
            if timeBlock1 and timeBlock2:
                conflicted = True
            conflictColumn.append(timeBlock1 and timeBlock2)
        except Exception as e:
            # conflictColumn.append(False)  File "C:\Coding\tutorIpadProject\test1.py", line 57, in conflict_by_day
            pass
    return conflicted

def check_conflict_by_week(tutor1, tutor2):
    listOfConflicts = {}
    for day in eval(tutor1).drop(columns=["Time"]):
        if conflict_by_day(day, tutor1, tutor2):
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
count = 0

goodPairs = []
# check pair conflict
for i, item1 in enumerate(tutors):
    for j, item2 in enumerate(tutors):
        if i < j:
            # process item1 and item2

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
                print(item1, item2)

                count += 1
            # print(hasNoConflict(item1, item2))
print("Good pairs: \n", listOfGoodPairs)
print(len(listOfGoodPairs))
print("count ", count)
tupleTriplets = ()
# ______________________________________________________________________

IPAD_LIST = {}


def assign_ipad(ipad_list, names, ipad_number):

    firstTutor = names[0]
    ipad_list[firstTutor] =  ipad_number

    namesWithThoutTutor1 = [name for name in names if name != firstTutor]

    for secondTutor in namesWithThoutTutor1 :
        if [firstTutor , secondTutor] in goodPairs:
            ipad_list[secondTutor] = ipad_number
            namesWithThoutBoth = [name for name in namesWithThoutTutor1 if name != secondTutor]
            if len(namesWithThoutBoth) != 0: assign_ipad(ipad_list, namesWithThoutBoth, ipad_number + 1)

assign_ipad(IPAD_LIST, tutors, 1)

print("please work: ", IPAD_LIST)

# ______________________________________________________________________
for mainTutor, subTutors in listOfGoodPairs.items():
    # print(mainTutor, subTutors)

    for i in range(len(subTutors)):
        # print(subTutors[i])
        secondTutor = subTutors[i]
        for thirdTutor in subTutors[i+1:]:
            if secondTutor in listOfGoodPairs.keys() and thirdTutor in listOfGoodPairs[secondTutor]:
                triplets = (mainTutor, secondTutor, thirdTutor)
                # tupleTriplets = list(tupleTriplets).append(triplets)
                tupleTriplets = (*tupleTriplets, triplets)

                # print(triplets)





# 'Arham', 'Ha', 'Huong'

hasNoConflict('Arham', 'Ha')
hasNoConflict('Ha', 'Huong')
hasNoConflict('Arham', 'Huong')

print(check_conflict_by_week('Dorsa', 'Ethan'))
print(check_conflict_by_week('Ethan', 'Suong'))
print(check_conflict_by_week('Dorsa', 'Suong'))


print(tupleTriplets)
print(len(tupleTriplets))

hasNoConflict('Dorsa', 'Ethan')
hasNoConflict('Ethan', 'Suong')
hasNoConflict('Dorsa', 'Suong')


print(check_conflict_by_week('Dorsa', 'Ethan'))
print(check_conflict_by_week('Ethan', 'Suong'))
print(check_conflict_by_week('Dorsa', 'Suong'))


maxIpad = []

finalAnswers = []

# pick each triplet first
for i in range(len(tupleTriplets)):
    newlisttupleTriplets = list(tupleTriplets)
    ipadList = []

    # ranNumber = random.randint(0, len(newlisttupleTriplets) - 1)

    ipadList.append(newlisttupleTriplets[i])
    namesInIpadList = [name for row in ipadList for name in row]

    while len(newlisttupleTriplets) != 0:
        for name in namesInIpadList:
            for three in newlisttupleTriplets:
                if name in three:
                    newlisttupleTriplets.remove(three)
        if len(newlisttupleTriplets) != 0:
            ipadList.append(newlisttupleTriplets[0])
            namesInIpadList = [name for row in ipadList for name in row]

    # maxIpad.append(len(ipadList))

    finalAnswers.append([len(ipadList), ipadList])

# print(maxIpad.sort(reverse=True))
# finalAnswers.sort([0][0], reverse=True)
# print(sorted(finalAnswers, key=lambda x: (x[0]))


bunXao = sorted(finalAnswers,key=lambda x: (x[0]), reverse=True)

# for ocXao in bunXao:
#     print(ocXao)


# print(sorted(finalAnswers,key=lambda x: (x[0]), reverse=True))

# for item in finalAnswers:
#     print(finalAnswers)




