import pandas as pd 
import matplotlib.pyplot as plt
# 한글 폰트 설정 (윈도우)
plt.rcParams['font.family'] = 'Malgun Gothic'

# 마이너스 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv("data/kbo_batter_stats.csv") # 파일 불러오기

print(df.head()) # 데이터의 상위 5명 불러오기

print("\n타율 TOP 10")      

top_avg = df.sort_values(by="AVG",ascending=False)

print(top_avg[["성명","AVG"]].head(10))

print("\n홈런 TOP 5")

top_HR = df.sort_values(by="HR",ascending=False)

print(top_HR[["성명","HR"]].head(5))

plt.bar(top_HR["성명"], top_HR["HR"])

plt.xticks(rotation=45)

plt.title("Top 10 Home Runs")

plt.show()