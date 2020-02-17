# eig zelfde als heads or tails maar dan even en oneven.

import random
import time
#print(random.randint(1,6))
money = ""

# toegewezen zodat ik in de functie van play_game() kan begginnen.
# begrijp nog niet of dit helemaal goed werkt
choice3 = ""
bet_size = ""
answer = ""
bet1 = ""
initial_budget = ""
game_playing = True
game_played = 1
answer_game = ""
result1 = (random.randint(1,6) + random.randint(1,6)) % 2

    # 0 is even, 1 is oneven


#functie voor dice
def choice():
    choice3 = input("Even or odds? ").lower()
    while choice3 == "even" or choice3.lower() == "odd":
        break
    else:
        print("Wrong input. Try: 'even' or 'odd'.")
        choice3 = input("Even or odds? ")
    global answer
    answer = choice3
    return answer

def bet_size1():
    bet_size = input("What is your bet size? ")
    while int(bet_size) > money:
        print("You can't bet more money than your budget. Your current budget is: " + str(money))
        bet_size = input("What is your bet size? ")
    global bet1
    bet1 = bet_size
    return bet1



def rol_dice():
    global money
    global bet1
    global game_played
    result1 = (random.randint(1, 6) + random.randint(1, 6)) % 2
    if answer == "even" and result1 == 0:
        print("The result was even, you won " + str(bet1) + " euro's")
        money += int(bet1)
        game_played += 1
        print(game_played)
        print("Current balance: " + str(money))
    elif answer == "odd" and result1 == 1:
        print("The result was odds, you won " + str(bet1) + " euro's")
        money += int(bet1)
        game_played += 1
        print(game_played)
        print("Current balance: " + str(money))
    elif answer == "odd" and result1 == 0:
        print("The result was even, you lost " + str(bet1) + " euro's")
        money -= int(bet1)
        game_played += 1
        print(game_played)
        print("Current balance: " + str(money))
    elif answer == "even" and result1 == 1:
        print("The result was odds, you lost " + str(bet1) + " euro's")
        money -= int(bet1)
        game_played += 1
        print(game_played)
        print("Current balance: " + str(money))
    else:
        print("Probably incorrect input")
        print(result1)

#playing the game
def play_game():
    while money > 0:
        if contin_playing() == "nooo":
            break
        choice()
        bet_size1()
        rol_dice()
    else:
        print("You ran out of money. You lost " + str(initial_budget))
        play_again()

#intro of the game
def intro():
    print("Welcome, let's play!")
    print("The rules of the game are simple. Two dices are rolled and you can bet whether they combined will be even or odd. You can bet an amount per turn.")
    print("Every time after 5 turns the game asks you if you want to continue playing or leave the table.")
    budget()
    return

#player can input his budget
def budget():
    global money
    global initial_budget
    initial_budget = int(input("For how many euros do you want to play? "))
    money = initial_budget
    while money:
        try:
            if money > 0 and money <= 200:
                break
            elif money <= 0:
                print("You can't play with negative money!")
                money = int(input("For how many euros do you want to play? "))
            elif money > 200:
                print("Maximum budget is 200 euros")
                money = int(input("For how many euros do you want to play? "))
        except:
            # Gaat maar 1 keer goed. Daarna valueerror
            print("Invalid input. Make sure to type only in numbers!")
            money = int(input("For how many euros do you want to play? "))

def play_again_loop():
    global answer_game
    while answer_game != "yes" and answer_game != "no":
        print("Wrong input. Please type only 'yes' or 'no'.")
        answer_game = input("Do you want to play again? ").lower()
    else:
        return answer_game

#Checking if player want to play again when budget hit 0
def play_again():
    global game_playing
    answer_game = input("Do you want to play again? ").lower()
    # deze loopt niet
    while answer_game != "yes" and answer_game != "no":
        print("Wrong input. Please type only 'yes' or 'no'.")
        answer_game = input("Do you want to play again? ").lower()
    else:
        if answer_game == "no":
            print("Thanks for playing")
            game_playing = False

        elif answer_game == "yes":
        #als je hier opnieuw weer speelt neemt die je vorige verliezen niet mee. Total games word wel meegenomen.
            print("Game restarting...")
            print("Please wait")
            time.sleep(4)
            print()
            print()

# optie ergens in te voegen om te stoppen. (om de 5 beurten?)
def contin_playing():
    global game_played
    global game_playing
    if game_played % 5 == 0:
        answer_play = input("Do you want to continue playing? ('yes' or 'no') ").lower()
        if answer_play == "yes":
            return
        elif answer_play == "no":
            game_playing = False
            return "nooo"
        else:
            print("wrong input. Fill in only 'yes' or 'no'.")
            answer_play = input("Do you want to continue playing? ('yes' or 'no') ").lower()
            #while answer_play != "yes" or answer_play != "no":
                #print("wrong input. Fill in only 'yes' or 'no'.")
                #answer_play = input("Do you want to continue playing? ('yes' or 'no') ").lower()
    else:
        return

def end_game():
    print("End game")
    if initial_budget < money:
        print("Congratulation! you walked away with a profit of " + str(money - initial_budget))
    elif initial_budget > money and money > 0:
        print("You lost " + str(initial_budget - money))
    elif money == 0:
        print("You lost your whole budget of " + str(initial_budget))
    elif initial_budget == money:
        print("You walked away with exactly your initial budget of " + str(initial_budget))


# total game
# hier kan ook weer een functie van worden gemaakt als je bepaalde spellen in 1 sheet wilt ophalen en spelen.
while game_playing == True:
    intro()
    play_game()
else:
    end_game()

#global choice3
#global bet_size
#choice3 = input("Even or odds? ")
#bet_size = input("What is your bet size? ")