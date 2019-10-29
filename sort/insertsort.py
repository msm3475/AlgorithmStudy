def insertSort(list):
    for i in range(1, len(list)):

        print("i : ", i)
        key = list[i]

        print("key :", key)

        j = i-1

        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            print("list : ", list)

            j-=1

        print("key before : ", list)
        list[j+1] = key
        print("key after : ", list)

print(insertSort([9,10,5,3,2]))
