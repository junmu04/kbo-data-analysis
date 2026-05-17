# pandas 라이브러리 불러오기
import pandas as pd

# 그래프를 그리기 위한 matplotlib 불러오기
import matplotlib.pyplot as plt

# 한글 폰트 설정 (윈도우 기준)
plt.rcParams['font.family'] = 'Malgun Gothic'

# 마이너스 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False

# CSV 파일 읽기
df = pd.read_csv("data/kbo_batter_stats_high100.csv")

#팀별 평균 ops 계산 (소수점 3자리로 반올림)
team_ops = df.groupby("팀")["OPS"].mean().round(3)

# 팀별 평균 ops 출력
print("\n팀별 평균 OPS:")
print(team_ops)

# ops 높은 순으로 정렬
team_ops_sorted = team_ops.sort_values(ascending=False)

# enumerate:
# 데이터를 순서와 함께 반복할 수 있게 해줌
# start=1 -> 1등부터 시작
# items() -> 딕셔너리의 키와 값을 튜플 형태로 반환(튜플 언패킹(tuple unpacking))
# rank -> enumrate로 얻은 순위, 순위 순서대로 번호를 붙여줌
for rank, (팀, ops) in enumerate(team_ops_sorted.items(), start=1):

    # 보기 좋게 출력
    print(f"{rank}등 {팀} - OPS: {ops}")

team_colors = {
    '삼성': '#074CA1',
    '두산': '#131230',
    'LG': '#C30452',
    'KT': '#000000',
    'SSG': '#CE0E2D',
    '롯데': '#041E42',
    '한화': '#FF6600',
    '키움': '#570514',
    'NC': '#071D56',
    'KIA': '#EA0029'
}

colors = [team_colors[팀] for 팀 in team_ops_sorted.index]

# 팀별 평균 OPS를 막대 그래프로 시각화
plt.bar(team_ops_sorted.index, team_ops_sorted.values, color=colors)

# x축 팀 이름이 겹칠 경우 회전
plt.xticks(rotation=45)

# y축 범위를 조정해 차이를 더 잘 보이게
plt.ylim(0.6, 0.9)  # OPS 범위에 맞게 조정

# 그래프 제목
plt.title("팀별 평균 OPS")

# x축 이름
plt.xlabel("팀")

# y축 이름
plt.ylabel("OPS")

# 레이아웃 자동 정리(plt.xticks(rotation=45)) 로 인해 그래프 요소들이 겹칠 수 있으므로,
# 레이아웃을 자동으로 정리하여 겹침을 방지
plt.tight_layout()

# 그래프 출력
plt.show()
