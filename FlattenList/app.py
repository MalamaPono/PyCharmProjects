def flatten(nested):

    result = []

    def recursion(nested):
        for item in nested:
            if(type(item) == tuple or type(item) == list):
                recursion(item)
            else:
                result.append(item)

    recursion(nested)
    return result

nested = [1, [ 2, [3,4,5,6] ], 7,8, [9,10, [11,12]]   ]

print(flatten(nested))