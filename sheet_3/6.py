d1 = {'a': 1}
d2 = {'a': 2}
d3 = {'b': 3}

all_dicts = [d1, d2, d3]
fin_di = {}

for dictionary in all_dicts:
    fin_di.update(dictionary)
    
print(fin_di)