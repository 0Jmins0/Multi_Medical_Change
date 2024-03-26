import csv

def read_data(p):
    other = '../data/data' + str(p) + '.csv'
    instance = {}
    csv_data = []
    with open(other, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            csv_data.append(row)
        n = int(csv_data[0][0])
        instance['n'] = n
        instance['need'] = csv_data[1:n+1]  # Extract need data
        instance['distence'] = csv_data[n+1:]  # Extract discharge data
    return instance

print(read_data(0))
