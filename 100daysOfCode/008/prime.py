
def prime(a):
    a = int(a)
    flag = False
    for i in range(2, a):
        if (a % i == 0):
            flag = True
        break

    if flag:
        print(a, "is not a prime number")
    else:
        print(a, "is a prime number")




number = input("Give me a number:\n")
prime(number)