def nLargest(list, N):
    size = len(list)
    list1 = []
    list.sort()
    i=0
    while(i<N):
        list1.append(list.pop())
        i+=1
        
    return list1

if __name__ == "__main__":
    list = [-45, 100, 200, 298, 900, 1000, 3579]
    N = 4
    print(nLargest(list, N))