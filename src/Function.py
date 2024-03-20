import Global_Parameter as GP
DIS_TO_COST = GP.DIS_TO_COST  # 送货车距离和代价的关系系数，距离 * 系数 = 代价
DIS_TO_CHARGE = GP.DIS_TO_CHARGE  # 距离和充电量的关系系数
DIS_TO_CONSUME_OF_DELIVERY = GP.DIS_TO_CONSUME_OF_DELIVERY  # 运输车辆距离和耗电量的关系系数
DIS_TO_CONSUME_OF_CHARGE = GP.DIS_TO_CONSUME_OF_CHARGE  # 充电车距离和耗电量的关系系数

BATTERY_CAPACITY_OF_DELIVERY = GP.BATTERY_CAPACITY_OF_DELIVERY  # 送货车电池容量
ORGAN_CAPACITY_OF_DELIVERY = GP.ORGAN_CAPACITY_OF_DELIVERY  # 送货车器官容量
SPEED_OF_DELIVERY = GP.SPEED_OF_DELIVERY  # 送货车速度（时间 * 参数 = 距离）
COST_OF_DELIVERY = GP.COST_OF_DELIVERY  # 送货车使用代价

BATTERY_CAPACITY_OF_CHARGE = GP.BATTERY_CAPACITY_OF_CHARGE  # 充电车电池容量
SPEED_OF_CHARGE = GP.SPEED_OF_CHARGE  # 充电车速度
COST_OF_CHARGE = GP.COST_OF_CHARGE  # 充电车使用代价


def get_route_cost(route):
    pass


def get_sol_cost(sol):
    pass


def get_init_sol(instance):
    pass


def remove_bank(bank,sol):
    pass