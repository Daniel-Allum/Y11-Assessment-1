from testhelper import test

def sum_number_lists(list1, list2):
    if len(list1) != len(list2):
        return "The lists are different lengths."

    if not all(isinstance(x, (int, float)) for x in list1) or not all(isinstance(x, (int, float)) for x in list2):
        return "One of the lists has a non-number character."

    return [x + y for x, y in zip(list1, list2)]


### TESTS - Run the code that calls the function to check it works.
test("Sum number lists 1", [4,5,7,8,10,11,13], sum_number_lists([1,2,3,4,5,6,7], [3,3,4,4,5,5,6]))
test("Sum number lists 2", [11,12,13,14,15,16,17], sum_number_lists([1,2,3,4,5,6,7], [10,10,10,10,10,10,10]))
