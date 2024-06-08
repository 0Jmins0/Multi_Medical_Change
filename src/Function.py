import Global_Parameter as GP

DIS_TO_COST = GP.DIS_TO_COST  # 送货车距离和代价的关系系数，距离 * 系数 = 代价
DIS_TO_CHARGE = GP.DIS_TO_CHARGE  # 距离和充电量的关系系数
DIS_TO_CONSUME_OF_DELIVERY = GP.DIS_TO_CONSUME_OF_DELIVERY  # 运输车辆距离和耗电量的关系系数
DIS_TO_CONSUME_OF_CHARGE = GP.DIS_TO_CONSUME_OF_CHARGE  # 充电车距离和耗电量的关系系数
CHARGE_TO_COST = GP.CHARGE_TO_COST  # 消耗的电量和花费的关系系数，电量 * 系数 = 代价

BATTERY_CAPACITY_OF_DELIVERY = GP.BATTERY_CAPACITY_OF_DELIVERY  # 送货车电池容量
ORGAN_CAPACITY_OF_DELIVERY = GP.ORGAN_CAPACITY_OF_DELIVERY  # 送货车器官容量
SPEED_OF_DELIVERY = GP.SPEED_OF_DELIVERY  # 送货车速度（时间 * 参数 = 距离）
COST_OF_DELIVERY = GP.COST_OF_DELIVERY  # 送货车使用代价

BATTERY_CAPACITY_OF_CHARGE = GP.BATTERY_CAPACITY_OF_CHARGE  # 充电车电池容量
SPEED_OF_CHARGE = GP.SPEED_OF_CHARGE  # 充电车速度
COST_OF_CHARGE = GP.COST_OF_CHARGE  # 充电车使用代价


def get_route_cost(route, instance):
    dis = 0
    for i in range(1, len(route)):
        dis += instance['distance'][i - 1][i]
    route_charge = dis * DIS_TO_CONSUME_OF_DELIVERY
    route_cost = route_charge * CHARGE_TO_COST
    return route_cost


def get_sol_cost(sol, instance):
    cost = 0
    for route in sol:
        cost += get_route_cost(route, instance) + COST_OF_DELIVERY
    return cost


def insert_node_to_route(node, route, instance):
    capacity = ORGAN_CAPACITY_OF_DELIVERY

    for nn in route:
        capacity -= instance['need'][nn]
    if (capacity - instance['need'][node] < 0):
        return -1, -1

    Min_cost = 99999999
    Min_pos = -1
    original = get_route_cost(route, instance)

    for i in range(1, len(route)):  # 可以插入到第 1 个点前到第 n + 1 个点前
        new_cost = original - instance['distance'][route[i - 1]][route[i]] + \
                   instance['distance'][route[i - 1]][node] + \
                   instance['distance'][node][route[i]]
        if (Min_cost > new_cost):
            Min_cost = new_cost
            Min_pos = i
    return Min_pos, Min_cost


def get_init_sol(instance):
    new_sol = []
    n = instance['n']
    for i in range(1, n + 1):  # 遍历客户点1-n
        pos = -1
        cost = 9999999
        route_index = -1
        for index, route in enumerate(new_sol):
            tmp_pos, tmp_cost = insert_node_to_route(i, route, instance)
            if tmp_cost == -1 or tmp_pos == -1:
                continue
            if tmp_cost < cost:

                cost = tmp_cost
                pos = tmp_pos
                route_index = index

        if pos == -1 or route_index == -1:
            route = []
            route.extend([0, i, n + 1])
            new_sol.append(route)
        else:
            new_sol[route_index].insert(pos, i)

    return new_sol, get_sol_cost(new_sol, instance)


def remove_bank(bank, sol):
    return [route for route in [[elem for elem in row if elem not in bank] for row in sol] if len(route) > 2]


# 将列表中两坐标之间的元素翻转
def reverse_ele_between(route, index1, index2):
    # 确保 index1 和 index2 在列表范围内
    if 0 <= index1 < len(route) and 0 <= index2 < len(route):
        # 选择要翻转的部分
        start_index = min(index1, index2)
        end_index = max(index1, index2)
        sublist = route[start_index:end_index + 1]

        # 翻转部分
        route[start_index:end_index + 1] = reversed(sublist)

    return route


def check_cap_of_route(route, instance):
    cnt = 0
    for ele in route:
        cnt += instance['need'][ele]
        if cnt > ORGAN_CAPACITY_OF_DELIVERY:
            return False
    return True


def check_route(route, instance):
    if check_cap_of_route(route, instance):
        return True
    else:
        return False
