import random
import time

from LNS import LNS
# from readData_cola import read_data
from Read_Data import read_data_random, read_data_cola
from DP import get_sol_charge
from clinitial import initcl
from Charge_Route import get_charge_route
from Force import get_sol_charge_force


def main(instance):
    start_time = time.perf_counter()
    # print(initcl(instance))
    # print(instance)
    # print("LNS求解送货车路线")
    sol, cost = LNS(instance)
    print("LNS 求得的sol", cost, sol)
    # print("DP 求解充电位置")
    charge_node = get_sol_charge(sol, instance)
    # charge_node[0][0][0] : 第 0 号路线的第 0 号解的第 0 条充电边: ((time_u,node_u),(time_v,node_v))
    print("DP 求得的充电位置:", charge_node)
    print("获得充电车代价", get_charge_route(charge_node, instance))
    end_time = time.perf_counter()
    print("运行时间", end_time - start_time)

    charge_node_force = get_sol_charge_force(sol, instance)


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
    return main(instance)
    # {'n': 6, 'need': [0, 1, 1, 4, 3, 2, 2, 0], 'distance': [[0, 598, 493, 480, 607, 607, 480, 0], [601, 0, 109, 124, 131, 131, 124, 601], [496, 118, 0, 17, 180, 180, 17, 496], [489, 129, 22, 0, 172, 172, 0, 489], [616, 137, 178, 173, 0, 0, 173, 616], [616, 137, 178, 173, 0, 0, 173, 616], [489, 129, 22, 0, 172, 172, 0, 489], [0, 598, 493, 480, 607, 607, 480, 0]]}
    # {'n': 3, 'need': [['1', '1'], ['2', '1'], ['3', '1']], 'distence': [['0', '19', '2', '3', '0'], ['19', '0', '4', '12', '19'], ['2', '4', '0', '8', '2'], ['3', '12', '8', '0', '3'], ['0', '19', '2', '3', '0']]}
