# pandas 불러오기
import pandas as pd

# CSV 읽기
df = pd.read_csv("data/kbo_batter_stats_high100.csv")

# OPS 0.9 이상 선수만 선택(필터링)
high_ops = df[df["OPS"] >= 0.9]

# 필요한 컬럼 출력
print(high_ops[["이름","oWAR","dWAR", "팀", "OPS"]])

# 홈런 5개 이상 AND OPS 0.9 이상
elite_hitters = df[(df["HR"] >= 5) & (df["OPS"] >= 0.9)]

# 출력
print(elite_hitters[["이름", "팀", "HR", "OPS"]])

# 공격형 선수 찾기
offensive_players = df[(df["oWAR"] > 1.5) & (df["dWAR"] <= 0)]

print(offensive_players[["이름", "팀", "oWAR", "dWAR"]])

#수비형 선수 찾기(dWAR이 높으면서, 같을 경우 oWAR이 낮은 선수 순)
defensive_players = df.sort_values(by=["dWAR","oWAR"], ascending=[False,True]).head(10)

print(defensive_players[["이름", "팀", "oWAR", "dWAR"]])

#ops가 0.8 이상이면서 홈런이 3개 이하인 선수 찾기 (단, 30경기 이상 출전한 선수로 제한함)
special_players = df[(df["OPS"] >= 0.8) & (df["HR"] <= 3)&(df["G"]>=30)]
    
special_players_sorted = special_players.sort_values(by="OPS", ascending=False)

print(special_players_sorted[["이름", "팀", "HR", "OPS"]].head(5))

#dWAR의 기술 통계량 출력
print(df["BB"].describe())

#규정타석 이상 선수 중 출루형 타자 top5 
High_OBP_Players = df[
    (df["OPS"] >= 0.8)
    &
    (df["HR"] <= 3)
    &
    (df["BB"] >= 20)
    &
    (df["PA"] >= 100)
].sort_values(
    by="OBP",
    ascending=False
).head(5)

# 결과 출력
print(High_OBP_Players[["이름", "팀", "BB", "PA", "OBP"]])

# 기본값 "보통"
df["OPS등급"] = "보통"

# OPS 0.9 이상은 "최상"
df.loc[df["OPS"] >= 0.9, "OPS등급"] = "최상"

# 결과 출력
print(df[["이름", "OPS", "OPS등급"]].head(100))

# war 상위 100명의 팀별 평균 HR 계산
team_hr = df.groupby("팀")["HR"].mean()
print(team_hr)

# war 상위 100명의 팀별 인원 수 계산
team_count = df["팀"].value_counts()
print(team_count)

# 기아 선수들만 추출 후 이름과 OPS 출력
kia_players = df[df["팀"] == "KIA"]
print(kia_players[["이름", "OPS"]])

# KIA와 LG 선수들만 추출 후 이름과 팀 출력
selected = df[df["팀"].isin(["KIA", "LG"])]
print(selected[["이름", "팀"]])