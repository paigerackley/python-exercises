# --1. You have rented some movies for your kids: The little mermaid (for 3 days),
#  Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know 
# yet if they're going to like it). If price for a movie per day is 3 dollars, 
# how much will you have to pay?
cost = 3
little_mermaid_days = 3 
brother_bear_days = 5
hercules_days = 1
total_days = little_mermaid_days + brother_bear_days + hercules_days
total_cost = total_days * cost
print(f'The total cost is {total_cost} dollars')
# --2. Suppose you're working as a contractor for 3 companies: Google, 
# Amazon and Facebook, they pay you a different rate per hour. 
# Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
# How much will you receive in payment for this week? You worked 10 hours for 
# Facebook, 6 hours for Google and 4 hours for Amazon.
google = 400
amazon = 380
facebook = 350
total_pay = (google * 6) + (facebook * 10) + (amazon * 4)
print('Exercise 3:', total_pay)

# --3. A student can be enrolled to a class only if the class is not full and 
# the class schedule does not conflict with her current schedule.
class_full = False
class_schedule_conflict = False
can_be_enrolled = not class_full and not class_schedule_conflict
print(can_be_enrolled)

# --4. A product offer can be applied only if people buys more than 2 items, 
# and the offer has not expired. Premium members do not need to buy a 
# specific amount of products.
is_premium =True
offer_expired = False 
no_items = 3
product_offer = (not offer_expired and no_items >2) or is_premium
print(product_offer)

# --5. Continue working in your data_types_and_variables.py file. 
# Use the following code to follow the instructions below: 
username = 'codeup'
password = 'notastrongpassword'
#Create a variable that holds a boolean value for each of the following conditions:
five_characters_or_more = len(password) >= 5
username_twenty_or_less = len(username) <= 20
password != username 
#-the password must be at least 5 characters
#-the username must be no more than 20 characters
#-the password must not be the same as the username
#-bonus neither the username or password can start or end with whitespace