def personal_info(**kwards):
    return kwards

print(personal_info(name=input("Enter your name: "), surname=input("Enter your surname: "),
                    birsday=input("Enter your birthday: "), city=input("Enter your city"), phone_number=input("Enter your phone number: ")))
