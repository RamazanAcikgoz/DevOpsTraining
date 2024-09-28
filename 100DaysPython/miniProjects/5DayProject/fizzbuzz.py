# fizzbuzz
# Your program should print each number from 1 to 100 include 100
# But wjen the number is divisble by 3 then instead of printing the number it should print "Fizz"
# When number is divisble by 5, then insteas of printing the number it should print "Buzz"
# When the number is divisible by both 3 and 5, then instead of printing the number it should print "FizzBuzz"

for number in range(1, 101):
    if number % 3 == 00 and number % 5 == 00:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 00:
        print("Fizz")
    else:
        print(number)