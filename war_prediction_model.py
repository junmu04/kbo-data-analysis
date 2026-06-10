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

from sklearn.model_selection import train_test_split

# 데이터셋을 훈련 세트와 테스트 세트로 분할
x_train, x_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

from sklearn.linear_model import LinearRegression

# 선형 회귀 모델 생성
model = LinearRegression()

# 모델 훈련
model.fit(x_train, y_train)

# 모델 예측
y_pred = model.predict(x_test)

print("예측된 WAR :", y_pred[:5])

# 실제 값과 예측된 값을 비교하는 데이터프레임 생성
result = pd.DataFrame({
    "실제 WAR": y_test,
    "예측된 WAR": y_pred.round(2)
})

print(result.head(5))

#print(df["WAR"].describe())

from sklearn.metrics import mean_squared_error

# Mean Squared Error (MSE) 계산
mse = mean_squared_error(
    y_test,
    y_pred
)

print(f"MSE : {mse:.3f}")

from sklearn.metrics import mean_absolute_error
import numpy as np

# Mean Absolute Error (MAE)와 Root Mean Squared Error (RMSE) 계산
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mse)

#Mean Absolute Error (MAE)와 Root Mean Squared Error (RMSE) 출력
print(f"MAE : {mae:.3f}")
print(f"RMSE : {rmse:.3f}")