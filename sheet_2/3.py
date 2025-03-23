file_name = "/home/user/projects/my_project/file.txt"
file_name = file_name.split("/")
file_name = file_name[5].split(".")

print(file_name[0]," , ", type(file_name))