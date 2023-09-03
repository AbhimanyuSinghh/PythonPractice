def swaplist(list):
    first = list.pop(0)
    last = list.pop(-1)
    
    list.insert(0,last)
    list.append(first)
    return list

if __name__    == "__main__":
    newList = [12,35,9,56,24]
    print(swaplist(newList))