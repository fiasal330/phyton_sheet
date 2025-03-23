sequence = [10, 20, 30, 40, 50, 60]
even_sum = 0
odd_sum = 0

for i in range(len(sequence)):
    if i % 2 == 0:
        even_sum += sequence[i]
    else:
        odd_sum += sequence[i]


print(f"Even sum: {even_sum}")
print(f"Odd sum: {odd_sum}")
