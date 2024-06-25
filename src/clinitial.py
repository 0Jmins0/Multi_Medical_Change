import math

a1 = 0.02
def initcl(instance):
    n = instance['n']
    CL = [[100000 for i in range(n + 2)] for j in range (n + 2)]
    for i in range(0, n + 2):
        for j in range(0, n + 2):
            if i == j:
                continue
            CL[i][j] = instance['distance'][i][j] + \
                       a1 * (math.fabs(instance['need'][i] - instance['need'][j]))
    return CL


