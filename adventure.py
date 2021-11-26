def play_again():
    print("Do you want to play again? ( y or n)?") 
    answer = input(">").lower()
    if "y" in answer:
        start()
    else:
        exit()
def game_over(reason):
    print("\n" + reason)
    print(" Game over!")
    play_again()
#dimond_room
def variables_room():
    print("\nVariables and Names !!! bet you proabably know a thing or 2 abouth them")
    print("Otherwise how els would you have made it here?")
    print("if you want to go further you must define variabls to a value of 10")
    answer = input(">")
    if "v" in answer:
        print("You typed the right answer but i ran out of ideas good job!")
        game_over("To be continued.... you won the chance to play again?")
    else:
        game_over("Go learn Ex4: Variables and Names at: https://www.youtube.com/watch?v=DDZUKaq7cCo&list=PLiEts138s9P2Cwe0PHZ8zndsEbvfV5P8N&index=6")
#monster_room
def numbers_room():
    print("\nIf i typed \nhens = 25 + 30 / 6  \t\nAnd \nRoosters = 100 - 25 * 3 % 4 into python")
    print("How many Chicken does Zed Shaw have?")
    answer = input(">")
    if answer == "127" :
        print("Correct!!!!")
        variables_room()
    elif answer < "126"  > "128":
        game_over("Please go to Zeds Excersize 3: Numbers and Math at https://www.youtube.com/watch?v=S9q_2cJDwR8&list=PLiEts138s9P2Cwe0PHZ8zndsEbvfV5P8N&index=6")
    else:
        game_over("Please go to Zed's Exercise 1: A good first program https://www.youtube.com/watch?v=WPN_gksmLHo&list=PLiEts138s9P2Cwe0PHZ8zndsEbvfV5P8N&index=3 take the link/hint!")
#bear room
def printing_room():
    print("\nSoOo you know how to give a #comment.")
    print("are you proficent in printing?")
    print("which is correct")
    print("1). print(this will print)")
    print("2). print('this will print')")
    print('3). print("this will also print")')
    print("4). print?")

    answer = input(">")
    if "2" in answer  and "and 3":
            print("correct")
            numbers_room()
    else:
        game_over("wrong you die")

    start()


def start():
    print("\nYour are standing in Zeds Learn python the hard way class room")
    print('What is the best way to tell python to "Comment out this line."')

    answer = input("> ").lower()

    if "#" in answer:
        print("Thats how its done alright")
        printing_room()

    else:
        game_over("Looks like you need to start with the Basics go to https://www.youtube.com/watch?v=8p_K9JjIu_Q&list=PLiEts138s9P2Cwe0PHZ8zndsEbvfV5P8N&index=4")

start()