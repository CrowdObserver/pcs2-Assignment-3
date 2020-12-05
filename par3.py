def par3(arr):
    l = [arr[0]]
    for i in arr[1:]:
        if i > arr[0]:
            l.append(i)
        elif i < arr[0]:
            l.insert(0, i)
        else:
            l.insert(l.index(i), i)
    return l


f = open("rosalind_par3.txt")
n = int(f.readline())
arr = list(map(int, f.readline().split()))
print(*par3(arr))