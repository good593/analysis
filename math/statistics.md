# statistics(with probability)

### Khan Academy
- https://ko.khanacademy.org/math/statistics-probability
- https://ko.khanacademy.org/math/precalculus-new/x9e81a4f98389efdf:prob-comb

-------
# [통계 기초 개념](https://www.youtube.com/watch?v=YaCQrJCgbqg)
> 통계는 데이터의 수집, 분석, 추론, 요약 등의 방법론을 다룬다.
> - Design(설계/계획)
> - Description(요약): 데이터를 요약 표현하기 위한 시각적, 수치적 방법
> - Inference(추론): 표본에 기반한 모집단에 대한 추론/예측
- 모집단(Poplulation): 통계학에서 관심/조사의 대상이 되는 개체의 전체 집합
- 모수(Parameter): 모집단에 대한 수치적 요약
  - 고등학생의 1일 평균 온라인게임 플레이 시간
  - 강아지보다 고양이를 좋아하는 성인의 비율
- 표본(Sample): 모집단을 적절히 대표하는 모집단의 일부
- 통계량(Statistic): 표본에 대한 수치적 요약
  - 고등학생 1000명의 1일 푱균 온라인게임 플레이 시간
  - 강아지보다 고양이를 좋아하는 성인의 비율(1000명)
> Sample statistic -> population parameter!
## 자료의 종류
- 범주형 자료: 속성의 범주화, 상대적 서열도 표현
  - 명목형 자료: 단순히 속성을 분류하기 위함(혈액형)
  - 순서형 자료: 상대적인 크기 비교(만족도, 최종학력)
- 양적 자료: 자료자체가 숫자로 표현됨
  - 이산형 자료: 셀 수 있음(빈도수, 불량품 수)
  - 연속형 자료: 셀 수 없음(길이, 시간)
## [통계량](./sub_statistics.md)
### 통계량 - 중심
- 최빈값(mode)
- 중앙값(median)
- 산술평균(Arithmetic Mean)
- 가중평균(Weighted Mean)
- 기하평균(Geometric Mean)
### 통계량 - 산포
- 분산(Variance)
- 표준편차(Standard Deviation)
- 왜도(Skewness)
- 첨도(Kurtosis)
### 통계량 - 상관
- 상관(Correlation)
- 공분산(Covariance)
- 상관계수(Correlation Coefficient): 피어슨 상관계수

## [확률](./sub_probability.md)
### 확률과 확률변수: 확률 정의
- 표본공간(S): 랜덤한 현상의 모든 가능한 결과의 집합
- 사건(event): 표본공간의 부분집합
- 확률의 고전적 정의
> 가능한 결과가 N가지이고, 각 결과가 나타날 가능성이 모두 같을 때, 사건 A에 속하는 결과가 m개라면 A의 확률
- 경험적 정의(상대도수)
- 확룔의 공리적 정의
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
- 종속사건: 한 사건의 발생이 다른 사건의 발생 확률에 영향을 줌
### 베이즈 정리
> 사건 A1, ... An이 표본 공간 S의 분할이고 P(A) > 0, P(B) > 0 일 때,
> $P(A_k|B) = {P(A \cap B) \over P(B)} = {P(A_k)P(B|A_k) \over \sum_{i=1}^n P(A_i)P(B|A_i)}$
### 확률변수
- 확률변수
- 확률분포
### 이산/연속 확률변수
- 이산확률변수(셀 수 있다.)
- 연속확률변수(키, 몸무게 등)
### 기대값(expected value)
> 확률변수의 모든 값의 평균
- 이산확률변수
- 연속확률변수
### 분산과 표준편차
- 분산: $Var(X) = E[(X-\mu)^2] = E(X^2) - (E(X))^2$
- 표준편차
  - $sd(X) = \sqrt{Var(X)} = \sqrt{E(X - \mu)^2} $
### 공분산과 상관계수
- 피어슨 상관계수 = ${ \sum(x_i - \bar{x})(y_i - \bar{y}) \over [\sum(x_i - \bar{x})^2 \sum(y_i - \bar{y})^2 ]^{1/2} }$
- $Cov(X,Y) = E[(X - \mu_{1})(Y - \mu_{2})]$
  - $Cov: 공분산$
- $Corr(X,Y) = {Cov(X,Y) \over sd(X)sd(Y)}$
  - $Corr: 피어슨 상관계수$
---------
1시간34분.....


