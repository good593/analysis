## 통계량
### 통계량 - 중심
- 최빈값(mode)
  - 발생빈도가 가장 높은 값
  - 극단값에 영향을 받지 않음
  - 주로 범주형 자료에 대한 대표값
- 중앙값(median)
  - 크기 순으로 정렬된 자료에서 가운데에 위치하는 값
  - 관측값 변화에 민감하지 않음
  - 극단값에 거의 영향을 받지 않음
- 산술평균(Arithmetic Mean)
  - 모든 자료의 값을 더하여 자료의 수로 나누어 준값
  - 모든 값을 반영하므로 극단값에 영향을 받음
  - $\bar{x} = {\sum_{i=1}^n x_i \over n} = {x_1+x_2 \cdots +x_i \over n}$
- 가중평균(Weighted Mean)
  - 자료의 중요성이 각기 다를 경우 중요도에 따라 가중치를 부여한 평균
  - $\bar{X} = {w_1\bar{X}_1+ \cdots +w_i\bar{X}_i  \over w_1+ \cdots +w_i } = {\sum w_i\bar{X}_i \over \sum w_i }$
- 기하평균(Geometric Mean)
  - 자료가 성장률, 증가율 등 앞 시점에 대한 비율로 나타난 경우 유용한 통계량
  - 음수가 아닌 자료값 only
  - 연간 물가 상승률
  - $기하평균(G) = \sqrt[n]{\prod_{i=1}^n x_i} (x_i = 상승률)$
  - Ex) 일일 주가 상승률(1%, 3%, 10%)의 평균을 구할 때는 기하평균으로 구해야함 
### 통계량 - 산포
- 분산(Variance)
  - 편차 제곱의 합을 자료의 수로 나눈 값
  - $\sum_{i=1}^n (x_i - \bar{x})^2 / (n -1)$
- 표준편차(Standard Deviation)
  - 분산을 제곱근한 값
  - $\sqrt{\sum_{i=1}^n (x_i - \bar{x})^2 / (n -1)}$
- 왜도(Skewness)
  - 분포의 비대칭도
  - Positive Skew: 오른쪽으로 꼬리가 길게 생긴 모양
    - Mean > Median > Mode
  - Negative Skew: 왼쪽으로 꼬리가 길게 생긴 모양
    - Mode > Median > Mean
  - Symmetrical Distribution: 표준정규분포 모양
    - Mean = Median = Mode
- 첨도(Kurtosis)
  - 뽀족한 정도
  - 표준정규분포의 첨도는 3이 된다.
### 통계량 - 상관
- 상관(Correlation)
  - 확률변수 X,Y의 변화가 서로 관계가 있을 때, 상관관계가 있다고 함
  - 선형적 관련성을 파악함
- 공분산(Covariance)
  > - $x편차 => x_i - \bar{x}$ 
  - $s_{XY} = {\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y}) \over n-1 }$
- 상관계수(Correlation Coefficient): 피어슨 상관계수
  > - 분자: x,y의 공분산
  > - 분모: x의 표준편차, y의 표준편차
  - ${\sum (x_i - \bar{x})(y_i - \bar{y}) \over [\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2]^{1/2}}$
  - 공분산을 두 변수의 표준편차의 곱으로 나눈 값
  - -1 <= r <= 1
  - 두 양적 변수 간의 선형적 연관성의 강도 측정
  - 단위가 없음
  - 절대값이 1에 가까울 수록 연관성의 강도가 높다