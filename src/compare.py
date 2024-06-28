import Global_Parameter as GP
import random
import time

from LNS import LNS
from Read_Data import read_data_random, read_data_cola
from DP import get_sol_charge
from Draw import draw_compair_of_DP_and_force

def main(instance):

    start_time_all = time.perf_counter()
    sol, cost = LNS(instance)

    start_time_DP = time.perf_counter()
    charge_node = get_sol_charge(sol, instance)
    end_time_DP = time.perf_counter()
    DP_time = end_time_DP - start_time_DP

    end_time_all = time.perf_counter()
    all_time = end_time_all - start_time_all

    start_time_force = time.perf_counter()
    # charge_node_force = get_sol_charge_force(sol, instance)
    end_time_force = time.perf_counter()
    force_time = end_time_force - start_time_force
    print("all time: ", all_time)
    print("DP time: ", DP_time)
    print("Force time: ", force_time)
    return all_time, DP_time, force_time


if __name__ == "__main__":
    k = GP.RANDOM_SEED
    random.seed(k)
    all_time = []
    DP_time = []
    force_time = []
    number = []
    for a in range(0, 100):
        a = str(a)
        # for b in ['', 'B','C']:
        #     a = a + b
        try:
            instance = {}
            # instance = read_data_cola(a)
            # number.append(int(a))
            instance = read_data_random(a)
            number.append(instance['n'])
            A, B, C = main(instance)
            all_time.append(A)
            DP_time.append(B)
            force_time.append(C)

            print(a, "完成")
        except Exception as e:
            continue
    print(number)
    print(all_time, '\n', DP_time, '\n', force_time)
    draw_compair_of_DP_and_force(DP_time, force_time, number)
    # 假设 all_time, DP_time, 和 force_time 已经被定义并包含了数据

    # 打开文件准备写入，使用 'w' 模式，这会创建文件（如果文件不存在的话）或者截断（清空）文件（如果文件已存在的话）
    with open('run_time_random', 'w') as file:

        file.write(', '.join(map(str, number)) + '\n')
        # 写入 DP_time 列表
        file.write(', '.join(map(str, DP_time)) + '\n')
        # 写入 force_time 列表
        file.write(', '.join(map(str, force_time)) + '\n')
        # 写入 all_time 列表，使用 '\n' 来分隔每个元素，然后换行
        file.write(', '.join(map(str, all_time)) + '\n')

    # {'n': 6, 'need': [0, 1, 1, 4, 3, 2, 2, 0], 'distance': [[0, 598, 493, 480, 607, 607, 480, 0], [601, 0, 109, 124, 131, 131, 124, 601], [496, 118, 0, 17, 180, 180, 17, 496], [489, 129, 22, 0, 172, 172, 0, 489], [616, 137, 178, 173, 0, 0, 173, 616], [616, 137, 178, 173, 0, 0, 173, 616], [489, 129, 22, 0, 172, 172, 0, 489], [0, 598, 493, 480, 607, 607, 480, 0]]}
    # {'n': 3, 'need': [['1', '1'], ['2', '1'], ['3', '1']], 'distence': [['0', '19', '2', '3', '0'], ['19', '0', '4', '12', '19'], ['2', '4', '0', '8', '2'], ['3', '12', '8', '0', '3'], ['0', '19', '2', '3', '0']]}
