def clearList(list):
    while(len(list)!=0):
        list.pop()
        
    print('list after clearing the elements is: ', list)
    
    
if __name__ == "__main__":
    list= [1,2,3,4,5,6,7,8,9,10]
    print('list before clearing the elements is: ', list)
    clearList(list)