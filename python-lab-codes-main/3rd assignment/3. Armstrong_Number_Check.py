num = int(input("Enter a number: "))
temp = num
total = 0
digits = len(str(num))
while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10
if num == total:
    print(f"{num} is an ARMSTRONG number.")
else:
    print(f"{num} is NOT an Armstrong number.")