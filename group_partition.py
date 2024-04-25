# 学生の人数 N，グループの個数 M，分割回数 K をそれぞれ標準入力として受け取り，
# 与えられた 5 つの制約 (README.md 参照) に基づいて，連言標準形 (CNF) として出力

from collections import deque
import math

N, M, K = map(int, input().split())

# 以下の式を基準として，変数 x_ijk から x_v への符号化を行なっている
# var = k + (j-1) * M + (i-1) * M * K

clauses = deque([])

# 制約 1 つ目
# 節の個数：N * K
# clauses.append(['No.1'])
for n in range(1, N+1):
    for k in range(1, K+1):
        literals = deque([])
        for m in range(1, M+1):
            literals.append(str(m + (k-1) * M + (n-1) * M * K))
        literals.append(0)
        clauses.append(literals)

# 制約 2 つ目
# 節の個数：(M * (M-1)) // 2 * N * K
# clauses.append(['No.2'])
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
# clauses.append(['No.3'])
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
# clauses.append(['No.4'])
if 0 != N % M:                # 割り切れない場合は制約 5 を用いるための変数 min を用意する
    r = int(math.ceil(N / M))
    min = 1
else:                         # 割り切れる場合は制約 5 は飛ばす
    r = N // M
    min = 0

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

# 用意した変数 (上の 4 つの制約まで) の総数
var_total = N * M * K + (s * (N % M) + t * (M - (N % M))) * K

# 制約 5 つ目 (N % M != 0 の場合のみ)
# 節の個数：(M - (N%M) - min - 1) * r + (M - (N%M) - min) * (min + 1)
# clauses.append(['No.5'])
save1 = []
save2 = []
for j in range(1, K+1):
    for k in range(1, M+1):
        save = k + (j - 1) * M
        if k <= N % M:
            save1.append(save)
        else:
            save2.append(save)

if min == 1:
    x = 0
    s_mid = (N % M) * K - min
    t_mid = (M - (N % M)) * K - min
    p = s_mid * min
    q = t_mid * min
    for i in range(1, N+1):
        for k in range(1, min+1):
            for j in range(1, t_mid):
                literals = deque([])
                literals.append('-'+str(j + (k-1) * t_mid + x + var_total))
                literals.append(str(j+1 + (k-1) * t_mid + x + var_total))
                literals.append(0)
                clauses.append(literals)

        for k in range(min+1):
            for j in range(1, t_mid+1):
                literals = deque([])
                literals.append('-'+str(save2[j+k-1] + (i-1) * M*K))
                if k != 0:
                    literals.append('-'+str(j + (k-1) * t_mid + x + var_total))
                if k != min:
                    literals.append(str(j + k * t_mid + x + var_total))
                literals.append(0)
                clauses.append(literals)
        x += q

    var_total += q * N

# 実行結果を .cnf ファイルにして出力
filename = str(N) + '-' + str(M) + '-' + str(K)
file = filename + '.cnf'

with open(file, 'w') as f:
    print('p cnf' +  ' ' + str(var_total) + ' ' + str(len(clauses)), file=f)
    for c in clauses:
        print(' '.join([str(d) for d in c]), file=f)
