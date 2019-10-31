def mergeSort(list) :
    if len(list) > 1:
        mid = len(list) // 2

        left = list[:mid]
        right = list[mid:]

        print("left : ", left)
        mergeSort(left)

        print("right : ", right)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j] :
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k +=1
        print("임시로 list 정렬 : ", list)

        while i < len(left) :
            list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1

        print("최종적으로 정렬된 list :", list)
        print("")


mergeSort([38,27,43,3,9,82,10])
