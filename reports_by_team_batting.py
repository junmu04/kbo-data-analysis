import pandas as pd

# CSV 파일 읽기
df = pd.read_csv("data/kbo_batter_stats_high100.csv")

# 팀별 타격 리포트 만들기

# 팀별로 OPS, HR, WAR의 평균(홈런은 총 합) 계산(groupby와 agg 사용)
team_report = df.groupby("팀").agg({
    "OPS": "mean",
    "HR": "sum",
    "WAR": "mean"
}) 

# round 함수를 사용하여 소수점 셋째 자리까지 반올림

team_report = team_report.round(3)

top_idx = team_report["OPS"].idxmax()
top_player = team_report.loc[top_idx]
print(top_player)


# 반복문을 사용하여 출력

for team in team_report.index:
    print(f"팀: {team}")
    print(f"평균 OPS: {team_report.loc[team, 'OPS']}")
    print(f"총 HR: {team_report.loc[team, 'HR']}")
    print(f"평균 WAR: {team_report.loc[team, 'WAR']}")
    print("-"*30)

# 팀별 OPS 1위 선수 찾기

for team,group in df.groupby("팀"):
    top_idx = group["OPS"].idxmax()
    top_player = group.loc[top_idx]
    print(f"팀: {team}, OPS 1위 선수: {top_player['선수명']}, OPS: {top_player['OPS']}")