### **主要关于时间维度的Gurobi问题**

如果不用时间维度，那么无法控制充电车出现在每一个边为不同运输车充电的顺序

如果使用时间维度，那么整个问题都需要重新编写

最好的解决方案是加入一些Constraint使得充电车的充电顺序可控

运输车到达时间、充电车到达时间

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

1. 所有点的集合：$I$ ，所有医院：$I'$， 所有医院加上起点：$I^0$，所有医院加上终点：$I^{n+1}$​
   1. 在Gurobi中可以直接表示为：
   2. 所有医院：`I[1:-1]`，所有医院加上起点：`I[:-1]`，所有医院加上终点：`I[1:]`

2. 送货车距离和代价的关系系数：$K_t$
3. 距离和充电量的关系系数：$\gamma$
4. 距离和耗电量的关系系数
   1. 运输车距离和耗电量的关系：$1$
   2. 充电车距离和耗电量的关系： $\phi$ 

#### 送货车参数

1. 电池容量：$\rho$
2. 器官容量：$Q$​
3. 速度参数：TBC
4. 使用代价：$K_v$

#### 充电车参数

1. 电池容量：$\beta$​
2. 速度参数：TBC
3. 使用代价：$K_c$​

### **三.变量**

#### **决策变量**

1. 送货车数量：$K$​ 
2. 充电车数量：$B$
3. 送货车出发携带的数量：$U_k$
4. 送货车是否到达任一医院：$y_{ik}$​
5. 送货车是否经过任一路径：$x_{ijk}$
6. 充电车是否到达任一医院：$w_{ib}$
7. 充电车是否独自经过任一路径：$z_{ijb}$
8. 充电车是否与运输车连接经过任一路径：$\delta_{ijkb}$

#### **状态变量**

1. 送货车在任一点的电量：$u_{ik}$
2. 充电车在任一点的电量：$v_{ib}$
3. 送货车到达任一点的时间：$tk_{ik}$
4. 充电车到达任一点的时间：$tb_{ib}$​

### **四. 限制条件**

#### 容量限制

