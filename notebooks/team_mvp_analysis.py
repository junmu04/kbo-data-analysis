import pandas as pd

# CSV 파일 읽기
df = pd.read_csv("data/kbo_batter_stats_high100.csv")

# 팀별 MVP 선수 찾기

# MVP 선정 점수 생성
df["MVP_Score"] = (
    df["oWAR"] * 5
    + df["dWAR"] * 3
    + df["RBI"] * 0.5
)

# 팀별로 MVP 선수 찾기
for team, group in df.groupby("팀"):
    top_idx = group["MVP_Score"].idxmax()
    mvp_player = group.loc[top_idx]
    print(f"팀: {team}, MVP 선수: {mvp_player['이름']}, MVP 점수: {mvp_player['MVP_Score']:.3f}")

# MVP 점수 상위 10명 출력

top_mvp_players = df.nlargest(10, "MVP_Score")
print("\nMVP 점수 상위 10명:")
for idx, row in top_mvp_players.iterrows():
    print(f"선수명: {row['이름']}, 팀: {row['팀']}, MVP 점수: {row['MVP_Score']:.3f}")