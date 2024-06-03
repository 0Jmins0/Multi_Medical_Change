
def read_txt_to_dict(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()

        type = ''
        distance = []
        need = []
        for line in lines:
            line = line.strip()
            if(len(line) > 0):
                if(line == '[Distance Matrix]'):
                    type = 'Distance Matrix'
                    cnt = 0
                elif(line == '[Pickup]' or line == '[Delivery]'):
                    type = 'node'
                    cnt = 0
                elif(line == '[Ride time]' or line == '[Depot]' or line == '[Speed 0]'):
                    type = ''
                else:
                    if(type == ''):
                        continue
                    parts = line.split(" ")
                    # print(parts)
                    parts = [int(x) for x in parts if len(x) > 0]
                    # print(parts)
                    if(type == 'Distance Matrix'):
                        distance.append(parts)
                    if(type == 'node'):
                        need.append(parts[1])



        instance = {}
        instance['n'] = len(distance)
        instance['need'] = need
        instance['distance'] = distance

    return instance






# 假设文件路径是 'your_file.txt'
file_path = '../hk_data_exmple/101-29.txt'
data = read_txt_to_dict(file_path)