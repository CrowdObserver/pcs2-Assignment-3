def Major(arr):
    g = {}
    b = False
    for _ in arr:
        if _ not in g:
            g[_] = arr.count(_)
    for _ in g:
        if g[_] > (len(arr) / 2):
            print(_, end = " ")
            b = True
            break
        else:
            continue
    if b == False:
        print(-1, end = " ")

f = open("rosalind_maj.txt")
l = list(map(int, f.readline().split()))
for m in range(l[0]):
    arr = list(map(int, f.readline().split()))
    Major(arr)