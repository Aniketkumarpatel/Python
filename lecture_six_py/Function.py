function

a  = 5
b =10
sum = a + b
print(sum)

# more lines of codes

a  = 5
b =15 
sum = a + b
print(sum)


def calc_sum(a,b):
    sum = a + b
    print(sum)
    return sum

calc_sum(5,6)

# #more lines of codes

calc_sum(6,6)

#more lines of codes
calc_sum(5,5)

# function definition
def calc_sum(a,b):
    return a+ b #parameters
sum = calc_sum(1,4)  # function call; arguments
print(sum) 


def print_Aniket():
    print("Aniket")

    print_Aniket()


# Question  cal avereage of 3 numns

def calc_avg(a,b,c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg
calc_avg(2,2,2,)

calc_avg(2,2,4,)

# calc 2 nums

def cal_prod(a=4 , b=5):
    print(a * b)
    return(a * b)

cal_prod()