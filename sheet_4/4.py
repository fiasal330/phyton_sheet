def average(*numbers):
    s = len(numbers)

    avg = 0
    for i in range(s):
        avg += numbers[i]

    return  avg/ s

avg = average(1, 2, 3, 4, 5)

print(avg)