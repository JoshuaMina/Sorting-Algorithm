def sort(nums):
    for i in range(5):
        minpos = i
        for j in range(i, 6):
            if nums[j] < nums[minpos]:
