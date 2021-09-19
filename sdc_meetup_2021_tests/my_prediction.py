import math
import random
import numpy as np
import pylab # additinal package rom matplotlib
from matplotlib import mlab # вспомогательные функции
from mpmath import findroot

global predict
predict = []

def solve_problem(y0, T, TotalTips, robot_price):
    return  y0 == TotalTips - T * robot_price

def f(n, robot_price, price_del, iteration, amount_del):
    TotalTips = 0
    zumzum = []
    zumzum02 = []
    for num in range(len(predict)):
        TotalTips += price_del - predict[num]
    k = 0
    y0 = 50
    for t in (100):
        k = findroot(lambda y: solve_problem(y, t, TotalTips, robot_price), y0)
        zumzum.append(k)
    for tik in range(len(zumzum)):
        zumzum02.append(TotalTips - zumzum[tik] * robot_price)
    print(zumzum)
    return max(zumzum02)

from collections import deque

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
        return koordinates[ttt]
    return koordinates[ttt]





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
    #for u in range(len(newArr[t])):
        newArr[t].insert(0, 1)
        newArr[t].append(1)
newArr.append([1] * (N + 2))
newArr.insert(0, [1] * (N + 2))
#input
T, D = map(int, input().split())  # amount of iterations, amount of delivery, amount robots in the city

R = 1# amount of robort
#xy = [[0] * 2] * R
xy = [[1, 1], [2, 2]]
print(R)  #do not delete
tutu = [[0, 0, 0, 0]]
magic = []#additional array
for count in xy:
    magic.append(count[0])
    magic.append(count[1])
print(*magic) #do not delete
magic = []
keep_coordinats = []
global res
res = [] # the path from one delivery
length_mas = 0  # the length of array
maxik = 0
maxik02 = 0
result = ''
destin = []
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
                  res.append('..STOP..THIS..IS..BUILDING.')
              keep_coordinats = []
              tutu = [[0, 0, FR - 1, FC - 1]]
          for smth in range(len(res)):
             length_mas += len(res[smth])
          if length_mas < 60:
              res.append('S' * (60 - length_mas))
          for dest in res:
              result += str(dest)
          i = 0
          while result[i] != 'S':
              destin.append(result[i])
              i += 1
          print(len(destin))
          predict.append(len(destin))
          print(result[:60])
          destin = []
          result = ''
          res = []
          length_mas = 0
print(predict)
ROBOT = f(N, MaxTips, Cost_C, T, D)
print(ROBOT)



