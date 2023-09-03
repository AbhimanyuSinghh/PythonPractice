def even(list):
    listEven = []
    for i in list:
        if i%2 == 0:
            listEven.append(i)
            
    return listEven

if __name__ == "__main__":
   list = [2, 7, 5, 64, 14]
   print(even(list))