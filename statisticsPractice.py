# 統計模組
import statistics as stat

# 計算平均數 5
averageNum=stat.mean([1,4,6,9])
print(averageNum)

# 計算中位數
medianNum = stat.median([1,4,6,9])
print(medianNum)

# 計算標準差 代表資料散布的狀況
stdevNum = stat.stdev([1,4,6,9])
print(stdevNum)