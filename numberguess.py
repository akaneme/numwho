import random
from colorama import Fore, Style #for cool colours in boring terminal

def numberguess():
    print(Fore.CYAN + "Welcome to the number guessing game ! Let's begin, shall we?" + Style.RESET_ALL)
    print(Fore.BLUE + "You have ten attempts to guess the random number!" + Style.RESET_ALL)

    while True:
        choice = input("Do you want to play the number guessing game ? (y/n) : ")

        if choice.lower() == 'n':
            print(Fore.YELLOW + "This soon? Sad to see you go" + Style.RESET_ALL)
            break

        elif choice.lower() != 'y':
            print(Fore.LIGHTMAGENTA_EX + "Please choose from either 'y' or 'n' :>" + Style.RESET_ALL) #if something else than 'y' or 'n'

        else:
            random_number = random.randint(1,100)
            count = 1

            while count <= 10:
                try:
                    print(f'This is your {count}/10 try')
                    number_guessed = int(input("Enter any number between 1 and 100 (your guess) : "))

                    if number_guessed > 100 or number_guessed < 1:
                        print(Fore.RED + "Oops! Numbers only between one and hundred!" + Style.RESET_ALL)

                    elif random_number == number_guessed:

                        if count == 1:
                            print(Fore.GREEN + "Yay! you really guessed the number in the first try! You're super good at this!" + Style.RESET_ALL)
                            break

                        else:
                            print(Fore.GREEN + f'Yay! you guessed the correct number within {count} tries! You did great!' + Style.RESET_ALL)
                            break

                    elif number_guessed > random_number:
                        print(Fore.RED + "ow, too high! try again?" + Style.RESET_ALL)
                        count += 1

                    else:
                        print(Fore.RED + "oof, too low! try again?" + Style.RESET_ALL)
                        count += 1

                except ValueError: #incase the user enters something other than an integer 
                    print(Fore.LIGHTRED_EX + "Please enter an integer only!" + Style.RESET_ALL)

            else:
                print(Fore.MAGENTA + f"Sorry, you've run out of attempts :/ the number was {random_number}. No worries, we'll get the next one!" + Style.RESET_ALL)

            print(Fore.LIGHTMAGENTA_EX + "Game Over. Would you like to play again?" + Style.RESET_ALL)

if __name__ == "__main__":
    numberguess()
