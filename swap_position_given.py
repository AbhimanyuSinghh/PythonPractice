#here positions given are actually numerical positions and not the index



def swaplist(list,pos1,pos2):
    first = list.pop(pos1)
    other = list.pop(pos2-1)
    
    list.insert(pos1, other)
    list.insert(pos2, first)
    return list

if __name__    == "__main__":
    newList = [1,5,3,4,2]
    pos1= 2
    pos2= 5
    print(swaplist(newList,pos1-1,pos2-1))