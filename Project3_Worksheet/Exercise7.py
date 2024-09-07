'''
7. Write a function which takes an argument which should be a numeric +ve integer. Depending on
the input supplied you have to print “I CAN”, “I WILL”. Suppose some one enters argument as 1 then
only “I CAN” should be printed. But if some one enters 2 then first “I CAN” should be printed then “I
WILL”. And if someone enters 3 then following should be printed in corresponding order: “I CAN”, “I
WILL”, “I CAN” and so on for any numbers entered.

'''

def print_statements(n):
    if n <= 0:
        return "Input must be a positive integer."
    
    for i in range(n):
        if i % 2 == 0:
            print("I CAN")
        else:
            print("I WILL")

print_statements(1)  # Output: "I CAN"
print_statements(2)  # Output: "I CAN" "I WILL"
