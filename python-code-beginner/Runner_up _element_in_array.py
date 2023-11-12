if __name__ == '__main__':
    #n = int(input())
    arr = map(int, input().split())

    li = []


    def duplicate_values(duplist):
        for i in duplist:
            if i not in li:
                li.append(i)
        return li


    duplicate_values(arr)

    li[0:] = sorted(li[0:], reverse=True)
    print(li[1])

    '''
    max = li[0]
    min = li[0]
    new_li = []

    for x in range(0, len(arr)):
        if li[x] >= max:
            max = li[x]

        elif li[x] <= min:
            min = li[x]
    print(new_li)
    '''

