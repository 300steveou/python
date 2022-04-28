# 二為列表

nums = [
   [0,1,2],
   [3,4,5],
   [6,7,8]
]

# result 2
print(nums[0][2])
# result7
print(nums[2][1])

for row in nums:
    for item in row:
        print(item)

