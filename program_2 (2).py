# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many 
# tickets are desired for each movie.  
# At the end of the program it prints out the total number of tickets desired by the user.  
# Use either a "for loop" or "while loop" to accomplish this.

def main():
    ######################
    # WRITE YOUR CODE HERE
    ######################
    tickets = 0
    while True:
        input('what movie would you like to watch? ')
        tickets += int(input('How many tickets would you like? '))
        repeat = input('do you want to watch another movie? ')
        if repeat == 'y':
            continue
        else :
            break
    print('total number of tickets is:',tickets)
    #ticket loop Ethan Collins 2/11/2025
if __name__ == '__main__':
    main()