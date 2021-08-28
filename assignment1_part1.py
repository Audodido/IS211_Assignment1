
#Create a function named listDivide that returns the number of elements in the numbers list that are divisible 
#by divide

# list1 = [1,3,5,6,8,9,12,6,7,78,24,55,23,16,88]

class ListDivideException(Exception):
    pass

def listDivide(numbers, divide=2):
    try:
        list2 = [i for i in numbers if i % divide ==0]
        return len(list2)
    except:
        raise ListDivideException()

def testListDivide():
    try:
        listDivide([1,2,3,4,5])
        listDivide([2,4,6,8,10])
        listDivide([30, 54, 63,98, 100], divide=10)
        listDivide([])
        listDivide([1,2,3,4,5], 1)
        # print("Success!") 
    except:
        raise ListDivideException()

testListDivide()


