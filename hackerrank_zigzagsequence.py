def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2) -1 #Mistake Cause the middle isn't a true middle
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2  #Should subtract n-2 cause we already decrement by 1 in n uptop
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1   #Decrease by 1 each time for the end

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)



