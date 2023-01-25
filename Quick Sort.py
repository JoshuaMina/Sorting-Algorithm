nums = [64, 97, 76, 20, 29, 34, 60, 89, 57, 85]
print("\t The Given Unsorted Array is:", nums,"\n")

def quick(arr, left, right):
    if left < right:
        partition_pos = partition(arr,left, right)
        quick(arr, left, partition_pos-1)
        quick(arr, partition_pos+1, right)



def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]
    print(arr)
    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]


    return i

quick(nums, 0, len(nums)-1)

print("\t\n The Final Sorted Array is:",nums)