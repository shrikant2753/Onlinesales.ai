# given code for debug
# def compute(n):
#     if n < 10:
#         out = n ** 2
#     elif n < 20:
#         out = 1
#         for i in range(1, n-10):
#             out *= i
#     else:
#         lim = n - 20
#         out = lim * lim
#         out = out - lim
#         out = out / 2 
#     print(out)

# n = int(input("Enter an integer: "))
# compute(n)

##################################################
# corrected code

# given function
def compute(n):
    if n < 10:
        out = n ** 2 #squearing the number
    elif n < 20:
        out = 1
        for i in range(1, n-9): #range corrected
            out *= i # calculating factorial
    else:
        lim = n - 19 #lim value corrected
        out = lim * lim
        out = out - lim
        out = out / 2 
    print(out)

# accepting input from user
n = int(input("Enter an integer: "))
compute(n)


# for number less than 10 code work exactly fine
# test cases -
    
    # Enter an integer: 9
    # 81
    
    # Enter an integer: 0
    # 0
    
    # Enter an integer: 4
    # 16
    
    # Enter an integer: -4
    # 16

# for no in between 10 and 20
# range is not appropriate - we have to iterate it one more time
# i.e. for i in range(1, (n-10)+1) -> for i in range(1, n-9):
    # for input 10 : as given (n-10) !=> (10-10)! => 0! => 1
    # Enter an integer: 10
    # 1

    # for input 15 : as given (n-10) !=> (15-10)! => 5! => 120
    # Enter an integer: 15
    # 120

    # for input 19 : as given (n-10) !=> (19-10)! => 9! => 362880
    # Enter an integer: 19
    # 362880

# for no greater than equal to 20
# lin is not appropriate - we have to add 1 in it
# we have to change the lim from n-20 to (n-20)+1 i.e n-19

    # for input 20 : as given (n-20) !=> sum of numbers from 1 to(20-20) => 0 => 0
    # Enter an integer: 20
    # 0.0

    # for input 21 : as given (n-20) !=> sum of numbers from 1 to(21-20) => 1 => 1
    # Enter an integer: 21
    # 1.0

    # # for input 25 : as given (n-20) !=> sum of numbers from 1 to(25-20) => 1+2+3+4+5 => 15
    # Enter an integer: 25
    # 15.0