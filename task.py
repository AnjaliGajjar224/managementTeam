
"""
1.  A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
    # Ask user for quantity
    # Assume each unit's cost is 100.
    # Judge and print total cost for user. 

2. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.

3. A student will not be allowed to sit in exam if his/her attendance is less than 75%.
    # Take following input from user:
    # Number of classes held
    # Number of classes attended.
    # And print:
    # percentage of class attended
    # Is student is allowed to sit in exam or not.
"""

quantity = int(input("Enter the quantity: "))

cost = quantity * 100

if cost >= 1000:
    discount = (cost * 10)/100
    total_cost = cost - discount
    print("Total cost: ", total_cost)

else:
    print("Total cost: ", cost)
