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

# challenge 2: Prime number  checker

print("\n=== Challenge 2: Prime Number Checker ===") # prints the header for challenge 2 

n = int(input("Enter a number: ")) # prompts user to enter a number 

print(f"Testing divisors from 2 to {n-1}...") # testing if any number from 2 to n-1 divides evenly into n  

prime = True # states that n is prime until it enters to for loop to see if it really is 

for i in range(2, n):
    if n % i ==0:
        print(f"{n} is not prime (divisible by {i})")
        prime = False # makes prime false because it it not a prime number 
        break # ends the for loop 
if prime:
    print(f"{n} is prime!")

# challenge 3: Multiplication table grid

print("\n=== Challenge 3: Multiplication Table ===") # prints the challenge 3 header

print("Multiplication Table:") # prints the multiplcation header

print("   ", end="")
for col in range(1,11):
    print(f"{col:4}", end="")
print()

for row in range(1,11):
    print(f"{row:2} ",end="")
    for col in range(1,11):
        product = row*col
        print(f"{product:4}",end="")
    print()





    
