# 1. Define a function named is_two. It should accept one input and return True if the 
# passed input is either the number or the string 2, False otherwise.
 def is_two(n):
     return n == 2 or n == '2'
# 2. Define a function named is_vowel. It should return True if the 
# passed string is a vowel, False otherwise.
 def is_vowel(string):
     return string.lower() in ['a', 'e', 'i', 'o', 'u']
# 3. Define a function named is_consonant. It should return True if the passed 
# string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(string):
     return not is_vowel(string)
# 4. Define a function that accepts a string that is a word. The function should capitalize 
# the first letter of the word if the word starts with a consonant.
def cap_cons(string):
    if is_vowel(string[0]):
        return string
    else:
        return string.capitalize()
# 5. Define a function named calculate_tip. It should accept a tip percentage 
# (a number between 0 and 1) and the bill total, and return the amount to tip.
def calculate_tip(tip, total):
    return tip * total
# 6. Define a function named apply_discount. It should accept a original price, and a 
# discount percentage, and return the price after the discount is applied.
def apply_discount(price, discount):
    return price * (discount / 100)
# 7. Define a function named handle_commas. It should accept a string that is a 
# number that contains commas in it as input, and return a number as output.
def handle_commas(string):
    if type(string) != str:
        return string.replace(',', '')
# 8. Define a function named get_letter_grade. It should accept a number and 
# return the letter grade associated with that number (A-F).
def get_letter_grade(num):
    if num >= 90:
        return "A"
    elif num >= 80:
        return "B"
    elif num >= 70:
        return "C"
    elif num >= 60:
        return "D"
    else:
        return "F"
    # 9. Define a function named remove_vowels that accepts a string and returns a 
    # string with all the vowels removed.
def remove_vowels(string):
    new_string = " "
    for char in string:
        if char.lower() not in 'aeiou':
            new_string += char
    return new_string
# 10. 10) Define a function named normalize_name. It should accept a string and return a 
# valid python identifier, that is:
# A) Anything that is not a valid python identifier should be removed 
# Aa) No key words 
# Ab) No leading numbers 
# Ac) No special symbles               
# B) Leading and trailing whitespace should be removed 
# C) Everything should be lowercase 
# D) Spaces should be replaced with underscores 
def normalize_name(string):
    name = lower(name) # lowercase it first
    name = name.strip(" ") # "remove leading and trailing whitespace"
    name = name.replace(" ", "_") #conver space to underscore
    name = [letter for letter in name if letter.isidentifier()] # removes everything that's 
    # not a valid identifier
        return name
 # 11
 def cumulative_sum(somenums):
     output = []
     for i, num in enumerate(somenums):
         sum_so_far = sum(somenums[:i + 1])
         output.append(sum_so_far)
    return output

  