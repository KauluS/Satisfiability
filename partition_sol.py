# partition_pre_sol.py で出力したものを標準入力として受け取り，
# j 回目に学生 i がどのグループに属しているかを出力
# このとき，変数 x_v を x_ijk に戻す

# 入力部分
N, M, K, R = map(int, input().split())
var = []
for _ in range(R):
    line = list(input().split())
    for l in line:
        if l != 'v' and l != '0':
            var.append(int(l))

# 解を出力
for j in range(1, K+1):
    print(str(j)+'回目')
    ans = [[] for _ in range(M)]
    for i in range(1, N+1):
        for k in range(1, M+1):
            v = k + (j - 1) * M + (i - 1) * M * K
            if v in var:
                ans[k-1].append(i)
    for a in ans:
        print(' '.join([str(b) for b in a]))