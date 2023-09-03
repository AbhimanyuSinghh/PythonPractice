def Indices(list, ele):
    size = len(list)
    for i in range(size-1):
        if list[i] == ele:
            print(i)
        
if __name__ == "__main__":
    list = [1, 2, 3, 1, 5, 4]
    item = 1
    Indices(list, item)