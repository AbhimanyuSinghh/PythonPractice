def emptyList(list):
    newlist = [] 
    for i in range(len(list)):
        if list[i] is []:
            newlist.append(list[i])
            
    return newlist

if __name__ == "__main__":
    list = [5, 6, [], 3, [], [], 9]
    print(emptyList(list))
    