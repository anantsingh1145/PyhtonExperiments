arr = map(int, input(print("enter a range of number :-")).split())

li = []

def duplicate_values(duplist):
    for i in duplist:
        if i not in li:
            li.append(i)
    return li
duplicate_values(arr)
print(li)
