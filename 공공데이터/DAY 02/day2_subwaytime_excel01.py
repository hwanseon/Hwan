import pandas  as pd
from tabulate import tabulate

file1 = r"C:\Hwan\공공데이터\DAY 02\subway.xls"

df = pd.read_excel(file1, sheet_name = "지하철 시간대별 이용현황", header = [0, 1])
print(df.head())

print(df.columns)

print(df[("호선명", "Unnamed: 1_level_1")])

print(df[("지하철역", "Unnamed: 3_level_1")])

commute_time_df = df.iloc[:, [1, 3, 10, 12, 14]]
print(tabulate(commute_time_df.head(), headers = "keys", tablefmt = "psql"))

print(commute_time_df.dtypes)

# 천 단위 콤마 제거
commute_time_df[("07:00:00~07:59:59", "승차")] = commute_time_df[("07:00:00~07:59:59", "승차")].apply(lambda x:x.replace(",", ""))
commute_time_df[("08:00:00~08:59:59", "승차")] = commute_time_df[("08:00:00~08:59:59", "승차")].apply(lambda x:x.replace(",", ""))
commute_time_df[("09:00:00~09:59:59", "승차")] = commute_time_df[("09:00:00~09:59:59", "승차")].apply(lambda x:x.replace(",", ""))

print(tabulate(commute_time_df.head(), headers="keys", tablefmt="psql"))

commute_time_df = commute_time_df.astype({("07:00:00~07:59:59", "승차"):"int64"})
commute_time_df = commute_time_df.astype({("08:00:00~08:59:59", "승차"):"int64"})
commute_time_df = commute_time_df.astype({("09:00:00~09:59:59", "승차"):"int64"})
print(commute_time_df.dtypes)

row_sum_df = commute_time_df.sum(axis = 1, numeric_only=True)
passenger_number_list = row_sum_df.to_list()
print(row_sum_df)

max_number = row_sum_df.max(axis = 0)
print(max_number)

max_index = row_sum_df.idxmax() # 최대값의 인덱스를 뽑아주는 
max_line, max_station = df.iloc[max_index, [1, 3]]

print(f"출근 시간대 최대 승차 인원역 : {max_line} {max_station} {max_number:,}명")

## 람다함수
students = [("Alice", 3.9, 20160303),
            ("Bob", 3.0, 20160302),
            ("Charlie", 4.3, 20160301)]

sorted_students1 = sorted(students, key=lambda s : s[2])
print(sorted_students1)

# 내림차순 정렬
sorted_students2 = sorted(students, key=lambda s : s[1], reverse = True)
print(sorted_students2)

class Students :
    def __init__(self, name, grade, number) :
        self.name = name
        self.grade = grade
        self.number = number 

    def __repr__(self) :
        return f'({self.name}, {self.grade}, {self.number})'
    
students = [Students("홍길동", 3.9, 20240303),
            Students("김유신", 3.0, 20240302),
            Students("박문수", 4.3, 20240301)]

print(students[0])

sorted_list = sorted(students, key = lambda s: s.name)
print(sorted_list)
sorted_list = sorted(students, key = lambda s: s.grade)
print(sorted_list)
sorted_list = sorted(students, key = lambda s: s.number)
print(sorted_list)