# CatBoost
- https://hyewon328.tistory.com/entry/CatBoost-CatBoost-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%97%90-%EB%8C%80%ED%95%9C-%EC%9D%B4%ED%95%B4
- https://dailyheumsi.tistory.com/136
> CatBoost는 대부분이 범주형변수로 이루어진 데이터셋에서 예측 성능이 우수한 것으로 알려져있습니다.  
> CatBoost는 Boosting 기반의 모델입니다. Boosting은 한줄로 요약하면 약한 분류기들을 결합하여 보다 더 강한 분류기를 만드는 알고리즘입니다. 
### CatBoost 알고리즘 특징
- 특이한 Categorical feature(범주형 변수) 처리의 특징  
> CatBoost는 범주형 변수를 One-hot Encoding, Label Encoding 등 encoding 작업을 하지 않고도 그대로 모델의 input으로 사용할 수 있다는 장점이 있습니다. (알아서 target encoding을 해주는데 뒷부분에서 설명하겠습니다!) 하지만 범주형 변수의 cardinality가 작은 경우에는 One-hot Encoding을 진행하기도 합니다. Python의 CatBoostClassifier 혹은 CatBoostRegressor의 one_hot_max_size를 설정하면 범주형 변수의 범주 수가 지정된 값보다 작으면 One-hot Encoding을 진행합니다.   
- Ordered Target Encoding  
> CatBoost에서는 범주형 변수를 그대로 모델에 넣어주면 알아서 Orderd Target Encoding을 진행합니다.    
- Ordered Boosting  
> 순서(order)에 따라 모델을 학습시키고 순차적으로 잔차를 계산하는 과정을 반복합니다.  