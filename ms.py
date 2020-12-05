def MergeSort(arr):
    if len(arr) == 1:
        return arr
    else:
        temp = []
        right = arr[:len(arr) // 2]
        left = arr[len(arr) // 2:]
        right = MergeSort(right)
        left = MergeSort(left)
        i = 0
        j = 0
    while i < len(right) and j < len(left):
        if right[i] <= left[j]:
            temp.append(right[i])
            i += 1
        else:
            temp.append(left[j])
            j += 1
    temp += right[i:]
    temp += left[j:]
    return temp


f = open("rosalind_ms.txt")
n = f.readline()
arr = list(map(int, f.readline().split()))
print(*MergeSort(arr))
