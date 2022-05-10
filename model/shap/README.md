# [SHAP(SHapley Additive exPlanation)](https://velog.io/@tobigs_xai/2%EC%A3%BC%EC%B0%A8-SHAP-SHapley-Additive-exPlanation)
- https://data-newbie.tistory.com/254
> 일반적으로 예측이든 분류든 얼마나 정확한지에 초점을 맞추고 있습니다. 하지만 모델링을 하면서 반드시 그 원인 인자를 찾고, 얼마나 결과에 영향을 주었는지를 파악해야할 때가 있습니다. 가령 공정 불량률 및 직행률 개선을 위한 프로젝트에선 필수입니다.    
> 이렇게 결과를 "설명"하는 것이 중요해지면서 XAI(eXplainable AI)가 점점 관심을 받고 있습니다.   
> "변수 j가 이 모델로부터 제거될 때 얼마나 이 예측 i에 변화를 줄까?"  이 물음에 대한 답은 SHAP values로 표현된다.  
> SHAP values는 한 예측에서 변수의 영향도를 방향과 크기로 표현한다.  
### 모델 특징에 따라 계산법을 달리하여 빠르게 처리함.
- Kernel SHAP: Linear LIME + Shapley Value  
- Tree SHAP: Tree based Model  
- Deep SHAP: DeepLearning based Model  