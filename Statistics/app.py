def constrained_compositions(n, m):
    # inputs: n is of type 'int' and m is a list of integers
    # output: a set of tuples

    k = len(m)
    parts = set()
    if k == n:
        if 1 <= min(m):
            parts.add((1,) * n)
    if k == 1:
        if n <= m[0]:
            parts.add((n,))
    else:
        for x in range(1, min(n - k + 2, m[0] + 1)):
            for y in constrained_compositions(n - x, m[1:]):
                parts.add((x,) + y)
    return parts

# modify this cell

# modify this cell

def face_sum(m, s):
    # inputs: m is list of integers and s is an integer
    # output: a variable of type 'float'

    valid_compositions = len(constrained_compositions(s, m))
    total_compositions = 1
    for i in m:
        total_compositions = i * total_compositions
    probability = valid_compositions / total_compositions
    return probability

print(face_sum([3, 4, 5], 13))
print(face_sum([2,2],3))
print(face_sum([3, 4, 5], 7))