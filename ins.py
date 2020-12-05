def insertionSort(n, arr):
    count = 0
    for i in range(1, n):
        g = arr[i]
        j = i - 1
        while j >= 0 and g < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            count += 1
        arr[j+1] = g
    print(count)

