# Python File I/O and JSON Handling: Comprehensive Guide

"""
Author: Kalim Amzad Chy
Email: kalim.amzad.chy@gmail.com

This Python script provides a comprehensive guide to file input/output operations and JSON handling.
We will explore:
1. Reading and writing to plain text files.
2. Working with CSV files using the csv module.
3. Handling JSON data with the json module.
4. Practical examples and real-world applications.

Each section includes detailed explanations, examples, and assignments.
"""

# Section 1: Plain Text Files
# ---------------------------
# Reading and writing plain text files is often the first step in file manipulation.

# Example 1: Writing to a Text File
#with open('data/example.txt', 'w') as file:
 #   file.write("Hello, Python developers!\n")
 #   file.write("Welcome to file I/O operations.")

# Example 2: Reading from a Text File
#with open('data/example.txt', 'r') as file:
#    content = file.read() # readlines(), readlines()
 #   print(content)

# Section 2: CSV Files
# --------------------
# CSV (Comma-Separated Values) files are commonly used for storing tabular data.

#import csv

# Example 3: Writing to a CSV File
#with open('data/example.csv', 'w', newline='') as file:
#    writer = csv.writer(file)
#    writer.writerow(["Name", "Age", "City"])
 #   writer.writerow(["Alice", 28, "New York"])
 #   writer.writerow(["Bob", 22, "Los Angeles"])
 #   writer.writerow(["Carol", 24, "Chicago"])

# Example 4: Reading from a CSV File
#with open('data/example.csv', 'r') as file:
#    reader = csv.reader(file)
#    for row in reader:
#        print(row)


# Section 3: JSON Data
# --------------------
# JSON (JavaScript Object Notation) is a lightweight data-interchange format.

#import json

# Example 5: Writing JSON to a File
#data = {
 #   "name": "Alice",
 #   "age": 30,
 #   "city": "New York"
#}
#with open('data/data.json', 'w') as file:
#    json.dump(data, file)


# Example 6: Reading JSON from a File
#with open('data/data.json', 'r') as file:
#    data = json.load(file)
#    print(data)

# Section 4: Practical Applications
# ---------------------------------
# Combining file I/O with real-world data processing.

# Example 7: Processing JSON Data from a File
# Suppose we have a JSON file containing multiple user records.
#users = [
#    {"name": "Alice", "age": 25, "email": "alice@example.com"},
#    {"name": "Bob", "age": 30, "email": "bob@example.com"}
#]
#with open('data/users.json', 'w') as file:
#    json.dump(users, file)

#with open('data/users.json', 'r') as file:
#    users = json.load(file)
#    for user in users:
 #       print(f"{user['name']} ({user['age']}): {user['email']}")

# Assignments
# -----------
# Assignment 1: Write a script that reads a CSV file containing product information and converts it into a JSON file.

import csv

# Define the file name
csv_file = 'products.csv'

# Open the file in write mode
with open(csv_file, 'w', newline='') as file:
    # Create a writer object
    writer = csv.writer(file)
    
    # Write the header row
    writer.writerow(["Product Name", "Product ID", "Price", "Quantity"])
    
    # Write data rows
    writer.writerow(["Laptop", 101, 800.50, 10])
    writer.writerow(["Smartphone", 102, 500.75, 25])
    writer.writerow(["Tablet", 103, 300.99, 15])
    writer.writerow(["Headphones", 104, 50.25, 50])
    writer.writerow(["Smartwatch", 105, 150.00, 20])

print(f"The file '{csv_file}' has been created successfully!")



import csv
import json

# Define file names
csv_file = 'products.csv'  # Input CSV file
json_file = 'products.json'  # Output JSON file

# Read the CSV file and convert it to a list of dictionaries
data = []
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)  # Read rows as dictionaries
    for row in reader:
        data.append(row)

# Write the data to a JSON file
with open(json_file, 'w') as file:
    json.dump(data, file, indent=4)  # Pretty-print with 4-space indentation

print(f"The file '{json_file}' has been created successfully!")
print("\n")



# Assignment 2: Create a log file writer that appends log messages to a file with timestamps.

from datetime import datetime

# Define the log file name
log_file = 'app.log'

def write_log(message):
    """
    Appends a log message with a timestamp to the log file.
    """
    # Get the current timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Format the log message
    log_message = f"[{timestamp}] {message}\n"
    
    # Append the log message to the file
    with open(log_file, 'a') as file:
        file.write(log_message)

    print(f"Log written: {log_message.strip()}")

# Example usage
write_log("Application started.")
write_log("Processing data...")
write_log("Application finished successfully.")

# Congratulations on completing the comprehensive section on Python file I/O and JSON handling!
# Review the assignments, try to solve them, and check your understanding of file operations and data formats.