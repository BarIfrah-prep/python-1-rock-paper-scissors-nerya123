import random




while True:

    try:
        userinput = int(input("Enter number(1-stone, 2-scissors, 3-paper) :"))
    except ValueError:
        print("you entered invalid input")
        continue
    if userinput not in range(1, 4):
        print("you entered invalid integer")
        continue
    print("user choise=" + str(userinput))
    usernum = userinput

    compnum = random.randint(1, 3)
    print("computer random choise=" + str(compnum))
    if usernum == compnum:
        print("its a tie play agein")
        continue
    if (usernum == 1 and compnum == 2) or (usernum == 2 and compnum == 3) or (usernum == 3 and compnum == 1):
        print("user win!!")

    if (usernum == 1 and compnum == 3) or (usernum == 2 and compnum == 1) or (usernum == 3 and compnum == 2):
        print("computer win!!")



















