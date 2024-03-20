import copy
import math
import random

import Global_Parameter
from Local_Search import LS
import Function as FC

REMOVE_POOL = Global_Parameter.REMOVE_POOL
INSERT_POOL = Global_Parameter.INSERT_POOL

MaxI = 100  # 最大迭代次数
Terminal = 0  # 迭代次数

NonImp = 1

T0 = 187
q = 0.88


def remove_random(cur_sol, instance):
    bank = []
    tmp_sol = []
    n = instance['n']
    bank = random.sample(range(1,n + 1), min(NonImp,n))
    tmp_sol = FC.remove_bank(bank,cur_sol)
    return bank,tmp_sol

# def insert_random(bank,cur_sol, instance):
#     try:
#         bank_copy = copy.deepcopy(bank)
#         for node in bank_copy:
#             route = random.sample(cur_sol, 1)
#             pos = random.randint(1,len(route)-1)
#     except Exception as e:
#         print(f"From Random_Ins get an error: {e}")


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
