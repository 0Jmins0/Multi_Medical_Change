import Global_Parameter as GP
import Function as FC

LOCAL_OPERATOR_POOL = GP.LOCAL_OPERATOR_POOL  # 邻域操作池

def LS(new_sol,instance):
    op_id = 0
    k = 0
    new_cost = FC.get_sol_cost(new_sol,instance)
    while(k < len(LOCAL_OPERATOR_POOL)):
        tmp_sol,tmp_cost = LS_OP(new_sol,instance)
        if(tmp_cost < new_cost):
            new_sol = tmp_sol
            new_cost = tmp_cost
            k = 0
        else k ++
        pos = (pos + 1) % len(LOCAL_OPERATOR_POOL)
    return new_sol,new_cost