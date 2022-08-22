from datetime import datetime
import pandas as pd
import time

t = time.localtime()
dic_date = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10,
            'Nov': 11, 'Dec': 12}
dic_date_inverse = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct',
                    11: 'Nov', 12: 'Dec'}
present_time = [dic_date_inverse[t.tm_mon], str(t.tm_year)]
present_time = " ".join(present_time)
# print(present_time)


test_1 = ['May 2021 – Present', 'Dec 2019 – May 2021', 'Oct 2018 – May 2019', 'Feb 2018 – Oct 2018',  'Oct 2017 – Jan 2018']
test_2 = ['Feb 2018 – Present', 'Oct 2016 – Feb 2018', 'Mar 2016 – Oct 2016']
# test_1 = ['5 2021 - 8 2022', '12 2019 - 5 2021', '10 2018 - 5 2019', '2 2018 - 10 2018']
# 输出：['12 2019 - 8 2022', '2 2018 - 5 2019', '10 2017 - 1 2018']
result = []


def date_clean(data):
    _result = []
    for _date in data:
        # print(_date)
        if _date.lower() == " present":
            _date = present_time
            Month = _date.split(" ")
            Year = _date.split(" ")
            # print(Month)
            # print(Year)
            _result.append(dic_date[Month[0]])
            _result.append(int(Year[1]))

        else:
            Month = _date.split(" ")
            Year = _date.split(" ")
            # print(Month)
            # print(Year)
            Month.remove("")
            Year.remove("")
            _result.append(dic_date[Month[0]])
            _result.append(int(Year[1]))
    return _result


result_temp = [0, 0, 0, 0]
result_continuous = []

i = 0
j = 1
while i < len(test_2) - 1:
    temp = test_2[i].split("–")
    temp = date_clean(temp)
    result_temp[0] = temp[0]
    result_temp[1] = temp[1]
    result_temp[2] = temp[2]
    result_temp[3] = temp[3]
    while j < len(test_2):
        temp_next = test_2[j].split("–")
        temp_next = date_clean(temp_next)
        if result_temp[0] == temp_next[2] and result_temp[1] == temp_next[3]:
            result_temp[0] = temp_next[0]
            result_temp[1] = temp_next[1]
            i = j
            j += 1
            # print(result_temp)
        else:
            # print(result_temp)
            i = j
            j += 1
            break
print(result_temp)
# print(result_continuous)

