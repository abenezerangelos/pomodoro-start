'''
This program is a program that tests if a given user inputted number is a prime number or not

I will write the solution (is prime function) in three ways

1. I will use my own algorithm instead of the trial division approach that was discussed in the prompt of the homework,
because i think there is an even easier way to tell whether any given number is prime or not.
    This implementation can be found as the is_prime1 and sum_prime1 functions in my code
    Note that: the is_prime function makes use of the is_prime1 function as a helper function.

2. I will use the trial division approach just because it was in the prompt and I definitely want to get those points.
    This implementation can be found as the is_prime and sum_prime functions in my code.

3. I will use an even more accurate description of the trial division approach that I found from Wikipedia.
   This implementation can be found as is_prime2 and sum_prime2 functions in my code.
   Both the time and space complexity of this implementation are terrible but they accurately fit the description of the assignment.

The time complexity of is_prime in the second implementation is O(n^2), while the time complexity of is_prime in the 1st implementation
is only O(n)
'''

# This is the first implementaton as described in the block comment above
def is_prime1(number):
    prime=True
    for i in range(2,number):
        if number%i==0:
            return False
            prime=False
    if prime:
        return True
def sum_prime1(n):
    sum=0
    for i in range(2,n+1):
        if is_prime1(i):
            sum+=i
    print(sum)
number= int(input("Please enter an integer >=2: "))
if number<2:
    print(number," is neither prime nor composite")
    number=int(input("This is not a viable option please reenter a number that is greater than 2: "))



# #This is the second and accurate implementation that implements the trial division approach just like the prompt of the home
# #notice how this is_prime is using the is_prime1 from above to make a good judgement if our number is prime or not,
# #I am doing this because nothing about this specific part is specified in the prompt.
# #notice that this sum_prime and is_prime is different from the one above.
def is_prime(number):
    for i in range(2,int(number**(1/2))+1):
        if number%i==0 and is_prime1(i):

            return False

    return True
def sum_prime(n):
    sum=0
    for i in range(2,n+1):
        if is_prime(i):

            sum+=i
    print(sum)


#this function is_prime2 is a third and more accurate implementatoin although the time complexity is really bad since it
# depends on the function  primal() which has both really bad time and space complexity
def is_prime2(n):

    for i in range(2,int(n**(1/2))+1):
        if n%i==0 and primal(i):

            return False

    return True
#prime generator or prime array
# we will first try a prime callback function, that will then later on might be applied recursively
# we will then try the recursive option possibly without generation but actually logic and testing

primal_array=[2]

def primal(n):

    for j in range(3, n + 1):
            prime = True


            for i in primal_array:
                if n == i:
                    print(True)

                    return True
                if j%i==0:
                    prime=False
            if prime:
                primal_array.append(j)


    if n in primal_array:

        return True
    else:

        return False

if is_prime2(number):
    print(f"{number} is a prime number!")
else:
    print(f"{number} is not a prime number, it is a composite!")

def sum_prime2(n):
    sum=0
    for i in range(2,n+1):
        if is_prime2(i):

            sum+=i
    print(f"Sum of prime between 2 and {n} is:", sum)
sum_prime2(number)















