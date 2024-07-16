import copy
import Global_Parameter as GP

vis = [[0 for i in range(10000)] for j in range(10000)]
ans_cost = 10000000
ans_dis = 10000000
ans_sol = []
check_list = []


def check(eages, instance):
    eages = [item for sub1 in eages for item in sub1]
    sorted_eages = sorted(eages, key=lambda x: (x[0][0], x[1][0]))
    # print("sorted:", sorted_eages)
    charge_sol = []
    init_charge_route = [0, instance['n'] + 1]
    charge_sol.append(init_charge_route)
    car_local = [0]  # 路线0的充电车目前的终点为 0
    car_time = [0]  # 路线0的充电车可以结束当前路线的时间
    car_battery = [GP.BATTERY_CAPACITY_OF_CHARGE]  # 路线0的充电车剩余的电量
    speed = GP.SPEED_OF_CHARGE
    tot_dis = 0
    for eage in sorted_eages:
        u = eage[0][1]
        v = eage[1][1]
        time_u = eage[0][0]
        time_v = eage[1][0]
        ok = 0
        for idx, charge_route in enumerate(charge_sol):
            now_time = car_time[idx]
            now_local = car_local[idx]
            dis = instance['distance'][now_local][u]
            charge_consume = instance['distance'][u][v] * GP.DIS_TO_CHARGE
            remain_charge = car_battery[idx]
            acc_time = time_u - now_time
            acc_dis = acc_time * speed
            if dis <= acc_dis and charge_consume <= remain_charge:
                ok = 1
                if u != charge_sol[idx][-2]:
                    charge_sol[idx].insert(len(charge_sol[idx]) - 1, u)
                if v != charge_sol[idx][-1]:
                    charge_sol[idx].insert(len(charge_sol[idx]) - 1, v)

                car_local[idx] = v
                car_time[idx] = time_v
                car_battery[idx] -= charge_consume
                tot_dis += dis + instance['distance'][u][v]
                break
        if ok == 0:
            charge_route = [0, instance['n'] + 1]
            if u != charge_route[-2]:
                charge_route.insert(len(charge_route) - 1, u)
            if v != charge_route[-1]:
                charge_route.insert(len(charge_route) - 1, v)
            charge_sol.append(charge_route)
            charge_consume = instance['distance'][u][v] * GP.DIS_TO_CHARGE
            car_local.append(v)
            car_time.append(time_v)
            car_battery.append(GP.BATTERY_CAPACITY_OF_CHARGE - charge_consume)

    return len(charge_sol) * GP.COST_OF_CHARGE, tot_dis, charge_sol


def dfs(charge_node, instance, pos, eage):
    global ans_cost, vis, check_list, ans_sol, ans_dis
    if pos >= len(charge_node):
        # if eage in check_list:
        #     print("wrong!!!")

        if len(eage) != 0:
            # check_list.append(copy.deepcopy(eage))
            tmp_cost, tmp_dis, tmp_sol = check(eage, instance)
            print("tmp", tmp_cost, tmp_sol)
            if tmp_cost == ans_cost and tmp_dis < ans_dis :
                ans_sol = tmp_sol
                ans_dis = tmp_dis

            if (tmp_cost < ans_cost):
                ans_cost = tmp_cost
                ans_sol = copy.deepcopy(tmp_sol)
                ans_dis = tmp_dis

        # if len(check_list) % 10000 == 0:
        #     print(len(check_list))
        # print(len(check_list))
        # print("check_list", check_list)
        # print("ans_cost", ans_cost)
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
    global ans_cost, check_list, vis, ans_sol, ans_dis
    ans_cost = 10000000
    ans_dis = 10000000
    ans_sol = []
    vis = [[0 for i in range(10000)] for j in range(10000)]
    print("get_charge_route")
    print(charge_node)
    # flat_charge_node = [item for sublist1 in charge_node for sublist2 in sublist1 for item in sublist2]
    # sorted_list = sorted(flat_charge_node, key=lambda x: x[0][0])
    dfs(charge_node, instance, 0, [])
    # print("答案数量：", len(check_list))
    # print(check_list)
    return ans_cost, ans_sol
