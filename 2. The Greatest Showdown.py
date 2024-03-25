# Task 1: Identify the Greatest

print("Enter first number:")
val_1 = input()

print("Enter second number:")
val_2 = input()

print("Enter thrid number:")
val_3 = input()

if val_1 > val_2 and val_1 > val_3:
    print("Largest number from inputs is: " + str(val_1))
elif val_2 > val_1 and val_2 > val_3:
    print("Largest number from inputs is: " + str(val_2))
elif val_3 > val_1 and val_3 > val_2:
    print("Largest number from inputs is: " + str(val_3))
else:
    print("No single largest number!")


# Task 2: Identify the Smallest

if val_1 < val_2 and val_1 < val_3:
    print("Smallest number from inputs is: " + str(val_1))
elif val_2 < val_1 and val_2 < val_3:
    print("Smallest number from inputs is: " + str(val_2))
elif val_3 < val_1 and val_3 < val_2:
    print("Smallest number from inputs is: " + str(val_3))
else:
    print("No single smallest number!")


# Task 3: Equality Check

