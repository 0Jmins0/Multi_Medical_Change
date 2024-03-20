import csv
import random
import Global_Parameter

RANDOM_SEED = Global_Parameter.RANDOM_SEED
RANDOM_N_L = Global_Parameter.RANDOM_N_L  # 客户点数量
RANDOM_N_R = Global_Parameter.RANDOM_N_R
RANDOM_ORGAN_L = Global_Parameter.RANDOM_ORGAN_L  # 器官需求数量
RANDOM_ORGAN_R = Global_Parameter.RANDOM_ORGAN_R
RANDOM_DIS_L = Global_Parameter.RANDOM_DIS_L
RANDOM_DIS_R = Global_Parameter.RANDOM_DIS_R


def data_generate(k):
    random.seed(RANDOM_SEED + k)

    n = random.randint(RANDOM_N_L, RANDOM_N_R)
    if k == 0:
        n = 3

    need = []
    for num in range(n):
        cnt = random.randint(RANDOM_ORGAN_L, RANDOM_ORGAN_R)
        medical = [num + 1, cnt]
        need.append(medical)

    distance = []
    for u in range(0, n + 2):
        dis = []
        for v in range(0, n + 2):
            if u == v or (u == 0 and v == n + 1) or (u == n + 1 and v == 0):
                dis.append(0)
            elif v == n + 1:
                dis.append(dis[0])
            elif v > u:
                dis.append(random.randint(RANDOM_DIS_L, RANDOM_DIS_R))
            else:
                dis.append(distance[v][u])
        distance.append(dis)

    file_name = '..\\data\\data' + str(k) + '.csv'
    with open(file_name, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([n])
        writer.writerows(need)
        writer.writerows(distance)


for i in range(50):
    data_generate(i)
