nums = [64, 97, 76, 20, 29, 34, 60, 89, 57, 85]
print("\t The Given Unsorted Array is:", nums,"\n")

def merge(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr) // 2:]

        merge(left_arr)
        merge(right_arr)

        i=0
        j=0
        k=0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1

