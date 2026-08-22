# WAF to print the length of a list.(liost is the parameter)

list  = ["delhi", "nodia", "chennai"]

def print_len(list):
    print(len(list))
    return list

print_len(list)

#  WAF to print the elements of list in a single line(list is the parameter)
heros  = ["delhi", "nodia", "chennai"]
def print_len(list):
    print(list)

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(heros)
print()

#  WAF  to find factorial of n ( n is the parameter)
# this is basic method

n = 5
fact = 1
for i in range(1,n+1):
    fact *= i
    print(fact)

#  function se
 
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
cal_fact(7)




      