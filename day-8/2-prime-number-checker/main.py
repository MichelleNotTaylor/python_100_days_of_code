#Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
n = int(input("Check this number: "))
prime_checker(number=n)

