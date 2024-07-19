import matplotlib.pyplot as plt
def draw_compair_of_DP_and_force(DP_time,force_time, number):
    # 绘制折线图
    plt.figure(figsize=(10, 5))  # 可以设置图像大小

    # 绘制第一条折线
    plt.plot(number, DP_time, label='DP Time', marker='o')

    # 绘制第二条折线
    plt.plot(number, force_time, label='Force Time', marker='s')

    # 添加图例
    plt.legend()

    # 添加标题和轴标签
    plt.title('Comparison of DP Time and Force Time')
    plt.xlabel('Index')  # 因为横坐标是均匀分布的，所以这里使用索引作为标签
    plt.ylabel('Time')

    # 设置x轴的范围，确保它覆盖所有number的值
    plt.xlim([min(number) - 1, max(number) + 1])

    # 设置x轴的刻度位置，使其均匀分布
    plt.xticks(number)

    # 可以添加网格
    plt.grid(True)

    # 展示图表
    plt.show()

def ddd():
    # 假设你的文件名为 'data.txt'，并且它的内容是按照你的描述组织的
    filename = 'run_time_DP_route'
    # filename = 'run_time_random'

    # 初始化空列表来存储数据
    numbers = []
    DP_time = []
    force_time = []

    # 打开文件并读取每一行
    with open(filename, 'r') as file:
        for i, line in enumerate(file):
            # 移除行尾的换行符并分割行以获取数据点
            data_points = line.strip().split(',')

            # 根据文件中的数据顺序，将数据点转换为浮点数并添加到相应的列表
            if i == 0:
                numbers = list(map(float, data_points))
            elif i == 1:
                DP_time = list(map(float, data_points))
            elif i == 2:
                force_time = list(map(float, data_points))

    # 确保所有列表长度相同
    assert len(numbers) == len(DP_time) == len(force_time)


    # 创建一个元组列表，每个元组包含 (number, DP_time, force_time, all_time)
    data = list(zip(numbers, DP_time, force_time))

    # 根据 force_time / DP_time 的值进行排序
    # 由于 DP_time 可能为 0，我们需要处理除以零的情况
    # 按照比例排序
    # sorted_data = sorted(data, key=lambda x: (x[1] == 0, x[2] / x[1]))
    # 按照点的数量排序
    # sorted_data = sorted(data, key=lambda x: x[0])
    sorted_data = data
    # delete_list = [110, 114, 106, 93, 121]
    delete_list = []
    # 使用列表推导式删除所有 number 元素等于 '110' 的元组
    sorted_data = [item for item in sorted_data if item[0] not in delete_list]

    # 现在，filtered_data 包含了所有不包含 '110' 的元组
    # 排序后的数据
    sorted_numbers, sorted_DP_time, sorted_force_time = zip(*sorted_data)

    sorted_numbers = [str(int(i)) for i in sorted_numbers]
    # sorted_DP_time = [i * 1000 for i in sorted_DP_time]
    # sorted_force_time = [i * 1000 for i in sorted_force_time]

    bi = [force_time_p / DP_time_p for force_time_p, DP_time_p in zip(sorted_force_time, sorted_DP_time)]
    # print(bi)

    # 绘制折线图
    import matplotlib.pyplot as plt

    # 绘制折线图
    plt.figure(figsize=(10, 5))

    # 绘制 DP_time 和 force_time 的折线图
    plt.plot(sorted_numbers, sorted_DP_time, label='DP Time', marker='o', color='blue')
    plt.plot(sorted_numbers, sorted_force_time, label='Force Time', marker='s', color='green')
    # plt.plot(sorted_numbers, bi, label='Force Time/DP_time', marker='s', color='red')

    # 添加图例
    plt.legend()

    # 添加标题和轴标签
    plt.title('Sorted DP Time and Force Time')
    plt.xlabel('Index')  # 使用索引作为标签
    plt.ylabel('Time')

    # 标注DP_time / force_time的倍数关系
    # for i, (dp, ft) in enumerate(zip(sorted_DP_time, sorted_force_time)):
    #     if ft != 0:  # 避免除以零
    #         ratio = dp / ft
    #     else:
    #         ratio = float('inf')  # 如果force_time为0，则倍数设置为无穷大
    #     # 在每个数据点的上方添加文本标注倍数关系
    #     plt.text(sorted_numbers[i], plt.ylim()[1], f'Ratio: {ratio:.2f}',
    #              ha='center', va='top', fontsize=9, color='red')

    # 自动调整x轴标签的旋转以防止重叠
    plt.xticks(rotation=45)

    # 展示图表
    plt.show()



def draw_sol(sol, instance):
