'''Find keyword and the left and right side words'''
import os
import numpy as np
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


path = os.getcwd()

with open(path + r'\Adam Bede(1859)_test.txt', 'r') as f:
    file_Adam = f.read()

keyword_1 = "Workshop"



def list_to_string(list):
    _str1 = ' '.join(list)
    return _str1



def keyword_l_r(file, File_name, keyword, n):
    # file must be use "Open" as f and f.read function to get the result with only "r" module
    _file_to_list = file.split()
    # np_file = np.array(_file_to_list)
    _n = n

    '''
    Create 5 list to store 
    # 1.ID 
    # 2.File name
    # 3.leftContext
    # 4.Hit(keyword)
    # 5.RightContext
    '''

    _leftContext = []
    _rightContext = []
    _Hit = []
    _id = []
    _fuz_accurcy = 75
    _fileName = File_name

    for i in range(0, len(_file_to_list)):
        if fuzz.ratio(keyword, _file_to_list[i]) >= _fuz_accurcy:
            _Hit.append(_file_to_list[i])
            if i - _n < 0:
                _leftContext.append(_file_to_list[0: i])
            else:
                _leftContext.append(_file_to_list[i - _n: i])

            if i + _n > len(_file_to_list):
                _rightContext.append(_file_to_list[i + 1: len(_file_to_list)])
            else:
                _rightContext.append(_file_to_list[i + 1: i + _n + 1])
        else:
            continue
    for j in range(0, len(_leftContext)):
        _id.append(j + 1)

    _fileName_list = [_fileName] * len(_leftContext)

    for k in range(0,len(_leftContext)):
        _leftContext[k] = list_to_string(_leftContext[k])
        _rightContext[k] = list_to_string(_rightContext[k])
    _id = list(map(str, _id))

    return _fileName_list, _leftContext, _Hit, _rightContext


a, b, c, d = keyword_l_r(file_Adam, 'Adam Bede(1859)_test.txt', keyword_1, 6)
print(len(a))
print(len(b))
print(len(c))
print(len(d))

