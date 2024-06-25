import random

from LNS import LNS
from readData_cola import read_data
from DP import get_sol_charge
from clinitial import initcl


def main(instance):

    # print(initcl(instance))
    # print(instance)
    # print("LNS求解送货车路线")
    sol, cost = LNS(instance)
    # print("LNS 求得的sol", sol, cost)
    # print("DP 求解充电位置")
    # charge_node = get_sol_charge(sol, instance)
    # print("DP 求得的充电位置:", charge_node)



def evaluate(a,k):
    random.seed(k)
    # file_name = '../hk_data_exmple/101-29.txt'
    instance = read_data(a)
    main(instance)