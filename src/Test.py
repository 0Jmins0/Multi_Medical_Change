import random
import time

from LNS import LNS
# from readData_cola import read_data
from Read_Data import read_data_random, read_data_cola
from DP import get_sol_charge
from clinitial import initcl
from Charge_Route import get_charge_route
from Force import get_sol_charge_force
import Function as F


def main(instance):
    start_time = time.perf_counter()
    best_deliver_sol, best_deliver_cost, best_charge_sol, best_tot_cost, best_T, Terminal = LNS(instance)
    end_time = time.perf_counter()
    run_time = end_time - start_time
    print("运行时间", run_time)
    return best_deliver_sol, best_deliver_cost, best_charge_sol, best_tot_cost, best_T, run_time, Terminal

def evaluate(a, k, p):
    random.seed(k)
    instance = {}
    # 读取可乐数据
    if p == 1:
        instance = read_data_cola(a)
    # 读取随机数据
    if p == 2:
        instance = read_data_random(a)
    # print(instance)
    best_deliver_sol, best_deliver_cost, best_charge_sol, best_tot_cost, best_T, run_time, Terminal= main(instance)
    return best_deliver_sol, best_deliver_cost, best_charge_sol, best_tot_cost, best_T, run_time, instance, Terminal
    # {'n': 6, 'need': [0, 1, 1, 4, 3, 2, 2, 0], 'distance': [[0, 598, 493, 480, 607, 607, 480, 0], [601, 0, 109, 124, 131, 131, 124, 601], [496, 118, 0, 17, 180, 180, 17, 496], [489, 129, 22, 0, 172, 172, 0, 489], [616, 137, 178, 173, 0, 0, 173, 616], [616, 137, 178, 173, 0, 0, 173, 616], [489, 129, 22, 0, 172, 172, 0, 489], [0, 598, 493, 480, 607, 607, 480, 0]]}
    # {'n': 3, 'need': [['1', '1'], ['2', '1'], ['3', '1']], 'distence': [['0', '19', '2', '3', '0'], ['19', '0', '4', '12', '19'], ['2', '4', '0', '8', '2'], ['3', '12', '8', '0', '3'], ['0', '19', '2', '3', '0']]}
