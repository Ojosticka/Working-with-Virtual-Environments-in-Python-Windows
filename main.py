#simple future age checker

age = input("How old are you? ")

if not age.isdigit():
    print("Please enter a valid age.")
else:
    print(f"In 10 years time, you will be {int(age) + 10} years old.")