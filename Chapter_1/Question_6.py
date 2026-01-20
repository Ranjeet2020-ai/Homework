total = 0.0

while True:
    user_input = input()
    
    if user_input == "0":
        print(f"The grand total is {total}")
        break
    
    try:
        num = float(user_input)
        total += num
        print(f"The total is now {total}")
    except ValueError:
        print("That wasn’t a number.")