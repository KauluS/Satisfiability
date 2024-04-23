from collections import deque
import math

N, M, K = map(int, input().split())

# 以下の式を基準として，x_ijk から x_v への符号化を行なっている
# var = k + (j-1) * M + (i-1) * M * K

clauses = deque([])

# 制約 1 つ目
# 節の個数：N * K
for n in range(1, N+1):
    for k in range(1, K+1):
        literals = deque([])
        for m in range(1, M+1):
            literals.append(str(m + (k-1) * M + (n-1) * M * K))
        literals.append(0)
        clauses.append(literals)

# 制約 2 つ目
# 節の個数：(M * (M-1)) // 2 * N * K
for n in range(1, N+1):
    for k in range(1, K+1):
        for i in range(1, M):
            for j in range(i+1, M+1):
                literals = deque([])
                literals.append('-' + str(i + (k-1) * M + (n-1) * M * K))
                literals.append('-' + str(j + (k-1) * M + (n-1) * M * K))
                literals.append(0)
                clauses.append(literals)

# 制約 3 つ目
# 節の個数：(N * (N-1)) // 2 * (K * (K-1)) // 2 * (M**2)
for a in range(1, N):
    for b in range(a+1, N+1):
        for i in range(1, K+1):
            for j in range(1, K+1):
                for k in range(1, M+1):
                    for l in range(1, M+1):
                        if a != b and i != j:
                            literals = deque([])
                            literals.append('-' + str(k + (i-1) * M + (a-1) * M * K))
                            literals.append('-' + str(k + (i-1) * M + (b-1) * M * K))
                            literals.append('-' + str(l + (j-1) * M + (a-1) * M * K))
                            literals.append('-' + str(l + (j-1) * M + (b-1) * M * K))
                            literals.append(0)
                            clauses.append(literals)

# 制約 4 つ目
# 節の個数：((N-r-1) * r + (N-r) * (r+1)) * (N mod M) + ((N-l-1) * l + (N-l) * (l+1)) * (M-(N mod M))
if 0 != N % M:
    r = int(math.ceil(N / M))
else:
    r = N // M

l = N // M

s = (N - r) * r
t = (N - l) * l

cnt, x = 0, 0
for v in range(1, K+1):
    for w in range(1, M+1):
        # 学生数 N がグループ数 M で割り切れないとき，
        # N mod M 個のグループは 1 グループあたり ceil(N / M) 人
        # M - (N mod M) 個のグループは 1 グループあたり floor(N / M) 人
        if cnt % M >= N % M:
            # 1 グループあたり floor(N / M) 人で分割する場合
            for k in range(1, l+1):
                for j in range(1, N-l):
                    literals = deque([])
                    literals.append('-'+str(j + (k-1) * (N-l) + x + N*M*K))
                    literals.append(str(j+1 + (k-1) * (N-l) + x + N*M*K))
                    literals.append(0)
                    clauses.append(literals)

            for k in range(l+1):
                for j in range(1, N-l+1):
                    literals = deque([])
                    literals.append('-'+str(w + (v-1) * M + (j+k-1) * M * K))
                    if k != 0:
                        literals.append('-'+str(j + (k-1) * (N-l) + x + N*M*K))
                    if k != l:
                        literals.append(str(j + k * (N-l) + x + N*M*K))
                    literals.append(0)
                    clauses.append(literals)

            for k in range(1, l):
                for j in range(1, N-l+1):
                    literals = deque([])
                    literals.append(str(j + (k-1) * (N-l) + x + N*M*K))
                    literals.append('-'+str(j + k * (N-l) + x + N*M*K))
                    literals.append(0)
                    clauses.append(literals)

            for k in range(1, l+1):
                for j in range(N-l+1):
                    literals = deque([])
                    literals.append(str(w + (v-1) * M + (j+k-1) * M * K))
                    if j != 0:
                        literals.append(str(j + (k-1) * (N-l) + x + N*M*K))
                    if j != N - l:
                        literals.append('-'+str(j+1 + (k-1) * (N-l) + x + N*M*K))
                    literals.append(0)
                    clauses.append(literals)

            x += t # 1 グループあたりの人数分を加算

        else:
            # 1 グループあたり ceil(N / M) 人で分割する場合
            for k in range(1, r+1):
                for j in range(1, N-r):
                    literals = deque([])
                    literals.append('-'+str(j + (k-1) * (N-r) + x + N*M*K))
                    literals.append(str(j+1 + (k-1) * (N-r) + x + N*M*K))
                    literals.append(0)
                    clauses.append(literals)

            for k in range(r+1):
                for j in range(1, N-r+1):
                    literals = deque([])
                    literals.append('-'+str(w + (v-1) * M + (j+k-1) * M * K))
                    if k != 0:
                        literals.append('-'+str(j + (k-1) * (N-r) + x + N*M*K))
                    if k != r:
                        literals.append(str(j + k * (N-r) + x + N*M*K))
                    literals.append(0)
                    clauses.append(literals)

            for k in range(1, r):
                for j in range(1, N-r+1):
                    literals = deque([])
                    literals.append(str(j + (k-1) * (N-r) + x + N*M*K))
                    literals.append('-'+str(j + k * (N-r) + x + N*M*K))
                    literals.append(0)
                    clauses.append(literals)

            for k in range(1, r+1):
                for j in range(N-r+1):
                    literals = deque([])
                    literals.append(str(w + (v-1) * M + (j+k-1) * M * K))
                    if j != 0:
                        literals.append(str(j + (k-1) * (N-r) + x + N*M*K))
                    if j != N - r:
                        literals.append('-'+str(j+1 + (k-1) * (N-r) + x + N*M*K))
                    literals.append(0)
                    clauses.append(literals)

            x += s
    
        cnt += 1

# 用意した変数の総数
var_total = N * M * K + (s * (N % M) + t * (M - (N % M))) * K

# 実行結果を .cnf ファイルにして出力
filename = str(N) + '-' + str(M) + '-' + str(K)
file = filename + '.cnf'

with open(file, 'w') as f:
    print('p cnf' +  ' ' + str(var_total) + ' ' + str(len(clauses)), file=f)
    for c in clauses:
        print(' '.join([str(d) for d in c]), file=f)