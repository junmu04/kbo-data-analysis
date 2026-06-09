from sklearn.model_selection import train_test_split

import pandas as pd

df = pd.read_csv("data/kbo_batter_stats_high100.csv")

# Feature와 Target 설정
X = df[
    [
        "OPS",
        "OBP",
        "SLG",
        "HR",
        "BB",
        "RBI"
    ]
]

y = df["WAR"]

# 데이터셋을 훈련 세트와 테스트 세트로 분할
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2, # 테스트 세트의 비율 (20%)
    random_state=1 # 랜덤 시드 설정 (재현 가능성 확보) 
)

print("전체 선수 수 :", len(df))

print("학습 데이터 :", len(X_train))

print("테스트 데이터 :", len(X_test))