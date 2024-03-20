### **一. 输入**

1. 第一行，一个数字 $n$ 表示送货医院的数量
2. 接下来 $n$ 行，每行有两个数字 $number, cnt$ 分别表示医院的编号和需求的器官数量$i\in I, d(i)$ `i, d[i]`
3. 接下来，一个 $(n+1)*(n+1)$的对称矩阵 $c$，`c[i][j]==c[j][i]` 表示点$i\to j$ ($j\to i$)的距离（0表示送货车和充电车的仓库）

### **二.问题设定**

1. 所有客户点都可以完成
2. 充电车从仓库出发，回到仓库
3. 充电车可以自己走，也可以跟运输车连接一起走
4. 充电车和送货车数量数无限（用来保证 1.）
   1. 送货车数量 $K$
   2. 充电车数量 $B$
5. 充电车和送货车的电量是有限的（充电车行驶的电量是无限的，可以充电的电量是有限的）
6. 送货车和充电车仓库在一起
   1. OAC仓库`I[0]`和`I[n+1]` 

#### **目标函数**

1. 送货车的距离代价：$K_t\sum_{(i,j)\in A}\sum_{k\in K}x_{ijk}c_{ij}$
2. 送货车的使用代价：$K_vK$
3. 充电车的使用代价：$K_cB$

#### **全局参数**

1. 送货车距离和代价的关系系数 (`DIS_TO_COST`) ：$K_t$
2. 距离和充电量的关系系数 (`DIS_TO_CHARGE`) ：$\gamma$
3. 距离和耗电量的关系系数
   1. 运输车距离和耗电量的关系  (`DIS_TO_CONSUME_OF_DELIVERY`) ：$1$
   2. 充电车距离和耗电量的关系  (`DIS_TO_CONSUME_OF_CHARGE`) ： $\phi$ 

#### 送货车参数

1. 电池容量 (`BATTERY_CAPACITY_OF_DELIVERY`) ：$\rho$
2. 器官容量 (`ORGAN_CAPACITY_OF_DELIVERY`)  ：$Q$​
3. 速度参数 (`SPEED_OF_DELIVERY`) ：TBC
4. 使用代价 (`COST_OF_DELIVERY`) ：$K_v$

#### 充电车参数

1. 电池容量 (`BATTERY_CAPACITY_OF_CHARGE`)：$\beta$​
2. 速度参数 (`SPEED_OF_CHARGE`) ：TBC
3. 使用代价 (`COST_OF_CHARGE`) ：$K_c$


