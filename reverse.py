def reverseList(list):
    size = len(list)
    l,r = 0, size-1
    while(l<r):
        temp = list[l]
        list[l]=list[r]
        list[r]=temp
        l+=1
        r-=1
    
    print('list after reversing is: ',list)


if __name__ == "__main__":
    list= [1,2,3,4,5,6]
    print('list before rebersing: ', list)
    reverseList(list)