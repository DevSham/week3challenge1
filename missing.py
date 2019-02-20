def miss(list):
    not_in_list = []
    for x in range(0,10):
         if x not in list:
            not_in_list.append(x)   
    return not_in_list
print(miss([2,4,5,6,7,8]))