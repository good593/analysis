## 확률
### 확률과 확률변수: 확률 정의
- 표본공간(S): 랜덤한 현상의 모든 가능한 결과의 집합
- 사건(event): 표본공간의 부분집합
  - 합사상: $A \cup B$
  - 곱사상: $A \cap B$
  - 여사상: $A^C$
  - 배반사상: $A \cap B = \phi$
- 예) Flipping Coin Twice
  - 표본공간 S: {HH, HT, TH, TT}
  - 사건 A: 동전을 두 번 던지는 시행에서 동전의 앞면이 1번만 나오는 사건
    - A: {HT, TH}
- 확률의 고전적 정의
> 가능한 결과가 N가지이고, 각 결과가 나타날 가능성이 모두 같을 때, 사건 A에 속하는 결과가 m개라면 A의 확률
  - $P(A) = {m \over N} = {앞면이 1번만 나오는 사건(2개) \over 표본공간(4개)} = {2 \over 4}$
    - P: 확률
    - A: 사건(부분집합)
- 경험적 정의(상대도수)
  - $P(A) = \lim_{N \to \infty}{n \over N}$ 
    - N은 시도 횟수
- 확룔의 공리적 정의
> 표본공간 S에서의 임의의 사상 A에 대하여,
  - $0 <= P(A) <= 1$
  - $P(S) = 1$
  - 서로 배반인 사상들에 대하여
    - $P(A_1 \cup A_2 \cup \cdots ) = P(A_1)+P(A_2)+\cdots$
    - 이 때, P(A)를 사상 A의 확률이라고 함
### 확률의 성질
- $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
- $P(A^C) = 1 - P(A) = P(S) - P(A)$
- An이 서로 배반사상일 때,
  - $P(A_1 \cup A_2 \cup \cdots \cup A_n ) = P(A_1)+P(A_2)+\cdots +P(A_n)$
- $A \subset B이면, P(A) <= P(B)$
### 조건부확률
> 한 사건이 일어날 것을 전제로 다른 사건이 일어날 확률 (변화된 표본공간에서의 사건 발생 확률)
- B가 일어났을 때, A가 일어날 확률
  - $P(A|B) = {P(A \cap B) \over P(B)}$
### 독립과 종속
- 독립사건: 한 사건의 발생이 다른 사건의 발생 확률에 영향을 주지 않음
  - 사건 A와 B가 서로 독립이면,
    - $P(A \cap B) = P(A)P(B)$
    - $P(A|B) = P(A)$
- 종속사건: 한 사건의 발생이 다른 사건의 발생 확률에 영향을 줌
  - $P(A \cap B) = P(A|B)P(B) = P(B|A)P(A)$
### 베이즈 정리
> 사건 A1, ... An이 표본 공간 S의 분할이고 P(A) > 0, P(B) > 0 일 때,
> $P(A_k|B) = {P(A \cap B) \over P(B)} = {P(A_k)P(B|A_k) \over \sum_{i=1}^n P(A_i)P(B|A_i)}$
> - $정규화 상수(새로운 표본 공간을 정의): \sum_{i=1}^n P(A_i)P(B|A_i)$ -> 계산량이 많아서 생력하는 경우도 있음
- P(A_k)는 원인의 가능성: 사전확률
- P(B|A_k)는 원인 A_k의 결과로서 B가 관측될 확률
  - 가능도(Likelihood)
- P(A_k|B)는 B가 관측된 후에 원인 A_k의 가능성: 사후확률
- 사전확률을 사후확률로 전환할 수 있음, 즉 B(관측값)을 알 수 있다면, A_k(원인)을 예측할 수 있음.
### 확률변수
- 확률변수
  - 표본공간에서 정의된 실수값 함수
    - 실수가 아니면 확률분포함수 정의할 수 없음
  - 일정 확률을 가지고 발생하는 사건에 수치를 부여한 것
  - 변수가 어떤 값을 취하는지가 확률적으로 결정된다.
    - 통계적 규칙성은 있다고 봄
- 확률분포
  - 확률변수의 값과, 확률을 대응시켜 표, 그래프, 함수로 표현한 것
