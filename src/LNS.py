import copy
import math
import random
import heapq

import Global_Parameter as GP
from Local_Search import LS
import Function as FC
from clinitial import initcl


REMOVE_POOL = GP.REMOVE_POOL
INSERT_POOL = GP.INSERT_POOL

MaxI = GP.MaxI  # 最大迭代次数
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
        # print("rem_string",Len, Del_len)
        start = random.randint(1, Len - Del_len + 1)  # [1,Len - Del_len + 1]
        end = start + Del_len - 1
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

def remove_shaw(cur_sol, instance):
    n = instance['n']
    Q, bank, vis = [], [], [0 for i in range(n + 1)]
    random_node = random.randint(1, n)
    heapq.heappush(Q,(0, random_node))
    num = 0
    CL = initcl(instance)
    while len(Q) > 0:
        tmp = heapq.heappop(Q)
        if vis[tmp[1]] == 1 :
            continue
        vis[tmp[1]] = 1
        bank.append(tmp[1])
        num += 1
        if num == NonImp or num == n:
            break
        for i in range(1, n + 1):
            if(vis[i] == 0):
                heapq.heappush(Q, (CL[i][tmp[1]], i))
    new_sol = FC.remove_bank(bank, cur_sol)
    return bank, new_sol



def insert_random(bank, cur_sol, instance):
    bank_copy = copy.deepcopy(bank)
    for node in bank_copy:
        if len(cur_sol) == 0:
            new_route = []
            new_route.extend([0, node, instance['n'] + 1])
            cur_sol.append(new_route)
        else:
            route_id = random.randint(0, len(cur_sol) - 1)
            pos, cost = FC.insert_node_to_route(node, cur_sol[route_id], instance)
            if (pos == -1):
                new_route = []
                new_route.extend([0, node, instance['n'] + 1])
                cur_sol.append(new_route)
            else:
                cur_sol[route_id].insert(pos, node)
    return cur_sol

#  贪心的插入每一个点
def insert_greedy(bank, cur_sol, instance):
    for node in bank:
        Min_pos = -1
        Min_cost = 999999999999
        Min_route_id = -1
        for route_id, route in enumerate(cur_sol):
            tmp_pos, tmp_cost = FC.insert_node_to_route(node, route, instance)
            if tmp_cost < Min_cost:
                Min_cost = tmp_cost
                Min_route_id = route_id
                Min_pos = tmp_pos
        if Min_pos == -1:
            cur_sol.append([0, node, instance['n'] + 1])
        else:
            cur_sol[Min_route_id].insert( Min_pos,node)

    return cur_sol


#  顺序的插入每一个点
def insert_sequential(bank, cur_sol, instance):
    for node in bank:
        ok = 0
        for route_pos in range(0, len(cur_sol)):
            Min_pos, Min_cost = FC.insert_node_to_route(node, cur_sol[route_pos], instance)
            if(Min_pos != -1):
                cur_sol[route_pos].insert(Min_pos, node)
                ok = 1
                break
        if ok == 0:
            cur_sol.append([0, node, instance['n'] + 1])
    return cur_sol

# 找到某个点的三个最好的插入位置的cost
def find_cost(node, cur_sol, instance):
    change_list = []
    for route_pos in range(0, len(cur_sol)):
        for pos in range(1, len(cur_sol[route_pos])):
            u = cur_sol[route_pos][pos - 1]
            v = cur_sol[route_pos][pos]
            cost_change = (instance['distance'][u][node] +
                           instance['distance'][node][v] -
                           instance['distance'][u][v])
            cur = [cost_change, route_pos, pos]
            tmp_route = copy.deepcopy(cur_sol[route_pos])
            tmp_route.insert(pos, node)
            if FC.check_route(tmp_route, instance):
                change_list.append(cur)

    change_list = sorted(change_list, key=lambda x: x[0])

    if len(change_list) == 0:
        return [0, 0, 0], [0, 0, 0], [0, 0, 0]
    if len(change_list) == 1:
        return change_list[0], [0, 0, 0], [0, 0, 0]
    if len(change_list) == 2:
        return change_list[0], change_list[1], [0, 0, 0]
    return change_list[0], change_list[1], change_list[2]


