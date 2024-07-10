import os
# 将文件名称提取并保存为列表
# def find_txt_files_with_digit_start(directory):
#     matching_files = []
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             if file.endswith('.txt'):
#                 full_path = os.path.join(root, file)
#                 # print(file, full_path)
#                 if file[0] >= '0' and file[0] <= '9':
#                     # 只添加文件名到列表
#                     matching_files.append(file[:-4])
#     return matching_files
#
# # 替换下面的路径为你的目标文件夹路径
# directory_path = '../cola'  # 你的文件夹路径
# matching_file_names = find_txt_files_with_digit_start(directory_path)
# print("找到符合条件的文件名列表：", matching_file_names)

import Global_Parameter as GP
from Test import evaluate

file_names = ['104', '105', '106', '110', '110B', '110C', '114', '115', '116', '117', '119', '121',
              '121B', '123', '127', '128', '129', '135', '136', '143', '145', '165', '30', '41', '43',
              '44', '51', '53', '54', '57', '59', '6', '60', '61', '62', '64', '64B', '65', '66', '68',
              '71', '75', '76', '77', '79', '80', '80B', '81', '82', '82B', '82C', '85', '85B', '86', '87',
              '87B', '87C', '88', '90', '91', '93', '98', '98B']
k = GP.RANDOM_SEED
p = 1

for file_name in file_names:
    res = evaluate(file_name, k, p)
