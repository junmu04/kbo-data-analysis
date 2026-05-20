# pandas 불러오기
import pandas as pd

# CSV 읽기
df = pd.read_csv("data/kbo_batter_stats_high100.csv")

# matplotlib 불러오기
import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'

# 마이너스 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False

# 그래프 크기 설정
plt.figure(figsize=(10, 7))

# 빈 컬럼 생성
df["타자유형"] = ""

# 출루형 추가
df.loc[
    (df["OBP"] >= 0.4)
    &
    (df["HR"] <= 5),
    "타자유형"
] += "출루형 "

# 장타형 추가
df.loc[
    (df["HR"] >= 8)
    &
    (df["SLG"] >= 0.5),
    "타자유형"
] += "장타형 "

# 수비형 추가
df.loc[
    (df["dWAR"] >= 0.3)
    &
    (df["OPS"] < 0.8),
    "타자유형"
] += "수비형 "

# 밸런스형 추가
df.loc[
    (df["oWAR"] >= 1)
    &
    (df["dWAR"] >= 0.2),
    "타자유형"
] += "밸런스형 "

# 타자유형 문자열에서 불필요한 공백 제거
df["타자유형"] = df["타자유형"].str.strip()

df.loc[
    df["타자유형"] == "",
    "타자유형"
] = "일반형"

# 결과 출력
print(df[["이름", "팀", "타자유형"]].head(20))

#타자 유형별 선수 분류

for player_type,group in df.groupby("타자유형"):

    print("\n========================================")
    print(f"{player_type}")
    print("========================================")

    print(group[["이름", "팀", "HR", "OBP", "SLG", "oWAR", "dWAR"]])
    print(f"{player_type} 선수 수: {len(group)}")

# 각 타자 유형의 최다 홈런 선수 찾기

for player_type, group in df.groupby("타자유형"):

    # HR 최대값의 인덱스 찾기
    max_hr_idx = group["HR"].idxmax()

    # 해당 선수 데이터 가져오기
    player = group.loc[max_hr_idx]

    print("\n====================")
    print(f"{player_type} 홈런 1위 선수")
    print("====================")

    print(
        f"{player['이름']} ({player['팀']}) "
        f"- HR: {player['HR']}"
    )

# 팀 별 OPS 1위 선수 찾기
df["팀 내 ops 순위"] = df.groupby("팀")["OPS"].rank(ascending=False, method="dense")

#
top_player = df[df["팀 내 ops 순위"] == 1]

print(top_player[["이름", "팀", "OPS"]])

# for team, group in df.groupby("팀"):

#     player = group.loc[group["팀 내 ops 순위"] == 1]

#     print("\n====================")
#     print(f"{team} OPS 1위 선수")
#     print("====================")

#     print(f"{player['이름'].values[0]} - OPS: {player['OPS'].values[0]}")