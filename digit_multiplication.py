import math
def calc(word,lst):
    """Takes any whole number as input and then outputs the result of each step, 
    starting with the input itself, until we hit a single digit.
    :param word:user input.
    :param lst:to print the output list.
    """
    element=[eval(i) for i in list(str(word))]
    if len(element)==1:
        print(lst)
        return
    value=math.prod(element)
    lst.append(value)
    calc(value,lst)

input_no=eval(input("enter the element."))
calc(input_no,lst=[])
