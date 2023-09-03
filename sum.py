def Sum(list):
    sum = 0
    size = len(list)
    while(size!=0):
        sum = sum + list.pop()
        size-=1
    
    return sum


if __name__ == "__main__":
    list = [11, 5, 17, 18, 23]
    print('the sum of elements of the list is: ', Sum(list))
        