My_file = open("hello fille", "a")
for i in range(1, 101):
    My_file.write(f"{i}\n" )
My_file.close()