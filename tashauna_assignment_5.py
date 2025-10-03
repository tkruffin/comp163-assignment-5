print("=== Challenge 1: Collatz Conjecture ===") # prints the header 

current_number = int(input("Enter starting number: ")) # takes the users first number to start the sequence
step_count = 0 # intialize the steps count as zero so that the program ca increment the amount of steps in he sequence

print("Sequence:",current_number, end=" ") # prints the sequence starter number

while current_number != 1: # will continjue the sequence unitl the number is now equal to 1 
    if current_number % 2 == 0:
        current_number = current_number // 2 # when the number is even it will get divided by 2
    else:
        current_number = 3 * current_number + 1 # when the number is odd it will multiply by 3 and add 1 
    step_count +=1  # increments the step count by one when there is another step taken
    print(current_number, end=" ") # prints the sequence  

print()
print(f"Steps: {step_count}") # prints the amount of steps took 

