import pymysql
import pandas as pd
import csv

conn = pymysql.connect(host = "localhost", user = "root", password = "1234", db = "skaila", charset = "utf8")

cur = conn.cursor()
cur.execute("select * from language")

desc = cur.description
for i in range(len(desc)) :
    print(desc[i][0], end = " ")
print()

rows = cur.fetchall()
for data in rows :
    print(data)
print()

cur.close()
conn.close()

# conn = pymysql.connect(host = "localhost", user = "hwansun", password = "1234", db = "skaila", charset = "utf8")
# cur = conn.cursor()
# cur.execute("select * from language")
# rows = cur.fetchall()
# print(rows)

# language_df = pd.DataFrame(rows)
# print(language_df)

# cur.close()
# conn.colse()

# import pymysql
# import pandas as pd

# conn = pymysql.connect(host = "localhost", user = "hwansun", password = "1234", db = "skaila", charset = "utf8")
# cur = conn.cursor(pymysql.cursors.DictCursor)
# cur.execute("select * from language")
# rows = cur.fetchall()

# language_df = pd.DataFrame(rows)
# print(language_df)
# print()
# print(language_df["name"])
# cur.close()
# conn.close()