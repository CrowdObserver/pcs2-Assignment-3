def binSearch(n, arr, bot, top):
    if n in arr:
        mid = (bot + top) // 2
        if n == arr[mid]:
            return mid + 1
        if n > arr[mid]:
            return binSearch(n, arr, mid + 1, top)
        if n < arr[mid]:
            return binSearch(n, arr, bot, mid - 1)
    else:
        return -1


f = open("rosalind_bins.txt")
top = int(f.readline())
k = int(f.readline())
arr = list(map(int, f.readline().split()))
temp = list(map(int, f.readline().split()))
bot = 0

for _ in temp:
    print(binSearch(_, arr, bot, top), end = " ")