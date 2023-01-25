nums = [64, 97, 76, 20, 29, 34, 60, 89, 57, 85]
print("\t The Given Unsorted Array is:", nums,"\n")

def merge(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr) // 2:]
