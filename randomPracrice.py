import random

# 隨機選取 choice /sample

# 從列表中選取一個資料
choiceNum = random.choice([0,1,5,9,8,6,4,3])
print(choiceNum)
# 從列表中隨機選取兩個資料
sampleNum = random.sample([0,1,5,9],2)
print(sampleNum)

# 隨機調換順序 洗牌的概念
data = [0,1,5,8,20,16]
random.shuffle(data)
print(data)

# 隨機亂數

randomData=random.random()
print(randomData)

random.uniform(0.0,1.0)

# 常態分配亂數
# 取得平均數10,標準差10
# 平均數0標準差5 得到資料介於-5~5
random.normalvariate(100,10)

