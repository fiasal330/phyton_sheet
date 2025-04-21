x = [1, 2, 10, 13, 1]
# output = [False, True, True, False, False]

x = [True if nums % 2 == 0 else False for nums in x]
print(x)