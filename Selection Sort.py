def sort(nums):
    for i in range(5):
        minpos = i
        for j in range(i, 6):
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

        print(nums)

nums = [64, 97, 76, 20, 29, 34, 60, 89, 57, 85]
sort(nums)

print(nums)