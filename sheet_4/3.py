family_names = ['mohmed', 'ali', 'ahmed', 'fisal',"sayed"]

unique_letters = {letter for name in family_names for letter in name}


print(unique_letters)