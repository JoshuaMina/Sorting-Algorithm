nums = [64, 97, 76, 20, 29, 34, 60, 89, 57, 85]

def sort(nums):
    for i in range(len(nums)):
        minpos = i
        for j in range(i, 10):
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

        print(nums)


sort(nums)

print(nums)