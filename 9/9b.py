visited = set([(0, 0)])
R = [[0, 0] for _ in range(10)]

with open('input.txt', 'r') as input:
    for line in input.read().splitlines():
        x, y = line.split()
        y = int(y)
        # print(f'{x} {y}')

        for _ in range(y):
            dx = 1 if x == "R" else -1 if x == "L" else 0
            dy = 1 if x == "U" else -1 if x == "D" else 0

            R[0][0] += dx
            R[0][1] += dy
            
            for i in range(9):
                H = R[i]
                T = R[i+1]
                _x = H[0] - T[0] # x difference 
                _y = H[1] - T[1] # y difference

                if abs(_x) > 1 or abs(_y) > 1:
                    if _x == 0:
                        T[1] += _y // 2
                    elif _y == 0:
                        T[0] += _x // 2
                    else:
                        T[0] += 1 if _x > 0 else -1
                        T[1] += 1 if _y > 0 else -1

            visited.add(tuple(R[-1]))
print(len(visited))