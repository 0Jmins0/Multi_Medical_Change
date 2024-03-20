DIS_TO_COST = 1  # 送货车距离和代价的关系系数，距离 * 系数 = 代价
DIS_TO_CHARGE = 1  # 距离和充电量的关系系数
DIS_TO_CONSUME_OF_DELIVERY = 1  # 运输车辆距离和耗电量的关系系数
DIS_TO_CONSUME_OF_CHARGE = 1  # 充电车距离和耗电量的关系系数

BATTERY_CAPACITY_OF_DELIVERY = 100  # 送货车电池容量
ORGAN_CAPACITY_OF_DELIVERY = 10  # 送货车器官容量
SPEED_OF_DELIVERY = 1  # 送货车速度（时间 * 参数 = 距离）
COST_OF_DELIVERY = 10000  # 送货车使用代价

BATTERY_CAPACITY_OF_CHARGE = 1000  # 充电车电池容量
SPEED_OF_CHARGE = 10  # 充电车速度
COST_OF_CHARGE = 10000  # 充电车使用代价

REMOVE_POOL = [1, 2, 3, 4]  # 删除操作池
INSERT_POOL = [1]  # 插入操作池
LOCAL_OPERATOR_POOL = [1, 2, 3, 4, 5]  # 邻域操作池

# 随机数据生成范围
RANDOM_SEED = 1234

RANDOM_N_L = 5  # 客户点数量
RANDOM_N_R = 50

RANDOM_ORGAN_L = 1  # 器官需求数量
RANDOM_ORGAN_R = 5

RANDOM_DIS_L = 1  # 任意两点距离
RANDOM_DIS_R = 20
