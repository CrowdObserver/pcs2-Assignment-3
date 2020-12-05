def threeSum(arr):
    s = sorted(arr)
    for i in range(len(arr)):
        a = s[i]
        bot = i + 1
        top = len(arr) - 1
        while bot < top:
            b = s[bot]
            c = s[top]
            if (a + b + c) == 0:
                result = sorted([arr.index(a) + 1, arr.index(b) + 1, arr.index(c) + 1])
                return result
            elif (a + b + c) > 0:
                top -= 1
            else:
                bot += 1
    return "-1"


f = open("rosalind_3sum.txt")
n, m = map(int, f.readline().split())
for i in range(n):
    print(*threeSum(list(map(int, f.readline().split()))))