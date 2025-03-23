def substitute(equation, **kwargs):

    for key, value in kwargs.items():
        
        equation = equation.replace(key, str(value))
    
    return eval(equation)


result = substitute("2 * x + 3 * y", x=4, y=5)
print(result)