1. 送货车携带数量不超过最大容量：$U_k\leq Q$
2. 送货车所有送货的点的需求相加等于携带数量：$\sum_{i\in I'}y_{ik}d_i= U_k$

#### 时间限制（速度参数TBC）

1. 送货车到达某一点的时间等于到达前一点的时间+两点间距离：$tk_{jk}=\sum_{i\in I} x_{ijk} (tk_{ik}+c_{ij})$
2. 充电车到达某一点的时间等于：用一个大数 $m$ 只需要在它成立的时候作用
   1. 如果充电车独自到达走过了上一条边：$tb_{jb}=\sum_{i\in I} z_{ijb}(tb_{ib}+c_{ij})$
   2. 如果充电车与运输车相连走过了上一条边：$tb_{jb}=\sum_{i\in I}\delta_{ijbk}tk_{jk}$
3. 如果充电车需要与运输车相连，那么它需要提前到达等候运输车：$(\sum_{j\in I}\delta_{ijkb}) tb_{ib}\leq tk_{ik}$ 

4. 运输车与充电车的初始化：$tb_{ib}=0$ and $tk_{ik}=0$​

#### 电量限制

1. 送货车电量为上一点电量减去上一边的消耗加上充电量：$u_{jk} = \sum_{i \in I} x_{ijk} (u_{ik} - c_{ij} + \gamma \sum_{b \in \mathcal{B}} \delta_{ijkb} c_{ij})$
2. 充电车电量更新：
   1. 如果充电车独自到达走过了上一条边：$v_{jb}=\sum_{i\in I}z_{ijb}(v_{ib}-\phi c_{ij})$
   2. 如果充电车与运输车相连走过了上一条边：$v_{jb}=\sum_{i\in I}\sum_{k\in K}\delta_{ijkb}(v_{ib}-\gamma c_{ij})$
3. 送货车和充电车的电量不能低于0：$u_{ik}\geq0$ and $v_{ib}\geq0$
4. 送货车的电量不能超过电池容量：$u_{ik}\leq\rho$
5. 送货车和充电车的电量初始化（暂定起点为0）：$u_{0k}=\rho$ and $v_{0b}=\beta$

#### 送货车路径限制

1. 所有需求点必须全部被访问（访问即满足）：$\sum_{i \in{I'}}\sum_{k\in K}y_{ik}=|I'|$
2. 送货车路径成环：$\sum_{j \in{I}^{n+1}} x_{ijk} = \sum_{j \in {I}^0} x_{jik} = y_{ik}$​
3. 送货车起点终点：$\sum_{j \in{I}^{n+1} } x_{0jk} = \sum_{j \in{I}^{0}} x_{j0k} = y_{0k} = 1$​​
   1. 因为有限制2的存在应该也可以写成：$y_{0k}=y_{(n+1)k}=1$
4. 每个点有且仅有一辆送货车访问（可覆盖限制1）：$\sum_{k\in K}y_{ik}=1$​
5. 送货车如果连接充电车，必须访问对应边：$\sum_{b\in\beta}\delta_{ijkb}\leq x_{ijk}$​
6. 送货车不可以从$(n+1)$点出发或者到达$0$点：$\sum_{i\in I}x_{i(0)k}=\sum_{i\in I}x_{(n+1)ik}=0$

#### 充电车路径限制

1. 所有充电车必须访问点才能被运输车连接：$\sum_{k\in K}\delta_{ijkb}\leq w_{ib}$ and $\sum_{k\in K}\delta_{ijkb}\leq w_{jb}$
2. 充电车路线成环：$\sum_{k\in K}\sum_{j \in{I}^{n+1}} (z_{ijb}+\delta_{ijkb}) = \sum_{k\in K}\sum_{j \in{I}^{0}} (z_{jib}+\delta_{jikb}) = w_{ib}$​
3. 充电车起点终点：$\sum_{k\in K}\sum_{j \in{I}^{n+1} } (z_{0jb}+\delta_{0jkb}) = \sum_{k\in K}\sum_{j \in{I}^{0}}(z_{j0b}+\delta_{j0kb}) = w_{0b} = 1$
   1. 因为有限制2的存在应该也可以写成：$w_{0b}=w_{(n+1)b}=1$
4. 同一辆充电车仅可在一条边上用一种方式走（已被2覆盖）

# 未解决问题

1. 如何处理充电量的非线形：当充电量超过电池容量时，自动停止充电，那么运输车剩余电量将会是 $u\gets min{(\rho,u+\gamma\delta)}$​​
   1. 常见mathematical representation: 
   2. 增加一个constraint比较普遍
   3. Gurobi可以接受 $min$ 函数
2. 充电车的放置问题：是否将充电车放置在各个医院，还是将充电车放置在送货车起始点，还是为**充电车设置自己的起始点**
3. Variable可以是一个range吗, $K$ and $B$​ ？
   1. `for k in K`













# **启发式部分算法 by Xinyue**



![image-20240316100130782](/Users/guyizhou/Library/Application Support/typora-user-images/image-20240316100130782.png)

#### LNS+LS 部分

inital solution $\to$ 迭代，破坏当前的solution

![image-20240316100523689](/Users/guyizhou/Library/Application Support/typora-user-images/image-20240316100523689.png)

![image-20240316100605167](/Users/guyizhou/Library/Application Support/typora-user-images/image-20240316100605167.png)

![image-20240316100647965](/Users/guyizhou/Library/Application Support/typora-user-images/image-20240316100647965.png)



求出来一个解

#### LS

![image-20240316100816865](/Users/guyizhou/Library/Application Support/typora-user-images/image-20240316100816865.png)

#### DP

![image-20240316101129749](/Users/guyizhou/Library/Application Support/typora-user-images/image-20240316101129749.png)

![image-20240316102539162](/Users/guyizhou/Library/Application Support/typora-user-images/image-20240316102539162.png)

