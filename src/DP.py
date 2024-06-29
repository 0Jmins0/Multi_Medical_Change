import numpy as np
import Global_Parameter as GP
import time


def get_binary(number):
    binary_representation = bin(number)
    return binary_representation[2:]


def get_charge_node(f, dis):
    p = GP.CHARGE_CONSUME
    charge = [x * p for x in dis]
    charge_node = []
    Max = GP.BATTERY_CAPACITY_OF_DELIVERY
    L = len(f)
    dp = np.zeros(2 ** (L + 1), dtype=int)
    vis = np.zeros(2 ** (L + 1), dtype=int)
    INF = -99999
    dp[0] = Max
    tot = 0
    for i in range(1, L):
        for j in range(0, (1 << (i - 1))):
            tot += 1
            k = j | (1 << (i - 1))
            # 该状态已经满足
            if vis[j] == 1:
                continue
            # 该状态不符合条件
            if dp[j] < 0:
                dp[j] = INF
                vis[j] = -1
                dp[k] = INF
                vis[k] = -1

            dp[k] = min(dp[j] - dis[i] + charge[i], Max)
            dp[j] = dp[j] - dis[i]

            # 判断合法情况
            if dp[j] >= f[i]:
                vis[j] = 1
                charge_node.append(j)
            if dp[k] >= f[i]:
                vis[k] = 1
                charge_node.append(k)
        # print("charge",[get_binary(x) for x in charge_node])
    print("DP循环总数", tot)
    return charge_node


def remove_dup(charge_node):
    del_node = []
    L = len(charge_node)
    for i in range(L):
        for j in range(i + 1, L):
            a = charge_node[i]
            b = charge_node[j]
            if a & b == a:
                del_node.append(b)
    for a in del_node:
        if a in charge_node:
            charge_node.remove(a)
    return charge_node


# 将二进制补全为一样长度
def auto_completion(charge_node, route):
    for i, charge in enumerate(charge_node):
        while len(charge) < len(route) - 1:
            charge = '0' + charge
        charge_node[i] = charge[::-1]
    return charge_node


def get_time_node(charge_node, route, time):
    charge_time_node = []
    for charge in charge_node:
        pair = []
        for j in range(len(charge)):  # route 的第 j 条边 连接点 j 和 j + 1
            if charge[j] == '1':
                pair.append(((time[j], route[j]), (time[j + 1], route[j + 1])))  # ((time_u,node_u),(time_v,node_v))
        charge_time_node.append(pair)
    return charge_time_node


def get_sol_charge(sol, instance):
    charge_list = []
    time_list = []
    for route in sol:
        f = []
        dis = []
        charge = 0
        for i in range(len(route) - 1, 0, -1):
            f.append(charge)
            dis.append(instance['distance'][route[i - 1]][route[i]])
            charge += dis[-1] * GP.DIS_TO_CHARGE
        f.append(charge)
        f.reverse()
        dis.append(0)
        dis.reverse()
        tt = 0
        Time = []  # 送货车到达点i的时间
        for dd in dis:
            tt += round(dd / GP.SPEED_OF_DELIVERY)
            Time.append(tt)
        time_list.append(Time)
        # print("route", route)
        # print("Time,f,dis", Time, f, dis)
        charge_node = get_charge_node(f, dis)
        # print("after_get", charge_node)
        charge_node = remove_dup(charge_node)
        # print("after_remove", charge_node)
        charge_node = [get_binary(x) for x in charge_node]
        # print("after_bin", charge_node)
        charge_node = auto_completion(charge_node, route)
        # print("after_com", charge_node)
        charge_node = get_time_node(charge_node, route, Time)
        charge_list.append(charge_node)

    return charge_list

# p = 3  # 充电相当与耗电量的系数(耗电1，充电p)
# f = [650, 450, 350, 250, 50, 0]  在第 i 个点的时候，还需要的电量
# dis = [0, 200, 100, 100, 200, 50]  第 i 和第 i-1 个点之间的距离
# charge = [x * p for x in dis]
# Max = 300
#
# # print(get_binary(4))
# # print( 4 | (1 << 3))
# charge = get_charge_node(f,dis,charge)
# print(charge)
# charge = remove_dup(charge)
# charge_node = [get_binary(x) for x in charge]
# print(charge_node)

# print("i:", i, "j:", j, "j | (1 << (i - 1)) : ", j | k)
# print("j:", get_binary(j))
# print("j | (1 << (i - 1)) :", get_binary(j | k))
# print("dp[j]:", dp[j])
