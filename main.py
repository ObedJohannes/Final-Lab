import random


def diceRoll():
    click = input("Press enter to shoot dice.")
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return die1, die2



def twoDice(dices):
    die1, die2 = dices
    print("You rolled a {} , and a {}.".format(die1, die2))
    print("Roll Total:", die1 + die2)


value = diceRoll()
twoDice(value)

sum_of_dices = sum(value)
result = 0
done = True
if sum_of_dices in (7, 11):
    print("Congratulations! \nYou rolled a", sum_of_dices, "you won!")
    result = done

elif sum_of_dices in (2, 3, 12):
    print("you rolled a", sum_of_dices, "\ntry again next time")
    result = done
else:
    result = not done
    currentPoint = sum_of_dices
    print("Your current point is", currentPoint, "good luck!")



while not done:
    value = diceRoll()
    twoDice(value)
    sum_of_dices = sum(value)

    if sum_of_dices == currentPoint:
        result = done

    elif sum_of_dices == 7:
        result = "lose"
        print("You rolled a 7 better luck next time.")

    elif sum_of_dices == 2:
        result = "lose"
        print("You rolled a 2 better luck next time.")


    elif sum_of_dices == 3:
        result = "lose"
        print("You rolled a 3 better luck next time.")


    elif sum_of_dices == 12:
        result = "lose"
        print("You rolled a 12 better luck next time.")


    if result == "win":
        print("congratulations,you won!")

    else:
        print("not your point,\ntry again next time.")

diceRoll()