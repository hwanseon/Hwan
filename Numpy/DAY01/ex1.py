import numpy as np
import pandas as pd

File = r"C:\Hwan\Numpy\DAY01\예제소스코드모음1\data\ch2_scores_em.csv"
df = pd.read_csv(File)

print(df.head())

scores = np.array(df["english"])[:10]
print(scores)

scores_df = pd.DataFrame({"score":scores}, index = pd.Index(["A", 'B','C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], name = "student"))

print(scores_df)


# 평균갑
print(sum(scores))
print(len(scores))
print(np.mean(scores))
print(scores_df.mean())

# 중앙값
sorted_scores = np.sort(scores)
print(sorted_scores)

# 최빈값
print(pd.Series([1, 1, 1, 2, 2, 3]).mode())

# 분산과 표준편차
mean = np.mean(scores)
deviation = scores-mean
print(deviation)
summary_df = scores_df.copy()
summary_df["deviation"] = deviation
print(summary_df)

print(summary_df.mean())

print(np.mean(deviation**2))

print(np.var(scores))

print(scores_df.var())

summary_df["square of deviation"] = np.square(deviation)
print(summary_df)

# 표준편차
np.sqrt(np.var(scores, ddof=0))
np.std(scores, ddof=0)

# 범위와 사분위 범위
np.max(scores) - np.min(scores)

scores_q1 = np.percentile(scores, 25)
scores_q3 = np.percentile(scores, 75)
scores_iqr = scores_q3 - scores_q1
print(scores_iqr)

# 데이터 정규화
z = (scores - np.mean(scores)) / np.std(scores)
print(z)

np.mean(z), np.std(z, ddof=0)

# 편찻값
z = 50 + 10*(scores - np.mean(scores))/np.std(scores)
print(z)

# 점수와 편찻값의 관계
scores_df["deviation value"] = z
print(scores_df)

# 데이터의 시각화
english_scores = np.array(df["english"])

pd.Series(english_scores).describe()

# 도수분포표
freq,_ = np.histogram(english_scores, bins=10, range=(0,100))
print(freq)

freq_class = [f"{i}~{i+10}" for i in range(0,100,10)]
freq_dist_df = pd.DataFrame({"frequency":freq}, index = pd.Index(freq_class, name="class"))
print(freq_dist_df)

# 도수분포표 - 각 계급을 대표하는 값으로 계급의 중앙값을 이용
class_value = [(i+(i+10))//2 for i in range(0, 100, 10)]
print(class_value)

rel_freq = freq/freq.sum()
print(rel_freq)

# 누적 상대도수
cum_rel_freq = np.cumsum(rel_freq)
print(cum_rel_freq)

# 계급값, 상대도수, 누적상대도수를 도수분포표에 추가
freq_dist_df["class value"] = class_value
freq_dist_df["relative frequency"] = rel_freq
freq_dist_df["cumulative relative frequency"] = cum_rel_freq
freq_dist_df = freq_dist_df[["class value", "frequency", "relative frequency", "cumulative relative frequency"]]

print(freq_dist_df)

# 최빈값
freq_dist_df.loc[freq_dist_df["frequency"].idxmax(), "class value"]

# 히스토그램
import matplotlib.pyplot as plt

fig = plt.figure(figsize = (10, 6))

ax = fig.add_subplot(111)

freq,_,_ = ax.hist(english_scores, bins=10, range=(0,100))
ax.set_xlabel("score")
ax.set_ylabel("person number")
ax.set_xticks(np.linspace(0, 100, 10+1))
ax.set_yticks(np.arange(0, freq.max()+1))
plt.show()

# 히스토그램에 누적 상대도수 꺾은선 그래프 
fig = plt.figure(figsize = (10, 6))
ax1 = fig.add_subplot(111)
ax2 = ax1.twinx()

weights = np.ones_like(english_scores) / len(english_scores)
rel_freq,_,_ = ax1.hist(english_scores, bins = 25, range=(0, 100), weights = weights)

cum_rel_freq = np.cumsum(rel_freq)
class_values = [(i+(i+4))//2 for i in range(0, 100, 4)]

ax2.plot(class_value, cum_rel_freq, Is = "--", marker="o", color = "gray")
ax2.grid(visible = False)

ax1.set_xlabel("score")
ax1.set_ylabel("relative frequency")
ax2.set_ylabel("cumulative relative frequency")
ax1.set_xticks(np.linspace(0, 100, 25+1))

plt.show()

# 상자그림
fig = plt.figure(figsize = (5, 6))
ax = fig.add_subplot(111)
ax.boxplot(english_scores, labels=["english"])

plt.show()

import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

x = range(0, 100)
y = [v*v for v in x]

ax1.plot(x, y)
ax2.bar(x, y)

plt.show()