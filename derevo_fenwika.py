def add( k, x):
    while k <= N:
        tree[k] += x
        k += k&-k

def s1(k):
    s = 0
    while k >= 1:
        s += tree[k]
        k -= k&-k
    return s

def add_a(k, x):
    array[k] += x

def SP():
    sp.append(0)
    for i in range(N):
        sp.append(sp[i] + array[i])
    return sp

def p(k):
    p_k = k &- k
    return p_k


def fenwick():
    for i in range(N+1):
        tree_k = sp[i] - sp[i - p(i)]
        tree.append(tree_k)
    return tree


N = int(input())
array = list(map(int,input().split()))
q = int(input())
tree = []
requests = [list() for i in range(q)]
num = []
sp = []
for i in range(q):
    t = int(input())
    requests[i].append(t)
    for j in range(t):
        x = list(map(int, input().split()))
        requests[i].append(x)
    y = list(map(int, input().split()))
    num.append(y)
SP()
fenwick()

for i in range(q):
    Sum = 0
    for j in range(1, requests[i][0] + 1):
        add(requests[i][j][0], requests[i][j][1])
        array[requests[i][j][0] - 1] += requests[i][j][1]
    sp = []
    SP()
    Sum = s1(num[i][1]) - s1(num[i][0] - 1)
    print(Sum)