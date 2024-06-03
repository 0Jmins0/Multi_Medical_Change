import random

from LNS import LNS
from Read_Data import read_data
from hk_data_read import read_txt_to_dict


def main(instace):
    sol = LNS(instace)


def evaluate(a,k):
    random.seed(k)
    file_name = '../hk_data_exmple/101-29.txt'
    instance = read_txt_to_dict(file_name)
    main(instance)