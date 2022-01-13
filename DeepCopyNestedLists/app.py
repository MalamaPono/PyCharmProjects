def recursion(nested):
    result = []
    for item in nested:
        if(type(item) == list):
            inner_result = recursion(item)
            result.append(inner_result)
        else:
            result.append(item)
    return result

nested = [1, [ 2, [3,4,5,6] ], 7,8, [9,10, [11,12]]   ]

deep_copy = recursion(nested)