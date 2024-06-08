import numpy as np


def get_binary(number):
    binary_representation = bin(number)
    return binary_representation[2:]
def get_charge_node(f, dis, charge):
    charge_node =[]
    L = len(f)
    dp = np.zeros(2 ** (L + 1), dtype=int)
    vis = np.zeros(2 ** (L + 1), dtype=int)
    INF = -99999
    dp[0] = Max
    for i in range(1, L):
        for j in range(0, (1 << (i - 1))):
            k = j | (1 << (i - 1))
            # 该状态已经满足
            if(vis[j] == 1) :
                continue
            # 该状态不符合条件
            if(dp[j] < 0) :
                dp[j] = INF
                vis[j] = -1
                dp[j | k] = INF
                vis[j | k] = -1

            dp[j | k] = min(dp[j] - dis[i] + charge[i], Max)
            dp[j] = dp[j] - dis[i]

            # 判断合法情况
            if(dp[j] >= f[i]):
                vis[j] = 1
                charge_node.append(j)
            if(dp[j | k] >= f[i]):
                vis[j | k] = 1
                charge_node.append((j | k))
        # print("charge",[get_binary(x) for x in charge_node])
    return charge_node

def remove_dup(charge_node):
    del_node = []
    L = len(charge_node)
    for i in range(L):
        for j in range(i + 1,L):
            a = charge_node[i]
            b = charge_node[j]
            if(a & b == a):
                del_node.append(b)
    for a in del_node:
        if(a in charge_node):
            charge_node.remove(a)
    return charge_node

def get_sol_charge(sol, instance):
    for route in sol:
        f = []
        dis = 0
        for i in range(len(route) - 1, 0, -1):
            f.append(dis)
            dis += instance['distance'][route[i - 1]][route[i]]
        f.append(dis)
        f.reverse()


p = 3  # 充电相当与耗电量的系数(耗电1，充电p)
f = [650, 450, 350, 250, 50, 0]
dis = [0, 200, 100, 100, 200, 50]
charge = [x * p for x in dis]
Max = 300

# print(get_binary(4))
# print( 4 | (1 << 3))
charge = get_charge_node(f,dis,charge)
charge = remove_dup(charge)
charge_node = [get_binary(x) for x in charge]
print(charge_node)

            # print("i:", i, "j:", j, "j | (1 << (i - 1)) : ", j | k)
            # print("j:", get_binary(j))
            # print("j | (1 << (i - 1)) :", get_binary(j | k))
            # print("dp[j]:", dp[j])
