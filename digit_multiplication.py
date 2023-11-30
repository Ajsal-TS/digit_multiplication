import math
def calc(word,lst):
    list1=list(str(word))
    element=[eval(i) for i in list1]
    if len(element)==1:
        print(lst)
        return
    value=math.prod(element)
    lst.append(value)
    calc(value,lst)

n=eval(input("enter the element."))
calc(n,lst=[])
