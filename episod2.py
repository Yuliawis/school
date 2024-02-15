N = int(input())
node_list = [list() for i in range(N)]
count_list = [list() for i in range(N)]
value_list = [list() for i in range(N)]

for i in range(N-1):
    a = list(map(int, input().split()))
    node_list[a[0]-1].append(a[1]-1)
    node_list[a[1] - 1].append(a[0] - 1)
pr = list(map(int,input().split()))
print(node_list)

def dfs(s, e):
    count_list[s] = 1
    value_list[s] = pr[s]
    for u in node_list[s]:
        if (u == e):
            continue
        dfs(u, s)
        count_list[s] += count_list[u]
        value_list[s] += value_list[u]

dfs(0, -1)
for i in range(N):
    print(i, ":", ' '.join(map(str, node_list[i])))
print(' '.join(map(str, count_list)))
print(' '.join(map(str, value_list)))

'''
8
1 2
1 3
1 4
2 5
2 6
4 7
6 8
3 4 5 2 1 7 3 4
'''