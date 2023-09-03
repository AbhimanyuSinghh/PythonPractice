def Multiply(list):
    mul = 1
    size = len(list)
    while(size!=0):
       mul = mul * list.pop()
       size-=1
    
    return mul


if __name__ == "__main__":
    list = [11, 5, 17, 18, 23]
    print('the product of elements of the list is: ', Multiply(list))
        