#볼넷형, 공격형, 수비형 선수 찾기 프로젝트

import pandas as pd

import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv("data/kbo_batter_stats_high100.csv")
 
#볼넷형 선수 찾기

df["볼넷형점수"] = (df["OBP"]*100 + df["BB"] - df["H"]  )

#볼넷형 선수 추출
OBP_Players = df.sort_values("볼넷형점수", ascending=False).head(20)

print(OBP_Players[["이름", "볼넷형점수" , "OBP", "BB", "SO"]].head(10))

#홈런형 선수 찾기

df["홈런형점수"] = (df["HR"]*5 + df["SLG"]*100 + df["SO"]*10)

#홈런형 선수 10명 추출
Power_Players = df.sort_values("홈런형점수", ascending=False).head(10)

print(Power_Players[["이름", "홈런형점수" , "HR", "SLG", "SO"]])

#수비형 선수 찾기
Defense_Players = df[(df["oWAR"] <= 0.3) & (df["PA"] >= 80) & (df["dWAR"] >= 0)]

#수비형 점수 계산
Defense_Players["수비형점수"] = (Defense_Players ["dWAR"]*100 - Defense_Players["OPS"]*10)

#수비형 선수 10명 추출
Defense_Players = Defense_Players.sort_values("수비형점수", ascending=False).head(10) 

print(Defense_Players[["이름", "수비형점수", "dWAR", "oWAR", "OPS"]])

# 볼넷형 & 홈런형 타자 산점도

plt.figure(figsize=(13, 9))

# -----------------------------
# 볼넷형 타자
# -----------------------------
plt.scatter(
    OBP_Players["SO"],
    OBP_Players["BB"],
    color="blue",
    s=80,              # 점 크기
    alpha=0.7,         # 투명도
    label="볼넷형 타자"
)

# 이름 + 점수 표시
for i in range(len(OBP_Players)):

    x = OBP_Players["SO"].iloc[i]
    y = OBP_Players["BB"].iloc[i]

    name = OBP_Players["이름"].iloc[i]
    score = OBP_Players["볼넷형점수"].iloc[i]

    plt.text(
        x + 0.3,
        y + 0.3,
        f"{name}\n{score:.1f}",
        fontsize=8,
        color="navy"
    )

# -----------------------------
# 홈런형 타자
# -----------------------------
plt.scatter(
    Power_Players["SO"],
    Power_Players["BB"],
    color="red",
    s=80,
    alpha=0.7,
    label="홈런형 타자"
)

# 이름 + 점수 표시
for j in range(len(Power_Players)):

    x = Power_Players["SO"].iloc[j]
    y = Power_Players["BB"].iloc[j]

    name = Power_Players["이름"].iloc[j]
    score = Power_Players["홈런형점수"].iloc[j]

    plt.text(
        x + 0.3,
        y - 0.5,
        f"{name}\n{score:.1f}",
        fontsize=8,
        color="darkred"
    )

# -----------------------------
# 그래프 꾸미기
# -----------------------------
plt.xlabel("삼진 (SO)", fontsize=12)
plt.ylabel("볼넷 (BB)", fontsize=12)

plt.title(
    "볼넷형 vs 홈런형 타자 분석",
    fontsize=16
)

# 격자 스타일
plt.grid(
    linestyle="--",
    alpha=0.5
)

# 범례
plt.legend(fontsize=11)

# 여백 자동 조정
plt.tight_layout()

plt.show()