import pandas as pd

# CSV 파일 읽기
df = pd.read_csv("data/kbo_batter_stats_high100.csv")

# OPS, OBP, SLG, HR, WAR 간의 상관관계 분석
print(
    df[["OPS", "OBP", "SLG", "HR", "WAR"]].corr()
)

# WAR과 다른 지표들 간의 상관관계 분석
print(
    df.corr(numeric_only=True)["WAR"].sort_values(ascending=False)
)