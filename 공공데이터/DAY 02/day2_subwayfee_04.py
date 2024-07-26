import csv
max = [0] * 4
max_station = [""]*4
label = ["유임승차", "유임하차", "무임승차", "무임하차"]

file1 = r"C:\Hwan\공공데이터\DAY 02\subwayfee.csv"

# with  open(file1, encoding = "utf-8-sig") as f:
#     data = csv.reader(f)
#     next(data)

#     for row in data :
#         for i in range(4, 8) :
#             row[i] = int(row[i])
#             if row[i] > max[i-4] :
#                 max[i-4] = row[i]
#                 max_station[i-4] = row[3] + " " + row[1]

# for i in range(4) :
#     print(f"{label[i]}: {max_station[i]} {max[i]:,}명")

import matplotlib.pyplot as plt
import koreanize_matplotlib

label = ["유임승차", "유임하차", "무임승차", "무임하차"]
color_list = ['#ff9999', '#ffc000',	'#8fd9b6', '#d395d0']
pic_count = 0
with open(file1, encoding = "utf-8-sig") as f:
    data = csv.reader(f)
    next(data)

    for row in data :
        for i in range(4, 8) :
            row[i] = int(row[i])
        print(row)
        plt.figure(dpi = 100)
        plt.title(row[3] + " " + row[1])
        plt.pie(row[4:8], labels = label, colors = color_list, autopct = "%.1f%%", shadow = True)
        plt.savefig("img/" +row[3] + " " +row[1] + ".png")
        plt.close()

        pic_count += 1
        if pic_count >= 10 :
            break