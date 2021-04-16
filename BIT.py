N, Q = map(int, input().split())
A = list(map(int, input().split()))

bit_0 = [0]*(N+1) # グラフの面積
bit_1 = [0]*(N+1) # グラフの高さ

# bitのi番目にaを足す
def bit_add(bit,i,a):
    while i <= N:
        bit[i] += a
        i += i & -i
    return bit


def bit_sum(bit, i):
    res = 0
    while i > 0:
        res += bit[i]
        i -= i & -i
    return res


# 初期化
for i in range(N):
    bit_0 = bit_add(bit_0, i+1, A[i])

for i in range(Q):
    query = list(map(str, input().split()))
    if query[0] == "Q":
        ans = 0
        l,r = int(query[1]), int(query[2])
        ans += bit_sum(bit_0,r)
        ans += bit_sum(bit_1, r)*r
        ans -= bit_sum(bit_0, l-1)
        ans -= bit_sum(bit_1, l-1)*(l-1)
        print(ans)
    else:
        l,r,c = int(query[1]), int(query[2]), int(query[3])
        bit_0 = bit_add(bit_0, l-1, -c*(l-1))
        bit_0 = bit_add(bit_0, r+1, c*r)
        bit_1 = bit_add(bit_1, l, c)
        bit_1 = bit_add(bit_1, r+1, -c)