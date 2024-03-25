# Task 1: Identify the Greatest

print("Enter first number:")
val_1 = input()

print("Enter second number:")
val_2 = input()

print("Enter third number:")
val_3 = input()

largest_value = val_1

if largest_value < val_2:
    largest_value = val_2

if largest_value < val_3:
    largest_value = val_3

print("Largest number from inputs is: " + str(largest_value))


# Task 2: Identify the Smallest
smallest_value = val_1

if smallest_value > val_2:
    smallest_value = val_2

if smallest_value > val_3:
    smallest_value = val_3

print("Smallest number from inputs is: " + str(smallest_value))


# Task 3: Equality Check

if val_1 == val_2 == val_3:
    print("All numbers are equal")
elif val_1 == val_2 or val_1 == val_3:
    print("Two numbers are equal, this is: " + str(val_1))
elif val_2 == val_3:
    print("Two numbers are equal, this is: " + str(val_2))