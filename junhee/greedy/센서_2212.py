N = int(input())
K = int(input())
if N <= K:
    print(0)
else :
    dis_sum = 0
    distance = []
    sensor = list(set(map(int, input().split())))
    if len(sensor)<=K:
        print(0)
    else:
        sensor.sort()
        for i in range(len(sensor)-1):
            distance.append(sensor[i+1]-sensor[i])

        distance = sorted(distance, reverse=True)

        for i in range(K-1):
            dis_sum += distance[i]

        print(sensor[-1]-sensor[0]-dis_sum)