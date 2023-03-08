#
# Python 3.9.2
#
# Author: Razvan Nanu
#
# A Tech Academy Python Course Project
# Demonstrating how to pass variables from function to function to produce a game
#
# function_name(variable) means we pass the variable



def start(nice=0,mean=0,name=""):
    #get user name
    name = describe_game(name)
    nice,mean,name = nice_mean2(nice,mean,name)
    


def describe_game(name):
    """
        Check to see if this is a new game or not
        If it is new, get the user's name.
        If it is not a new game, thank the player for
        playing again and continue with the game
    """
    # If we do not have the user's name
    # They are a new player and we need to get their name.
    if name != "":
        print("\n Thank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>>").capitalize()
                if name != "":
                    print('\n Welcome {}!'.format(name))
                    print('\n In this game, you will be greeted \n by several different people.\n You can choose to be nice or mean.')
                    print('\n but at the end of the game your fate\n will be sealed by your actions')
                    stop = False
    return name

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\n A stranger approaches you for a \nconversation. Will you be nice?\nor mean (N/M)\n>>>: ").lower()
        if pick == "n":
            print("The stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\n The stranger glares at you \nmenacingly and storms off...")
            mean = (mean +1)
            stop = False
    score(nice,mean,name) #pass the 3 variables to score()
    

def nice_mean2(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\n You see someone drop \ntheir wallet do you\return it? (N/M)\n>>>: ").lower()
        if pick == "n":
            print("You give back the wallet and gain a friend")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\n You find nothing inside and are caught")
            mean = (mean +1)
            stop = False
        score(nice,mean,name) #pass the 3 variables to score()




def show_score(nice,mean,name):
    print('\n{}, your current total: \n({},Nice) and ({}, Mean)'.format(name,nice,mean))
    #prints out their name and total nice and mean score


def score(nice,mean,name):
    #score function is being passed the values stored within the 3 variables
    if nice > 2: #if the condition is valid, call win function passing in the variable so it can use them
        win(nice,mean,name)
    if mean > 2:    #if condition is valid, call lose function passing in the variables so it can use them
        lose(nice,mean,name)
    else:   # else, call nice_mean function passing in the variables so it can use them
        nice_mean(nice,mean,name)
              


def win(nice,mean,name):
    print("\nNice Job {}, you win \nEveryone loves you and you've made\nlots of friends along the way!".format(name))
    #call again function and pass in our variable
    again(nice,mean,name)


def lose(nice,mean,name):
    print("\nAhhhh too bad, game over! \n{}, you live in a dirty beat-up \nvan by the river,wrteched and alone".format(name))
    #call again function and pass in our variables
    again(nice,mean,name)




def again(nice,mean,name):
    stop = True
    while stop:
        choice = input('\nWould you like to play again? (y/n): \n>>>').lower()
        if choice == 'y':
            stop = False
            reset(nice,mean,name)
        if choice == 'n':
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print('\nEnter (Y) for "YES", (N) for "NO":\n>>>')



def reset(nice,mean,name):
    nice = 0
    mean = 0
    #did not reset name variable since the same user is playing
    start(nice,mean,name)






if __name__ == "__main__":
    start()
