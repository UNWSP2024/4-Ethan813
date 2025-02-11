# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the 
# month and keep a running total. (Enter 0 to exit the loop)  
# When the loop finishes, the program should display the amount that the 
# user is over or under budget.

def main():
    budget = 0.0
    difference = 0.0
    spent = 0.0         #initialize for while loop
    total = 0.0

    ######################
    # WRITE YOUR CODE HERE
    ######################
    budget = float(input('enter your budget for a month: '))
    while True:
        spent = float(input('enter your expenses: '))
        total += spent
        if spent == 0:
            break
        else:
            continue
    difference = budget - total
    if difference < 0:
        print("looks like you're in debt, you went over budget by $",difference)
    elif difference == 0:
        print("you're broke but not in debt, your balance is $",difference)
    elif difference > 0:
        print("you're good with saving, you are under budget by $",difference,)
#Ethan Collins 2/11/2025 the balancer



if __name__ == '__main__':
    main()