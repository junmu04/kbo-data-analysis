# pandas 불러오기
import pandas as pd

# matplotlib 불러오기
import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'

# 마이너스 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False

# CSV 파일 읽기
df = pd.read_csv("data/kbo_batter_stats_high100.csv")

# 그래프 크기 설정
plt.figure(figsize=(10, 7))

# 산점도 생성
plt.scatter(df["HR"], df["OPS"])

# 각 선수 이름 표시
for i in range(len(df)):
    
    if df["OPS"][i] >0.7:  # OPS가 0.7 이상인 선수만 이름표시

        # x축 값 (홈런)
        x = df["HR"][i]

        # y축 값 (OPS)
        y = df["OPS"][i]

        # 선수 이름
        name = df["이름"][i]

        # 그래프에 텍스트 추가
        plt.text(x, y, name, fontsize=8)

# 그래프 제목
plt.title("홈런과 OPS의 관계")

# x축 이름
plt.xlabel("홈런")

# y축 이름
plt.ylabel("OPS")

# 그래프 출력
plt.show()