# $N$ 人の学生を $M$ 個のグループに $K$ 回分割する問題を SAT で定式化

変数 $x_{ijk}$ を，「学生 $i$ が $j$ 回目でグループ $k$ に属している」と定義する．以下の 4 つの制約に従って定式化を行う．

* 学生 $i$ は $j$ 回目でグループ $1 \sim M$ のいずれかに属する．
* $i$ は $j$ 回目で複数のグループに属してはいけない．
* 学生 $a, b$ は複数回同じグループにならない．
* 各 $j, k$ について，
  * $N$ mod $M = 0$ ならば，1 グループあたり $\frac{N}{M}$ 人
  * $N$ mod $M \neq 0$ ならば
    * 1 グループあたり $\left\lceil \frac{N}{M} \right\rceil$ 人を $N$ mod $M$ 個
    * 1 グループあたり $\left\lfloor \frac{N}{M} \right\rfloor$ 人を $M - N$ mod $M$ 個
    
  に分割する．


### [ 4 月 25 日 追記 ]
以上の 4 つの制約に加えて，

* $N$ が $M$ で割り切れないとき，学生 $i$ が 1 グループあたり $\left\lfloor \frac{N}{M} \right\rfloor$ 人のグループに高々 1 回属する．

を新たな制約として追加．
