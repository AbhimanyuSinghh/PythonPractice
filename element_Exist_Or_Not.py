def checkElement(testlIST, num):
    
        if testlIST.count(num) > 0:
            print( str(num) + ' is present in your list')
        else:
            print( str(num) +  ' is not present in your list')    
            
if  __name__ == "__main__":
    
        list= [1, 6, 3, 5, 3, 4]
        number= int(input("enter the element you wish to check if it is in the list\n"))
        checkElement(list, number)