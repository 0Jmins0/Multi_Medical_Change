import copy
import math
import random

import Global_Parameter as GP
from Local_Search import LS
import Function as FC

REMOVE_POOL = GP.REMOVE_POOL
INSERT_POOL = GP.INSERT_POOL

MaxI = 100  # 最大迭代次数
Terminal = 0  # 迭代次数

NonImp = 1

T0 = 187
q = 0.88


# 随机删除
def remove_random(cur_sol, instance):
    bank = []
    tmp_sol = []
    n = instance['n']
    bank = random.sample(range(1, n + 1), min(NonImp, n))
    tmp_sol = FC.remove_bank(bank, cur_sol)
    return bank, tmp_sol


# 移除后，距离变化最大的点集
def remove_distance(cur_sol, instance):
    Dis_list = []
    for route in cur_sol:
        for i in range(1, len(route) - 1):
            # 删除点i后，距离的变化
            change = (instance['distance'][route[i - 1]][route[i + 1]] -
                      instance['distance'][route[i - 1]][route[i]] -
                      instance['distance'][route[i]][route[i + 1]])
            Dis_list.append([change, route[i]])

    Dis_list = sorted(Dis_list, key=lambda x: x[0], reverse=True)
    n = instance['n']
    bank = [row[1] for row in Dis_list[:min(NonImp, n)]]
    tmp_sol = FC.remove_bank(bank, cur_sol)
    return bank, tmp_sol


# 每一条路线 随机删除一段路线
def remove_string(cur_sol, instance):
    bank = []
    for sol in cur_sol:
        Len = len(sol) - 2
        Max_del = min(NonImp, Len)
        Del_len = random.randint(Max_del, Len)  # [Max_del,Len]
        start = random.randint(1, Len - Del_len)  # [1,Len - Del_len + 1]
        end = start + Del_len

        bank.extend(sol[start:end])

    new_sol = FC.remove_bank(bank,cur_sol)
    return bank, new_sol


def remove_worst(cur_sol, instance):
    cost_list = []
    for route in cur_sol:
        for i in range(1, len(route) - 1):
            change = (instance['distance'][route[i - 1]][route[i + 1]] -
                      instance['distance'][route[i - 1]][route[i]] -
                      instance['distance'][route[i]][route[i + 1]]) * GP.DIS_TO_COST
            if len(route) == 3:
                change += GP.COST_OF_DELIVERY
            cost_list.append([change, route[i]])
    cost_list = sorted(cost_list, key = lambda x: x[0], reverse=True)
    n = instance['n']
    bank = [row[1] for row in cost_list[:min(NonImp, n)]]
    tmp_sol = FC.remove_bank(bank,cur_sol)
    return bank, tmp_sol


def insert_random(bank, cur_sol, instance):
    try:
        bank_copy = copy.deepcopy(bank)
        for node in bank_copy:
            route_id = random.randint(len(cur_sol))
            pos, cost = FC.insert_node_to_route(node, cur_sol[route_id], instance)
            if (pos == -1):
                new_route = []
                new_route.extend([0, node, instance['n'][0] + 1])
                cur_sol.append(new_route)
            else:
                cur_sol[route_id].insert(node, pos)
        return cur_sol


    except Exception as e:
        print(f"From Random_Ins get an error: {e}")

#  贪心的插入每一个点
def insert_greedy(bank, cur_sol, instance):
    pass

#  顺序的插入每一个点
def insert_sequential(bank, cur_sol, instance):
    pass


def distroy_and_repair(current_sol, removal_id, insert_id, instance):
    try:
        bank = []
        new_sol = current_sol
        new_cost = float('inf')

        # Removel
        if removal_id == 1:
            pass

        # Insert
        if insert_id == 1:
            pass

        return new_sol, new_cost
    except Exception as e:
        print(f"From Distroy_and_Repair get an error: {e}")


def LNS(instance):
    global NonImp, T0, q, MaxI, Terminal

    T = T0
    init_sol, init_cost = FC.get_init_sol(instance)
    best_sol, best_cost = init_sol, init_cost
    current_sol, current_cost = init_sol, init_cost
    print("初始化", init_sol, init_cost)

    print("迭代退火")

    while Terminal < MaxI:
        removal_id = random.choice(REMOVE_POOL)
        insert_id = random.choice(INSERT_POOL)
        new_sol, new_cost = distroy_and_repair(current_sol, removal_id, insert_id, instance)

        if new_cost < best_cost:
            new_sol, new_cost = LS(new_sol, instance)

        T *= q

        diff = new_cost - current_cost
        if diff < 0:
            current_sol = new_sol
            current_cost = new_cost
        else:
            r = random.random()
            if T >= 0.01 and math.exp((diff) / (10000 * T)) >= r:
                cur_sol = new_sol
                cur_cost = new_cost

        if current_cost < best_cost:
            best_sol = current_sol
            best_cost = current_cost
            NonImp = 1  # 连续没有提升的次数归零
        else:
            NonImp += 1
        Terminal += 1

    print("After LNS:best_sol,best_cost", best_sol, best_cost)

    return best_sol, best_cost
