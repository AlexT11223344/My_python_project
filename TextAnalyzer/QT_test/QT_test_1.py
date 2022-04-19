import os
import numpy as np
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

path = os.getcwd()

with open(path + r'\Adam Bede(1859)_test_Rows.txt', 'r') as f:
    file_Adam = f.read()

keyword_1 = "Workshop"
fuz_accurcy = 75
test_1 = "123.."
test_2 = "b"
test_3 = "c"
str_1 = '.'
print(len(file_Adam))
# keyword_1 = ['Brother', 'other', 'other', 'other', 'mother', 'other', 'other', 'mother', 'rather', 'mother', 'brother',
#              'other', 'brother', 'brother,',
#              'other', 'other', 'brother’s', 'brother', 'brother', 'brother’s', 'brother’s', 'rather', 'mother',
#              'brothers.', 'brothers,', 'rather', 'brother',
#              'brother,', 'other', 'brother.', 'rather', 'brother', 'brother’s', 'brother’s', 'brother’s', 'brother,',
#              'brother?', 'other', 'mother', 'other,',
#              'other', 'rather', '“other', 'other', 'other', 'other,', 'other', 'other', 'rather', 'rather', 'rather',
#              'brother,', 'other', 'brothers,',
#              'brothers', 'other', 'other', 'other', 'rather', 'rather', 'mother', 'rather', 'rather', 'brothers',
#              'rather', 'other', 'other', 'other',
#              'other', 'other', 'other', 'brother', 'other', 'other,', 'mother', 'brother', 'mother', 'brother',
#              'rather', 'rather', 'mother', 'brother’s',
#              'other', 'others', 'brother', 'brother', 'brother.”', 'brother,', 'brother,”', 'brother', 'brother',
#              '“Brother', 'brother,', 'rather', 'brothers,',
#              'other', 'brother,', 'brother', 'brother,', 'brother;', 'mother', 'brother,', 'other', 'mother',
#              'brother,', 'brother', 'brother’s', 'brother',
#              'other', 'other', 'brother']
#
# rowList_1 = ['1', '55', '64', '72', '112', '123', '129', '130', '134', '143', '172', '189', '199', '206', '214', '215',
#              '261', '282', '290', '295', '301',
#              '307', '313', '352', '362', '378', '383', '390', '398', '402', '405', '405', '435', '450', '466', '471',
#              '474', '513', '550', '573', '618',
#              '639', '679', '707', '720', '731', '746', '788', '796', '803', '818', '840', '859', '880', '881', '901',
#              '920', '953', '954', '965', '972',
#              '1013', '1019', '1055', '1055', '1090', '1117', '1121', '1123', '1130', '1140', '1145', '1150', '1156',
#              '1165', '1188', '1191', '1199', '1225',
#              '1229', '1231', '1258', '1281', '1290', '1294', '1321', '1341', '1356', '1372', '1382', '1403', '1415',
#              '1428', '1429', '1431', '1432', '1435',
#              '1446', '1449', '1452', '1455', '1464', '1465', '1472', '1478', '1501', '1505', '1541', '1546', '1560',
#              '1592']
#
#
# def order_Change(Keyword_Sorted, Index_list, Sub_Array_To_Be_Sorted):
#     if len(Keyword_Sorted) != len(Sub_Array_To_Be_Sorted):
#         return None
#
#     _sorted_list = Keyword_Sorted
#     _index_list = Index_list
#     _new_sorted_list = [0] * len(_sorted_list)
#     for i in range(0, len(_index_list)):
#         _new_sorted_list[i] = Sub_Array_To_Be_Sorted[_index_list[i]]
#     return _new_sorted_list
#
# keyword_sorted = sorted(keyword_1)
# index_list = sorted(range(len(keyword_1)), key=keyword_1.__getitem__)
# print(keyword_1)
# print(index_list)
# a = order_Change(keyword_sorted, index_list, rowList_1)
# print(a)
# b = ["Null"] * 5
# print(b)
