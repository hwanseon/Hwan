import matplotlib.pyplot as plt
import pandas as pd
import koreanize_matplotlib
from tabulate import tabulate

file1 = r"C:\Hwan\공공데이터\DAY 02\subway.xls"

df = pd.read_excel(file1, sheet_name = "지하철 시간대별 이용현황", header = [0, 1])

print(df.columns)

# print(df[("호선명", "Unnamed: 1_level_1")])

# print(df[("지하철역", "Unnamed: 3_level_1")])

commute_time_df = df.iloc[:, [1, 3, 11, 13]]
# print(tabulate(commute_time_df.head(), headers = "keys", tablefmt = "psql"))

commute_time_df[("07:00:00~07:59:59", "하차")] = commute_time_df[("07:00:00~07:59:59", "하차")].str.replace(",", "")
commute_time_df[("08:00:00~08:59:59", "하차")] = commute_time_df[("08:00:00~08:59:59", "하차")].str.replace(",", "")

commute_time_df = commute_time_df.astype({("07:00:00~07:59:59", "하차"):"int"})
commute_time_df = commute_time_df.astype({("08:00:00~08:59:59", "하차"):"int"})
# print(commute_time_df.dtypes)

# ----------------------------------------------------------------------------------------
line1 = commute_time_df[commute_time_df[("호선명", "Unnamed: 1_level_1")] == "1호선"]
line1_total = line1[("07:00:00~07:59:59", "하차")] + line1[("08:00:00~08:59:59", "하차")]  

max_1_line = line1_total.idxmax()
max_1_station = df.iloc[max_1_line, 3]
max_1_line = line1_total.max()

print(f"출근 시간대 1호선 최대 하차역 : {max_1_station}, 하차인원 : {max_1_line:,}명")
# ----------------------------------------------------------------------------------------
line2 = commute_time_df[commute_time_df[("호선명", "Unnamed: 1_level_1")] == "2호선"]
line2_total = line2[("07:00:00~07:59:59", "하차")] + line2[("08:00:00~08:59:59", "하차")]  

max_2_line = line2_total.idxmax()
max_2_station = df.iloc[max_2_line, 3]
max_2_line = line2_total.max()

print(f"출근 시간대 2호선 최대 하차역 : {max_2_station}, 하차인원 : {max_2_line:,}명")
# ----------------------------------------------------------------------------------------
line3 = commute_time_df[commute_time_df[("호선명", "Unnamed: 1_level_1")] == "3호선"]
line3_total = line3[("07:00:00~07:59:59", "하차")] + line3[("08:00:00~08:59:59", "하차")]  

max_3_line = line3_total.idxmax()
max_3_station = df.iloc[max_3_line, 3]
max_3_line = line3_total.max()

print(f"출근 시간대 3호선 최대 하차역 : {max_3_station}, 하차인원 : {max_3_line:,}명")
# ----------------------------------------------------------------------------------------
line4 = commute_time_df[commute_time_df[("호선명", "Unnamed: 1_level_1")] == "4호선"]
line4_total = line4[("07:00:00~07:59:59", "하차")] + line4[("08:00:00~08:59:59", "하차")]  

max_4_line = line4_total.idxmax()
max_4_station = df.iloc[max_4_line, 3]
max_4_line = line4_total.max()

print(f"출근 시간대 4호선 최대 하차역 : {max_4_station}, 하차인원 : {max_4_line:,}명")
# ----------------------------------------------------------------------------------------
line5 = commute_time_df[commute_time_df[("호선명", "Unnamed: 1_level_1")] == "5호선"]
line5_total = line5[("07:00:00~07:59:59", "하차")] + line5[("08:00:00~08:59:59", "하차")]  

max_5_line = line5_total.idxmax()
max_5_station = df.iloc[max_5_line, 3]
max_5_line = line5_total.max()

print(f"출근 시간대 5호선 최대 하차역 : {max_5_station}, 하차인원 : {max_5_line:,}명")
# ----------------------------------------------------------------------------------------
line6 = commute_time_df[commute_time_df[("호선명", "Unnamed: 1_level_1")] == "6호선"]
line6_total = line6[("07:00:00~07:59:59", "하차")] + line6[("08:00:00~08:59:59", "하차")]  

max_6_line = line6_total.idxmax()
max_6_station = df.iloc[max_6_line, 3]
max_6_line = line6_total.max()

print(f"출근 시간대 6호선 최대 하차역 : {max_6_station}, 하차인원 : {max_6_line:,}명")
# ----------------------------------------------------------------------------------------
line7 = commute_time_df[commute_time_df[("호선명", "Unnamed: 1_level_1")] == "7호선"]
line7_total = line7[("07:00:00~07:59:59", "하차")] + line7[("08:00:00~08:59:59", "하차")]  

max_7_line = line7_total.idxmax()
max_7_station = df.iloc[max_7_line, 3]
max_7_line = line7_total.max()

print(f"출근 시간대 7호선 최대 하차역 : {max_7_station}, 하차인원 : {max_7_line:,}명")
# -----------------------------------------------------------------------------3----------
xticks_list = [f"1호선 {max_1_station}", f'2호선 {max_2_station}', f'3호선 {max_3_station}', f'4호선 {max_4_station}',
               f'5호선 {max_5_station}', f'6호선 {max_6_station}', f'7호선 {max_7_station}']
plt.figure(figsize = (14, 10))
plt.title("출근시간대 지하철 노선별 최대 하차 인원 및 하차역", size = 16)
plt.bar(xticks_list, [max_1_line, max_2_line, max_3_line, max_4_line, max_5_line, max_6_line, max_7_line], color='skyblue')
plt.xlabel('지하철 노선 및 역')
plt.ylabel('하차 인원 수')
plt.xticks(rotation=45)
plt.show()

