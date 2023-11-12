if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    n = int(input())
    li = []
    for x in range(0, a + 1):
        for y in range(0, b + 1):
            for z in range(0, c + 1):
                li.append([x,y,z])
                #print(li)
    #m = len(li)
    #print(m)
    new_li = []
    for i in (li):
        if i[0] + i[1] + i[2] != n:
            new_li.append(i)
    print(new_li)
