# Program #3: Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average 
# rainfall over a period of years.  
# The program should first ask for the number of years.  
# The outer loop will iterate once for each year. 
# The inner loop will iterate twelve times, once for each month.  
# Each iteration of the inner loop will ask the user for inches of rainfall for each month.  
# After all iterations, the program should display the number of months, 
# the total inches of rainfall, and the average rainfall per month for the entire period.

def main():
    ######################
    # WRITE YOUR CODE HERE
    ######################    
    rain_fall = 0
    years = int(input('how many years? '))
    months = years * 12
    total_months = months * years
    for count in range(years):
        for count in range(months):
            inches_of_rain = float(input('how many inches of rain? '))
            rain_fall += inches_of_rain
        print('total months:',total_months, ', total inches of rainfall:',rain_fall, ', average rainfall per month in inches:',rain_fall / total_months )
# Ethan Collins 2/11/2025 rain collector
if __name__ == '__main__':
    main()