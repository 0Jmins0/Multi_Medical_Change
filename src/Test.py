import random

from LNS import LNS
from Read_Data import Read_Data


def main(instace):
    sol = LNS(instace)


def evaluate(a,k):
    random.seed(k)
    instance = Read_Data(a)
    main(instance)