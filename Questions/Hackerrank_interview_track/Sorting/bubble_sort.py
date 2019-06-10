def countSwaps(a,n):
    num_swaps=0
    for i in range(n):
        for j in range(i,n):
            if a[i]>a[j]:
                num_swaps+=1
                a[i],a[j]=a[j],a[i]

    print "Array is sorted in {} swaps.".format(num_swaps)
    print "First Element: {}".format(a[0])
    print "Last Element: {}".format(a[-1])


if __name__ == '__main__':
    n = int(raw_input())

    a= map(int, raw_input().rstrip().split())

    countSwaps(a,n)