def insert_regret2(bank, cur_sol, instance):
    regret_list = []
    new_sol = copy.deepcopy(cur_sol)
    while len(bank) != 0:
        random.shuffle(bank)
        regret_list.clear()
        tmp_bank = copy.deepcopy(bank)
        for node in tmp_bank:
            # l1 = [cost, route_pos, pos]
            l1, l2, l3 = find_cost(node, new_sol, instance)
            if l1[0] == 0 and l1[1] == 0 and l1[2] == 0:
                new_sol.append([0, node, instance['n'] + 1])
                bank.remove(node)
            else:
                regret = l1[0] - l2[0]
                cur = [regret, node, l1]
                regret_list.append(cur)

        if len(regret_list) > 0 :
            regret_list = sorted(regret_list, key=lambda x: x[0])
            route = regret_list[0][2][1]
            pos = regret_list[0][2][2]
            node = regret_list[0][1]
            new_sol[route].insert(pos, node)
            bank.remove(node)

    return new_sol


def insert_regret3(bank, cur_sol, instance):
    regret_list = []
    new_sol = copy.deepcopy(cur_sol)
    while len(bank) != 0:
        random.shuffle(bank)
        regret_list.clear()
        tmp_bank = copy.deepcopy(bank)
        for node in tmp_bank:
            # l1 = [cost, route_pos, pos]
            l1, l2, l3 = find_cost(node, new_sol, instance)
            if l1[0] == 0 and l1[1] == 0 and l1[2] == 0:
                new_sol.append([0, node, instance['n'] + 1])
                bank.remove(node)
            else:
                regret = l1[0] - l3[0]
                cur = [regret, node, l1]
                regret_list.append(cur)

        if len(regret_list) > 0 :
            regret_list = sorted(regret_list, key=lambda x: x[0])
            route = regret_list[0][2][1]
            pos = regret_list[0][2][2]
            node = regret_list[0][1]
            new_sol[route].insert(pos, node)
            bank.remove(node)

    return new_sol



def distroy_and_repair(current_sol, removal_id, insert_id, instance):
    # try:
    bank = []
    new_sol = current_sol
    new_cost = float('inf')

    # print("rem:",removal_id, "ins:",insert_id)
    # Removel
    if removal_id == 1:
        bank, new_sol = remove_random(current_sol, instance)
    if removal_id == 2:
        bank, new_sol = remove_distance(current_sol, instance)
    if removal_id == 3:
        bank, new_sol = remove_string(current_sol, instance)
    if removal_id == 4:
        bank, new_sol = remove_worst(current_sol, instance)
    if removal_id == 5:
        bank, new_sol = remove_shaw(current_sol, instance)

    # print("new_sol_rem:", new_sol,bank)

    # Insert
    if insert_id == 1:
        new_sol = insert_random(bank, new_sol, instance)
    if insert_id == 2:
        new_sol = insert_greedy(bank, new_sol, instance)
    if insert_id == 3:
        new_sol = insert_sequential(bank, new_sol, instance)
    if insert_id == 4:
        new_sol = insert_regret2(bank, new_sol, instance)
    if insert_id == 5:
        new_sol = insert_regret3(bank, new_sol, instance)

    # print("new_sol_ins:",new_sol)
    new_cost = FC.get_sol_cost(new_sol, instance)

    return new_sol, new_cost
    # except Exception as e:
    #     print(f"From Distroy_and_Repair get an error: {e}")


def LNS(instance):
    global NonImp, T0, q

    Terminal = 0  # 迭代次数
    NonImp = 1
    n = instance['n']

    T = T0
    init_sol, init_cost = FC.get_init_sol(instance)
    best_sol, best_cost = init_sol, init_cost
    current_sol, current_cost = init_sol, init_cost
    print("初始化cost",  init_cost)
    # print("初始化sol", init_sol)

    print("迭代退火")

    # new_sol, new_cost = LS(init_sol, instance)
    #
    # print("sdfsadfsdfsdfsdf")
    # print(new_cost)

    while Terminal < MaxI and NonImp <= n:
        removal_id = random.choice(REMOVE_POOL)
        insert_id = random.choice(INSERT_POOL)
        new_sol, new_cost = distroy_and_repair(current_sol, removal_id, insert_id, instance)

        if new_cost < best_cost:
            print("pre_LS", new_cost)
            new_sol, new_cost = LS(new_sol, instance)
            print("after_LS", new_cost)

        T *= q

        diff = new_cost - current_cost
        if diff < 0:
            current_sol = new_sol
            current_cost = new_cost
        else:
            r = random.random()
            # print(diff)
            if T >= 0.01 and math.exp((diff) / (100000 * T)) >= r:
                # print("acc")
                current_sol = new_sol
                current_cost = new_cost

        if current_cost < best_cost:
            best_sol = current_sol
            best_cost = current_cost
            NonImp = 1  # 连续没有提升的次数归零
        else:
            NonImp += 1
        Terminal += 1
        if(Terminal % 10 == 0):
            print(Terminal, "cur:", current_cost, "best:", best_cost)

    print("After LNS:best_sol,best_cost", len(best_sol), best_cost)

    return best_sol, best_cost
