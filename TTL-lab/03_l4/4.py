n = input("Enter the word and see if it is palindrome: ")  # check palindrome
if n == n[::-1]:
    print("This word is palindrome")
else:
    print("This word is not palindrome")

# 5


def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)


num = int(input("Enter a number: "))

if num < 0:
    print("Negative number you idiot")
elif num == 0:
    print("1")
else:
    print(recur_factorial(num))


# 6

def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))


n = int(input("Enter number of terms:"))
print("Fibonacci sequence:")
for i in range(n):
    print(fibonacci(i))

# 7

# Function to check sum of
# digit using recursion


def sum_of_digit(n):
    if n == 0:
        return 0
    return (n % 10 + sum_of_digit(int(n / 10)))


num = 12345
result = sum_of_digit(num)
print("Sum of digits in", num, "is", result)
