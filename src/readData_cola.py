def read_data(datain):
    vehicle = 20
    Penalty = 5
    capacityVechicle = 1000
    maxdistrip = 200
    Depots = []
    speedprofile = []
    mu, lamda = 9, 17
    pc, pe, arfa = 0.6, 0.5, 0.4

    sumq = 0
    pickups = []
    num_pair = 0
    speedMatrix = []
    Cluster = 0
    dis = []
    # global  NumVechicle,capacityVechicle,maxdistrip,Depots,pickups,num_pair,speedMatrix,speedprofile,Cluster,sumq
    st = '../cola/'
    st = st + datain + '.txt'
    with open(st, 'r', encoding='utf8') as f:
        cont = True
        c = 0
        li = []
        flag = 0
        pickups.append(({}))
        while cont:
            cont = f.readline()
            li.append(cont.split())
            li = [x for x in li if x != []]
            # print(li)
            if cont == '\n' and li != []:
                c = c + 1
                if c == 1:
                    num_pair = int(li[0][0])
                    capacityVechicle = 250  # float(li[1][0])
                    maxdistrip = 200  # float(li[2][0])

                elif li[0][0] == "[Node]" or li[0][0] == "[node]":
                    for i in li[1:]:
                        Depots.append(({
                            "idx": int(i[0]),
                            "x": float(i[1]),
                            "y": float(i[2])
                        }))
                    # print("Depots",Depots)
                elif li[0][0] == "[pickup]" or li[0][0] == "[Pickup]":
                    for i in li[1:]:
                        pickups.append(({
                            "idx": int(i[0]),
                            "ID": int(i[1]),
                            "load": float(i[2]),
                            # "servtime": float(i[3])
                        }))


                elif li[0][1] == "choose":
                    for i in li[1:]:
                        speedMatrix.append([int(s) for s in i])
                li = []
    # print(speedMatrix)
    Cluster = int(sumq // capacityVechicle) + 1
    # print(len(speedMatrix))
    mp = {}
    with open('../cola/Customer2ID.txt', 'r', encoding='utf8') as f:
        cont = True
        li = []
        while cont:
            cont = f.readline()
            li = []
            li.append(cont.split())
            li = [x for x in li if x != []]
            if li != []:
                mp[int(li[0][0])] = int(li[0][1])
    DisT = [[0 for _ in range(2000)] for i in range(2000)]
    # print(len(DisT[1]))
    with open('../cola/ODMatrix.txt', 'r', encoding='utf8') as f:
        cont = True
        li = []
        while cont:
            cont = f.readline()
            li = []
            li.append(cont.split())
            li = [x for x in li if x != []]
            if li != []:
                DisT[int(li[0][0])][int(li[0][1])] = float(li[0][2])
    # print("dd", DisT[1][7])
    # print("dd",DisT[1][7])
    # global dis
    dis = [[0 for i in range(num_pair + 2)] for j in range(num_pair + 2)]
    # print(mp[504558778],mp[504557490],DisT[1184] [1180])
    for i in range(0, num_pair + 2):
        if i == 0 or i == num_pair + 1:
            idx = 1
        else:
            idx = mp[pickups[i]["ID"]]
        for j in range(0, num_pair + 2):
            if j == 0 or j == num_pair + 1:
                jdx = 1
            else:
                jdx = mp[pickups[j]["ID"]]
            # if idx == 1 and jdx == 7: print(i,j,idx,jdx,DisT[1][7])
            dis[i][j] = max(DisT[idx][jdx], 0.0000000001)
            # if dis[i][j] == 0.0000000001:
            # print(i,j)

    # print(dis[1])
    long = {}
    with open('../cola/long', 'r', encoding='utf8') as f:
        cont = True
        li = []
        while cont:
            cont = f.readline()
            li = []
            li.append(cont.split())
            li = [x for x in li if x != []]
            if li != []:
                long[int(li[0][0])] = [float(li[0][-2]), float(li[0][-1])]
    for i in range(1, len(pickups)):
        pickups[i]["x"] = long[pickups[i]["ID"]][0]
        pickups[i]["y"] = long[pickups[i]["ID"]][1]
        # print("i = ", i, pickups[i])

    n = len(pickups) - 1
    loads = []
    loads.append(0)
    loads.extend([int(pickups[i]['load']) % 4 + 1 for i in range(1, n + 1)])
    loads.append(0)
    dis_matrix = [[round(d[i]) for i in range(n + 2)] for d in dis]

    # print(n)  # 客户点数量
    # print(loads)  # [[0, 0], [1, 24], [2, 25], [3, 38], [4, 48], [5, 48], [6, 50], [7, 56],,,,]
    # print(dis_matrix)  # [[0, 59839, 49142, 49255,,,,][60106, 0, 10759, 10872,,,,,]]
    instance = {}
    instance['n'] = n
    instance['need'] = loads
    instance['distance'] = dis_matrix
    return instance



# list = [30, 41, 43, 44,51, 53, 54, 57, 59, ]
# while True:
#     print("data: ")
#     datain = str(input())

# read_data(str(30))