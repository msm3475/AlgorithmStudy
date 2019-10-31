def selectionSort(list):
    for i in range(len(list)):

        print("iiiiiiiiiiiiiii : ", i)
        min_index = i

        for j in range(i+1, len(list)):
            if list[min_index] > list[j]:
                print("-------------")
                print("list[min_index] : ", list[min_index])
                print("list[j] : ", list[j])

                min_index = j
                print(list)
                print("min_index : ", min_index)

        list[i], list[min_index] = list[min_index], list[i]

selectionSort([9,10,5,3,2])
