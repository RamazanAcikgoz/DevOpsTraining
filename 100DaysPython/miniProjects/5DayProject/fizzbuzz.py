# fizzbuzz
# Your program should print each number from 1 to 100 include 100
# But wjen the number is divisble by 3 then instead of printing the number it should print "Fizz"
# When number is divisble by 5, then insteas of printing the number it should print "Buzz"
# When the number is divisible by both 3 and 5, then instead of printing the number it should print "FizzBuzz"

def fizz_buzz(target):
    nums = []
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            nums.append("FizzBuzz")
        elif number % 3 == 0:
            nums.append("Fizz")
        elif number % 5 == 0:
            nums.append("Buzz")
        else:
            nums.append(number)
            print(nums)


fizz_buzz(15)