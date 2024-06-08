import random

from LNS import LNS
from readData_cola import read_data


def main(instance):
    print(instance)
    sol = LNS(instance)
    print(sol)


def evaluate(a,k):
    random.seed(k)
    # file_name = '../hk_data_exmple/101-29.txt'
    instance = read_data(a)
    main(instance)