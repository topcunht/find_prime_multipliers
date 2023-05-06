
number_user = int(input("Enter a number : "))

def MyIsPrime(number):
    i = 2
    flag = True
    while flag:
        if number < 2:
            flag = False
            break
        if i == number:
            break
        else:
            if number % i == 0:
                flag = False
                break
            else:
                i +=1
    return flag
def Other(number_user):
    
    if MyIsPrime(number_user) == True:
        print(f"{number_user} is a prime number")
    elif MyIsPrime(number_user) == False:
        i = 2
        print("The prime multipliers of the number are :")
        while number_user != 1:
            if MyIsPrime(i) == True and number_user % i == 0:
                print(i)
                number_user = number_user / i
                if number_user % i != 0:
                    i += 1
            else:
                i += 1
            
Other(number_user)
        


