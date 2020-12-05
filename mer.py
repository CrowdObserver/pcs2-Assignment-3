def mergeSort(arr1, arr2, arr):
    while len(arr1) != 0 or len(arr2) != 0:
        if len(arr1) == 0:
            arr += arr2
            arr2 = []
        elif len(arr2) == 0:
            arr += arr1
            arr1 = []
        else:
            if arr1[0] > arr2[0]:
                arr.append(arr2[0])
                arr2.remove(arr2[0])
            else:
                arr.append(arr1[0])
                arr1.remove(arr1[0])
    print(*arr)


f = open("rosalind_mer.txt")
n = int(f.readline())
arr1 = list(map(int, f.readline().split()))
m = int(f.readline())
arr2 = list(map(int, f.readline().split()))
arr = []
mergeSort(arr1, arr2, arr)