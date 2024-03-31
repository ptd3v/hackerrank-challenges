#Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
#Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4==0 and year % 400==0:  #Initial Testing idea, 1/6 failed. 1992 fail. Giving False.
        
    #Why is this returning false? Lets check the three condidions.
    #Condition 1: The year can be evenly divided by 4, is a leap year, unless:
        #Reworded: if year%4 == 0, leap = True
    #Condition 2: The year can be evenly divided by 100, it is NOT a leap year, unless:
        #Reworded: if year%100 == 0, leap = False
    #Condition 3: The year is also evenly divisible by 400. Then it is a leap year.
        #Reworded: if year%4==0 and year%400 == 0, leap = True
        
        return True
    else:
        return False
        
    return leap

year = int(input())
print(is_leap(year))


