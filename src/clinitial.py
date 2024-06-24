import math

a1 = 0.02
def init(instance):
    n = instance['n']
    CL = [[100000 for i in range(n)] for j in range (n)]
    for i in range(1, n):
        for j in range(1, n):
            if i == j:
                continue
            CL[i][j] = instance['distance'][i][j] + \
                       a1 * (math.fabs(instance['need'][i] - instance['need'][j]))
    return CL
