import Global_Parameter as GP
DIS_TO_COST = GP.DIS_TO_COST  # 送货车距离和代价的关系系数，距离 * 系数 = 代价
DIS_TO_CHARGE = GP.DIS_TO_CHARGE  # 距离和充电量的关系系数
DIS_TO_CONSUME_OF_DELIVERY = GP.DIS_TO_CONSUME_OF_DELIVERY  # 运输车辆距离和耗电量的关系系数
DIS_TO_CONSUME_OF_CHARGE = GP.DIS_TO_CONSUME_OF_CHARGE  # 充电车距离和耗电量的关系系数
CHARGE_TO_COST = GP.CHARGE_TO_COST   # 消耗的电量和花费的关系系数，电量 * 系数 = 代价

BATTERY_CAPACITY_OF_DELIVERY = GP.BATTERY_CAPACITY_OF_DELIVERY  # 送货车电池容量
ORGAN_CAPACITY_OF_DELIVERY = GP.ORGAN_CAPACITY_OF_DELIVERY  # 送货车器官容量
SPEED_OF_DELIVERY = GP.SPEED_OF_DELIVERY  # 送货车速度（时间 * 参数 = 距离）
COST_OF_DELIVERY = GP.COST_OF_DELIVERY  # 送货车使用代价

BATTERY_CAPACITY_OF_CHARGE = GP.BATTERY_CAPACITY_OF_CHARGE  # 充电车电池容量
SPEED_OF_CHARGE = GP.SPEED_OF_CHARGE  # 充电车速度
COST_OF_CHARGE = GP.COST_OF_CHARGE  # 充电车使用代价


def get_route_cost(route,instance):
    dis = 0
    for i in range(1,len(route)):
        dis += instance['distance'][i - 1][i]
    route_charge = dis * DIS_TO_CONSUME_OF_DELIVERY
    route_cost = route * CHARGE_TO_COST
    return route_cost


def get_sol_cost(sol,instance):
    cost = 0
    for route in sol:
        cost += get_route_cost(route,instance)
    return cost

def insert_node_to_route(node,route,instance):
    capacity = ORGAN_CAPACITY_OF_DELIVERY
    for nn in route:
        capacity -= instance['need'][nn]
    if(capacity - instance['need'][node] < 0):
        return -1
    Min_cost = 99999999
    Min_pos = -1
    orgion_cost = get_route_cost(route)
    for i in range(1,n + 2):  #可以插入到第 1 个点前到第 n + 1 个点前
        new_cost = orgion_cost - instance['distance'][route[i - 1]][route[i]] + \
                    instance['distance'][route[i -1]][node] + \
                    instance['distance'][node][route[i]]
        
        if(Min_cost > new_cost):
            Min_cost = new_cost
            Min_pos = i
    
    return Min_pos,Min_cost


def get_init_sol(instance):
    new_sol = []
    n = instance['n'][0]
    for i in range(1,n + 1): # 遍历客户点1-n
        pos = -1
        cost = 9999999
        route_index = -1
        for index,route in enumerate(new_sol):
            tmp_pos,tmp_cost = insert_node_to_route(i,route,instance)
            if(tmp_cost < cost):
                cost = tmp_cost
                pos = tmp_pos
                route_index = index
        if pos == -1 or route_index == -1:
            route = []
            route.extend([0,i,n + 1])
            new_sol.append(route)
        else:
            new_sol[route_index].insert(pos,i)

    return new_sol


def remove_bank(bank,sol):
    return [[elem for elem in row if elem not in bank] for row in sol]