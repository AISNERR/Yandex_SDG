from collections import deque
import random

def what_robot(koordinates, ox, oy, maze, nnn , ttt):
    a = []
    for xyz in range(len(koordinates)):
        if maze[koordinates[xyz][0]][koordinates[xyz][1]] != 1:
            a.append(find_path_bfs03(maze, koordinates[xyz], ox, oy))
    ttt = 0
    if a:
        nnn = len(a[0])
        for i in range(len(a)):
            if len(a[i]) < nnn:
                ttt = i
                nnn = len(a[i])
    else:
        index = ttt
        return koordinates[ttt]
    index = ttt
    return koordinates[ttt]

def randomizer(n, MTips, Cost, T, D):
    if MTips > Cost:
        if D > T and 103 >= n >= 4:
            return n - 3
        elif D > T and n <= 4:
            return 1
        elif D == T and 103 >= n >= 16:
            return n - 32
        elif D == T and 16 >= n >= 4:
            return 1
        elif D == T and n >= 103:
            if MTips > Cost // 2:
                return 25
            elif MTips > Cost // 4:
                return 50
            elif MTips > Cost // 8:
                return 75
            else:
                return random.randint(75, 100)
        elif D < T:
            return n // 2 - 1
        else:
            return random.randint(75, 100)
    else:
        if MTips <= Cost // 2:
            if 4 <= n <= 50:
                return random.randint(1, 5)
            elif 4 <= n <= 50:
                return random.randint(5, 15)
            elif n < 4:
                return 1
            else:
                return random.randint(15, 30)
        elif MTips <= Cost // 4:
            if 4 <= n <= 50:
                return random.randint(1, 20)
            elif 50 <= n <= 70:
                return random.randint(20, 30)
            elif n < 4:
                return 1
            else:
                return random.randint(30, 50)

def create_koordinates(maze, map_size):
    x1, y1 = random.randint(1, map_size), random.randint(1, map_size)
    if maze[x1][y1] == 1:
        create_koordinates(maze, map_size)
    else:
        return x1, y1

def randomizer_core(robots, map_size, maze):
    koordinates_rob = []
    x1, y1 = 0, 0
    for item in range(robots):
        x1, y1 = create_koordinates(maze, map_size)
        koordinates_rob.append([x1, y1])
    return koordinates_rob

def maze2graph(maze):
    height = len(maze)
    width = len(maze[0]) if height else 0
    graph = {(i, j): [] for j in range(width) for i in range(height) if not maze[i][j]}
    for row, col in graph.keys():
        if row < height - 1 and not maze[row + 1][col]:
            graph[(row, col)].append(("D", (row + 1, col)))
            graph[(row + 1, col)].append(("U", (row, col)))
        if col < width - 1 and not maze[row][col + 1]:
            graph[(row, col)].append(("R", (row, col + 1)))
            graph[(row, col + 1)].append(("L", (row, col)))
    return graph

def find_path_bfs(maze, arr):
    if ((arr[0][2] + 1) == (arr[1][0] + 1)) and ((arr[0][3] + 1) == (arr[1][1] + 1)):
        start, goal = (arr[1][0] + 1, arr[1][1] + 1), (arr[1][2] + 1, arr[1][3] + 1)
        queue = deque([("", start)])
        visited = set()
        graph = maze2graph(maze)
        while queue:
            path, current = queue.popleft()
            if current == goal:
                return 'T' + path + 'P'
            if current in visited:
                continue
            visited.add(current)
            for direction, neighbour in graph[current]:
                queue.append((path + direction, neighbour))
        return "NO WAY!"
    else:
        start, goal = (arr[1][0] + 1, arr[1][1] + 1), (arr[1][2] + 1, arr[1][3] + 1)
        queue = deque([("", start)])
        visited = set()
        graph = maze2graph(maze)
        while queue:
            path, current = queue.popleft()
            if current == goal:
                return find_path_bfs02(maze, arr) + 'T' + path + 'P'
            if current in visited:
                continue
            visited.add(current)
            for direction, neighbour in graph[current]:
                queue.append((path + direction, neighbour))
        return "NO WAY!"

