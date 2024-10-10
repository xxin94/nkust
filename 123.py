from datetime import datetime

# 輸入今天的日期
today = input("請輸入今天的日期 (格式: YYYY-MM-DD): ")
# 輸入要倒數的日期
target_date = input("請輸入要倒數的日期 (格式: YYYY-MM-DD): ")

# 將輸入的日期轉換成 datetime 物件
today_date = datetime.strptime(today, "%Y-%m-%d")
target_date = datetime.strptime(target_date, "%Y-%m-%d")

# 計算兩個日期之間的差異
countdown = target_date - today_date

# 顯示倒數天數
print(f"距離 {target_date.strftime('%Y-%m-%d')} 還有 {countdown.days} 天")

from datetime import datetime

# 輸入今天的日期
today = input("請輸入今天的日期 (格式: YYYY-MM-DD): ")
# 輸入要倒數的日期
target_date = input("請輸入要倒數的日期 (格式: YYYY-MM-DD): ")

# 將輸入的日期轉換成 datetime 物件
today_date = datetime.strptime(today, "%Y-%m-%d")
target_date = datetime.strptime(target_date, "%Y-%m-%d")

# 計算兩個日期之間的差異
countdown = target_date - today_date

# 顯示倒數天數
print(f"距離 {target_date.strftime('%Y-%m-%d')} 還有 {countdown.days} 天")