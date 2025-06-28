 num = int(input("Enter a number: "))
original = num
rev = 0

while num > 0:
    digit = num % 10
    rev = sum+(digit**3)
    num //= 10

if original == rev:
    print(f"{original} is a palindrome")
else:
     print(f"{original} is not a palindrome")