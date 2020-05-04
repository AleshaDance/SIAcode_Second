matr = []

with open("2_5 (Turtle).txt") as f:
    h, w = [int(x) for x in f.readline().split(" ")]
    for _ in range(h):
        matr.append([int(x) for x in f.readline().split(" ")])
for x in range(1, w):
    matr[0][x] = matr[0][x] + matr[0][x-1]
for x in range(1, h):
    matr[x][0] = matr[x][0] + matr[x-1][0]
for x in range(1, h):
    for y in range(1, w):
        matr[x][y] = matr[x][y] + max(matr[x-1][y], matr[x][y-1])

print("Max amount: {}".format(matr[h-1][w-1]))
