n = int(input('Entre com um número: '))

for x in range(1, n+1):
    if (n % 3 == 0 and n / 5 == 0) :
        print("FizzBuzz\n")

    elif n % 3 == 0:
        print("Fizz\n")
    elif (n % 5 == 0):
        print("Google Buzz\n")
    else:
      print(n + "\n")

   