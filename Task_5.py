def sum_num():
    s = 0
    while True:
        in_list = input("Enter a number, input 'w' to exit").split()
        for num in in_list:
            if num == "w":
                return s
            else:
                try:
                    s += int(num)
                except ValueError:
                    print("To exit the program, enter - 'w'.")
                    print(f"Sum of numbers = {s}")


    print(sum_num())
