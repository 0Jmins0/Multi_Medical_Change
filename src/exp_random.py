import Global_Parameter as GP
from Test import evaluate
import csv

# 定义变量名称和值
global_variables = {
    'DIS_TO_COST': GP.DIS_TO_COST,
    'DIS_TO_CONSUME_OF_DELIVERY': GP.DIS_TO_CONSUME_OF_DELIVERY,
    'CHARGE_CONSUME': GP.CHARGE_CONSUME,
    'DIS_TO_CHARGE': GP.DIS_TO_CHARGE,
    'BATTERY_CAPACITY_OF_DELIVERY': GP.BATTERY_CAPACITY_OF_DELIVERY,
    'ORGAN_CAPACITY_OF_DELIVERY': GP.ORGAN_CAPACITY_OF_DELIVERY,
    'SPEED_OF_DELIVERY': GP.SPEED_OF_DELIVERY,
    'COST_OF_DELIVERY': GP.COST_OF_DELIVERY,
    'BATTERY_CAPACITY_OF_CHARGE': GP.BATTERY_CAPACITY_OF_CHARGE,
    'SPEED_OF_CHARGE': GP.SPEED_OF_CHARGE,
    'COST_OF_CHARGE': GP.COST_OF_CHARGE
}

if __name__ == '__main__':
    k = GP.RANDOM_SEED
    p = 2
    lines = []
    with open(GP.OUTPUT_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        global_keys = list(global_variables.keys())
        global_values = list(global_variables.values())
        header = ['点的数量', 'cost', '运行时间', '最佳解轮数', 'tot_T']
        # writer.writerow(global_keys)
        # writer.writerow(global_values)
        # writer.writerow(header)
        for i in range(24, 26):
            print("running", i)
            best_deliver_sol, best_deliver_cost, best_charge_sol, \
                best_tot_cost, best_T, run_time, instance, tot_T = evaluate(i, k, p)
            line = [i, best_tot_cost, run_time, best_T, tot_T]
            writer.writerow(line)
