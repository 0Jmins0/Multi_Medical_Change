import random
import time
from DP import get_sol_charge
from Read_Data import read_data_random
from Force import get_sol_charge_force
from Draw import ddd
def get_compare_data():
    random.seed(7777)
    a = 1314
    instance = read_data_random(str(a))
    n = instance['n']
    number = []
    DP_time = []
    force_time = []
    for i in [5, 9, 12, 15, 17, 18, 20, 21, 22, 23]:
        route = random.sample(range(1, n), i)
        print(len(route), route)
        sol = [route]

        print("DP begin")
        start_time_DP = time.perf_counter()
        get_sol_charge(sol, instance)
        end_time_DP = time.perf_counter()
        run_time_DP = end_time_DP - start_time_DP
        print("DP end", run_time_DP)

        print("force begin")
        start_time_force = time.perf_counter()
        get_sol_charge_force(sol, instance)
        end_time_force = time.perf_counter()
        run_time_force = end_time_force - start_time_force
        print("force end", run_time_force)

        print("\n run_time_force / run_time_DP:", run_time_force / run_time_DP)
        number.append(str(i))
        DP_time.append(run_time_DP)
        force_time.append(run_time_force)

    print(DP_time, '\n', force_time, '\n')
    with open('run_time_DP_route', 'w') as file:

        file.write(', '.join(map(str, number)) + '\n')
        # 写入 DP_time 列表
        file.write(', '.join(map(str, DP_time)) + '\n')
        # 写入 force_time 列表
        file.write(', '.join(map(str, force_time)) + '\n')


if __name__ == '__main__':
    get_compare_data()
    ddd()