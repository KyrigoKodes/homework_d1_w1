# #first question
# weather = "sunny"

# if weather == "sunny":
#     print("Wear sunglasses!")
# else:
#     print("Take an umbrella!")

# # Second question: Task 2: Your Mood Today,
# mood = input("How are you feeling today? ")
# answer = "I'm feeling " + mood + " today!"
# if mood == "happy":
#     print("That's great to hear!")
# elif mood == "sad":
#     print("I hope your day gets better!")

# # Third question: Task 3: Naming Convention Practice
# pi_value = 3.14
# user_age = 25
# USER_LOCATION = "New York"
# max_limit = 1000

# print(pi_value, user_age, USER_LOCATION, max_limit)

#Arithmetic Operations in Daily Life
# Task 1: Grocery Store Math Calculate
store_items = ["apple", "lasagna", "milk", "cheesecake"]
store_prices = [100, 6841, 202, 0.75]
total_cost = sum(store_prices)
combined_items = [item + " $" + str(price) for item, price in zip(store_items, store_prices)] #zip means to store the values from the array and interate through
print(combined_items)

# Task 2: Bank Interest Calculator
def calculate_total_amount(initial_amount, interest_rate): #defining the function (I've used functions in Javascript before so I'm familiar with the syntax)
    # Calculate the total amount after a year
    total_amount = initial_amount + (initial_amount * (interest_rate / 100))
    return total_amount

#making an amount of 30000 and interest rate of 9%
initial_amount = 30000  # Initial amount in dollars
interest_rate = 9      # Fixed yearly interest rate in percent

total_amount = calculate_total_amount(initial_amount, interest_rate) #changing the variable name 
#to total_amount as to include; 
#initial amount & interest rate
print("Total amount after a year: ${:.2f}".format(total_amount)) #the {:.2f} means to round to 2 decimal places
#printing the total amount after a year FORMATTED with 2 decimal places and the total amount