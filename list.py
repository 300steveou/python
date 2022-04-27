# 清單用法
 
name="a"
name="b"
name="c"
name="d"
name="e"

# 轉換為
names =["a","b","c","d","e"]

# print(names)
# print(names[2])
# print(names[-2])

# b :2=>取得第二位的所有值
print(names[1:2])
# abc
print(names[0:3])
# cde
print(names[2:5])
# cd
print(names[2:4])

# 從第一位開始取 取到結束
print(names[1:])

phrase = "Hello World"
print(phrase[6])
print(phrase[5])

print(phrase[1:3])

# 函式 extend
scores=["90","70","85","40","50"]
names.extend(scores)

print(names)
names.append("777")
print(names)

# 插入 參數1為第幾個
names.insert(2,"666")
print(names)

# 移除
names.remove("666")
print(names)

# pop 移除列表的最後一位
names.pop()
print(names)

# clear 清除 把列表全清除
names.clear()
print(names)

# 排序
names =["10","50","35","40","38","40"]
names.sort()
print(names)

# 反轉
names.reverse()
print(names)

# index 一定要包含裡面的
print(names.index("50"))
# print(names.index("80"))

# count 清單有多少個40
print(names.count("40"))
print(names.count("99"))