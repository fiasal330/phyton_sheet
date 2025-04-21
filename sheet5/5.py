
def modlist(lst):
    for i in range(len(lst)):
        lst[i] = 10 * lst[i]

def modvar(num):
    num += 10

lst = [1, 2, 3]
modlist(lst)
print(lst)

x = 0
modvar(x)
print(x)

#the output will bee [10, 20, 30]
# 0