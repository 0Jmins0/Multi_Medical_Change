import numpy as np
import Global_Parameter as GP
import time
import DP

def get_sol_charge_force(sol, instance):
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
        charge_node = DP.get_charge_node(f, dis)
        # print("after_get", charge_node)
        charge_node = DP.remove_dup(charge_node)
        # print("after_remove", charge_node)

        charge_node = [DP.get_binary(x) for x in charge_node]
        # print("after_bin", charge_node)
        charge_node = DP.auto_completion(charge_node, route)
        # print("after_com", charge_node)
        charge_node = DP.get_time_node(charge_node, route, Time)
        charge_list.append(charge_node)

    return charge_list

