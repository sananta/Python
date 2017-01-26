## prog3.py
## Srivarshini Ananta
## February 11, 2016

def power(m, n):
    " " " Compute the value when the base m is raised to the exponent n " " "  
    if m < 0 or n < 0:
        print("Error") 
    elif n == 0:
        return 1 
    else:
        k = m
        while n > 1:
            m = m * k
            n = n-1
        return m

def harmonic(n):
    " " " Compute the sum of the first n terms. Ex: 1 + 1/2 + 1/3 + ... + 1/n " " "
    k = 0
    while n > 0:
        k = k + 1/n
        n = n - 1
    return k

def printPar(w, h):
    " " " Print a parallelogram with asteriks represented with the width w and height h " " "
    counter = 1
    for p in range(h):
        print(" "*(h-counter)+"*"*w)
        counter = counter + 1
        
def allButMax():
    " " " Asks user to enter numbers greater than or equal to 0 and computes the sum of all the numbers excluding the greatest number " " "
    str = "";
    sum = 0;
    max = 0
    while str != "end":
        str = input("Enter next number: ")
        if str != "end":
            n = float(str)
            if n > max:
                sum = sum + max
                max = n
            else: sum = sum + n 
        else:
            print("The sum of all values except for the maximum value is: " +format(sum))
            return sum   
               
def avgSumOfSquares():
    " " " Asks user to input a series of numbers and computes the sum of the square of each of the numbers " " "
    str = "";
    sum = 0;
    term = 0;
    average = 0.0;
    while str != "end":
        str = input("Enter next number: ")
        if str != "end":
            n = float(str)
            if n >= sum or n <= sum:
                sum = sum + (n * n)
                term = term + 1
                average = sum/term
        elif term > 0:
            print("The average sum of the squares is: " + format(average))
            return average
    if str == "end" and term == 0:
        print("No numbers were entered.")
    
