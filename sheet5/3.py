# the output will be [2, 3, 4]


def apply(lst, fn):
    result = []
    for elem in lst:
        result.append(fn(elem))
    return result

def add_1(num):
    return num + 1

r = apply([1, 2, 3], add_1)
print(r)

#The map function

def sum_1(x):
    return x + 1

r = list(map(sum_1, [1, 2, 3]))  
print(r)  


