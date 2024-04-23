# .ki ファイルをコマンドライン引数として受け取り，
# 充足可能である場合は変数の割り当てを出力する

import sys, os

# ファイルを引数として与えているか判定
if 2 <= len(sys.argv):
    file = sys.argv[1]
else:
    print('No input file')
    exit()

# ファイル名から，N, M, K となる部分のみ取ってくる
# e.g. 4-2-3.ki から 4, 2, 3 のみを取ってくる
path = './' + str(file)
sp = os.path.splitext(os.path.basename(path))[0]
sp = sp.split('-')

f = open(file, 'r')

for s in sp:
    print(s, end=' ')

# 行の先頭文字が 'v' ならば，充足可能となる割り当てが存在することを指すので，それを配列 sol に格納
# cnt は先頭文字が 'v' で始まる行数
cnt = 0
sol = []
for data in f:
    if data[0] == 'v':
        sol.append(data.rstrip('\n'))
        cnt += 1

# 割り当てられている変数をすべて表示 (行数も表示)
print(cnt)
for s in sol:
    print(''.join([str(l) for l in s]))

f.close()