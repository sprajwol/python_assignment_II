# 8. Write a function, is_prime, that takes an integer and returns True if
# the number is prime and False if the number is not prime.


def is_prime(integer):
    if (integer == 1):
        return False
    elif (integer == 2):
        return True
    else:
        for j in range(2, integer):
            if (integer % j == 0):
                return False
        return True


n = int(input("Enter a number:"))

ans = is_prime(n)
print(ans)
