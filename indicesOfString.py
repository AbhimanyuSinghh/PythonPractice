def indicesString(list):
    list1 = []
    for i in range(len(list)-1):
        if type(list[i]) is str:
            list1.append(i)
            
    return list1


if __name__ == "__main__":
    list = ['sravan', 98, 'harsha', 'jyothika', 'deepika', 78, 90, 'ramya']
    print(indicesString(list))