### 이산/연속 확률변수
- 이산확률변수(셀 수 있다.)
  - 이산표본공간에서 정의된 확률변수의 값이 유한 혹은 countably infinite
  - 확률질량함수: 이산확률변수 X의 값 x1, ..., xn의 각 확률을 대응
- 연속확률변수(키, 몸무게 등)
  - 특정 구간 내의 모든 값을 취하는 확률변수
  - 확률변수의 값이 무한개이며 셀 수 없음
  - 확률밀도함수(PDF): 확률변수 X가 어떤 구간 [l, u]의 모든 값을 취하고 이 구간에서의 함수 f(x)
    - 확률밀도함수의 특정 구간의 넓이가 확률임.
    - CDF를 미분한 것이 PDF(확률밀도함수)임.
  > - $f(x) >= 0, \int_{l}^{u} f(x)dx = 1(전체 확률의 합은 1)$
  > - $P\{a<=X<=b\} = \int_{a}^b f(x)dx (단, l<=a<b<=u): 특정 구간의 확률$
### 기대값(expected value)
> 확률변수의 모든 값의 평균
- 이산확률변수
  - 확률변수의 값이 x1, ... 이고 X = xi일 확률이 f(xi)일 때,
    - $E(X) = \sum x_if(x_i)$
    - $f(x_i): 활률질량함수$ -> 확률변수(X; 사건)의 특정값(xi)이 발생할 확률
- 연속확률변수
  - 확률변수 X가 [l, u] 구간의 모든 값을 취하고 X의 확률밀도함수가 f(x)일 때,
    - $E(X) = \int_{l}^u xf(x)dx$
### 기대값의 성질
> $a, b, c는 상수이고 X, Y는 확률변수이고 g()는 함수$
- $E(a) = a$
- $E(aX) = aE(X)$
- $E(X \pm b) = E(X) \pm b$
- $E(aX \pm b) = aE(X) \pm b$
- $E[c_1g_1(X) + c_2g_2(X)] = c_1E[g_1(X)] + c_2E[g_2(X)]$
### 분산과 표준편차
- 분산: $Var(X) = E[(X-\mu)^2] = E(X^2) - (E(X))^2$
  - $\mu = E(X)$
  - 이산확률변수: $Var(X) = E[(X-\mu)^2] = \sum (x_i-\mu)^2f(x_i)$
    - 확률질량함수: $f(x_i)$
  - 연속확률변수: $Var(X) = E[(X-\mu)^2] = \int (x-\mu)^2f(x)dx$
    - 확률밀도함수(PDF): $f(x)$
- 표준편차
  - $sd(X) = \sqrt{Var(X)} = \sqrt{E(X - \mu)^2} $
### 분산과 표준편차의 성질
- 분산
  - $Var(X \pm b) = Var(X)$
  - $Var(aX) = a^2Var(X)$
  - $Var(aX \pm b) = a^2Var(X)$
- 표준편차
  - $\sigma(X \pm b) = \sigma(X)$
  - $\sigma(aX) = a\sigma(X)$
  - $\sigma(aX \pm b) = a\sigma(X)$
### 공분산과 상관계수
- 피어슨 상관계수 = ${ \sum(x_i - \bar{x})(y_i - \bar{y}) \over [\sum(x_i - \bar{x})^2 \sum(y_i - \bar{y})^2 ]^{1/2} }$
- $Cov(X,Y) = E[(X - \mu_{1})(Y - \mu_{2})]$
  - $Cov: 공분산$
- $Corr(X,Y) = {Cov(X,Y) \over sd(X)sd(Y)}$
  - $Corr: 피어슨 상관계수$
### 공분산과 상관계수의 성질
- $Cov(aX + b, cY + d) = acCov(X,Y)$
- $Corr(aX + b, cY + d) = Corr(X,Y) ac > 0 또는 -Corr(X,Y) ac < 0$
  - $-1 <= Corr(X,Y) <= 1$
- 두 확률변수 합의 분산
  - $Var(X + Y) = Var(X) + Var(Y) + 2Cov(X,Y)$
  - $Var(X - Y) = Var(X) + Var(Y) - 2Cov(X,Y)$
  - X,Y가 독립인경우,
    - $Cov(X,Y) = 0$




