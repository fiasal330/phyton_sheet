
number_of_runs = 0
total_time = 0.0

while True:
    
    user_input = input("Enter 10 km run time : ")

    if user_input == "" or user_input == "0":
        break

        
    run_time = float(user_input)
    total_time += run_time
    number_of_runs += 1


av = total_time / number_of_runs
print(f"Average of {av} , over {number_of_runs} runs ")
