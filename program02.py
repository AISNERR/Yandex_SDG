N, MaxTips, Cost_C = map(int, input().split())  # number of row and colums, tips, price of ine robot (Cost ≤ 10^9)

A = [list(map(str, input().split())) for i in range(N)]


T, D = map(int, input().split())  # amount of iterations, amount of delivery, amount robots in the city
for u in range(1, T+1):
      t = int(input())  # how many iterations in one work of robot
      for v in range(1, t + 1):
            SR, SC, FR, FC = map(int, input().split(maxsplit=4))
#body
R = 1        # amoubt of robot
x, y = 1, 1  # coordinates of robot

for j in range (len(A)):
    for k in range (len(A[j][0])):
        if A[j][0][k] == '.':
                print('ok!')
        elif A[j][0][k] == '#':
                print("THIS IS obstacle")
        else:
                print("symbol not found")
print(A)
