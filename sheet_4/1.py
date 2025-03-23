import random

def pa(length, characters):
    return ''.join(random.choice(characters) for x in range(length))

x = int(input("pleace Enther the password amount :  "))
y = input("Enter a charcther in youre password : ")
p = pa(x,y)
print(p)