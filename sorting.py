#a function that takes a list and returns a dictionary with keys evens, odds, and chars.
def sort(list_sort):
#creating an empty dictionary to hold the output.
    dictionary = {}
#creating empty lists to hold the even, odd and
    even = []
    cahr = []
    odd = []
#cheking for values in the list
    for x in list_sort:
#if x in an integer and divisible by 2, place it in the even list.
        if isinstance(x, int):
            if x%2 == 0:
                 even.append(x)     
#if x in an integer and not divisible by 2, place it in the odd list.
            elif x%2 != 0:
                odd.append(x) 
#if x is a float and divisible by 2, place it in the even list.
        elif isinstance(x, float):
            if x%2 == 0:
                even.append(x) 
#if x in an float and not divisible by 2, place it in the odd list.
            elif x%2 != 0:
                odd.append(x)     
#if x is a string, place it in the characters list.
        elif isinstance(x, str):
            cahr.append(x)    
#adding list values and keys to the dictionary.        
    dictionary["even"] = sorted(even)
    dictionary["odd"] = sorted(odd)
    dictionary["char"] = sorted(cahr)
    return dictionary
#calling the function.
print(sort([1, 9, 9.0, 4.6,5,7,6,10,12,20,30,14,17,12,"d", "u", "g"]))
