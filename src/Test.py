import random

from LNS import LNS
from Read_Data import read_data


def main(instace):
    sol = LNS(instace)


def evaluate(a,k):
    random.seed(k)
    instance = read_data(a)
    main(instance)