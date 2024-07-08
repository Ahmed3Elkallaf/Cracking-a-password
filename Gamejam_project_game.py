print("Main menu")
print("")
print("How to play?")
print("You are going to crack a password, The password consists of 4 digits from 0 to 9 you must guess them correctly and write them at the end to win,You have only 4 attempts for each digit, if you failed to guess one of the digits you will lose the Game")
print("The Game will help you while you are guessing the password")
print("")
#cracking
import random

first_number = random.randint(0,9)
second_number = random.randint(0,9)
third_number = random.randint(0,9)
fourth_number = random.randint(0,9)
random_number = str(first_number)+str(second_number)+str(third_number)+str(fourth_number)
out_of_crack = 0
crack_attempt1 = 0
crack_attempt2 = 0
crack_attempt3 = 0
crack_attempt4 = 0
limit_attempt1 = 4
limit_attempt2 = 4
limit_attempt3 = 4
limit_attempt4 = 4
failed = False


if  out_of_crack == 0:
   
    while crack_attempt1 < limit_attempt1 and out_of_crack == 0:
        try:
            number1 = int(input("Enter first digit of the password: "))
            if number1 == first_number:
                 out_of_crack = 1
                 print("")
            elif number1 < first_number:
                 print("Very low!")
                 crack_attempt1 += 1
            else:
                 print("Very high!")
                 crack_attempt1 += 1

        except ValueError:
             print("Error you must write numbers!")
             

else:
    failed = True
    

if  out_of_crack == 1:
    print("First digit is correct!")
    print("")

    while crack_attempt2 < limit_attempt2 and out_of_crack == 1:
        try:
            number2 = int(input("Enter second digit of the password: "))
            if number2 == second_number:
                 out_of_crack = 2
                 print("")
            elif number2 < second_number:
                 print("Very low!")
                 crack_attempt2 += 1
            else:
                 print("Very high!")
                 crack_attempt2 += 1

        except ValueError:
             print("Error you must write numbers!")
             

else:
    failed = True


if  out_of_crack == 2:
    print("Second digit is correct!")
    print("")

    while crack_attempt3 < limit_attempt3 and out_of_crack == 2:
        try:
            number3 = int(input("Enter third digit of the password: "))
            if number3 == third_number:
                 out_of_crack = 3
                 print("")
            elif number3 < third_number:
                 print("Very low!")
                 crack_attempt3 += 1
            else:
                 print("Very high!")
                 crack_attempt3 += 1

        except ValueError:
             print("Error you must write numbers!")
             

else:
    failed = True


if  out_of_crack == 3:
    print("Third digit is correct!")
    print("")

    while crack_attempt4 < limit_attempt4 and out_of_crack == 3:
        try:
            number4 = int(input("Enter fourth digit of the password: "))
            if number4 == fourth_number:
                 out_of_crack = 4
                 print("")
            elif number4 < fourth_number:
                 print("Very low!")
                 crack_attempt4 += 1
                 if crack_attempt4 == limit_attempt4:
                     failed = True
                

            else:
                 print("Very high!")
                 crack_attempt4 += 1
                 if crack_attempt4 == limit_attempt4:
                     failed = True

        except ValueError:
             print("Error you must write numbers!")
             

if out_of_crack == 4:
    print("Fourth digit is correct!")
    print("")
    try:
        password = input("Enter all the digits of the password: ")
        if password == random_number:
            print("You have unlocked the password, you win!")
        else:
            failed = True

    except ValueError:
        print("Error you must write numbers!")


if failed:
    print("You failed to get the password")



print("This Game developed by Ahmed Elkallaf")
