def countInversions(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        temp = []
        right = arr[:len(arr) // 2]
        left = arr[len(arr) // 2:]
        right, invRight = countInversions(right)
        left, invLeft = countInversions(left)
        i = 0
        j = 0
        inv = invRight + invLeft
    while i < len(right) and j < len(left):
        if right[i] <= left[j]:
            temp.append(right[i])
            i += 1
        else:
            temp.append(left[j])
            j += 1
            inv += (len(right) - i)
    temp += right[i:]
    temp += left[j:]
    return temp, inv



f = open("rosalind_inv.txt")
n = int(f.readline())
arr = list(map(int, f.readline().split()))
print(countInversions(arr)[1])