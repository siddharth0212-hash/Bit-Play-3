# Program to find the longest consecutive 1's in binary representation of a number

def max1(number):

    #Initialize result
    count = 0

    # Count the number of iterations to reach number = 0
    while (number!=00):

        #This operation reduces length
        # of every sequence of 1's by one.
        number = (number & ( number << 1))

        count=count+1

    return count

number = int(input("Enter your number : "))
print("Longest consecutive 1's length : ",max1(number))
    