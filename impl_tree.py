n = int(input())
edges = list(map(int, input().split()))

tree = [[-1, -1] for _ in range(n + 1)]
for i in range(0, len(edges), 2):
    parent, child = edges[i], edges[i + 1]

    if tree[parent][0] == -1:
        tree[parent][0] = child
    else:
        tree[parent][1] = child

for x in tree:
    print(x[0], x[1])
