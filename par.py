def twoWayPartition(arr):
    l = [arr[0]]
    for i in arr[0:]:
        if i > arr[0]:
            l.append(i)
        elif i < arr[0]:
            l.insert(0,i)
    return l


f = open("rosalind_par.txt")
n = int(f.readline())
arr = list(map(int, f.readline().split()))
print(*twoWayPartition(arr))