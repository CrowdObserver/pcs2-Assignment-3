def twoSum(arr):
    d = {}
    for i in range(len(arr)):
        if -arr[i] in d:
            print(d[-arr[i]] + 1, i + 1)
            return
        else:
            d[arr[i]] = i
    print(-1)
    return

f = open("rosalind_2sum.txt")
n, m = map(int, f.readline().split())
for i in range(n):
    twoSum(list(map(int, f.readline().split())))
