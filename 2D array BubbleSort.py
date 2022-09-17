def bubblesort():
    array = [[[]for i in range(2)]for j in range(10)]
    for j in range(10):
        a = random.randint(1,100)
        array[j][1].append(a)

    count = 0
    flag = False
    while not flag:
        flag = True
        for x in range(9-count):
            if array[x][1] > array[x+1][1]:
                temp = array[x][1]
                array[x][1] = array[x+1][1]

                array[x+1][1] = temp
        count = count + 1
    return array