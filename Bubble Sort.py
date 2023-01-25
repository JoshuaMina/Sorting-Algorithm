nums = [64, 97, 76, 20, 29, 34, 60, 89, 57, 85]
print("\t The Given Unsorted Array is:", nums,"\n")

for i in range(len(nums)-1,0,-1):
    for j in range(i):
        if nums[j] > nums[j + 1]:
            temp = nums[j]
            nums[j] = nums[j + 1]
            nums[j + 1] = temp