nums = [64, 97, 76, 20, 29, 34, 60, 89, 57, 85]
print("\t The Given Unsorted Array is:", nums,"\n")

def insert(arr):
    for i in range(1, len(arr)):
        j = 1
        while arr[j - 1] > arr[j] and j > 0: