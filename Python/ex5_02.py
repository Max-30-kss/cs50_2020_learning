largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == 'done':
        break
    
    try:
        num = int(num)
        if largest is None or num > largest:
            largest = num
        if smallest is None or num < smallest:
            smallest = num
    except ValueError:
        print("Invalid input")

if largest is None and smallest is None:
    print("No valid numbers were entered.")
else:
    print(f"Maximum is {largest}")
    print(f"Minimum is {smallest}")