def find_path_bfs02(maze, arr):
    start, goal = (arr[0][2] + 1, arr[0][3] + 1), (arr[1][0] + 1, arr[1][1] + 1)
    queue = deque([("", start)])
    visited = set()
    graph = maze2graph(maze)
    while queue:
        path, current = queue.popleft()
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for direction, neighbour in graph[current]:
            queue.append((path + direction, neighbour))
    return "NO WAY!"

def find_path_bfs03(maze, arrik, x1, y1):
    start, goal = (arrik[0], arrik[1]), (x1 + 1, y1 + 1)
    queue = deque([("", start)])
    visited = set()
    graph = maze2graph(maze)
    while queue:
        path, current = queue.popleft()
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for direction, neighbour in graph[current]:
            queue.append((path + direction, neighbour))
    return "NO WAY!"

#input
N, MaxTips, Cost_C = map(int, input().split())
listOne = str([list(map(str, input().split())) for i in range(N)])
#creation new array for working
arr = []
for j in range(len(listOne)):
    #for j in range(len(listOne[i])):
        if listOne[j] == '#':
            arr.append(1)
        elif listOne[j] == '.':
            arr.append(0)
m = N
newArr = [[arr[i] for i in range(j * m, j * m + m)] for j in range(m)]
for t in range(len(newArr)):
        newArr[t].insert(0, 1)
        newArr[t].append(1)
newArr.append([1] * (N + 2))
newArr.insert(0, [1] * (N + 2))
#input
T, D = map(int, input().split())  # amount of iterations, amount of delivery, amount robots in the city
R = randomizer(N, MaxTips, Cost_C, T, D)  # amount of robort
xy = randomizer_core(R, N, newArr)
print(R)  #do not delete
tutu = [[0, 0, 0, 0]]
magic = []#additional array
for count in xy:
    print(*count)  #do not delete
keep_coordinats = []
global res
res = [] # the path from one delivery
length_mas = 0  # the length of array
maxik = 0
maxik02 = 0
result = ''
global index
index = 0
#body the program start working
for u in range(1, T + 1):
      t = int(input()) # how many iterations in one work of robot
      if t == 0:
          print('S' * 60)
      else:
          for v in range(1, t + 1):
              SR, SC, FR, FC = map(int, input().split(maxsplit=4))
              keep_coordinats.append(SR - 1)
              keep_coordinats.append(SC - 1)
              keep_coordinats.append(FR - 1)
              keep_coordinats.append(FC - 1)
              # we choose the nearest robot !
              magic = what_robot(xy, SR - 1, SC - 1, newArr, maxik, maxik02)
              tutu[0][2] = magic[0] - 1
              tutu[0][3] = magic[1] - 1
              tutu.append(keep_coordinats)
              if newArr[tutu[0][2] + 1][tutu[0][3] + 1] == 0:
                  res.append(find_path_bfs(newArr, tutu))
              elif newArr[tutu[0][2] + 1][tutu[0][3] + 1] == 1:
                  res.append('S')
              keep_coordinats = []
              tutu = [[0, 0, FR - 1, FC - 1]]
              xy[index] = [FR, FC]
          for smth in range(len(res)):
             length_mas += len(res[smth])
          if length_mas < 60:
              res.append('S' * (60 - length_mas))
          for dest in res:
              result += str(dest)
          i = 0
          print(result[:60])
          destin = []
          result = ''
          res = []
          length_mas = 0

# Уважаемые сотрудники Yandex, мне было очень увлекательно решать данную задачу. Насколько я понимаю, данная задача
# нацелена на оптимизацию. Вывести нужную формулу, в которой можно было бы продемонстрировать зависимости от всех переменных
# возможно и очень нужно. На данный момент у меня есть идеи для того, чтобы вывести ее - насколько понимаю это будет
# исследование неявной функции или же создание параметра и решение его с помощье отдельных библеотек python.
# Более сложное и интересное решение содержало бы модель (основанная на машинном обучении), которая бы, изучив
# закономерности данной программы при самых разноообразных переменных делала бы выводы о количестве и размещениях
# роботов и тогда в задаче процент получения TotalTips мог вы возрасти на огромный процент.
                                                              
