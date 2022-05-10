# Ensemble
- https://bkshin.tistory.com/entry/%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-11-%EC%95%99%EC%83%81%EB%B8%94-%ED%95%99%EC%8A%B5-Ensemble-Learning-%EB%B0%B0%EA%B9%85Bagging%EA%B3%BC-%EB%B6%80%EC%8A%A4%ED%8C%85Boosting
- http://www.dinnopartners.com/__trashed-4/
## Voting
- 여러 개의 분류기가 투표를 통해 최종 예측 결과를 결정하는 방식  
- 서로 다른 알고리즘을 여러 개 결합하여 사용
- 보팅 방식
  - 하드보팅: 다수의 분류기가 예측한 결과값을 최종 결과로 선정  
  - 소프트보팅: 모든 분류기가 예측한 레이블 값의 결정 확률 평균을 구한 뒤 가장 확률이 높은 레이블 값을 최종결과로 선정
## Bagging
- 데이터 샘플링(Bootstrap)을 통해 모델을 학습시키고 결과를 집계(Aggregating)하는 방법
- 모두 같은 유형의 알고리즘 기반의 분류기를 사용
- 데이터 분할 시 중복을 허용
- Categorical Data: 다수결 투표 방식으로 결과 집계
- Continuous Data: 평균값 집계
- Overfitting: 방지에 효과적
- 대표적인 배깅 방식: 랜덤 포레스트 알고리즘
## Boosting
- 여러 개의 분류기가 순차적으로 학습을 수행 
- 이전 분류기가 예측이 틀린 데이터에 대해서 올바르게 예측할 수 있도록 다음 분류기에게 가중치를 부여하면서 학습과 예측을 진행  
- 계속하여 분류기에게 가중치를 부스팅하며 학습을 진행하기에 부스팅 방식이라고 불림
- 예측 성능이 뛰어나 앙상블 학습을 주도 
- 대표적인 부스팅 모둘: XGBoost, LightGBM
- 보통 부스팅 방식은 배기에 비해 성능이 좋지만, 속도가 느리고 과적합이 발생할 가능성이 존재하므로 상황에 따라 적절하게 사용해야 함

