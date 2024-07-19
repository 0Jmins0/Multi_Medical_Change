import Global_Parameter as GP
import Function as F
from Test import evaluate

if __name__ == 'main':
    k = GP.RANDOM_SEED
    p = 2
    for i in range(0, 100):
        deliver_route, charge_route, instance = evaluate(i, k, p)
        tot_cost = F.get_total_cost(deliver_route, charge_route, instance)
