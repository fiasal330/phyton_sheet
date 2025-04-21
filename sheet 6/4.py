My_file = open("hello fille", "r")
y = My_file.readlines()  
My_file.close()

for x in y[49:60]:  
    print(x.strip())