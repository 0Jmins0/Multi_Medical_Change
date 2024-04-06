import Global_Parameter as GP
import Function as FC
import copy

LOCAL_OPERATOR_POOL = GP.LOCAL_OPERATOR_POOL  # 邻域操作池


# 单个路径

# 选取一个路线中任意两点，反转包括其在内的中间的点
def opt2_exchange(sol, instance):
    pre_sol = copy.deepcopy(sol)
    num_of_route = len(sol)

    for idx in range(num_of_route):
        route_idx = idx
        route = copy.deepcopy(sol[route_idx])
        route_cost = FC.get_sol_cost(route, instance)

        # 路径中少于两个点
        if len(route) < 4:
            continue

        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route) - 1):
                index1, index2 = i, j
                tmp_route = FC.reverse_ele_between(route, index1, index2)
                tmp_cost = FC.get_route_cost(tmp_route, instance)
                if tmp_cost < route_cost:
                    sol[route_idx] = tmp_route
                    return sol

    return pre_sol


# 选取一条路线中连续的两点，将其放在其他位置
def or_opt(sol, instance):
    pre_sol = copy.deepcopy(sol)
    num_of_route = len(sol)

    for idx in range(num_of_route):
        route_idx = idx
        route = copy.deepcopy(sol[route_idx])
        route_cost = FC.get_sol_cost(route, instance)

        # 如果路径中少于3个点
        if (len(route) < 5):
            continue

        for i in range(1, len(route) - 2):
            for j in range(1, len(route) - 4):

                index1 = i
                index2 = i + 1

                ele1 = route[index1]
                ele2 = route[index2]

                route.remove(index1)
                route.remove(index2)

                index3 = j
                index4 = j + 1

                route.insert(index3, ele1)
                route.insert(index4, ele2)

                tmp_cost = FC.get_route_cost(route, instance)

                if tmp_cost < route_cost:
                    sol[route_idx] = route
                    return sol
    return pre_sol


# 路径间

# 选择路径1的节点A和路径2的节点B，交换它们，并将A后面的节点接到B的位置，将B后面的节点接到A的位置。
def opt2_exchange_mul(sol, instance):
    pre_sol = copy.deepcopy(sol)
    num_of_route = len(sol)

    # 选择两个路径
    for index1 in range(num_of_route):
        for index2 in range(index1 + 1, num_of_route):
            route1 = copy.deepcopy(sol[index1])
            route2 = copy.deepcopy(sol[index2])

            # 计算当前两路径的成本
            pre_cost = FC.get_route_cost(route1, instance) + FC.get_route_cost(route2, instance)

            # 如果某个路径的长度小于4，则无法进行切割交换
            if len(route1) < 4 or len(route2) < 4:
                continue

            # 选择切割点
            for cut1 in range(1, len(route1) - 2):
                for cut2 in range(1, len(route2) - 2):
                    # 切割并交换部分路径
                    route1_L = route1[:cut1]
                    route1_R = route1[cut1:]
                    route2_L = route2[:cut2]
                    route2_R = route2[cut2:]

                    route1_new = route1_L + route2_R
                    route2_new = route2_L + route1_R

                    # 检查交换后路径的约束条件
                    if FC.check_route(route1_new, instance) == False or FC.check_route(route2_new, instance) == False:
                        continue

                    # 计算交换后的成本
                    new_cost = FC.get_route_cost(route1_new, instance) + FC.get_route_cost(route2_new, instance)

                    # 如果成本降低，则接受新解，并立即返回
                    if new_cost < pre_cost:
                        sol[index1] = route1_new
                        sol[index2] = route2_new
                        return sol
    return pre_sol


def LS_OP(sol, instance, op_id):
    operator = LOCAL_OPERATOR_POOL[op_id]
    if operator == 1:
        new_sol = opt2_exchange(sol, instance)
        new_cost = FC.get_sol_cost(new_sol, instance)
        return new_sol, new_cost
    elif operator == 2:
        new_sol = or_opt(sol, instance)
        new_cost = FC.get_sol_cost(new_sol, instance)
        return new_sol, new_cost
    elif operator == 3:
        new_sol = opt2_exchange_mul(sol, instance)
        new_cost = FC.get_sol_cost(new_sol, instance)
        return new_sol, new_cost


def LS(new_sol, instance):
    op_id = 0
    k = 0
    new_cost = FC.get_sol_cost(new_sol, instance)
    while k < len(LOCAL_OPERATOR_POOL):
        tmp_sol, tmp_cost = LS_OP(new_sol, instance, op_id)
        if tmp_cost < new_cost:
            new_sol = tmp_sol
            new_cost = tmp_cost
            k = 0
        else:
            k = k + 1
        op_id = (op_id + 1) % len(LOCAL_OPERATOR_POOL)
    return new_sol, new_cost
