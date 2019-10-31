#encoding=utf-8
def quicksort(arr):
    if len(arr) <=1 :
        return arr

    pivot = arr[len(arr) //2]
    print("pivot: ",pivot)

    left = [x for x in arr if x < pivot]
    print("left: ", left)

    middle = [x for x in arr if x == pivot]
    print("middle: ", middle)

    right = [x for x in arr if x > pivot]
    print(right)

    return quicksort(left) + middle + quicksort(right)

print(quicksort([3,6,8,10,1,2,1]))
