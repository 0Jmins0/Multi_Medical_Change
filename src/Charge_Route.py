import copy
vis = [[0 for i in range(10000)] for j in range(10000)]
ans = 10000000
check_list = []


def dfs(charge_node, instance, pos, eage):
    global ans, vis, check_list
    if pos >= len(charge_node):
        if eage in check_list:
            print("wrong!!!")

        if len(eage) != 0:
            check_list.append(copy.deepcopy(eage))
        if len(check_list) % 10000 == 0:
            print(len(check_list))
        # print(len(check_list))
        # print("check_list", check_list)
        # print("eage:", eage)
        return
        # ans = min(ans, eage)
    for i in range(len(charge_node[pos])):
        if vis[pos][i] == 0:
            vis[pos][i] = 1
            sol = charge_node[pos][i]
            eage.append(sol)
            dfs(charge_node, instance, pos + 1, eage)
            eage.pop()
            vis[pos][i] = 0


def get_charge_route(charge_node, instance):
    global ans, check_list
    print("get_charge_route")
    print(charge_node)
    dfs(charge_node, instance, 0, [])
    print("答案数量：", len(check_list))
    # print(check_list)
    return ans
