# --1. Conditional Basics
#write the python code that calculates the weekly paycheck. 
# You get paid time and a half if you work more than 40 hours
# --1a. prompt the user for a day of the week, print out whether the day is Monday or not
day = input("What day of the week is it?")

if day.lower() in ['Monday', 'mon']:
    print('Happy Monday!')
else:
    print(f'Today is {day.capitalize()}')
# --1b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend
day = input("What day of the week is it?")

if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    print("It's a weekday!")
else:
    print("Enjoy your weekend!")
# --1c. Create variables and make up values for:
#  -- the number of hours worked in one week
#  -- the hourly rate
# -- how much the week's paycheck will be
# --write the python code that calculates the weekly paycheck.
# You get paid time and a half if you work more than 40 hours
hours_worked = 41
hourly_rate = 22
next_weeks_pay = (hours_worked * hourly_rate)
if hours_worked > 40:
    hourly_rate = (hourly_rate * 1.5)
print(next_weeks_pay)
# -- 2. Loop basics
# While
# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.
i = 5

while i <= 15:
    print(i)
    i = i + 1
# Create a while loop that will count by 2's starting with 0 and ending at 100. 
# Follow each number with a new line.
i = 0

while i <= 100:
    print(i)
    i= i + 2
# Alter your loop to count backwards by 5's from 100 to -10.
i = 100

while i >= -10:
    print(i)
    i = i - 5
# Create a while loop that starts at 2, and displays the number squared on each
#  line while the number is less than 1,000,000
i = 2

while i <= 1000000:
    print(i)
    i = i ** 2
# Write a loop that uses print to create the output shown below.
i = 100
while i >= 5:
    print(i)
    i += -5
# For loops. Write some code that prompts the user for a number, then shows a 
# multiplication table up through 10 for that number.
entered_number = input("Enter a number")
entered_number = int(entered_number)
for n in range (1,11):
    print(f'{entered_number} X {n} = {entered_number* n}')

# Create a for loop that uses print to create the output shown below.
for n in range(1,10):
    print(str(n) * n)

# Break and continue: i.
while True:
    entered_number = input('Please insert an odd number between 1 and 50: ')
    if entered_number.isdigit():
        if int(entered_number) % 2 == 1 and int(entered_number) <= 50:
         break

# d. 
while True: 
    positive_number = input("Enter a positive number")
    if positive_number.isdigit():
            if int(positive_number) > 0:
                break
positive_number = int(positive_number)
for n in range(0, positive_number + 1):
    print(n)
# e. Write a program that prompts the user for a positive integer. Next write a 
# loop that prints out the numbers from the number the user entered down to 1.
while True:
    positive_number = input("Please enter a positive nunber")
    if positive_number.isdigit():
        if int(positive_number) > 0:
            break
positive_number = int(positive_number)
for n in range(positive_number, 0, -1):
    print(n)
# 3. Fizzbuzz
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('Fizzbuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
# 4. Display a table of powers
num = input("Please enter a positive number")

print('Here is your table!')
print('squared|squared|squared')
print('-----|-----|------')

num = int(num)
for i in range(1, num + 1):
    print(f' {i}|   {i ** 2}   | {I ** 3}')
    









