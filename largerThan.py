def largerThen(list, value):
    size = len(list)
    for i in range(size-1):
        if list[i]>value:
            list.pop(i)
            
    return list
if __name__ == '__main__':
    list = [12, 33, 10, 20, 25]
    value = 21
    print(largerThen(list, value))
    