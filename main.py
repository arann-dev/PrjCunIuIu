import pandas
import pandas as pd

import openpyxl

path = 'data/T6 K11.xlsx'
path_out= 'data/Book2.xlsx'
df = pd.read_excel(path)

def check_class(num):
    for x in range(1, num):
        name = 'Period ' + str(x) + "/Tiết " + str(x)
        nan = df[df[name].isnull()]
        listnan = list(nan.index)
        for i in listnan:
            df['Tiết Trống'][i] = str(df['Tiết Trống'][i]).replace("nan","")+str(x)+','

    df.to_excel(path_out,
                 sheet_name='Sheet2')

list_room = ['A313', 'A302', 'B413', 'B411']

def check_room(num):
    # response = []
    # all_room = df['Phòng tự học'].values
    #
    # # for a in list_room:
    # count = 0
    # count2 = 0
    # for i in all_room:
    #     if i == list_room[1]:
    #         count = count+1
    # for x in range(count):
    #     print(df.loc[x]['Period 1/Tiết 1'])
    #     if df.loc[x]['Period 1/Tiết 1'] == "x":
    #         count2 = count2 + 1
    # print(count2)
    out = []
    for x in range(1, num):
        name = 'Period ' + str(x) + "/Tiết " + str(x)
        list_nan_in_room = []
        for i in list_room:
            a= df['Phòng tự học'].isin([i])
            b = df[name].isnull()
            list_nan_in_room.append(df[a & b].shape[0])
        print(list_nan_in_room)
        out.append(list_nan_in_room)
    print(out)
    pd.DataFrame(out, columns=list_room).to_excel(path_out)

check_room(8)