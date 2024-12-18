# Python Conditional Logic: Mastering Control Flow

"""
Author: Kalim Amzad Chy
Email: kalim.amzad.chy@gmail.com

This Python script is designed to provide an in-depth understanding of Python's conditional statements.
We will explore:
1. Basic if, if-else, and if-elif-else statements.
2. Logical and boolean operations in conditions.
3. Real-world applications with engaging examples.
4. Nested conditional statements for complex decision making.

Each section includes detailed explanations, examples, and assignments.
"""

# Section 1: Basic Conditional Statements
# ---------------------------------------
# The `if` statement is the simplest form of control flow, allowing for conditional execution of code blocks.

# Example 1: Simple if statement
"""age = 20
if age >= 18:
    print("You are eligible to vote.")
    print("Please register to vote as soon as possible.")

# The `if-else` statement provides an alternative execution when the `if` condition is not met.
# Example 2: if-else statement
temperature = 30
if temperature > 25:
    print("It's a hot day.")
else:
    print("It's not a hot day.")

# The `if-elif-else` structure allows for multiple conditions to be checked sequentially.
# Example 3: if-elif-else statement
score = 75
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D or F")"""

# Assignment 1: Write a Python script that determines if a number is positive, negative, or zero using if-elif-else.
# Write your code below:

number = int(input("Enter a number: "))

if number > 0:
    print("Positive Number")
elif number < 0:
    print("Negative Number")
else:
    print("Zero")

print ("\n")



# Section 2: Logical and Boolean Operations
# -----------------------------------------
# Logical operators (and, or, not) are used to combine conditional statements.

# Example 4: Using logical operators
"""height = 175
weight = 70
if height > 170 and weight > 65:
    print("You are fit for the sports team.")
else:
    print("You do not meet the physical requirements for the sports team.")

# Example 5: Combining conditions with or
day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
else:
    print("It's a weekday.")"""

# Assignment 2: Create a script that checks if a person is eligible for a senior citizen discount based on age and residency.
# Write your code below:

def solve(age, residency):
    # Check for invalid age
    if age <= 0:
        print("Not eligible")
        return

    # Check eligibility for senior citizen discount
    if age >= 60 and (residency == "YES" or residency == "yes" or residency == "Yes"):
        print("You are eligible for the senior citizen discount.")

    elif age >= 60 and (residency == "NO" or residency == "No" or residency == "no"):
        print("Not eligible.")
        
    else:
        print("Not eligible.")

def main():
    # Input age and residency
    age = int(input("Enter your age: "))
    residency = input("Are you a resident? (yes/no): ")

    # Call the solve function
    solve(age, residency)

if __name__ == "__main__":
    main()


print("\n");




# Section 3: Real-World Applications
# -----------------------------------
# Applying conditional logic to solve real-world problems.

# Example 6: Nested if-elif-else in a real-world context
# Ticket pricing system with age and membership checks
"""age = 65
member = True

if age < 18:
    price = 10
elif age >= 18:
    if member:
        price = 15
    else:
        price = 20

    if age >= 65:
        price -= 5  # Discount for seniors

print(f"Ticket price: ${price}")"""

# Assignment 3: Write a script that simulates a basic login system. Check username and password correctness.
# Write your code below:

def solve(user_email, user_password, correct_email, correct_pass):
    # Check if the entered email and password match the correct credentials
    if user_email == correct_email and user_password == correct_pass:
        return True
    return False

def main():
    # Input from user
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    
    # Predefined correct email and password
    correct_email = "abc@gmail.com"
    correct_pass = "admin"
    
    # Call the solve function to validate credentials
    is_valid = solve(email, password, correct_email, correct_pass)
    
    # Output result
    if is_valid:
        print("Valid password")
    else:
        print("Sorry, password or email is invalid. Try again later.")

if __name__ == "__main__":
    main()

print("\n");




# Example 7: Loan Approval System
# This example uses multiple conditions to determine if an applicant qualifies for a personal loan.
"""income = 45000
credit_score = 700
employment_status = "employed"
existing_loans = False

if (income > 40000 and credit_score >= 650) and (employment_status == "employed" and not existing_loans):
    print("Loan approved.")
else:
    print("Loan denied.")

# Example 8: Environment Control System
# A system that adjusts temperature and humidity based on multiple sensor readings.
temperature = 22
humidity = 85
weather_outside = "rainy"

if temperature < 20 or (humidity > 80 and weather_outside == "rainy"):
    print("Turning on heating and dehumidifier.")
elif temperature > 30 or (humidity < 30 and weather_outside == "sunny"):
    print("Turning on air conditioning and humidifier.")
else:
    print("No change needed.")

# Example 9: Custom Shipping Logic
# Determine shipping costs based on weight, distance, and customer loyalty.
weight = 5  # in kilograms
distance = 300  # in kilometers
is_loyal_customer = True

if weight > 10:
    shipping_cost = 25
elif weight > 5:
    shipping_cost = 15
else:
    shipping_cost = 5

if distance > 200:
    shipping_cost += 10

if is_loyal_customer:
    shipping_cost *= 0.9  # 10% discount for loyal customers

print(f"Total shipping cost: ${shipping_cost:.2f}")"""

# Assignment 4: Implement a system that categorizes a day based on temperature and weather conditions.
# Use nested if-elif-else and logical operators to determine if it's a beach day, skiing day, or a stay-home day.


def categorize_day(temperature, weather):
    # Convert weather to lowercase for case-insensitive comparison
    weather = weather.lower()

    # Categorize the day based on weather and temperature
    if weather == "sunny":
        if 25 <= temperature <= 35:
            print("It's a perfect beach day!")
        else:
            print("It's sunny but too hot. Stay hydrated indoors.")
    elif weather == "snowy":
        if temperature <= 0:
            print("It's a perfect skiing day!")
        else:
            print("It's snowy but not cold enough for skiing. Enjoy the scenery!")
    elif weather == "rainy" or weather == "cloudy" or (20 <= temperature <= 25):
        print("It's a rainy day. Better to stay home and relax.")
    else:
        print("Weather condition unknown. Stay safe and check the forecast!")

# Input temperature and weather condition
temperature = float(input("Enter the temperature (°C): "))
weather = input("Enter the weather condition (Sunny, Rainy, Snowy, Cloudy): ")

# Call the function to categorize the day
categorize_day(temperature, weather)




# Congratulations on completing the advanced section on Python conditional statements!
# Review the assignments, try to solve them, and check your understanding of control flow in Python.