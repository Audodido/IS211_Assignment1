#Original template

#Create a function named listDivide that returns the number of elements in the numbers list that are divisible by 2


class ListDivideException(Exception):
    pass


def listDivide(numbers, divide=2):

    """
    Returns number of elements in the numbers list that are divisible by another number (default=2)

    Args:
        numbers (list): List of numbers to check 
        divide (int): Number to divide elements in list by

    Returns:
        Sum (int) of instances where list element was divisible by "divide"
    """

    try:
        list2 = [i for i in numbers if i % divide ==0]
        return len(list2)
    except:
        raise ListDivideException()


def testListDivide():
    """
    Tests listDivide function for errors
    """
    try:
        listDivide([1,2,3,4,5])
        listDivide([2,4,6,8,10])
        listDivide([30, 54, 63,98, 100], divide=10)
        listDivide([])
        listDivide([1,2,3,4,5], 1)
        # print("Success!") 
    except:
        raise ListDivideException()

if __name__ == "__main__":
    testListDivide()


