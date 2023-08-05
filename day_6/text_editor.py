Q = int(input())
S = ''
arr = []
for i in range(Q):
    a = input()
    if a[0] == '1':
        arr.append(S)
        S += a[2:]
    if a[0] == '2':
        arr.append(S)
        ind = int(a[2:])
        S = S[:len(S)-ind]
    if a[0] == '3':
        ind = int(a[2:])
        print(S[ind-1])
    if a[0] == '4':
        S = arr.pop()